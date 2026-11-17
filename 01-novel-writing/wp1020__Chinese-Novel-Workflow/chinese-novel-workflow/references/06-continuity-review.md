# Continuity Review

Use this when reviewing a narrative unit, outline, chapter, scene, short story, continuation, or rewritten passage for collapse, contradictions, weak pacing, character drift, lost foreshadowing, broken continuity, or readability problems.

## Severity

- Blocking: must fix before saving, publishing, or treating as canon.
- High: likely damages reader trust or future continuity.
- Medium: weakens the unit effect but can survive temporarily.
- Low: polish-level improvement.

## Review Dimensions

| Dimension | Check |
| --- | --- |
| 人设一致 | Decisions, dialogue, values, and emotional reactions match established character. |
| 叙事人称一致 | First-person, third-person, and second-person narration do not drift into each other. Third-person limited POV does not accidentally become first-person "I" narration. |
| 性格阶段 | Characters do not jump stages without trigger, cost, or scene support. |
| 心理/情感连续 | Body state, psychological state, surface emotion, hidden emotion, and relationship posture continue from prior context. |
| 角色认知 | Characters do not know facts they have not learned. |
| 设定自洽 | Power, geography, rules, organizations, and costs remain consistent. |
| 现实逻辑 | 场景中描述的物理现象、技术设备行为、日常物品反应符合故事时代/技术背景。不会出现"CRT电视的关机方式发生在LED屏幕上"这类跨时代技术细节泄漏。 |
| 时间线 | Events occur in possible order with plausible elapsed time. |
| 伏笔 | New, advanced, delayed, or paid-off foreshadowing is tracked. |
| 节奏张力 | Scenes have pressure, change, and forward pull. |
| 回报密度 | Rewards, reversals, competence moments, emotional payoffs, or aftertaste appear at useful intervals. |
| 叙事衔接 | The unit connects to previous and next story needs, or clearly functions as a standalone piece. |
| 详细剧情一致 | 正文、章节细纲与章节大纲的`本章详细剧情说明`在事件、行动、关键选择和直接结果上保持一致。 |
| 剧情重叠 | The chapter does not rewrite, replay, or merely extend the previous chapter's completed event chain, climax, or hook. |
| 字数达标 | Actual prose word count meets the chapter minimum from the AI writing instruction, chapter detail, chapter outline, or project writing specification. |
| 正文元信息泄漏 | Prose does not leak outline, volume outline, chapter planning, author-note, workflow structure labels, word count, counting method, or bookkeeping lines such as `本章字数`, `番茄计字法`, `字数统计`, volume number, current volume, next chapter, later plot, arc closure, or mainline node unless they are valid in-world text. |
| 正文内结构元叙事 | Narration, character psychology, and ordinary dialogue do not mention chapter/volume/outline/future-plot structure such as `第几章`, `第几卷`, `本卷`, `下一章`, `后续剧情`, `阶段收束`, or `主线节点` unless visible in-world or approved metafiction. |
| 去 AI 味残留 | Summary, explanation, generic emotion, and uniform dialogue are controlled. |

## 详细剧情一致性审查

对照章节大纲中的`本章详细剧情说明`、章节细纲执行版和正文，逐项检查：

- 开场压力与事件触发是否保留；
- 主角的连续行动和主要阻碍是否被跳过或替换；
- 关键选择是否仍由主角完成，动机和代价是否改变；
- 直接结果和结尾状态是否与规划一致；
- 正文是否擅自新增重大事件、揭示、关系变化或结尾结果；
- 是否把详细剧情说明写成了大纲字段的机械复述，而没有落实为场景行动。

缺少`本章详细剧情说明`、字段内容过于概括，或大纲、细纲、正文存在重大事件冲突时，标记为 High；若已经无法判断本章到底发生了什么，标记为 Blocking。输出证据、影响和修改方向，不直接改正文。

## 剧情重叠审查

Check whether the chapter repeats the previous chapter's completed events.

Review these points:

- 开头是否重复前章收束
- 中段是否重讲前章高潮
- 是否把同一冲突在两章里重复起爆
- 结尾是否只是前章的延长，而不是新钩子
- 本章是否缺少新的冲突升级、信息释放、视角变化或关系变化

If the chapter is mainly a reworded retelling of the previous chapter, mark it as High. If the overlap breaks chapter boundary, pacing, or hook function, mark it as Blocking.

Evidence should compare the previous chapter's completed event with the current chapter's opening, middle climax, and ending result. Do not treat normal pressure inheritance as overlap unless the new chapter fails to add a new obstacle, choice, information, consequence, or relationship shift.

## Word Count Review Gate

When reviewing chapter prose continuity, check the actual prose word count before recommending finalization or polishing.

Read, when available:

1. Chapter prose
2. Chapter AI writing instruction
3. Single-chapter detail / scene-card file
4. Target chapter outline entry
5. `设定/04-创作规格.md`

Output the word count check:

```markdown
## 字数核查
- 字数来源:
- 本章最低字数:
- 正文实际字数:
- 是否达标: [是 / 否 / 需要作者确认]
- 差额:
- 字数缺失 / 冲突:
```

If the prose is below the chapter minimum, list it as a Blocking issue when the target is saving/publishing/finalizing, or High when the user only asked for diagnostic review.

Only output an expansion plan when `是否达标: 否`.

- If `是否达标: 是`, do not output `## 扩写方案`.
- If `是否达标: 需要作者确认`, do not output `## 扩写方案`; first list the missing or conflicting word count source that needs author confirmation.
- If `是否达标: 否`, output `## 扩写方案` and do not recommend padding.

```markdown
## 扩写方案（仅当正文字数低于本章最低字数时输出）
| 场景 | 建议补充字数 | 扩写内容 | 不能补的内容 |
| --- | --- | --- | --- |
```

Good expansion targets:

- Action chain under pressure
- Pressure escalation or obstacle response
- Dialogue conflict and subtext
- Character body/mental/emotional reaction
- Sensory detail that changes attention or choice
- Information release that was too compressed
- Transition, aftermath, or next-scene bridge

Do not fill the gap with repeated exposition, empty scenery, generic introspection, slogan-like summaries, or retelling information readers already know.


## 正文内结构元叙事审查

Check whether narration, character psychology, or ordinary dialogue exposes author, outline, table-of-contents, platform, or future-chapter perspective.

Review:

- 叙述句是否提到第几卷、第几章、本卷、下一章。
- 人物心理是否知道自己处在某一章、某一卷、某个主线节点。
- 普通对白是否说出“后续剧情”“阶段收束”“卷末危机”“本章真正的冲突”等作者规划语言。
- 这些词是否是故事内合法文本，例如系统界面、档案名、书名、公告、任务面板、卷宗标题。

If not in-world visible text or approved metafiction, mark High.
If it breaks immersion, exposes future plot planning, or makes the narrator sound like an outline/commentary voice, mark Blocking.

Revision direction: do not merely smooth these phrases. Replace them with in-world action, pressure, information, character inference, or visible consequence.

## Prose Meta-Leak Review Gate

During continuity review, scan the prose for structural meta language that belongs to outlines, volume plans, author notes, or workflow planning rather than the story world.

Flag these as issues when they appear in narration, ordinary dialogue, or character psychology without in-world justification:

Word-count metadata leak examples:

- `本章字数：3086字（番茄计字法）`
- `字数统计` / `番茄计字法` / `本章最低字数` / `字数规则`
- `章节备注` / `创作说明` / `以下是正文` / `正文如下` / `本章完成`


- `第几卷`, `第X卷`, `本卷`, `上卷`, `下卷`
- `卷末`, `卷尾`, `本卷结束`
- `下一章`, `后续剧情`, `后文`, `前文`
- `阶段收束`, `弧线收束`, `主线节点`, `支线收束`
- `剧情推进到`, `作者计划`, `读者将看到`, `接下来会`

Only allow them when the evidence shows they are:

- A chapter title, volume title, or table-of-contents label.
- Text visible inside the story world, such as a file name, archive title, system UI, task panel, case file, letter, or book title.
- Part of an author-approved metafiction style where characters knowingly perceive chapter / volume / plot structure.
- Explicitly requested by the user for the current prose.

When found, list the exact evidence, explain whether it breaks immersion, exposes outline planning, or creates false volume/chapter status, and give a current-text revision direction. Do not rewrite the prose unless the user asks.

## Output Template

```markdown
## 审查结论
- 是否建议定稿:
- 最大风险:

## 字数核查
- 字数来源:
- 本章最低字数:
- 正文实际字数:
- 是否达标:
- 差额:
- 字数缺失 / 冲突:

## 问题列表
| 严重度 | 维度 | 证据 | 影响 | 修改方向 |
| --- | --- | --- | --- | --- |

## 扩写方案（仅当正文字数低于本章最低字数时输出）
| 场景 | 建议补充字数 | 扩写内容 | 不能补的内容 |
| --- | --- | --- | --- |

## 优先修改
1.
2.
3.
```

## Review Boundary Gate

Review output must stop at current-text issue confirmation.

Allowed output:

- Issue / risk
- Evidence from the current text or source file
- Impact on continuity, character, pacing, word count, or readability
- Revision direction for the current text

Forbidden unless the user explicitly asks for next-step planning:

- Archiving prose
- Generating chapter memory
- Updating the global lore database
- Finalizing, publishing, or saving as canon
- Starting the next chapter
- Preparing the next chapter outline or AI writing instruction
- Saying "字词精修后即可进入下一步", "可以推进下一阶段", "可以归档", "可以生成记忆", or similar workflow progression advice

## Rules

- Findings must include concrete evidence from the text or outline.
- When reviewing chapter planning or prose, verify the complete `本章详细剧情说明` before judging whether the chapter is coherent. A missing or one-line description is a planning defect, not permission to invent missing plot.
- Do not invent canon that is not provided.
- Treat narrative person drift as a continuity problem: if a third-person protagonist such as "林墨 / 他" becomes narrative "我" without source support, list it as an issue and distinguish it from valid dialogue or direct inner quotation.
- Treat prose meta leaks as continuity and immersion problems: if outline-only or table-of-contents language such as "第几卷", "第几章", "本卷", "卷末", "下一章", "后续剧情", "阶段收束", "主线节点", "读者会看到", or "本章真正的冲突" appears in narration, character psychology, or ordinary dialogue without in-world justification, list it as an issue.
- Treat word-count metadata leaks as prose contamination: if `本章字数`, `字数统计`, `番茄计字法`, `本章最低字数`, `字数规则`, `章节备注`, or generation notes appear in prose, list them as issues and direct removal. Word count may remain in the review report, not in正文.
- Treat chapter-to-chapter plot overlap as a major continuity and pacing problem: if this chapter mostly repeats the previous chapter's completed event chain, climax, or hook, mark it High or Blocking and require a new obstacle, information release, decision, consequence, or relationship shift.
- If context is missing, label a risk as "需要对照前文确认".
- Prefer actionable fixes over abstract criticism.
- Do not rewrite the whole unit unless the user asks.
- If the prose is below `本章最低字数`, do not approve it as ready for finalization; provide an expansion plan before polishing.
- If the prose meets `本章最低字数`, do not output an expansion plan.
- If the minimum word count is missing or conflicting, do not output an expansion plan; ask the author to confirm the word count rule first.
- Do not recommend archiving, memory generation, finalization, publishing, next-chapter preparation, or next-stage progression unless the user explicitly asks for next-step planning.

## Common Problems

- Characters explain the plot to each other despite both already knowing it.
- A secret leaks through narration before its reveal window.
- A victory has no cost, making later conflict weaker.
- A unit ends after explanation instead of after a new pull, payoff, or aftertaste.
- The scene solves tension too neatly.
- A standalone piece lacks a clear emotional turn or final landing.
- A character suddenly softens, forgives, confesses, blackens, or collapses without a staged trigger.
- A character keeps the same voice but loses their inner logic.
- A physical detail (device behavior, object reaction, environmental phenomenon) belongs to a different technological era than the story setting, e.g. CRT-era screen behavior described on a modern LED display, mechanical sounds on a solid-state device, or pre-internet habits in a post-smartphone scene.
- The prose leaks outline or author-planning language, e.g. "本卷的主线到这里开始收束", "下一章他将迎来反击", "这是第二卷的关键节点", "本章真正的冲突才刚刚开始", or "读者会看到真正的反噬", when those phrases are not visible in-world text or an approved metafiction device.
- The prose contains bookkeeping or word-count lines, e.g. "本章字数：3086字（番茄计字法）", "字数统计", or "以下是正文".
- The chapter opens by summarizing the previous chapter, then spends its middle replaying the previous climax, so the new chapter has no fresh conflict, information, decision, or result.

