# UPSTREAM

- Source repository: https://github.com/netflypsb/webnovel-mcp
- Source Skill directory: `webnovel-author/`
- Skill URL: https://github.com/netflypsb/webnovel-mcp/tree/main/webnovel-author
- Skill entry: https://github.com/netflypsb/webnovel-mcp/blob/main/webnovel-author/SKILL.md
- Upstream directory commit: `2f772e74e14cdb97c669a3cef7f56c25509b8b95`
- `last_upstream_updated_at`: `2026-03-30T02:08:57Z` (UTC)
- License: MIT (original repository-root `LICENSE` retained as `LICENSE`)
- License source: https://github.com/netflypsb/webnovel-mcp/blob/2f772e74e14cdb97c669a3cef7f56c25509b8b95/LICENSE
- Synced at: `2026-11-25T16:53:21.531Z` (UTC)
- Package scope: all 14 files beneath the upstream `webnovel-author/` Skill directory, plus the original MIT license and this provenance file.

## Host integration boundary

The Skill describes host-provided file and scratchpad operations such as `read_skill_file`, `createFile`, `writeFile` and `scratchpad_write`. These are not bundled implementations. The upstream repository also contains a separate Python MCP server and optional Pro licensing integration; that application, its server code and its dependencies are outside this Skill directory and are not included in this package. Adapt the host operations to the target agent environment before relying on them.

## Mirrored upstream files

- `SKILL.md`
- `chapters/chapter-template.md`
- `characters/change-log-template.json`
- `characters/template.md`
- `examples/cultivation-system.md`
- `examples/foreshadowing-example.json`
- `metadata/foreshadowing-tracker-template.json`
- `prompts/style-guide.md`
- `templates/litconfig.json`
- `templates/litrpg-stats-tracker.json`
- `templates/novel.json`
- `templates/romance-arc-tracker.json`
- `worldbuilding/timeline-template.json`
- `worldbuilding/world-state-template.json`
- `LICENSE` (repository-root MIT license)
