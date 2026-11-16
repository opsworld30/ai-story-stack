# 上游镜像记录

- 上游仓库：https://github.com/zenstory-ai/oh-story-claudecode
- 上游版本：`v0.10.5`
- 上游提交：`41a9b6c855d7d29a2bf214b4eefda2b10e0a8afb`
- Skill 目录最后提交时间：`2026-11-13T06:21:21Z`（UTC）
- Release 发布时间：`2026-11-13T06:27:36Z`（UTC）
- 许可证：MIT，已核验上游根目录 `LICENSE`
- 功能镜像范围：完整保留 `skills/` 下 14 个 Skill 的 435 个文件；另保留根许可证和 `.agents/skills -> ../skills` 软链接。
- Skill 目录文件数：435；静态代码文件：86；入口 `SKILL.md`：14。
- 上游仓库文件总数：856。本镜像不是整个上游仓库的逐文件克隆，而是完整的 Skill 功能依赖闭包。

## 保留内容

`skills/` 下的全部文件均已镜像，包含每个 Skill 的 `SKILL.md`、references、scripts、assets、templates、agents、hooks、宿主配置和升级说明。没有从 Skill 目录内部删减运行依赖。文件路径、文件模式和上游 blob SHA 记录在同目录的 `MANIFEST.json`。

## 未纳入的上游根目录内容

以下内容不属于 14 个 Skill 的运行依赖闭包，因此没有复制：

- 根目录开发用 `scripts/`、`tests/`、Playwright 配置与测试环境专用包；
- `demo/` 示例项目与演示素材；
- `.github/` 工作流、CI 与发布流程；
- `.agents/notes/` 开发过程笔记；
- 上游根目录宣传型 README、CHANGELOG、英文说明和非必要项目文档；
- 插件市场发布清单与 Marketplace 包装元数据。

上游宿主安装排查文档仍可在 [docs/hosts.md](https://github.com/zenstory-ai/oh-story-claudecode/blob/main/docs/hosts.md) 查阅。本地中文 README 已整理核心安装步骤和宿主边界。未纳入的根目录文件不影响这 14 个 Skill 目录内的相对引用闭包，但本镜像不是上游 Marketplace 插件仓库的替代品。

## 审查记录

- 核对 14 个 Skill 入口及其引用的本地 references/scripts/assets 等路径；未发现入口文档引用的缺失文件。
- 对 86 个 Python、JavaScript、Shell、TypeScript 运行代码文件做静态模式扫描，并对浏览器进程管理、登录态采集、Dashboard 文件写入/删除、部署清理和生图 API 回退做重点人工核读。
- 对全部 435 个 Skill 文件检查常见硬编码凭据格式；未发现匹配项。
- 未执行上游脚本、未安装依赖、未启动浏览器、未调用外部 API。

静态审查不等于动态安全认证。涉及登录态、文件删除和网络访问的能力请先阅读同目录外的 `SECURITY_NOTES.md`。

## 版本更新

后续更新按 `SYNC_POLICY.md`：先比较 Skill 目录提交 SHA 与时间；只有上游 Skill 目录变化时才重新读取内容。更新时同步完整依赖闭包、许可证、清单和本地说明。
