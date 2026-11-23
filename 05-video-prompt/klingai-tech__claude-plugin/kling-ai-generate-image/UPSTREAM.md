# Upstream

- Repository: https://github.com/klingai-tech/claude-plugin
- Branch: main
- Skill path: `skills/kling-ai-generate-image`
- Skill URL: https://github.com/klingai-tech/claude-plugin/tree/main/skills/kling-ai-generate-image
- Upstream directory commit: `701145fb28641b5fd1289d6280ba7454ee56dbd4`
- Upstream directory updated at: `2026-11-18T06:51:45Z` (UTC)
- License: MIT; original repository-root LICENSE is at the owner/repo package root, unchanged (Copyright (c) KLING AI Pte Ltd).
- Mirrored files in this Skill directory: 4 (SKILL.md, required references, this UPSTREAM.md).
- Sync time: `2026-11-23T04:05:01Z` (UTC)
- Function: Kling image-generation prompt construction and scene workflows.
- Dependency closure: this package includes all three sibling Skill directories because specialized instructions use relative links to the base Skill and shared references.
- Runtime: configure the Global MCP endpoint `https://kling.ai/mcp/plugin` and authorize a Global Kling account in the host; service access, credits and OAuth remain external.
- Excluded: Claude/Copilot/Gemini plugin manifests, marketplace metadata, package/CLI files, tests, integration scripts and unrelated plugin documentation; not required by the Markdown Skill files.
- Safety: static copy only; no scripts executed, no packages installed, no credentials accessed and no generated assets copied.