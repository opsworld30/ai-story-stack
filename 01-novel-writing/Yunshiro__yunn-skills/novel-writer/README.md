# Novel Writer｜小说创作工坊

面向中文商业网文与纯文学的小说创作 Skill。它将需求确认、角色 DNA、大纲、情绪节拍、正文创作、分层润色和长篇连续性拆成可确认、可恢复、可检查的阶段。

- 上游：[Yunshiro/yunn-skills](https://github.com/Yunshiro/yunn-skills/tree/main/skills/novel-writer)
- 入口：[SKILL.md](./SKILL.md)
- 许可证：MIT（保留上游根目录 LICENSE）
- 上游提交：`b526f80d45ce275644d2169f3c50af98ad6a25f9`
- 1 个 Skill 入口、6 份参考文档、1 个 OpenAI Agent 元数据文件、1 个可选 Python 检查脚本。
- 共镜像 10 个上游文件（包含 LICENSE）；本地另有 `README.md` 与 `UPSTREAM.md`。

## 核心能力

- **商业网文模式**：面向番茄、七猫、起点等平台，规划黄金三章、冲突升级、爽点、节奏和读者代入感。
- **文学模式**：面向纯文学、征文和个人创作，关注人物选择、价值转折、潜台词与余韵，不强套商业爽点。
- **长篇连续性**：维护角色 DNA、章节节拍、人物状态、伏笔、时间线和跨会话续写入口。
- **正文检查与修订**：支持单章和全稿检查，并按代入感、去 AI 味、节奏、对白和环境心理分层润色。

## 目录内容

- `references/planning.md`：需求采集、角色设计和大纲规划。
- `references/commercial-mode.md`：商业网文结构与平台节奏。
- `references/shuanwen-tech.md`：爽感结构与商业网文技巧。
- `references/literary-mode.md`：文学创作模式。
- `references/writing-and-revision.md`：正文写作与分层修订。
- `references/long-form-continuity.md`：长篇连续性与续写。
- `scripts/check_novel.py`：可选的单章/全稿检查脚本。

## 使用方式

将整个 `novel-writer/` 目录放入宿主支持的 Skills 目录，保留 `references/`、`scripts/` 和 `agents/` 结构。具体调用方式以所用 Agent 宿主为准。

脚本未在本次镜像维护中执行；不要将“文件已镜像”理解为“运行测试已通过”。

## 镜像范围

本公开包只镜像上游的 `skills/novel-writer` 目录及仓库根目录 MIT LICENSE；没有复制同仓库的爬虫或其他无关 Skill。来源提交、文件数与镜像范围见 [UPSTREAM.md](./UPSTREAM.md)。
