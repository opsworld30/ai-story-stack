#!/usr/bin/env python3
"""Dependency-free length counter for long-form fiction manuscripts.

Count rule: every CJK ideograph is one unit; every run of Latin letters or digits is one
word. The default `count` is CJK ideographs plus Latin word tokens, which matches the
character targets used for Chinese manuscripts while staying sane for English text.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U000323af]")
LATIN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:['\u2019-][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*")
SUFFIXES = frozenset({".md", ".markdown", ".txt"})
SKIP_DIRS = frozenset({"node_modules", ".git", "__pycache__"})
DEFAULT_DIR_EXCLUDES = frozenset({"bible.md", "chapter-contracts.md"})


def count_text(text: str) -> dict[str, int]:
    cjk = len(CJK.findall(text))
    latin = len(LATIN.findall(text))
    return {
        "count": cjk + latin,
        "cjk_chars": cjk,
        "latin_words": latin,
        "non_space_chars": sum(1 for char in text if not char.isspace()),
        "lines": len(text.splitlines()),
    }


def _is_excluded(path: Path, root: Path | None, excludes: frozenset[str]) -> bool:
    if not excludes:
        return False
    if path.name in excludes:
        return True
    if root is not None:
        try:
            if path.relative_to(root).as_posix() in excludes:
                return True
        except ValueError:
            pass
    return False


def manuscript_files(
    path: Path,
    *,
    excludes: frozenset[str] = frozenset(),
    include_planning: bool = False,
) -> list[Path]:
    if path.is_file():
        return [] if _is_excluded(path, None, excludes) else [path]
    if not path.is_dir():
        raise OSError(f"not a file or directory: {path}")
    dir_excludes = excludes if include_planning else (excludes | DEFAULT_DIR_EXCLUDES)
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        here = Path(dirpath)
        for filename in sorted(filenames):
            item = here / filename
            if item.suffix.lower() not in SUFFIXES:
                continue
            if _is_excluded(item, path, dir_excludes):
                continue
            found.append(item)
    return found


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except (OSError, ValueError):
            pass

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="manuscript files or directories")
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="filename or relative POSIX path to skip (repeatable, e.g. --exclude notes.md)",
    )
    parser.add_argument(
        "--include-planning",
        action="store_true",
        help="include bible.md and chapter-contracts.md when scanning directories",
    )
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args(argv)

    excludes = frozenset(item.replace("\\", "/") for item in args.exclude)
    rows: list[dict] = []
    seen: set[Path] = set()
    for raw in args.paths:
        try:
            files = manuscript_files(raw, excludes=excludes, include_planning=args.include_planning)
        except OSError as exc:
            print(f"count_words: {exc}", file=sys.stderr)
            return 2
        for path in files:
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            try:
                text = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError) as exc:
                print(f"count_words: cannot read {path}: {exc}", file=sys.stderr)
                return 2
            rows.append({"file": str(path), **count_text(text)})

    if not rows:
        print("count_words: no manuscript files found", file=sys.stderr)
        return 2

    total = {
        key: sum(row[key] for row in rows)
        for key in ("count", "cjk_chars", "latin_words", "non_space_chars", "lines")
    }
    total["files"] = len(rows)
    if args.json:
        print(json.dumps({"files": rows, "total": total}, ensure_ascii=False, indent=2))
        return 0

    width = max(len("file"), len("TOTAL"), *(len(row["file"]) for row in rows))
    print(f"{'file'.ljust(width)}  {'count':>8}  {'cjk':>8}  {'words':>8}  {'lines':>8}")
    for row in rows:
        print(
            f"{row['file'].ljust(width)}  {row['count']:>8}  {row['cjk_chars']:>8}  "
            f"{row['latin_words']:>8}  {row['lines']:>8}"
        )
    print(
        f"{'TOTAL'.ljust(width)}  {total['count']:>8}  {total['cjk_chars']:>8}  "
        f"{total['latin_words']:>8}  {total['lines']:>8}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
