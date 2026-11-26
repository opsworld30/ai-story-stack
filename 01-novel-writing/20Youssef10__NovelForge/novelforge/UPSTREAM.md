# Upstream

- Repository: 20Youssef10/NovelForge
- Repository URL: https://github.com/20Youssef10/NovelForge
- Branch: `main`
- Skill source path: `skills/`
- Entry Skill: `skills/novel-orchestrator/SKILL.md`
- Required dependency path: `templates/`
- Skill-directory last commit: `b255b090896bf1d0ac3ac87a0eccef8c654464b`
- Skill-directory last updated at: `2026-10-01T14:10:47Z` (UTC; path-specific commit metadata)
- Template-directory last commit: `b255b090896bf1d0ac3ac87a0eccef8c654464b`
- Template-directory last updated at: `2026-10-01T14:10:47Z` (UTC; path-specific commit metadata)
- License: MIT
- Original license: `LICENSE`
- License URL: https://github.com/20Youssef10/NovelForge/blob/main/LICENSE
- License blob at pinned source commit: `958bb11f0cf02852e04df89159b3b9554c063c05`
- Synchronized at: `2026-11-26T16:26:31Z` (UTC)

## Included upstream content

This is the complete Agent Skills bundle and its referenced project templates, not a mirror of the entire upstream repository.

| Content | Files |
|---|---:|
| Standalone `SKILL.md` files under `skills/` | 50 |
| Referenced `skills/*/references/` documents | 5 |
| Project, workspace, series and workflow templates under `templates/` | 59 |
| Original MIT license | 1 |
| **Upstream files included** | **115** |

All 50 Skill directories are preserved beneath `skills/`. The five referenced documents are included in their original relative locations. The complete `templates/` tree is included because the orchestrator and quality-gate Skills reference those templates. Both `skills/` and `templates/` resolve to the same path-specific commit and timestamp shown above.

## Excluded upstream repository content

The following repository-level material is not required to load the standard Agent Skills bundle and is not included:

- Agent-host integration manifests and path aliases: `.agents/`, `.claude-plugin/`, `.codex-plugin/`, `.gemini/`, `.opencode/`, `.github/`, `plugin.json`
- Optional host commands and session hooks: `commands/`, `hooks/`
- Development and validation tooling: `scripts/`, `AGENTS.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `.gitignore`
- Generated catalog, examples and repository overview: `catalog/`, `examples/`, `README.md`

These exclusions do not remove a dependency referenced by the included Skills: all Skill files, all five in-tree references and all project templates were retained. The source package contains Markdown only in the included paths; no symlinks or binary files were present.

## Static verification

- Every included upstream blob was fetched at the pinned commit and its SHA matched the recursive source tree.
- Skill-local `references/` links were checked against the included tree.
- The orchestrator's `templates/project/` dependency and the quality-gate's `templates/QUALITY_GATE.md` dependency are included.
- No upstream script was executed and no dependency was installed.
- The source license and copyright notice are retained unchanged.
