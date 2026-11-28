"""Tests for scripts/count_words.py.

Run: python3 -m unittest discover -s longform-fiction/tests -q
"""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
SCRIPT = SKILL / "scripts" / "count_words.py"
sys.path.insert(0, str(SKILL / "scripts"))

import count_words  # noqa: E402


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


class CountWordsTests(unittest.TestCase):
    def test_mixed_chinese_accented_latin_and_contractions(self) -> None:
        stats = count_words.count_text("你好世界 café naïve don't well-known 42\n第二行")
        self.assertEqual(stats["cjk_chars"], 7)
        self.assertEqual(stats["latin_words"], 5)
        self.assertEqual(stats["count"], 12)
        self.assertEqual(stats["lines"], 2)

    def test_directory_total_skip_dirs_exclude_and_dedup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "chapter-01.md").write_text("\ufeff甲乙丙\n", encoding="utf-8")
            (root / "chapter-02.txt").write_text("丁戊\n", encoding="utf-8")
            (root / "bible.md").write_text("故事圣经元数据", encoding="utf-8")
            (root / "chapter-contracts.md").write_text("章节合同", encoding="utf-8")
            (root / "notes.md").write_text("草稿笔记", encoding="utf-8")
            (root / "cover.png").write_bytes(b"not text")
            (root / ".git").mkdir()
            (root / ".git" / "notes.md").write_text("ignored", encoding="utf-8")
            (root / "node_modules").mkdir()
            (root / "node_modules" / "pkg.md").write_text("ignored", encoding="utf-8")

            # Directory scan skips bible.md & chapter-contracts.md by default; --exclude skips extras
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = count_words.main(
                    ["--json", "--exclude", "notes.md", str(root), str(root / "chapter-01.md")]
                )
            self.assertEqual(code, 0)
            report = json.loads(buf.getvalue())
            self.assertEqual(report["total"]["files"], 2)
            self.assertEqual(report["total"]["cjk_chars"], 5)
            self.assertEqual(report["total"]["non_space_chars"], 5)  # BOM stripped
            self.assertEqual(report["total"]["lines"], 2)

            # --include-planning counts bible.md and chapter-contracts.md when requested
            buf_inc = io.StringIO()
            with contextlib.redirect_stdout(buf_inc):
                code_inc = count_words.main(
                    ["--json", "--include-planning", "--exclude", "notes.md", str(root)]
                )
            self.assertEqual(code_inc, 0)
            self.assertEqual(json.loads(buf_inc.getvalue())["total"]["files"], 4)

            # Explicitly passing bible.md as a file argument still counts it
            buf_explicit = io.StringIO()
            with contextlib.redirect_stdout(buf_explicit):
                code_exp = count_words.main(["--json", str(root / "bible.md")])
            self.assertEqual(code_exp, 0)
            self.assertEqual(json.loads(buf_explicit.getvalue())["total"]["cjk_chars"], 7)

    def test_skip_dirs_does_not_reject_ancestor_directory_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            nested = Path(directory) / "node_modules" / "book"
            nested.mkdir(parents=True)
            (nested / "1.md").write_text("一二三", encoding="utf-8")
            files = count_words.manuscript_files(nested)
            self.assertEqual(files, [nested / "1.md"])

    def test_table_output_short_filename_alignment_and_utf8_cli(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            chapter = Path(directory) / "第一章.md"
            chapter.write_text("hello there\n", encoding="utf-8")
            result = run(str(chapter))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("第一章.md", result.stdout)
            self.assertIn("TOTAL", result.stdout)

            # Short filename alignment via in-process main
            short = Path(directory) / "1.md"
            short.write_text("abc", encoding="utf-8")
            buf = io.StringIO()
            cwd = Path.cwd()
            try:
                import os

                os.chdir(directory)
                with contextlib.redirect_stdout(buf):
                    code = count_words.main(["1.md"])
            finally:
                os.chdir(cwd)
            self.assertEqual(code, 0)
            lines = buf.getvalue().splitlines()
            self.assertEqual(len(lines[0]), len(lines[-1]))

    def test_missing_unreadable_and_empty_paths_fail(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = run(str(root / "missing.md"))
            self.assertEqual(result.returncode, 2)
            self.assertIn("count_words:", result.stderr)

            empty = root / "empty"
            empty.mkdir()
            result_empty = run(str(empty))
            self.assertEqual(result_empty.returncode, 2)
            self.assertIn("no manuscript files", result_empty.stderr)

            bad_utf8 = root / "bad.md"
            bad_utf8.write_bytes(b"\xff\xfe")
            buf_err = io.StringIO()
            with contextlib.redirect_stderr(buf_err):
                code = count_words.main([str(bad_utf8)])
            self.assertEqual(code, 2)
            self.assertIn("cannot read", buf_err.getvalue())


if __name__ == "__main__":
    unittest.main()
