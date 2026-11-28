# UPSTREAM｜Rachel Digital Human Production

- 上游仓库：Jingyi-Wu-Richael/rachel-digital-human-production
- 上游目录：`.`（仓库根目录）
- Skill URL：[SKILL.md](https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production/blob/a20258b8eb38eb370cf3402fb4414754b4c44c2a/SKILL.md)
- 分支：`main`
- 上游目录最近提交：`a20258b8eb38eb370cf3402fb4414754b4c2a`
- 上游更新时间：`2026-07-16T10:57:17Z`（UTC）
- 许可证：MIT（原始 LICENSE 已保留；版权声明为 Rachel Wu）
- 保留上游文件：10 个
- 本次同步时间：`2026-11-28T04:14:04.644Z`（UTC）

## 保留文件
- `.gitignore`
- `LICENSE`
- `README.md`
- `SKILL.md`
- `agents/openai.yaml`
- `references/api-facts.md`
- `references/checklists.md`
- `references/public-safety.md`
- `scripts/init_job_state.py`
- `scripts/preflight_assets.py`

## 依赖与安全边界
- 两个 Python 辅助脚本只作为 Skill 包静态文件保留；未执行、未安装依赖。
- `preflight_assets.py` 在实际运行时会调用宿主环境中的 `ffprobe`；本次没有运行该脚本。
- 上游仓库未包含真实 API Key、私有语音样本、肖像输入、客户视频或生成任务状态文件；`.gitignore` 中的本地工作目录与媒体文件未被纳入。
- 该 Skill 要求对声音和肖像具有授权，并对付费 API 操作设置用户审批门槛；Skill 不提供第三方账号、API 权限或付费额度。

## 完整性说明
按上游固定提交递归核对的 10 个文件完整保留，文件 Git Blob SHA 与上游一致；只静态读取和复制。
