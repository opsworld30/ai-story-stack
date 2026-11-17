# 场景资产

本分类收录场景设计、环境生成、空间搭建、道具与 2D/3D 美术资产，以及场景灯光和资产质检。

## 实际收录统计

- **13 个完整 Skill 包 / 13 个 Skill 入口**。
- **3 个上游来源仓库**：eternityspring/shuohao-skills、Runware/runware-skills、scenario-labs/skills。

## Skill 清单

| Skill 入口 | 功能 | 上游来源 | 许可证 |
|---|---|---|---|
| [novel-art](./eternityspring__shuohao-skills/novel-art/SKILL.md) | 小说场景、道具与美术资产设计 | eternityspring/shuohao-skills | Apache-2.0 |
| [composite-scene](./Runware__runware-skills/composite-scene/SKILL.md) | 多参考图场景合成 | Runware/runware-skills | MIT |
| [image-to-3d-asset](./Runware__runware-skills/image-to-3d-asset/SKILL.md) | 图片/文本转 3D 模型 | Runware/runware-skills | MIT |
| [game-assets-2d](./Runware__runware-skills/game-assets-2d/SKILL.md) | 成套 2D 道具、Sprite 与图标 | Runware/runware-skills | MIT |
| [scenario-3d](./scenario-labs__skills/scenario-3d/SKILL.md) | 3D 网格生成、编辑与导出 | scenario-labs/skills | MIT |
| [scenario-3d-worlds](./scenario-labs__skills/scenario-3d-worlds/SKILL.md) | 可探索 3D 世界与 Gaussian Splat | scenario-labs/skills | MIT |
| [scenario-asset-analysis](./scenario-labs__skills/scenario-asset-analysis/SKILL.md) | 资产分析、检索与控制图 | scenario-labs/skills | MIT |
| [scenario-meshy](./scenario-labs__skills/scenario-meshy/SKILL.md) | Meshy 模型族专用工作流 | scenario-labs/skills | MIT |
| [scenario-rodin](./scenario-labs__skills/scenario-rodin/SKILL.md) | Rodin 模型族专用工作流 | scenario-labs/skills | MIT |
| [scenario-sparc3d](./scenario-labs__skills/scenario-sparc3d/SKILL.md) | SPARC3D 模型族专用工作流 | scenario-labs/skills | MIT |
| [scenario-blender](./scenario-labs__skills/scenario-blender/SKILL.md) | Scenario Blender 插件入口 | scenario-labs/skills | MIT |
| [scenario-blender-blockout](./scenario-labs__skills/scenario-blender-blockout/SKILL.md) | 场景灰盒、空间与镜头预演 | scenario-labs/skills | MIT |
| [scenario-blender-lighting-rendering](./scenario-labs__skills/scenario-blender-lighting-rendering/SKILL.md) | 灯光、渲染、合成与质检 | scenario-labs/skills | MIT |

## 运行依赖与边界

- Runware 资产 Skill 需要 Runware 基础 Skill 和 API Key，见 [Agent Tools](../10-agent-tools/README.md)。
- Scenario Skill 需要 Scenario MCP 基础 Skill 和可用账号权限，见 [Agent Tools](../10-agent-tools/README.md)。
- Blender 工作流需要兼容版本的 Blender；Blockout 还会使用 Scenario Blender 插件。参考资料和脚本已随包保留，但没有执行或做运行测试。
