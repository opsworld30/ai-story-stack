# 知识库

本分类收录 RAG 检索、长期记忆、文件型上下文和知识系统维护能力。

## 实际收录统计

- **3 个完整 Skill 包 / 3 个 Skill 入口**。
- **2 个上游来源仓库**：smallnest/chao-rag-wiki、muratcankoylan/Agent-Skills-for-Context-Engineering。

## Skill 清单

| Skill 入口 | 功能 | 上游来源 | 许可证 |
|---|---|---|---|
| [chao-rag-wiki](./smallnest__chao-rag-wiki/SKILL.md) | Dense + BM25 + Full-text 混合检索 RAG | smallnest/chao-rag-wiki | MIT |
| [memory-systems](./Agent-Skills-for-Context-Engineering/memory-systems/SKILL.md) | 持久记忆、实体追踪、知识图谱与检索 | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |
| [filesystem-context](./Agent-Skills-for-Context-Engineering/filesystem-context/SKILL.md) | 文件型上下文和任务状态管理 | muratcankoylan/Agent-Skills-for-Context-Engineering | MIT |

## 运行提示

Chao RAG Wiki 需要 Python 3、turbovec、numpy、requests 和外部 Embedding API；密钥必须由使用者自行配置。其他 Skill 需要按其文档配置 Agent Runtime 与存储后端。所有脚本均随包保留，但未执行或安装依赖。
