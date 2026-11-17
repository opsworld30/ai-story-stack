# Chao RAG Wiki（混合检索知识库）

基于本地 Markdown/TXT 文档建立可增量更新的 RAG 索引。默认组合 Dense 向量检索、BM25 关键词检索与全文匹配，并可选用 LLM rerank。

## 运行要求

- Python 3；依赖 `turbovec`、`numpy`、`requests`。
- 一个 OpenAI 兼容 Embedding API。上游默认 Qianfan，也支持 OpenAI、Voyage、OneAPI/OpenRouter 和本地 vLLM。
- 可选 LLM rerank API。
- 原始资料放在 `raw/`，生成索引放在 `.rag/`。

## 使用注意

1. 首次使用先配置自己的 Embedding API Key 并执行上游 preflight。
2. 不要假设 API Key 已经预先配置；上游文档中针对原作者环境的状态描述不适用于其他用户。
3. 密钥只放在环境变量，不要写入文件或提交到仓库。
4. 改变 Embedding 模型或维度后需要重建索引。
5. 本 Skill 与脚本均为静态镜像，未执行或安装依赖。

## 文件

原始英文说明见 [README.md](./README.md)，Skill 入口为 [SKILL.md](./SKILL.md)，上游版本和许可证信息见 [UPSTREAM.md](./UPSTREAM.md)。
