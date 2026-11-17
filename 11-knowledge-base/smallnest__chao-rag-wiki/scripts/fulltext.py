"""Literal full-text matching for chao-rag-wiki — the exact-string leg of hybrid.

Unlike BM25 (tokenized, ranked) or dense (semantic), this matches the query as a
literal substring (case-insensitive), or as a regex with use_regex=True, against
each chunk text. It only fires when the exact string appears, so in hybrid it
boosts chunks containing verbatim phrases, code identifiers, error strings, or
names, and contributes nothing when there is no literal hit — leaving dense+BM25
to carry paraphrased queries.

Built at query time from meta.json chunk texts: no index file, no rebuild, no
API key. Pure Python + stdlib only.
"""
import re


class FullText:
    """Literal / regex substring matcher over a fixed list of chunk texts."""

    def __init__(self, docs):
        self.docs = docs
        self._lower = [d.lower() for d in docs]

    def scores(self, query: str, use_regex: bool = False):
        """Return a match count per document (index-aligned)."""
        out = [0.0] * len(self.docs)
        q = query.strip()
        if not q:
            return out
        if use_regex:
            try:
                pat = re.compile(query, re.IGNORECASE)
            except re.error:
                return out  # invalid regex → contribute nothing, don't crash
            for i, d in enumerate(self.docs):
                out[i] = float(len(pat.findall(d)))
        else:
            ql = q.lower()
            for i, d in enumerate(self._lower):
                out[i] = float(d.count(ql))
        return out

    def top_k(self, query: str, k: int, use_regex: bool = False):
        """Return [(doc_index, count), …] for the top-k by match count, >0 only."""
        scored = [(i, s) for i, s in enumerate(self.scores(query, use_regex))
                  if s > 0]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:k]
