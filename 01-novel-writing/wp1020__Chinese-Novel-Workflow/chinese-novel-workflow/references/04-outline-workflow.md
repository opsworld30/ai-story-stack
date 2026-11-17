# Outline Workflow

Use this when creating story outlines, volume outlines, chapter outlines, narrative-unit outlines, serialized pacing plans, short-form story beats, or foreshadowing plans.

For scene cards or detailed narrative-unit plot expansion, use `references/11-chapter-detail-expansion.md` after this file.

## Outline Hierarchy

Use chapter-first levels:

1. Story spine: beginning, turning points, midpoint, crisis, climax, ending.
2. Volume arc, when the work truly has volumes: promise, escalation, reversal, payoff.
3. Chapter outline or exact narrative-unit outline: what changes in this chapter/unit.
4. Chapter detailed beats: pressure, beats/scenes, character change, information release, hook/payoff, and forbidden drift.
5. Scene card: concrete location, cast, action, conflict, dialogue, information, emotional turn, and transition. Use `references/11-chapter-detail-expansion.md` for this level.

Broad structural phases are analysis tools only. Do not use them as default file categories, prose targets, or AI writing instruction targets. If source material is a broad phase summary, split it into chapter outlines before any detailed beat expansion or AI writing instruction generation.

## Chapter Outline Word Count Gate

Before creating chapter outlines, read `设定/04-创作规格.md` or the author-confirmed equivalent. Every chapter outline must carry an explicit minimum word count field.

Use this source priority:

1. Project writing specification: global chapter minimum, overflow policy, and whether chapter-level overrides are allowed.
2. Author-confirmed chapter override, only when the specification allows overrides.
3. If the specification is missing or does not define a minimum word count, write `本章最低字数: 需要作者确认` instead of guessing.

Each chapter outline must include:

```markdown
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
```

## Total Outline Template

```markdown
## 总纲
- 开局处境:
- 主线目标:
- 核心对手:
- 中期反转:
- 最大代价:
- 终局答案:

## 分卷规划
| 卷 | 主题 | 主冲突 | 关键升级 | 结尾钩子 |
| --- | --- | --- | --- | --- |

## 伏笔规划
| 伏笔 | 首次出现 | 推进节点 | 回收节点 | 回收效果 |
| --- | --- | --- | --- | --- |
```

## Chapter Outline Template

```markdown
## 第 N 章大纲
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
- 本章目标:
- 本章详细剧情说明:
  1. 开场压力与事件触发:
  2. 主角连续行动与遭遇阻碍:
  3. 冲突升级与关键选择:
  4. 选择造成的直接结果与结尾状态:
- 情绪拉扯状态: [蓄水期(抑) / 爆发期(扬) / 震荡期(余波)]
- 开场压力:
- 主要场景:
  1.
  2.
  3.
- 人物变化:
- 信息释放:
- 伏笔推进:
- 爽点/情绪点:
- 结尾钩子:
- 禁止写偏:
```


## Independent Chapter Rule

For chaptered fiction, chapter outlines must never merge multiple chapters into one heading.

Forbidden heading patterns:

```text
第002-003章
第004/005章
第006章-第008章
第010章及后续
上半章 / 下半章
前两章 / 接下来几章
```

Each chapter outline item must contain exactly one chapter and must have its own:

- Chapter number
- 本章详细剧情说明: a complete chronological event chain, not a one-line summary
- Title
- Minimum word count and word count source
- Opening pressure
- 本章详细剧情说明（按时间顺序写清事件、行动、阻碍、选择和结果）
- 3-6 concrete event nodes
- Main opposition or obstacle
- Protagonist choice or action
- Character change
- Information release
- Ending hook
- Next-chapter bridge
- Forbidden drift

If one item contains multiple chapter numbers, multiple slash-separated titles, or a "this chapter plus next chapter" event chain, split it before continuing.

One-line rule:

```text
章节大纲允许简略，但不允许合章；细纲允许详细，但必须单章执行。
```

## Split-Merged-Chapter Test

If one outline item contains more than one of the following, split it into separate chapter outlines:

- Two or more major locations
- Two or more major confrontations
- Two clear climax beats
- Two possible ending hooks
- Two separate character state changes
- One event that only sets pressure and another event that resolves a different pressure
- A setup chapter plus a payoff chapter compressed into one entry
- A broad event chain that would naturally require separate opening pressure and ending pull

When splitting, preserve continuity:

```text
Chapter A ending hook -> Chapter B opening pressure
```

Do not let Chapter B restart the story from a summary. It should inherit Chapter A's last image, unresolved pressure, and character state.
## Broad Summary To Chapter Outline

When the user provides only a broad stage/phase summary, first convert it into chapter outlines:

```markdown
## 章节大纲

### 第001章 [标题]
- 章节定位:
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
- 开场压力:
- 本章主要事件:
- 本章人物变化:
- 本章信息释放:
- 本章结尾钩子:
- 下一章承接:

### 第002章 [标题]
...
```

Do not generate prose or AI writing instructions from a broad summary until each target chapter has at least a chapter outline.

Do not invent a default minimum word count in chapter outlines. Use the project writing specification confirmed during setup. Only write a chapter-level override when the author has confirmed that this chapter should differ from the global rule and the project writing specification allows overrides. If the source is missing, keep the chapter outline usable but mark `本章最低字数: 需要作者确认`.
Do not output combined chapter entries when converting broad summaries. If the source summary naturally covers multiple chapters, split it into separate chapter outline items even when the source text phrases them together.

Minimum chapter-outline density:

- Opening pressure must be concrete enough to start the chapter.
- Main events must be a numbered chain, not one compressed sentence.
- The protagonist must make at least one visible choice or action.
- The ending hook must be different from the next chapter's full conflict; it should pull, not consume.
- The next-chapter bridge must state what pressure or image carries forward.
- The detailed plot must let a reader retell the chapter from beginning to end and identify the protagonist's key choice and its direct result.

## Handoff To Detailed Plot

A narrative-unit outline is not ready for drafting until it can answer:

- Who is in each scene?
- Where are they standing or moving?
- What pressure starts the scene?
- What does the protagonist do under constraint?
- What does the opposing force do?
- Which specific information is released in this scene?
- Which line, action, object, or decision creates the scene's payoff?
- How does the scene transition into the next one?

If any answer is vague, use `references/11-chapter-detail-expansion.md` before drafting.

Before handing off, verify `本章详细剧情说明` separately from the scene list. It must answer: what starts the chapter, what the protagonist does, what blocks them, what choice changes the situation, and what new result remains. If it cannot answer these questions, do not generate chapter detail yet.

## Detailed Plot Quality Gate

Reject or return the chapter outline for enrichment when `本章详细剧情说明` is:

- one sentence or a keyword chain;
- only a list of scenes or locations;
- a result-only summary with no actions or choices;
- a string of vague phrases such as “发生冲突”“局势升级”“继续调查”;
- a merged description of two or more chapters;
- missing the direct result that changes the chapter-ending state.

A valid description follows:

```text
开场压力 -> 事件触发 -> 主角行动 -> 阻碍/反应 -> 冲突升级 -> 关键选择 -> 直接结果 -> 新的结尾状态
```

It is planning scaffolding, not prose. Do not expand it into dialogue or atmosphere until the detail stage.

If a chapter outline still reads like `核心事件: 002章A，003章B`, it is not a valid chapter outline. Split it into independent chapter outlines before using `references/11-chapter-detail-expansion.md`.

## Pacing Rules

- **情绪抑扬拉扯 (Suppression-Release Curve)**: Each narrative unit must plan its emotional pacing. Do not resolve conflicts instantly. Designate units as either:
  1. **蓄水期 (Suppression/抑)**: Build up adversary pressure, hold back the protagonist's main counter-moves, and accumulate reader anticipation/frustration.
  2. **爆发期 (Release/扬)**: Reveal the trump cards, execute the counterattack, and deliver a satisfying payoff.
  3. **震荡期 (Aftertaste/余波)**: Show secondary reactions (e.g., shock/regret of onlookers, collapse of opponents) and emotional lingering.
- Each narrative unit should change at least one of: information, relationship, status, danger, resource, location, or inner decision.
- Early units need clear external pressure before complex lore.
- A hook can be a new threat, new clue, relationship fracture, reversal, deadline, or uncomfortable choice.
- Do not make every unit end with the same cliffhanger or punchline pattern.
- Foreshadowing must be visible enough to remember and quiet enough to avoid solving itself.

## Continuity Rules

- Keep unit goals aligned with the current story promise and, when relevant, the volume arc.
- Do not introduce a major setting detail without deciding whether it is canon.
- Track unresolved promises to readers.
- Before writing prose, identify what must not be contradicted.
- Before generating AI writing instructions, confirm that the target is a specific chapter or exact narrative unit, not a broad structural phase.
- Before handing off to detailed beats, confirm that no chapter heading or event line merges two or more chapters.
- Before handing off to detailed beats, confirm every chapter outline includes `本章最低字数`; if it is `需要作者确认`, do not silently replace it with a guessed number.


