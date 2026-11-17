# Memory Update

Use this after a narrative unit is finalized or when the user asks to extract memory, update canon, summarize unit state, track foreshadowing, or prepare structured notes.

## Memory Position Gate

Before generating chapter memory, read enough position sources to determine where the chapter sits in the book or volume. Do not rely only on the chapter prose.

For chapter N, read:

1. Chapter prose: `正文/第N章_标题.md`
2. Target chapter detail / scene-card source: for multi-volume projects, use the target chapter section inside `大纲/第XX卷/03-章节细纲.md`; for single-volume projects, use the project's equivalent chapter-detail source
3. Chapter AI writing instruction: `创作指令/第N章_标题_AI创作指令.md`
4. Chapter outline: for multi-volume projects, use `大纲/第XX卷/02-章节大纲.md`; otherwise use `大纲/01-章节大纲.md` or the equivalent chapter outline file
5. Optional chapter-detail index: `大纲/02-章节细纲索引.md`, only if the project actually maintains this file
6. Total outline or volume plan: `大纲/00-总纲.md`, `大纲/第XX卷/00-卷纲.md`, or equivalent project outline
7. Previous chapter narrative memory: `记忆/第N-1章_叙事记忆.md`, if available
8. Relevant global lore entries: timeline, character state, relationship state, location state, organization changes, foreshadowing state, and canon constraints

If a source is missing, state it under "缺失来源" and mark the affected position judgement as "未确认" instead of inventing it.

If `大纲/02-章节细纲索引.md` does not exist and the project does not use a chapter-detail index, do not list it under `缺失来源`. This is not a missing required source; rely on the chapter outline plus the target chapter section in `03-章节细纲.md`.

If the project uses volume folders under `大纲/第XX卷/`, do not look for root-level `大纲/章节细纲/` or a target volume `03-章节细纲/` folder as the required detail location. Their absence is normal; use the target volume's `03-章节细纲.md` file and extract the target chapter section.

Never infer volume ending, arc ending, or book ending from prose tone alone. A chapter may have a strong payoff, quiet aftertaste, or temporary closure without ending a volume.

## Memory Categories

Extract only facts that should matter later:

- Unit summary
- Ending hook, payoff, or emotional aftertaste
- Characters present
- Character state changes
- Character stage changes
- Psychological and emotional state changes
- Character knowledge changes
- Relationship changes
- Location, organization, item, or rule updates
- New foreshadowing
- Foreshadowing progress
- Foreshadowing payoff
- Timeline events
- Canon constraints
- Graph nodes and edges
- Chapter position and volume/book status, only when supported by outline or author-provided structure

## Memory Template Integrity Gate

The chapter memory template is mandatory. Keep every required heading, field, and table even when the chapter has little content for that category.

Required sections:

1. `## 叙事单元记忆`
2. `## 章节位置校验`
3. `## 人物状态变化`
4. `## 人物情感锚点`
5. `## 角色认知变化`
6. `## 关系变化`
7. `## 伏笔`
8. `## 时间线`
9. `## Canon`
10. `## 图谱建议`
11. `## 记忆格式自检`

Rules:

- Do not omit required sections.
- Do not omit required fields.
- Do not delete tables because there is no content.
- Do not merge sections.
- Do not convert required tables into prose summaries.
- If a category has no confirmed content, write `无`.
- If a source is missing or a claim cannot be verified, write `未确认`.
- If any required section is missing during self-check, add the missing section before outputting the final memory.

## Required Output Template

```markdown
## 叙事单元记忆
- 单元:
- 形式:
- 摘要:
- 结尾钩子 / 情绪落点:

## 章节位置校验
- 已读取来源:
- 缺失来源:
- 当前章节:
- 全书预计总章数:
- 当前卷:
- 当前卷预计章节范围:
- 是否卷末: [是 / 否 / 未确认]
- 是否阶段 / 弧线收束: [是 / 否 / 未确认]
- 判断依据:
- 不得推断项:

## 人物状态变化
| 角色 | 性格阶段 | 心理变化 | 情感变化 | 行动变化 | 证据 |
| --- | --- | --- | --- | --- | --- |

## 人物情感锚点
| 角色 | 表层情绪 | 隐藏情绪 | 触发点 | 后续风险 |
| --- | --- | --- | --- | --- |

## 角色认知变化
| 角色 | 新知道 | 仍不知道 | 误解 |
| --- | --- | --- | --- |

## 关系变化
| A | 关系 | B | 变化 | 证据 |
| --- | --- | --- | --- | --- |

## 伏笔
| 类型 | 内容 | 状态 | 关联单元 | 后续建议 |
| --- | --- | --- | --- | --- |

## 时间线
| 时间点 | 事件 | 影响 |
| --- | --- | --- |

## Canon
- 新增不可违背事实:
- 需要避免的矛盾:

## 图谱建议
- 节点:
- 边:

## 记忆格式自检
- 是否包含叙事单元记忆: [是 / 否]
- 是否包含章节位置校验: [是 / 否]
- 是否包含人物状态变化: [是 / 否]
- 是否包含人物情感锚点: [是 / 否]
- 是否包含角色认知变化: [是 / 否]
- 是否包含关系变化: [是 / 否]
- 是否包含伏笔: [是 / 否]
- 是否包含时间线: [是 / 否]
- 是否包含 Canon: [是 / 否]
- 是否包含图谱建议: [是 / 否]
- 缺失区块:
- 修复状态:
```

## Rules

- Do not store draft-only ideas as canon.
- Separate explicit facts from inference.
- Keep memory concise and reusable.
- Keep the required memory template complete.
- Record uncertainty when a fact depends on later confirmation.
- Track the reader's knowledge separately from character knowledge when relevant.
- For standalone short pieces, record only reusable style, character, world, or motif facts unless the user wants a broader project memory.
- If there is no content for a required section, keep the section and write "无" instead of deleting it.
- If evidence is insufficient, keep the section and write "未确认" instead of deleting it.
- If the self-check contains any "否", repair the missing section before final output.
- Do not infer "本卷结束", "阶段收束", "主线告一段落", "全书进入尾声", or "最终结局临近" from prose tone alone.
- Write "是否卷末: 是" only when the chapter outline, chapter index, volume outline, total outline, or author instruction explicitly supports it.
- If total chapter count, current volume range, or arc boundary is unknown, write "未确认" rather than guessing.
- If the current chapter number is far from the planned total chapters, treat long-range status as ongoing unless source files explicitly say otherwise.
- Separate chapter-level ending hook / payoff from volume-level ending.
- Do not let a strong chapter ending poison future memory as a false volume or book status.
