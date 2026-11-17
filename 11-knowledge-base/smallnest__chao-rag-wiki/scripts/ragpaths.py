"""Resolve the RAG working directory for chao-rag-wiki.

The corpus (`raw/`) and generated index (`.rag/`) live under a single root.
That root is `RAG_ROOT` if the env var is set, otherwise the current working
directory. `--raw` / `--out` still override these per-invocation.
"""
import os


def rag_root() -> str:
    """RAG_ROOT if set (and non-empty), else the current working directory."""
    return os.environ.get("RAG_ROOT") or os.getcwd()


def default_raw() -> str:
    return os.path.join(rag_root(), "raw")


def default_out() -> str:
    return os.path.join(rag_root(), ".rag")
