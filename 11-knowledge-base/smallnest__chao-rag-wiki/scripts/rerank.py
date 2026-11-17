"""LLM listwise reranker for chao-rag-wiki.

After hybrid retrieval returns a candidate pool, this re-scores each candidate's
true relevance to the query with an LLM (a cross-encoder-style judge), which
catches cases pure vector/keyword similarity gets wrong — and reorders.

Provider-agnostic OpenAI-compatible chat endpoint, configured via env:

  RAG_RERANK_BASE_URL  chat API base (no /chat/completions).
                       Default: RAG_EMBED_BASE_URL, else Qianfan v2.
  RAG_RERANK_API_KEY   Bearer key. Falls back to the embedding key chain
                       (RAG_EMBED_API_KEY / QIANFAN_API_KEY / OPENAI_API_KEY).
  RAG_RERANK_MODEL     chat model. Default: ernie-3.5-8k

Listwise design: the model sees the query + all candidates at once and returns
a JSON array of per-candidate relevance scores (0-10). One call reranks the
whole pool, which is cheaper and more consistent than scoring each pair. On any
failure the caller keeps the original order, so rerank is always best-effort.
"""
import json
import os
import re
import sys

import requests

# Reuse the embedding provider's config as the default chat provider.
_EMBED_BASE = os.environ.get("RAG_EMBED_BASE_URL", "https://qianfan.baidubce.com/v2")
BASE_URL = os.environ.get("RAG_RERANK_BASE_URL", _EMBED_BASE).rstrip("/")
MODEL = os.environ.get("RAG_RERANK_MODEL", "ernie-3.5-8k")
SNIPPET_CHARS = int(os.environ.get("RAG_RERANK_SNIPPET", "500"))


def _api_key():
    for var in ("RAG_RERANK_API_KEY", "RAG_EMBED_API_KEY",
                "QIANFAN_API_KEY", "OPENAI_API_KEY"):
        v = os.environ.get(var)
        if v:
            return v
    return None


def _build_prompt(query, candidates):
    lines = [
        "You are a search-relevance judge. Score how well each document "
        "answers the query, from 0 (irrelevant) to 10 (directly answers it).",
        "Judge meaning, not keyword overlap. Penalize off-topic or boilerplate.",
        "",
        f"Query: {query}",
        "",
        "Documents:",
    ]
    for i, c in enumerate(candidates):
        head = (c.get("title") or "").strip()
        sub = (c.get("heading") or "").strip()
        body = (c.get("text") or "").strip().replace("\n", " ")[:SNIPPET_CHARS]
        label = f"{head} › {sub}" if sub else head
        lines.append(f"[{i}] {label}\n{body}")
    lines += [
        "",
        f"Return ONLY a JSON array of {len(candidates)} objects "
        '{"i": <index>, "score": <0-10>}, no prose.',
    ]
    return "\n".join(lines)


def _parse_scores(content, n):
    """Extract per-index scores from the model's reply; tolerant of stray text."""
    m = re.search(r"\[.*\]", content, re.DOTALL)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
    except json.JSONDecodeError:
        return None
    scores = [0.0] * n
    seen = False
    for obj in arr:
        try:
            i = int(obj["i"])
            s = float(obj["score"])
        except (KeyError, ValueError, TypeError):
            continue
        if 0 <= i < n:
            scores[i] = s
            seen = True
    return scores if seen else None


def rerank(query, candidates, timeout=60):
    """Return (order, scores) where order is candidate indices best-first.

    Best-effort: on any failure returns (None, None) so the caller can fall
    back to the pre-rerank order. `candidates` is a list of dicts with
    title/heading/text.
    """
    if not candidates:
        return None, None
    key = _api_key()
    if not key:
        print("  rerank skipped: no API key resolvable", file=sys.stderr)
        return None, None

    url = f"{BASE_URL}/chat/completions"
    payload = {
        "model": MODEL,
        "messages": [{"role": "user",
                      "content": _build_prompt(query, candidates)}],
        "temperature": 0,
        "max_tokens": 2048,
    }
    try:
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {key}",
                     "Content-Type": "application/json"},
            json=payload, timeout=timeout,
        )
        if r.status_code != 200:
            print(f"  rerank skipped: HTTP {r.status_code}: {r.text[:160]}",
                  file=sys.stderr)
            return None, None
        content = r.json()["choices"][0]["message"]["content"]
    except Exception as e:  # noqa: BLE001 - best-effort, never fatal
        print(f"  rerank skipped: {e}", file=sys.stderr)
        return None, None

    scores = _parse_scores(content, len(candidates))
    if scores is None:
        print("  rerank skipped: could not parse model output", file=sys.stderr)
        return None, None

    order = sorted(range(len(candidates)), key=lambda i: scores[i], reverse=True)
    return order, scores
