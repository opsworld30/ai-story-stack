# Upstream

- Source repository: https://github.com/kevinchin12/storyboard-director
- Branch: `main`
- Source Skill directory: `storyboard-scene-pipeline-skill/`
- Skill entry: `storyboard-scene-pipeline-skill/SKILL.md`
- Skill URL: https://github.com/kevinchin12/storyboard-director/tree/main/storyboard-scene-pipeline-skill
- Upstream directory commit: `208782096ad7be19d609b4f3f70568507245ef30`
- `last_upstream_updated_at`: `2026-07-30T03:47:47Z` (UTC)
- License: MIT (the original repository-root `LICENSE` is included unchanged as `LICENSE`)
- Upstream Skill-directory files mirrored: 28 (all files beneath the Skill directory)
- Local package files: 30 (28 upstream Skill-directory files + original `LICENSE` + this `UPSTREAM.md`)
- Synced at: `2026-11-26T04:23:12Z` (UTC)
- Package scope: main storyboard-director Skill, four nested stage Skills, Agent metadata, session templates, integration notes and all 14 scripts.
- Excluded: no files within `storyboard-scene-pipeline-skill/`; repository-level README, GitHub configuration/workflows and unrelated files outside the Skill directory are excluded. The root MIT license is retained.
- Runtime notes: the Skill expects a host that provides image generation. Python scripts use the standard library; Pillow is used by image normalization/reference and storyboard-sheet operations. The upstream package does not pin a Pillow version.
- Audit: static path/reference review completed. All four nested stage Skills and their local script/template dependencies are included. No upstream scripts, installer, tests or dependencies were executed or installed during synchronization.
- Note: this is a complete functional mirror of the registered Skill directory, not a clone of the entire upstream repository.
