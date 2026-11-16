# Chinese Novelist｜中文小说创作 Skill

这是 `PenglongHuang/chinese-novelist-skill` 的功能完整镜像，包含入口 Skill、全部 18 份运行时参考资料、3 个运行脚本、2 个测试文件和原始 MIT LICENSE。

## 能做什么

- 从创意出发，分阶段收集题材、主角、核心冲突、世界观、叙事视角和读者定位。
- 生成标题候选、人物档案、章节大纲和写作计划。
- 支持逐章串行、子 Agent 并行和 Agent Teams 三种写作模式。
- 通过项目文件保存创作进度，支持中断后续写。
- 提供章节摘要初始化、字数检查、项目校验脚本。
- 包含章节指南、对话、人物、钩子、标题、情节结构和内容扩充参考。

## 目录结构

```text
chinese-novelist/
├── SKILL.md
├── LICENSE
├── README.md
├── UPSTREAM.md
├── references/
│   ├── flows/       # Phase 0–4 创作流程
│   └── guides/      # 章节、人物、对话、钩子、标题等指南
└── scripts/
    ├── check_chapter_wordcount.mjs
    ├── init_chapter_summaries.mjs
    ├── validate_project.mjs
    └── tests/
```

## 安装方式

把整个 `chinese-novelist/` 目录放入当前 Agent 支持的 Skills 目录，并保留内部目录结构。

常见位置：
- Claude Code：`.claude/skills/chinese-novelist/`
- Codex：`.agents/skills/chinese-novelist/`

其他 Agent 请使用其官方支持的 Skills 目录。若宿主不支持子 Agent，选择逐章串行模式；Agent Teams 模式需要 Claude Code 相应能力。

安装后，在对话中调用 `chinese-novelist`，或提出“使用中文小说创作助手帮我写一部小说”。

## 脚本依赖

- Node.js（脚本使用 Node.js 内置模块，无额外 npm 运行依赖）。
- 不需要 Python、外部 API Key 或向量数据库。
- 并行写作依赖宿主的 Agent / 子 Agent 能力，不是脚本依赖。

常用检查命令：

```bash
node scripts/check_chapter_wordcount.mjs <章节文件路径>
node scripts/validate_project.mjs <小说项目目录> --json
node scripts/init_chapter_summaries.mjs <小说项目目录> --json
node --test scripts/tests/*.test.mjs
```

这些命令仅供使用者在自己的小说项目中运行。本仓库镜像维护过程没有执行上游脚本；尚未在本地环境完成运行测试，不标记为“已测试”。

## 镜像范围与排除项

本包保留了所有被 `SKILL.md` 引用的流程文档、指南、脚本和测试。上游 `assets/` 中的 7 张 PNG（赞助商横幅、演示截图和微信群二维码）不是 Skill 运行依赖，且图片素材授权需单独确认，因此未复制。上游 README 含有这些图片和赞助推广内容，本地 README 由资料库重新编写；请通过 [上游 README](https://github.com/PenglongHuang/chinese-novelist-skill/blob/master/README.md) 查看原始介绍。

许可证、上游提交和文件清单见 [UPSTREAM.md](./UPSTREAM.md)。
