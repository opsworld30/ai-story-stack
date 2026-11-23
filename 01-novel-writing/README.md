# 小说创作

本分类只收录**小说文本本身的创作与维护**：网文、长篇、短篇、题材与故事设定、小说大纲、人物塑造、章节正文、续写、修订、拆文分析和连载管理。

**分类边界：** 小说大纲是为小说章节与正文服务的结构；小说正文以叙述、描写、人物行动和对话构成。影视/短剧的分集大纲、场次表、动作节拍、台词本和剧本不放在本分类。

## 当前收录

**13 个 Skill 包（来自 13 个上游仓库），43 个 Skill 入口。**

> 统计口径：Skill 包按独立镜像包及 `UPSTREAM.md` 记录计数；Skill 入口按目录中实际存在的 `SKILL.md` 文件计数。Oh Story 提供 14 个入口，Snowflake Fiction 提供 13 个入口，Calliope Writing Skills 提供 6 个入口。

### 1. [Chinese Novelist｜中文小说创作](./PenglongHuang__chinese-novelist-skill/chinese-novelist/README.md)

- 许可证：MIT
- 上游版本：2.3.2
- 1 个 Skill 入口，包含 18 份流程与写作参考、3 个 Node.js 脚本和 2 个测试文件。
- 能力：分阶段构思、人物和大纲规划、章节写作、断点续写、字数检查与项目校验。

### 2. [Oh Story｜中文网文全流程工具箱](./zenstory-ai__oh-story-claudecode/README.md)

- 许可证：MIT
- 上游版本：v0.10.5
- 14 个 Skill 入口、435 个 Skill 目录文件、86 个代码文件（以该包的 `UPSTREAM.md` 和 `MANIFEST.json` 为准）。
- 小说核心能力：长短篇写作、拆文分析、题材扫榜、导入已有小说、审稿、去 AI 味。
- 配套能力：发布资料、小说封面、写作项目部署和浏览器工具。
- 不包含影视/短剧剧本创作；剧本能力归入 [02 剧本创作](../02-script-adaptation/README.md)。

### 3. [Novel Writing｜小说写作与维护](./wgwtest__novel-writing/README.md)

- 许可证：MIT
- 1 个 Skill 入口，包含 11 份参考文件、1 个可选 Python 标准库检查脚本和 OpenAI Agent 元数据。
- 能力：全书/卷/章规划、小说正文起草与续写、人物视角、自然对白、场景因果、文风保留和修订交接。
- 上游文档以 Codex 为目标宿主；本库不声称其他宿主已验证。
- 只处理小说文本，不处理影视/短剧剧本；剧本能力归入 [02 剧本创作](../02-script-adaptation/README.md)。

### 4. [Qiaomu Novel Generator｜中文短篇小说生成](./joeseesun__qiaomu-novel-generator/README.md)

- 许可证：MIT
- 1 个 Skill 入口；包含创作访谈、剧情引擎、反 AI 腔参考、原创示例和校验/诊断脚本。
- 能力：从主题或人物设定形成短篇故事策略，设计冲突升级、开篇钩子、反转和结尾余味。
- 适用：中文短篇、网文样章和单次完整故事；不替代百万字长篇项目管理。

### 5. [RoleTrace｜角色决策与人格一致性](./LCnKeo__roletrace/README.md)

- 许可证：MIT
- 1 个 Skill 入口，附带对白测试样例。
- 能力：AUDIT / REWRITE / DECIDE / VOICEPRINT，检查角色认知、动机、行动代价、对白声纹和人物失真。
- 适用：小说人物和对白专项分析；不负责整本小说的长期记忆。

### 6. [Longform Fiction｜长篇小说工作流](./oldwinter__skills/README.md)

- 许可证：MIT
- 1 个 Skill 入口，包含 OpenAI 元数据、Python 字数统计脚本和测试。
- 能力：先建立故事圣经与章节合同，再按正典推进章节，合并连续性并检查篇幅目标。
- 适用：长篇、系列和连载；脚本依赖 Python 标准库，尚未执行测试。

### 7. [Fiction Humanizer ZH｜中文小说去 AI 味](./deedeekong07-alt__fiction-humanizer-zh/README.md)

- 许可证：MIT
- 1 个 Skill 入口，包含 4 份按需加载的参考资料。
- 能力：修复剧情跳步、人物行动、对白汇报腔、情绪断层、场景空泛和章末钩子，同时保留作者文风。
- 适用：中文小说润色、精修、续写和去 AI 味；不是通用剧本润色工具。


### 8. [Snowflake Fiction｜雪花写作法小说创作套件](./hestudy__snowflake-fiction/snowflake-fiction/README.md)

- 许可证：MIT
- 13 个 Skill 入口；镜像 77 个上游文件（包含上游说明与许可证文件，不等同于 77 个纯功能文件）；包含主编排器、构思、角色设计、场景规划、章节写作、审稿、去 AI 味、质量检查、开篇/角色/创意检查与导出。
- 配套：Claude Code 插件元数据、agents、commands 和按需加载的 references。
- 上游：hestudy/snowflake-fiction。未执行脚本或安装依赖。

### 9. [Chinese Novel Workflow｜中文叙事创作工作流](./wp1020__Chinese-Novel-Workflow/chinese-novel-workflow/README.md)

- 许可证：Apache-2.0
- 1 个 Skill 入口，17 份参考文档，附 OpenAI Agent 元数据与使用流程文档。
- 能力：项目管理、世界观/人物、分卷与章节细纲、正文生成、连续性审查、自然化润色、终审和记忆沉淀。
- 上游：wp1020/Chinese-Novel-Workflow。

### 10. [Novel Writer｜小说创作工坊](./Yunshiro__yunn-skills/novel-writer/README.md)

- 许可证：MIT
- 1 个 Skill 入口，6 份参考文档、OpenAI Agent 元数据和小说检查脚本。
- 能力：商业网文与纯文学双模式、长篇连续性、规划、章节写作和分层修订。
- 仅发布 novel-writer 目录及必要依赖，不包含上游仓库的其他爬虫/工具 Skill。
- 上游：Yunshiro/yunn-skills。

## 分类规则

- 小说总纲、卷纲、章纲：归本分类。
- 小说章节正文、续写、润色、去 AI 味：归本分类。
- 对已出版/已完成小说的拆解分析：归本分类。
- 影视/短剧分集大纲、场次、动作节拍、台词和剧本：归 02。
- 镜头拆分、分镜表和拍摄调度：归 [03 分镜与导演](../03-storyboard/README.md)。


### 11. [Calliope Writing Skills｜小说创作训练](./Calliope-Editor__writing-skills/README.md)

- 许可证：MIT
- 6 个 Skill 入口：人物卡构建、从正文反推人物卡、对白训练、文风节奏、叙事距离和场景结构。
- 定位：写作训练和诊断，不替作者生成或改写正文。
- 上游：Calliope-Editor/writing-skills。

### 12. [Chinese WebNovel Master｜中文网文创作工作流](./TianHengZhuang__Chinese-WebNovel-Master/README.md)

- 许可证：MIT
- 1 个 Skill 入口，覆盖选题与受众定位、故事架构、人物圣经、伏笔、黄金三章、十章节奏、章节钩子和发布优化。
- 本次镜像独立 SKILL.md 与许可证；上游额外知识库、提示词和工具文档未纳入此 Skill 包。
- 上游：TianHengZhuang/Chinese-WebNovel-Master。
### 13. [Fantasy World Building｜奇幻小说世界构建规范](./wordflowlab__novel-writer-skills/fantasy/SKILL.md)

- 许可证：MIT（原始仓库级 LICENSE 随包保留）。
- 1 个 Skill 入口，包含自包含的 `SKILL.md`，没有额外本地 references、templates、scripts 或 assets 依赖。
- 能力：奇幻类型框架、硬/软魔法系统、世界地理、社会文化、历史纵深、种族与生物生态，以及设定一致性检查。
- 上游：wordflowlab/novel-writer-skills，路径 `templates/skills/genre-knowledge/fantasy`。
- 该发布仅覆盖 fantasy 独立 Skill，不代表上游仓库其余 12 个模块已完整镜像。
