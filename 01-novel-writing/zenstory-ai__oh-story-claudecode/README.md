# Oh Story｜中文网文全流程 Skill 工具箱

**许可证：MIT** · 上游版本：`v0.10.5`

Oh Story 是面向中文网络小说创作的完整 Skill 工具箱，覆盖选题研究、长短篇写作、拆文分析、项目记忆、审稿、去 AI 味和发布准备。它面向**小说文本创作**，不是影视或短剧剧本工具。

- **14 个 Skill 入口**
- **435 个功能文件**
- **86 个代码文件**
- 上游提交：`41a9b6c855d7d29a2bf214b4eefda2b10e0a8afb`
- 许可证：[MIT](./upstream/LICENSE)

## Skill 清单

### 小说创作核心

| Skill | 用途 |
|---|---|
| [story](./upstream/skills/story/SKILL.md) | 小说工具箱总入口与任务路由 |
| [story-long-write](./upstream/skills/story-long-write/SKILL.md) | 长篇网文规划、细纲、正文、续写与连载状态 |
| [story-short-write](./upstream/skills/story-short-write/SKILL.md) | 短篇小说构思、写作与交付检查 |
| [story-import](./upstream/skills/story-import/SKILL.md) | 导入已有小说，重建设定、大纲和追踪状态 |
| [story-review](./upstream/skills/story-review/SKILL.md) | 多视角审稿、结构与连续性检查 |
| [story-deslop](./upstream/skills/story-deslop/SKILL.md) | 网文去 AI 味，修订表达、叙事与故事因果 |
| [story-long-analyze](./upstream/skills/story-long-analyze/SKILL.md) | 长篇小说拆解与结构分析 |
| [story-short-analyze](./upstream/skills/story-short-analyze/SKILL.md) | 短篇小说拆解与结构分析 |
| [story-long-scan](./upstream/skills/story-long-scan/SKILL.md) | 长篇网文平台扫榜与题材趋势研究 |
| [story-short-scan](./upstream/skills/story-short-scan/SKILL.md) | 短篇网文平台扫榜与题材趋势研究 |

### 小说出版与运行辅助

| Skill | 用途 |
|---|---|
| [story-publish](./upstream/skills/story-publish/SKILL.md) | 整理书名、简介、分类、标签等发布资料 |
| [story-cover](./upstream/skills/story-cover/SKILL.md) | 小说封面设计提示词与可选生图 |
| [story-setup](./upstream/skills/story-setup/SKILL.md) | 写作项目初始化、多宿主部署与配置 |
| [browser-cdp](./upstream/skills/browser-cdp/SKILL.md) | 通过 Chrome DevTools Protocol 执行浏览器操作 |

## 推荐使用流程

**新建长篇小说**

1. 使用 `story-setup` 初始化写作项目。
2. 使用 `story` 进入小说工作流，或直接调用 `story-long-write`。
3. 完成设定、卷纲、细纲，再按章节创作与续写。
4. 使用 `story-review` 检查结构、人物和连续性；需要时使用 `story-deslop` 修订。
5. 准备发布时使用 `story-publish`，需要封面时使用 `story-cover`。

**创作短篇小说**

使用 `story-short-write`；需要研究参考作品时，先用 `story-short-analyze` 拆解样本。

**已有小说继续写**

使用 `story-import` 整理已有正文和项目状态，再进入长篇或短篇写作流程。

## 运行环境与安全说明

- 长篇写作和部分工具需要 Node.js 18+；部分分析、记忆和处理脚本需要 Python 3。
- 浏览器采集需要 Chrome 与 `agent-browser`，仅在用户授权的账号和数据范围内使用。
- 封面 API 回退需要用户自己的 `GPT_IMAGE_API_KEY`；支持内置生图的宿主可优先使用内置能力。
- 不要公开提交 Cookie、Admin-Token、API Key、浏览器调试配置或写作项目中的私人资料。
- 使用前请阅读[安全与使用边界](./SECURITY_NOTES.md)。

完整上游文件清单和版本记录见 [UPSTREAM.md](./upstream/UPSTREAM.md) 与 [MANIFEST.json](./upstream/MANIFEST.json)。

## 分类边界

本 Skill 套件负责网络小说的构思、分析、正文、续写与修订。短剧/影视剧的分集大纲、场次、动作节拍和剧本对白属于剧本创作分类，不属于本套件的小说正文写作范围。
