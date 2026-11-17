# Agent 工具

本分类收录 Agent 工具设计、MCP 接入、模型执行基础设施、工具调用规范与多 Agent 协作。

## 实际收录统计

- **7 个完整 Skill 包 / 7 个 Skill 入口**。
- **4 个上游来源仓库**：Runware/runware-skills、muratcankoylan/Agent-Skills-for-Context-Engineering、obra/superpowers-lab、scenario-labs/skills。

## Skill 清单

| Skill 入口 | 功能 | 上游来源 | 许可证 |
|---|---|---|---|
| [runware-run](./Runware__runware-skills/runware-run/SKILL.md) | Schema、上传、执行与轮询 | Runware/runware-skills | MIT |
| [runware-models](./Runware__runware-skills/runware-models/SKILL.md) | 实时模型目录与能力查询 | Runware/runware-skills | MIT |
| [runware-prompting](./Runware__runware-skills/runware-prompting/SKILL.md) | 模型家族提示词策略 | Runware/runware-skills | MIT |
| [tool-design](./Agent-Skills-for-Context-Engineering/tool-design/SKILL.md) | 工具描述、Schema 与错误恢复设计 | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [multi-agent-patterns](./Agent-Skills-for-Context-Engineering/multi-agent-patterns/SKILL.md) | Supervisor、委派和多 Agent 协作 | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [mcp-cli](./obra__superpowers-lab/mcp-cli/SKILL.md) | 按需发现和调用 MCP Server | obra/superpowers-lab | MIT |
| [scenario](./scenario-labs__skills/scenario/SKILL.md) | Scenario MCP 连接、Schema 与资产生命周期 | scenario-labs/skills | MIT |

## 共享依赖说明

Runware 的音频和场景资产 Skill 依赖前三个 Runware 基础 Skill。Scenario 场景资产 Skill 依赖 Scenario MCP 基础 Skill。MCP CLI 需要单独安装 mcp 命令行程序；本仓库不附带二进制、凭据或托管服务。
