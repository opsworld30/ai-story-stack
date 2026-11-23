# UPSTREAM

- **Source repository:** `klingai-tech/claude-plugin`
- **Source branch:** `main`
- **Source directory:** `skills/kling-ai-generate-image`
- **Skill URL:** https://github.com/klingai-tech/claude-plugin/tree/main/skills/kling-ai-generate-image
- **Entry file:** `skills/kling-ai-generate-image/SKILL.md`
- **Upstream directory commit:** `701145fb28641b5fd1289d6280ba7454ee56dbd4`
- **Upstream directory updated at (UTC):** `2026-11-18T06:51:45Z`
- **License:** MIT — root `LICENSE` from the source repository, copied unchanged into this package.
- **Synchronized at (UTC):** `2026-11-23T04:22:53Z`

## Package contents

- `skills/kling-ai-generate-image/SKILL.md`
- `skills/kling-ai-generate-image/references/prompt-construction.md`
- `skills/kling-ai-generate-image/references/scene-patterns.md`

- **Functional upstream files:** 3
- **Package license:** original MIT text, retained verbatim.
- **Shared connection configuration:** the bundle-level `.mcp.json` records the official Global endpoint `https://kling.ai/mcp/plugin`. It contains no credentials; the host performs OAuth.
- **Dependency closure:** This Skill links to the sibling `kling-ai` core Skill and uses its shared references for MCP, capability discovery, model parameters, asset workflows, billing and results. The core Skill is included as a sibling package in this bundle.

## Exclusions

Only the Agent Skill directory and its referenced Markdown dependencies are copied. The upstream plugin's marketplace/manifest files, README/marketing material, logo asset, release checklist, package metadata, verification script and tests are not part of this Skill package. No upstream script was executed. The MIT notice applies to the plugin source only; it does not license the Kling AI service or generated content.
