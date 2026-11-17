"""Shared embedding helper for chao-rag-wiki — provider-agnostic.

Talks to any OpenAI-compatible /embeddings endpoint. Configure via env:

  RAG_EMBED_BASE_URL   API base, no trailing /embeddings.
                       Default: https://qianfan.baidubce.com/v2
  RAG_EMBED_API_KEY    Bearer key. Falls back to QIANFAN_API_KEY (back-compat),
                       then OPENAI_API_KEY, so existing setups keep working.
  RAG_EMBED_MODEL      Model name. Default: bge-large-zh
  RAG_EMBED_DIM        Expected vector dimension. Default: 1024
  RAG_EMBED_BATCH      Inputs per request. Default: 16

Examples:
  Qianfan (default)  — nothing to set beyond QIANFAN_API_KEY.
  OpenAI             — RAG_EMBED_BASE_URL=https://api.openai.com/v1
                       RAG_EMBED_API_KEY=$OPENAI_API_KEY
                       RAG_EMBED_MODEL=text-embedding-3-small RAG_EMBED_DIM=1536
  Voyage (Anthropic's recommended embeddings; Claude has no embedding API)
                     — RAG_EMBED_BASE_URL=https://api.voyageai.com/v1
                       RAG_EMBED_API_KEY=$VOYAGE_API_KEY
                       RAG_EMBED_MODEL=voyage-3 RAG_EMBED_DIM=1024
  Any OpenAI-compatible gateway (OneAPI / OpenRouter / local vLLM) works the
  same way — just point BASE_URL/KEY/MODEL at it.

The request/response shape is the OpenAI standard ({"model","input"} ->
{"data":[{"embedding"}]}), which Qianfan also implements. Batches inputs and
retries transient failures so one flaky call doesn't abort a long build.
"""
import os
import sys
import time

import requests

DEFAULT_BASE_URL = "https://qianfan.baidubce.com/v2"

BASE_URL = os.environ.get("RAG_EMBED_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
MODEL = os.environ.get("RAG_EMBED_MODEL", "bge-large-zh")
DIM = int(os.environ.get("RAG_EMBED_DIM", "1024"))
BATCH = int(os.environ.get("RAG_EMBED_BATCH", "16"))


def api_key() -> str:
    """Resolve the API key, preferring the generic var but accepting legacy ones."""
    for var in ("RAG_EMBED_API_KEY", "QIANFAN_API_KEY", "OPENAI_API_KEY"):
        val = os.environ.get(var)
        if val:
            return val
    sys.exit("error: no embedding API key — set RAG_EMBED_API_KEY "
             "(or QIANFAN_API_KEY) in the environment")


def endpoint() -> str:
    return f"{BASE_URL}/embeddings"


def embed(texts, batch=BATCH, retries=4):
    """Embed a list of strings -> list of float vectors (insertion order)."""
    if not texts:
        return []
    key = api_key()
    url = endpoint()
    out = []
    for start in range(0, len(texts), batch):
        chunk = texts[start:start + batch]
        # Empty strings make some endpoints unhappy; substitute a single space.
        payload_input = [t if t.strip() else " " for t in chunk]
        last_err = None
        for attempt in range(retries):
            try:
                r = requests.post(
                    url,
                    headers={"Authorization": f"Bearer {key}",
                             "Content-Type": "application/json"},
                    json={"model": MODEL, "input": payload_input},
                    timeout=60,
                )
                if r.status_code != 200:
                    last_err = f"HTTP {r.status_code}: {r.text[:200]}"
                    raise RuntimeError(last_err)
                data = r.json()["data"]
                data.sort(key=lambda d: d["index"])
                out.extend(d["embedding"] for d in data)
                last_err = None
                break
            except Exception as e:  # noqa: BLE001 - retry any transient failure
                last_err = str(e)
                time.sleep(1.5 * (attempt + 1))
        if last_err is not None:
            sys.exit(f"error: embedding batch at offset {start} failed "
                     f"({url}, model={MODEL}): {last_err}")
        print(f"  embedded {min(start + batch, len(texts))}/{len(texts)}",
              file=sys.stderr, flush=True)
    return out
