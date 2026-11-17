"""Query a chao-rag-wiki index — hybrid (dense + BM25 + full-text) retrieval.

Four modes (--mode):
  hybrid (default) — fuse dense vector search (turbovec), lexical BM25, and
                     literal full-text matching with Reciprocal Rank Fusion
                     (RRF). Best general recall.
  dense            — vector search only (semantic similarity).
  bm25             — keyword search only (exact-term / rare-token matches).
  fulltext         — literal substring / regex match only (verbatim phrases,
                     code identifiers, error strings, names). Use --regex to
                     treat the query as a regular expression.

Dense uses the same embedding model as the build; BM25 and full-text are built
on the fly from meta.json chunk texts, so no rebuild is needed to use them.

Output: human-readable by default, or --json for the LLM to synthesize from.

Usage:
  python query_rag.py --out OUT_DIR --query "..." [-k 8] [--mode hybrid]
                      [--json] [--full] [--rrf-k 60] [--regex]
"""
import argparse
import json
import os
import sys

import numpy as np
from turbovec import TurboQuantIndex

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from embed import embed, MODEL, BASE_URL  # noqa: E402
from bm25 import BM25  # noqa: E402
from fulltext import FullText  # noqa: E402
from ragpaths import default_out  # noqa: E402

# How many candidates each retriever contributes before fusion. Wider than the
# final k so fusion has material to reorder.
CANDIDATE_POOL = 50


def dense_search(out_dir, query, meta_len, k):
    """Return [(row_id, raw_score), …] from turbovec, best first."""
    idx = TurboQuantIndex.load(os.path.join(out_dir, "index.tv"))
    qv = np.asarray(embed([query]), dtype="float32")
    scores, ids = idx.search(qv, k=min(k, meta_len))
    scores = np.asarray(scores).ravel().tolist()
    ids = np.asarray(ids).ravel().tolist()
    return [(int(i), float(s)) for s, i in zip(scores, ids)
            if 0 <= int(i) < meta_len]


def rrf_fuse(rank_lists, rrf_k=60):
    """Reciprocal Rank Fusion: combine ranked lists by 1/(rrf_k + rank).

    rank_lists: list of [(row_id, _score), …], each already sorted best-first.
    Returns [(row_id, fused_score), …] sorted best-first. Scores from the two
    retrievers live on different scales, so we fuse on RANK, not raw score.
    """
    fused = {}
    for ranked in rank_lists:
        for rank, (rid, _score) in enumerate(ranked):
            fused[rid] = fused.get(rid, 0.0) + 1.0 / (rrf_k + rank)
    return sorted(fused.items(), key=lambda x: x[1], reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None,
                    help="index dir from build_rag.py "
                         "(default: $RAG_ROOT/.rag, else ./.rag)")
    ap.add_argument("--query", required=True)
    ap.add_argument("-k", type=int, default=8)
    ap.add_argument("--mode", choices=["hybrid", "dense", "bm25", "fulltext"],
                    default="hybrid")
    ap.add_argument("--regex", action="store_true",
                    help="treat the query as a regex for the full-text leg")
    ap.add_argument("--rrf-k", type=int, default=60,
                    help="RRF constant; higher = flatter rank weighting")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--full", action="store_true",
                    help="print full chunk text instead of a snippet")
    ap.add_argument("--rerank", action="store_true",
                    help="LLM-rerank the candidate pool before taking top-k")
    ap.add_argument("--rerank-pool", type=int, default=20,
                    help="how many retrieved candidates to rerank (default 20)")
    args = ap.parse_args()
    if args.out is None:
        args.out = default_out()

    meta_path = os.path.join(args.out, "meta.json")
    tv_path = os.path.join(args.out, "index.tv")
    if not os.path.exists(meta_path):
        sys.exit(f"error: no index in {args.out} — run build_rag.py first")
    if args.mode in ("dense", "hybrid") and not os.path.exists(tv_path):
        sys.exit(f"error: {tv_path} missing — needed for mode={args.mode}")

    meta = json.load(open(meta_path))
    n = len(meta)

    # Dense search re-embeds the query, so the live embedding config must match
    # what the index was built with — otherwise vectors are incomparable.
    if args.mode in ("dense", "hybrid"):
        manifest_path = os.path.join(args.out, "manifest.json")
        if os.path.exists(manifest_path):
            man = json.load(open(manifest_path))
            built_model = man.get("model")
            built_url = man.get("base_url")
            if built_model and built_model != MODEL:
                sys.exit(f"error: index was built with model '{built_model}' but "
                         f"RAG_EMBED_MODEL is '{MODEL}'. Use the same model, or "
                         f"rebuild. (mode=bm25 needs no embedding and is unaffected.)")
            if built_url and built_url != BASE_URL:
                print(f"warning: index built against {built_url} but querying "
                      f"{BASE_URL}; results assume the same model behind both.",
                      file=sys.stderr)

    dense_ranked = []
    bm25_ranked = []
    fulltext_ranked = []
    if args.mode in ("dense", "hybrid"):
        dense_ranked = dense_search(args.out, args.query, n, CANDIDATE_POOL)
    if args.mode in ("bm25", "hybrid"):
        bm = BM25([m["text"] for m in meta])
        bm25_ranked = bm.top_k(args.query, CANDIDATE_POOL)
    if args.mode in ("fulltext", "hybrid"):
        ft = FullText([m["text"] for m in meta])
        fulltext_ranked = ft.top_k(args.query, CANDIDATE_POOL, use_regex=args.regex)

    # Per-source score lookups so we can annotate each fused hit.
    dense_by_id = dict(dense_ranked)
    bm25_by_id = dict(bm25_ranked)
    fulltext_by_id = dict(fulltext_ranked)

    if args.mode == "dense":
        ordered = dense_ranked
    elif args.mode == "bm25":
        ordered = bm25_ranked
    elif args.mode == "fulltext":
        ordered = fulltext_ranked
    else:
        ordered = rrf_fuse([dense_ranked, bm25_ranked, fulltext_ranked],
                           rrf_k=args.rrf_k)

    # Optional LLM rerank: re-score the top `rerank-pool` candidates by true
    # relevance and reorder. Best-effort — on any failure we keep retrieval
    # order. We rerank a pool wider than k so the LLM can pull a better hit up.
    reranked = False
    rr_scores = {}
    if args.rerank and ordered:
        from rerank import rerank as llm_rerank  # lazy import
        pool_size = max(args.rerank_pool, args.k)
        base_pool = ordered[:pool_size]          # [(row_id, retrieval_score), …]
        cands = [meta[rid] for rid, _ in base_pool]
        order, scores = llm_rerank(args.query, cands)
        if order is not None:
            # scores[i] is the LLM score for base_pool[i]; `order` sorts them.
            rr_scores = {base_pool[i][0]: scores[i] for i in range(len(base_pool))}
            ordered = [base_pool[i] for i in order] + ordered[pool_size:]
            reranked = True

    results = []
    for rid, score in ordered[:args.k]:
        m = meta[rid]
        results.append({
            "score": round(float(score), 4),
            "rerank": round(float(rr_scores[rid]), 2) if rid in rr_scores else None,
            "dense": round(dense_by_id[rid], 4) if rid in dense_by_id else None,
            "bm25": round(bm25_by_id[rid], 4) if rid in bm25_by_id else None,
            "fulltext": (int(fulltext_by_id[rid])
                         if rid in fulltext_by_id else None),
            "path": m["path"],
            "dups": m.get("dups", []),
            "title": m["title"],
            "heading": m.get("heading", ""),
            "text": m["text"],
        })

    if args.json:
        print(json.dumps({"query": args.query, "mode": args.mode,
                          "reranked": reranked, "results": results},
                         ensure_ascii=False, indent=2))
        return

    rr_tag = "  +rerank" if reranked else ""
    print(f"Query: {args.query}   [mode={args.mode}{rr_tag}]\n{'=' * 60}")
    for i, r in enumerate(results, 1):
        loc = r["path"] + (f"  ›  {r['heading']}" if r["heading"] else "")
        if r["dups"]:
            loc += f"  (+{len(r['dups'])} dup copies)"
        tags = []
        if r["rerank"] is not None:
            tags.append(f"rerank={r['rerank']}")
        if r["dense"] is not None:
            tags.append(f"dense={r['dense']}")
        if r["bm25"] is not None:
            tags.append(f"bm25={r['bm25']}")
        if r["fulltext"] is not None:
            tags.append(f"fulltext={r['fulltext']}")
        tagstr = ("  (" + " ".join(tags) + ")") if tags else ""
        body = r["text"] if args.full else (r["text"][:280] +
                                            ("…" if len(r["text"]) > 280 else ""))
        print(f"\n[{i}] score={r['score']}{tagstr}  {r['title']}\n"
              f"    {loc}\n    {body}")


if __name__ == "__main__":
    main()
