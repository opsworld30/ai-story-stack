# Upstream Source Record

- Repository: https://github.com/wgwtest/novel-writing
- Branch: `main`
- Skill directory: `novel-writing/`
- Upstream commit affecting this Skill directory: `838729695148008d42c01bd7c3c0c1a5c15de830`
- Directory last updated (UTC): `2026-09-26T16:45:58Z`
- License: MIT; original `LICENSE` retained.
- Mirror type: functional dependency closure, not a full repository clone.
- Included upstream files: 15 (1 SKILL.md, 11 references, 1 optional Python script, 1 agent metadata file, 1 LICENSE).

## Included paths

- `novel-writing/SKILL.md`
- `novel-writing/references/*.md` (11 files)
- `novel-writing/scripts/check_manuscript_text.py`
- `novel-writing/agents/openai.yaml`
- `LICENSE`

## Excluded paths and reasons

The following repository-root items are outside the Skill directory and are not referenced as runtime dependencies by its entrypoint:

- `.github/`, `CODEX_START_HERE.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`: repository governance and contributor material.
- `README.md`, `README.zh-CN.md`: repository-level onboarding; this package has a locally authored Chinese overview.
- `assets/`, `docs/`, `examples/`: demonstration and explanatory material, not required by the Skill's runtime dependency chain.
- root `scripts/`, `tests/`: repository-level development and test files; the Skill's own optional checker under `novel-writing/scripts/` is included.

## Dependency and compatibility notes

- All reference files linked by `novel-writing/SKILL.md` are included.
- The optional Python checker uses only the standard library.
- `AGENTS.md` in the lifecycle reference is an example of a project-local rules file that may be created in the user's novel workspace; it is not an upstream package dependency.
- The upstream README describes this Skill as Codex-oriented. No broader host compatibility is claimed here.
- All upstream files were read statically; no scripts were executed and no dependencies were installed.
