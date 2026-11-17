"""Build a turbovec RAG index from raw/ markdown documents.

Walks the corpus, splits each file into heading-aware chunks, embeds them with
Qianfan bge-large-zh, and writes:
  - <out>/index.tv     : turbovec quantized vector index
  - <out>/meta.json    : sidecar mapping row -> {path, title, heading, text}
  - <out>/manifest.json: build config + per-file content hashes (for --update)

turbovec.search returns integer row ids in insertion order, so meta.json rows
line up 1:1 with the order chunks were add()-ed.

Usage:
  python build_rag.py --raw RAW_DIR --out OUT_DIR [--update] [--bit-width 4]
"""
import argparse
import hashlib
import json
import os
import re
import sys

import numpy as np
from turbovec import TurboQuantIndex

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from embed import embed, DIM, MODEL, BASE_URL  # noqa: E402
from ragpaths import default_raw, default_out  # noqa: E402

MAX_CHARS = 1200      # target chunk size
OVERLAP = 150         # char overlap between sub-splits of a long section
MIN_CHARS = 40        # skip near-empty chunks


def file_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:]
    return text


def split_long(block: str):
    """Hard-split an over-long section into overlapping windows."""
    out = []
    i = 0
    while i < len(block):
        out.append(block[i:i + MAX_CHARS])
        i += MAX_CHARS - OVERLAP
    return out


def chunk_markdown(text: str):
    """Yield (heading, chunk_text) split on markdown headings, size-capped."""
    text = strip_frontmatter(text)
    lines = text.splitlines()
    sections = []
    cur_head = ""
    cur = []
    for ln in lines:
        m = re.match(r"^(#{1,6})\s+(.*)", ln)
        if m:
            if cur:
                sections.append((cur_head, "\n".join(cur).strip()))
            cur_head = m.group(2).strip()
            cur = []
        else:
            cur.append(ln)
    if cur:
        sections.append((cur_head, "\n".join(cur).strip()))

    for head, body in sections:
        body = body.strip()
        if len(body) < MIN_CHARS and not head:
            continue
        combined = (head + "\n" + body).strip() if head else body
        if len(combined) <= MAX_CHARS:
            if len(combined) >= MIN_CHARS:
                yield head, combined
        else:
            for piece in split_long(body):
                pc = ((head + "\n" + piece).strip() if head else piece).strip()
                if len(pc) >= MIN_CHARS:
                    yield head, pc


def first_title(text: str, fallback: str) -> str:
    for ln in strip_frontmatter(text).splitlines():
        m = re.match(r"^#{1,6}\s+(.*)", ln)
        if m:
            return m.group(1).strip()
        if ln.strip():
            return ln.strip()[:80]
    return fallback


def collect_files(raw_dir: str):
    for root, _, files in os.walk(raw_dir):
        for fn in sorted(files):
            if fn.lower().endswith((".md", ".txt", ".markdown")):
                yield os.path.join(root, fn)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", default=None,
                    help="corpus dir (default: $RAG_ROOT/raw, else ./raw)")
    ap.add_argument("--out", default=None,
                    help="index dir (default: $RAG_ROOT/.rag, else ./.rag)")
    ap.add_argument("--bit-width", type=int, default=4)
    ap.add_argument("--update", action="store_true",
                    help="reuse cached embeddings; only (re)embed new/changed files")
    ap.add_argument("--check", action="store_true",
                    help="dry run: report what would change, embed/write nothing")
    ap.add_argument("--no-dedup", action="store_true",
                    help="keep duplicate chunks (default: collapse identical text)")
    args = ap.parse_args()
    if args.raw is None:
        args.raw = default_raw()
    if args.out is None:
        args.out = default_out()
    if args.check:
        args.update = True  # --check only makes sense against an existing index

    os.makedirs(args.out, exist_ok=True)
    manifest_path = os.path.join(args.out, "manifest.json")
    meta_path = os.path.join(args.out, "meta.json")
    vecs_path = os.path.join(args.out, "vectors.npy")  # cache for --update only

    prev_hashes = {}
    prev_meta = []
    prev_vecs = None
    if args.update and os.path.exists(manifest_path) and os.path.exists(meta_path):
        prev_hashes = json.load(open(manifest_path)).get("hashes", {})
        prev_meta = json.load(open(meta_path))
        if os.path.exists(vecs_path):
            prev_vecs = np.load(vecs_path)

    # Group previously-embedded chunks (with their cached vector) by source path.
    # prev_paths tracks every file seen last build, including zero-chunk stubs,
    # so they don't get miscounted as "changed" on every subsequent --update.
    prev_by_path = {}
    prev_paths = set(prev_hashes.keys())
    if prev_vecs is not None and len(prev_vecs) == len(prev_meta):
        for i, m in enumerate(prev_meta):
            prev_by_path.setdefault(m["path"], []).append((m, prev_vecs[i]))

    meta = []           # final per-row metadata (no vectors stored here)
    vec_rows = []       # per-row float32 vector, parallel to meta (None = needs embed)
    hashes = {}
    n_files = 0
    n_added = n_changed = n_unchanged = 0  # for the per-run summary

    # Dedup state: chunk-text hash -> row index already kept in `meta`.
    seen_chunks = {}
    n_dup = 0

    def add_row(rel, title, head, chunk, vec):
        """Append a chunk row, collapsing exact-duplicate text unless --no-dedup.

        vec is a float32 array (cached) or None (to be embedded later). On a
        duplicate we keep the first occurrence and record the extra source path
        under its 'dups' list, so a hit can show every file it came from.
        """
        nonlocal n_dup
        if not args.no_dedup:
            ch = hashlib.sha256(chunk.encode("utf-8")).hexdigest()
            kept = seen_chunks.get(ch)
            if kept is not None:
                n_dup += 1
                dups = meta[kept].setdefault("dups", [])
                if rel not in dups and rel != meta[kept]["path"]:
                    dups.append(rel)
                return
            seen_chunks[ch] = len(meta)
        meta.append({"path": rel, "title": title, "heading": head, "text": chunk})
        vec_rows.append(np.asarray(vec, dtype="float32") if vec is not None else None)

    for fp in collect_files(args.raw):
        rel = os.path.relpath(fp, args.raw)
        try:
            text = open(fp, encoding="utf-8", errors="replace").read()
        except Exception as e:  # noqa: BLE001
            print(f"  skip {rel}: {e}", file=sys.stderr)
            continue
        n_files += 1
        h = file_hash(text)
        hashes[rel] = h
        title = first_title(text, os.path.basename(fp))

        cached = prev_by_path.get(rel, [])
        if args.update and rel in prev_hashes and prev_hashes[rel] == h:
            # Unchanged file: reuse its cached chunks (may be zero for stubs).
            n_unchanged += 1
            for m, v in cached:
                add_row(rel, m["title"], m.get("heading", ""), m["text"], v)
            continue

        if args.update:
            if rel in prev_paths:
                n_changed += 1
            else:
                n_added += 1

        for head, chunk in chunk_markdown(text):
            add_row(rel, title, head, chunk, None)

    # Rows still needing a vector (fresh chunks: vec is None).
    to_embed_rows = [i for i, v in enumerate(vec_rows) if v is None]
    to_embed_texts = [meta[i]["text"] for i in to_embed_rows]

    # Files present last time but gone now (deleted from raw/) are simply not
    # re-added, so their chunks drop out of the index automatically.
    n_removed = len([p for p in prev_paths if p not in hashes]) if args.update else 0

    if args.update:
        print(f"scan: files={n_files} | +{n_added} new  ~{n_changed} changed  "
              f"={n_unchanged} unchanged  -{n_removed} removed", file=sys.stderr)
    else:
        print(f"scan: files={n_files} (full rebuild)", file=sys.stderr)
    print(f"chunks={len(meta)} "
          f"(reused={len(meta) - len(to_embed_texts)} new={len(to_embed_texts)}"
          f"{'' if args.no_dedup else f' deduped={n_dup}'})",
          file=sys.stderr)

    if args.check:
        # Dry run: report what would change, embed nothing, write nothing.
        if to_embed_texts or n_removed:
            print(f"check: {len(to_embed_texts)} chunks would be (re)embedded, "
                  f"{n_removed} files removed. Run without --check to apply.",
                  file=sys.stderr)
        else:
            print("check: index is up to date, nothing to do.", file=sys.stderr)
        return

    if args.update and not to_embed_texts and not n_removed and prev_meta:
        print("up to date — no changes, skipping rewrite.", file=sys.stderr)
        return

    if to_embed_texts:
        fresh = embed(to_embed_texts)
        for row_idx, v in zip(to_embed_rows, fresh):
            vec_rows[row_idx] = np.asarray(v, dtype="float32")

    if not meta:
        sys.exit("error: no chunks produced — is the raw dir empty?")

    # Assemble vector matrix in row order.
    mat = np.asarray(vec_rows, dtype="float32")
    if mat.shape[1] != DIM:
        sys.exit(f"error: embedding dim {mat.shape[1]} != expected {DIM}")

    idx = TurboQuantIndex(dim=DIM, bit_width=args.bit_width)
    idx.add(mat)
    idx.prepare()
    idx.write(os.path.join(args.out, "index.tv"))

    # meta.json holds only metadata (light); raw vectors go to vectors.npy so
    # --update can reuse them without re-embedding.
    json.dump(meta, open(meta_path, "w"), ensure_ascii=False)
    np.save(vecs_path, mat)
    json.dump(
        {"model": MODEL, "base_url": BASE_URL,
         "dim": DIM, "bit_width": args.bit_width,
         "n_chunks": len(meta), "n_files": n_files, "hashes": hashes},
        open(manifest_path, "w"), ensure_ascii=False, indent=2,
    )
    print(f"OK index.tv + meta.json written to {args.out} "
          f"({len(meta)} chunks)", file=sys.stderr)


if __name__ == "__main__":
    main()
