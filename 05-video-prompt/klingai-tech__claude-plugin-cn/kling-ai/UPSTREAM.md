# UPSTREAM

- **Source repository:** `klingai-tech/claude-plugin-cn`
- **Source branch:** `main`
- **Source directory:** `skills/kling-ai`
- **Skill URL:** https://github.com/klingai-tech/claude-plugin-cn/tree/main/skills/kling-ai
- **Entry file:** `skills/kling-ai/SKILL.md`
- **Upstream directory commit:** `b6fab2b12d159301038a726716e3fc35e4e18ca7`
- **Upstream directory updated at (UTC):** `2026-11-20T02:58:05Z`
- **License:** MIT — root `LICENSE` from the source repository, copied unchanged into this package.
- **Synchronized at (UTC):** `2026-11-23T04:22:53Z`

## Package contents

- `skills/kling-ai/SKILL.md`
- `skills/kling-ai/references/asset-workflows.md`
- `skills/kling-ai/references/capability-discovery.md`
- `skills/kling-ai/references/mcp-contract.md`
- `skills/kling-ai/references/model-parameters.md`
- `skills/kling-ai/references/prompt-examples.md`
- `skills/kling-ai/references/tool-workflows.md`
- `skills/kling-ai/references/troubleshooting.md`

- **Functional upstream files:** 8
- **Package license:** original MIT text, retained verbatim.
- **Shared connection configuration:** the bundle-level `.mcp.json` records the official China endpoint `https://klingai.com/mcp/plugin`. It contains no credentials; the host performs OAuth.
- **Dependency closure:** This core router is cross-linked to the sibling `kling-ai-generate-image` and `kling-ai-generate-video` Skill directories in the same bundle. Install/use the three sibling Skill directories together to preserve those relative links.

## Exclusions

Only the Agent Skill directory and its referenced Markdown dependencies are copied. The upstream plugin's marketplace/manifest files, README/marketing material, icon asset, release checklist, package metadata and tests are not part of this Skill package. No upstream script was executed. The MIT notice applies to the plugin source only; it does not license the Kling AI service or generated content.
