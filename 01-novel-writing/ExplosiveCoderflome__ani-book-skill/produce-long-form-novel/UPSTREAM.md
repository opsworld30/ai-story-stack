# UPSTREAM

## Source

- Repository: [ExplosiveCoderflome/ani-book-skill](https://github.com/ExplosiveCoderflome/ani-book-skill)
- Source path: repository root; entry file `SKILL.md`
- Branch: `main`
- Pinned commit: [`c2750bfa1bb687d6b94abf11b3399d81b264d962`](https://github.com/ExplosiveCoderflome/ani-book-skill/commit/c2750bfa1bb687d6b94abf11b3399d81b264d962)
- `last_upstream_updated_at`: `2026-11-20T17:34:46Z` (UTC, latest commit touching the Skill source path)
- Version file: `VERSION` = `0.3.1`
- License: Apache-2.0
- License evidence: upstream `LICENSE` and `NOTICE`; both are copied unchanged. The NOTICE states that Apache-2.0 applies to files contained in this repository and distinguishes the separately licensed AI-Novel-Writing-Assistant source project. No files from that separate project were copied.

## Mirror scope

This is a **functional Skill package mirror**, not a clone of the full upstream repository.

- Upstream files mirrored: **49**
- Main entry: `SKILL.md`
- References: 27 files under `references/`
- Scripts: 13 files under `scripts/` (copied as data; never executed)
- Agent metadata: `agents/openai.yaml`
- Runtime declaration: `requirements.txt` (`PyYAML>=6.0,<7`)
- Version: `VERSION`
- Workspace templates: 2 files under `assets/workspace-template/production/`
- Linked QA reference: `docs/qa/2026-10-15-behavioral-regressions.md`
- Original licensing: `LICENSE`, `NOTICE`

## Excluded upstream paths and reasons

- `.github/**` (including `.github/workflows/validate.yml`): repository workflow/issue templates; not part of Skill runtime and no GitHub Actions are used here.
- `.gitattributes`, `.gitignore`: repository housekeeping.
- `AGENTS.md`: untrusted repository instructions; not required by the Skill and not copied.
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`: repository governance/support documents, not Skill runtime dependencies.
- `README.md`, `README.en.md`: replaced by a locally authored archive README; upstream links and commit are retained here.
- `apps/workspace-reader/**`: a separate React application with its own package manifest, server and UI. The Codex-native Skill does not require it; full applications are excluded from the published Skill package.
- `assets/workflow-hero.png`: 1.66 MB marketing/hero image, not consumed by the Skill.
- `docs/design/readme-hero.md`, `docs/plans/**`, `docs/releases/**`: design, planning and release-history documentation, not required for the Skill workflow.
- `docs/examples/书中末行/**`: example manuscript and screenshot; not required by the Skill and not copied as third-party/example content.
- `tests/**`: development test suite, not a runtime dependency; not executed.
- `analyses/.gitkeep`, `libraries/.gitkeep`, `novels/.gitkeep`, `trends/.gitkeep`: empty workspace placeholders; user workspaces are created as needed.
- The referenced QA file under `docs/qa/` is included; no other QA file was present in the pinned tree.

## Known upstream documentation gaps

- `references/ai-novel-writing-assistant-v2-adapter.md` mentions `docs/wiki/**` paths that are absent from the pinned upstream tree.
- `references/remote-skill-sources.md` mentions legacy `scripts/list-skills.py` and `scripts/install-skill-from-github.py`; these files are absent from the pinned tree. The current `scripts/skill_sources.py` is preserved, but no equivalence is assumed.

These unresolved links are recorded as upstream documentation gaps, not silently replaced. The main Skill entry's references and script files included in this mirror are present.

## Safety and validation

- All files were retrieved at the single pinned commit above and copied statically.
- No upstream script was executed; no dependencies were installed; no tests or app were run.
- This process confirms file presence and provenance, not runtime behavior.
- Sync time: `2026-11-22T16:53:30Z` (UTC).
