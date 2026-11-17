"""Lexical (BM25) retrieval for chao-rag-wiki — the keyword half of hybrid RAG.

Built at query time from meta.json chunk texts (no separate index file), so it
works against any existing index with no rebuild. Corpora here are mixed
zh/en, so the tokenizer is CJK-aware:
  - ASCII runs are lowercased and split into word tokens.
  - CJK runs are split into overlapping character bigrams (a cheap,
    dependency-free stand-in for word segmentation that works well for BM25).

Pure Python + the stdlib only — no extra deps in the venv.
"""
import math
import re
from collections import Counter

_TOKEN_RE = re.compile(r"[a-z0-9]+", re.IGNORECASE)
_CJK_RE = re.compile(r"[一-鿿぀-ヿ가-힯]")


def tokenize(text: str):
    """Mixed zh/en tokenizer: ASCII words + CJK character bigrams."""
    text = text.lower()
    tokens = []
    # ASCII / alphanumeric words.
    tokens.extend(_TOKEN_RE.findall(text))
    # CJK: contiguous runs -> overlapping bigrams (plus unigrams for 1-char runs).
    for run in re.findall(r"[一-鿿぀-ヿ가-힯]+", text):
        if len(run) == 1:
            tokens.append(run)
        else:
            tokens.extend(run[i:i + 2] for i in range(len(run) - 1))
    return tokens


class BM25:
    """Okapi BM25 over a fixed list of documents (chunk texts)."""

    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.doc_tokens = [tokenize(d) for d in docs]
        self.doc_len = [len(t) for t in self.doc_tokens]
        self.n = len(docs)
        self.avgdl = (sum(self.doc_len) / self.n) if self.n else 0.0

        self.tf = [Counter(t) for t in self.doc_tokens]
        df = Counter()
        for tfd in self.tf:
            df.update(tfd.keys())
        # BM25+ idf (always positive), avoids negative weights for common terms.
        self.idf = {
            term: math.log(1 + (self.n - freq + 0.5) / (freq + 0.5))
            for term, freq in df.items()
        }

    def scores(self, query: str):
        """Return a list of BM25 scores, one per document (index-aligned)."""
        q_terms = [t for t in tokenize(query) if t in self.idf]
        out = [0.0] * self.n
        if not q_terms:
            return out
        for i in range(self.n):
            tfd = self.tf[i]
            if not tfd:
                continue
            dl = self.doc_len[i]
            denom_norm = self.k1 * (1 - self.b + self.b * dl / (self.avgdl or 1))
            s = 0.0
            for term in q_terms:
                f = tfd.get(term, 0)
                if f:
                    s += self.idf[term] * (f * (self.k1 + 1)) / (f + denom_norm)
            out[i] = s
        return out

    def top_k(self, query: str, k: int):
        """Return [(doc_index, score), …] for the top-k by BM25, score>0 only."""
        scored = list(enumerate(self.scores(query)))
        scored = [(i, s) for i, s in scored if s > 0]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]
