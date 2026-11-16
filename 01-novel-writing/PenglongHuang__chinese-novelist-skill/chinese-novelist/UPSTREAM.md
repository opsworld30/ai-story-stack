# Upstream & Mirror Record

- Project: `PenglongHuang/chinese-novelist-skill`
- Upstream: https://github.com/PenglongHuang/chinese-novelist-skill
- Branch: `master`
- Upstream commit: `d1fb0ca5737ded47934b366b10b8d50b52557e57`
- Commit time: `2026-11-15T09:24:34Z`
- Upstream version: `2.3.2` (README / ROADMAP)
- License: MIT
- License file: [LICENSE](./LICENSE) (copied verbatim)
- Source Skill: [SKILL.md](./SKILL.md)
- Mirror date: 2026-11-16
- Mirror type: functional Skill package; not a full repository clone.
- Upstream files mirrored: 25 (SKILL.md, LICENSE, 18 references, 3 scripts, 2 tests)
- Local maintenance documents: README.md, UPSTREAM.md

## Integrity and dependency review

- All 18 Markdown references used by the entry Skill and referenced recursively by those references are present in the mirror.
- All 3 runtime scripts and 2 Node.js test files are included.
- Static inspection found Node.js built-in imports and local filesystem operations. The validator invokes the local Node runtime to run the companion word-count script; no remote API calls or telemetry were found in the five scripts inspected.
- Runtime dependency: Node.js. No package.json or external npm package is required by the mirrored scripts.
- Parallel and Agent Teams modes depend on capabilities exposed by the user's Agent host.
- Tests are included but were not executed during this static mirror operation.

## Excluded upstream paths

- `assets/**` (7 PNG files): promotional banners, screenshots, and a WeChat group QR image. They are not referenced by the runtime Skill flow; separate asset rights were not established.
- `.github/FUNDING.yml`: repository sponsorship metadata, not required at runtime.
- Original upstream README and ROADMAP are not mirrored verbatim because the README embeds excluded promotional assets and sponsor content. See upstream originals:
  - https://github.com/PenglongHuang/chinese-novelist-skill/blob/master/README.md
  - https://github.com/PenglongHuang/chinese-novelist-skill/blob/master/ROADMAP.md

The upstream MIT license is retained. This mirror does not claim that excluded promotional assets are covered by the code license.
