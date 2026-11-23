# Upstream

- Repository: https://github.com/klingai-tech/claude-plugin
- Branch: main
- Skill path: `skills/kling-ai-generate-video`
- Skill URL: https://github.com/klingai-tech/claude-plugin/tree/main/skills/kling-ai-generate-video
- Upstream directory commit: `53ff743cec8322f5930d86d4e1bf34fe485769e5`
- Upstream directory updated at: `2026-11-20T03:07:27Z` (UTC)
- License: MIT; original repository-root LICENSE is at the owner/repo package root, unchanged (Copyright (c) KLING AI Pte Ltd).
- Mirrored files in this Skill directory: 5 (SKILL.md, required references, this UPSTREAM.md).
- Sync time: `2026-11-23T04:05:01Z` (UTC)
- Function: Kling video generation, motion, model routing and shot planning.
- Dependency closure: this package includes all three sibling Skill directories because specialized instructions use relative links to the base Skill and shared references.
- Runtime: configure the Global MCP endpoint `https://kling.ai/mcp/plugin` and authorize a Global Kling account in the host; service access, credits and OAuth remain external.
- Excluded: Claude/Copilot/Gemini plugin manifests, marketplace metadata, package/CLI files, tests, integration scripts and unrelated plugin documentation; not required by the Markdown Skill files.
- Safety: static copy only; no scripts executed, no packages installed, no credentials accessed and no generated assets copied.