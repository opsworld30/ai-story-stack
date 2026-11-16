# Oh Story 安全与使用边界

本文件基于上游 v0.10.5 的静态代码检查整理。没有执行任何脚本，也没有安装依赖。

## 需要特别留意的能力

### 1. Browser CDP 与 Chrome 登录态

`browser-cdp/scripts/setup-cdp-chrome.js` 会建立独立的 `~/chrome-debug-profile`，并从默认 Chrome Profile 复制或刷新登录态相关文件，包括 Cookies、Login Data、Web Data 和 Local State。

- 已有 Chrome 进程时，默认要求交互确认后才会关闭进程；非交互环境拒绝静默关闭。
- `--yes` 会跳过确认，只有用户明确同意关闭 Chrome 后才应使用。
- `--reset` 会删除独立的 debug profile，再重建；不要把它误认为只清缓存。
- 不要把 CDP 端口暴露到公网，也不要将 debug profile 或 Cookie 文件提交到 Git。

### 2. 黑岩书库采集

`story-short-scan/scripts/heiyan-booklist-scraper.js` 会从已登录的 Chrome 页面读取 `Admin-Token` Cookie，并用 Bearer Token 请求黑岩管理后台 API。

- 仅在你有权访问的账号和数据范围内使用。
- Token 属于敏感凭据，不要复制到聊天、日志、README、仓库或共享报告。
- 脚本会把采集结果写入指定输出目录；运行前确认目录和数据范围。

### 3. Story Dashboard

Dashboard 默认绑定 `127.0.0.1`，并限制本机请求；路径解析拒绝工作区外路径和符号链接。它可以编辑并删除工作区内受支持的 Markdown、TXT、JSON、YAML、TOML 文件。

- 使用前确认 `--root` 指向正确的小说项目目录。
- 不要随意启用 `--allow-network`：该选项会关闭默认本机请求限制，Dashboard 没有配套的登录认证，不应暴露到局域网或公网。
- 删除接口有文件版本校验，但仍应保留版本控制或备份。

### 4. Story Setup 部署与清理

`story-setup` 会在写作项目中创建或更新宿主所需的 Skills、Agents、Rules、Hooks 和配置文件。

- Antigravity 部署器只替换 Oh Story 管理的 14 个 Skill 目录，其他 Skill 会保留；已有 `.agents/skills` 软链接时，默认不跟随写入，需要明确迁移授权。
- `copy-path-safety.py --prune-orphans` 会删除目标受管目录中上游已不存在的文件，只能对确认由 Oh Story 管理的目标目录使用。
- 首次部署或迁移前先检查项目路径和现有配置；不要把整个用户级 Skills 目录当作清理目标。

### 5. 小说章节与记忆维护

长篇写作的提交流程会在章节提交成功后清理该章的临时工作目录；追踪迁移逻辑会将已退役的追踪文件归档，而不是静默丢弃。不要手动删除 `.story/` 或 `追踪/` 中的状态文件，除非已备份并理解当前项目协议。

### 6. 封面 API 回退

`story-cover` 的 API 回退脚本使用 `GPT_IMAGE_API_KEY`，并向配置的图片 API 地址发送提示词和可选参考图。

- API Key 只放在本机环境变量或受保护的密钥管理器中。
- 如果使用兼容代理，确认 `GPT_IMAGE_BASE_URL` 是可信服务。
- `REF_IMAGE` 为 URL 时会被下载到临时文件；只使用可信图片地址。
- 有内置生图能力时优先使用宿主内置能力，不必配置 API Key。

### 7. 扫榜与外部站点

长短篇扫榜会访问第三方小说网站或读取浏览器页面。请遵守网站条款、访问频率和账号权限，不要将需要授权的后台数据公开发布。

## 审查边界

静态扫描未发现常见格式的硬编码 API Key、GitHub Token、云密钥或私钥；这不能证明所有运行环境和外部服务都安全。上游脚本保持原样，本地没有运行或修改其行为。
