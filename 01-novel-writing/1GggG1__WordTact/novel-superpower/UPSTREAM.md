# UPSTREAM

- **Upstream repository:** [1GggG1/WordTact](https://github.com/1GggG1/WordTact)
- **Upstream path:** `novel/`
- **Agent Skill entry:** [novel/SKILL.md](https://github.com/1GggG1/WordTact/blob/63e7c402c03f845b5c1db0df654a8030154d27c2/novel/SKILL.md)
- **Pinned upstream commit:** `63e7c402c03f845b5c1db0df654a8030154d27c2`
- **Path-specific upstream update time:** `2026-11-04T09:30:56Z` (UTC)
- **License:** MIT; original `LICENSE` retained. Copyright: 2026 1GggG1.
- **Synced at:** `2026-11-27T03:58:59Z` (UTC)
- **Package:** `novel-superpower`, one dispatcher Skill plus eight child Skills.

## Package scope

This mirror preserves the complete runtime Skill bundle from `novel/`:

- `LICENSE`, `README.md`, and the root `SKILL.md`
- All eight child Skill directories under `user/`
- Every referenced Markdown resource and runtime Python script under those child directories
- `novel-expander/THIRD_PARTY_NOTICES.md`, including its upstream Humanizer-zh and Humanizer MIT notices

The 58 retained upstream files (529,984 bytes) are copied with their relative paths intact. This includes nine `SKILL.md` entrypoints in total (the dispatcher plus eight child Skills).

## Explicit exclusions

The upstream `novel/` tree contains 110 files. The following 52 development/validation files are excluded because they are not loaded as runtime Skill dependencies:

- `design/**` (22 files): maintainer blueprints, contracts, implementation goals, dispatch/design notes, and test catalogues.
- `tests/**` (28 files): test code and test fixtures.
- `scripts/build_source_package.py` and `scripts/validate_source_package.py` (2 files): source-package build/validation utilities.

No runtime Skill file, relative reference, or runtime script under `user/` was excluded. The README's benchmark reference points outside the `novel/` package and remains an upstream link; it is not a runtime dependency.

## Handling and verification

All source files were read from the pinned commit tree and copied statically. No upstream scripts were executed, no dependencies were installed, and no tests were run. The original MIT license and third-party notices are preserved.