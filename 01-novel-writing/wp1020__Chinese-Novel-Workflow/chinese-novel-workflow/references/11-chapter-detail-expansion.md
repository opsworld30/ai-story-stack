# Narrative Unit Detail Expansion

Use this when the user asks for 叙事单元详细剧情, 章节详细剧情, 场景卡, 节拍拆解, 详细场景拆解, 把大纲扩成可写正文, or when an outline is too broad for stable drafting.

## Core Rule

Turn a narrative-unit outline into concrete, writable scene/beat cards without changing the unit's fixed plot, point of view, character arc, information release, foreshadowing, ending hook, or forbidden drift.

This workflow sits between outline and drafting:

```text
04-outline-workflow -> 11-chapter-detail-expansion -> 12-prewriting-instruction-generator -> 05-chapter-generation
```

For serialized or chaptered fiction, detail expansion must target one chapter at a time. If the source material is a broad structural summary or a merged chapter outline item, first split it into independent chapter outlines with `references/04-outline-workflow.md`, then expand only the requested chapter into detailed beats.

For multi-volume projects, do not create separate per-chapter detail files. Store each target chapter's detailed beats as an independent section inside the volume's canonical chapter-detail file: `大纲/第XX卷/03-章节细纲.md`.

## Required Inputs

Extract or infer:

- Unit identifier, chapter number if relevant, and title
- For chaptered fiction: exact chapter number and title
- Project writing specification, including the global minimum word count rule and any confirmed chapter-level override
- Source chapter outline's word count fields: word count source, final adopted minimum word count, overflow policy, override value, and missing/conflict status
- Unit goal
- Opening pressure
- Main scene list
- Main event chain with 3-6 concrete chapter-level nodes
- Source chapter outline's complete `本章详细剧情说明`, including chronological actions, obstacles, key choice, and direct result
- Main opposition or obstacle
- Protagonist's visible choice or action
- Character change
- Character stage, psychological state, and emotional state
- Information release
- Foreshadowing
- Emotional or爽点 beats
- Ending hook
- Forbidden drift
- Point of view and main cast, if provided

If a missing fact would change canon, ask. Otherwise make a labeled assumption.

## Detail Word Count Gate

Before creating a single-chapter detail expansion, inherit and verify the target chapter's word count fields.

1. Read the target chapter outline entry first.
2. If the chapter outline has `本章最低字数`, inherit it into the detail file.
3. If the chapter outline lacks `本章最低字数`, read `设定/04-创作规格.md` and fill the detail file from the project rule.
4. If the project writing specification is missing or does not define a minimum word count, write `本章最低字数: 需要作者确认`.
5. Do not invent a default number and do not accept a chapter override unless it is author-confirmed and allowed by the project writing specification.

The detail file must include:

```markdown
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
```

For multi-volume projects, write these fields inside the target chapter section in `大纲/第XX卷/03-章节细纲.md`, not in a separate `第XXX章_标题_细纲.md` file.

## Chapter Overlap Gate

Before expanding a chapter into detailed beats, compare it with the previous chapter ending.

The new chapter must not simply retell what the previous chapter has already completed. If the opening only repeats the previous chapter's action, reaction, climax, or hook, rewrite it before expansion.

A valid chapter detail must first preserve and expand the source `本章详细剧情说明`, then clearly separate:

- 本章详细剧情说明（执行版）: the complete chapter event chain in chronological order
- 承接: the pressure inherited from the previous chapter
- 重复: any event that has already been finished in the previous chapter
- 推进: the new conflict, obstacle, information, or choice this chapter adds
- 新结果: the new state, hook, or cost left at the end of this chapter

If the chapter opening is only a replay, revise it toward one or more of these entries:

- 直接接承压点
- 进入新的阻碍
- 推出新的信息
- 做出新的决策

When enriching a thin independent outline, include the overlap gate fields:

```markdown
### 第 N 章 [标题] - 事件链补足
- 本章详细剧情说明（执行版）:
  1. 开场压力与事件触发:
  2. 主角行动与连续阻碍:
  3. 冲突升级与关键选择:
  4. 直接结果与结尾状态:
- 上章已完成:
- 本章新增:
- 本章禁止重演:
- 本章新结果:
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
- 开场压力:
- 本章主要对抗:
- 事件链:
  1.
  2.
  3.
  4.
- 主角本章选择:
- 人物变化:
- 信息释放:
- 结尾钩子:
- 下一章承接:
```

Quality gate: the target chapter has been checked against the previous chapter so its opening does not retell completed events, and its ending leaves a new result instead of extending the same beat.

## Pre-Expansion Gate

Before creating scene cards, confirm the source chapter outline is not merged and not too thin.

Reject or split first if the source contains:

- A heading like `第002-003章`, `第004/005章`, or `第006章-第008章`
- A title with slash-separated chapter concepts, such as `崩塌/邻居`
- Event text that says `002章...，003章...`
- Two chapter endings or two separate chapter climaxes
- A setup event and a payoff event that need different chapter openings

If the outline is independent but too thin, first enrich it into an event chain before scene cards:

```markdown
### 第 N 章 [标题] - 事件链补足
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
- 本章详细剧情说明（执行版）:
  1. 开场压力与事件触发:
  2. 主角行动与连续阻碍:
  3. 冲突升级与关键选择:
  4. 直接结果与结尾状态:
- 上章已完成:
- 本章新增:
- 本章禁止重演:
- 本章新结果:
- 开场压力:
- 本章主要对抗:
- 事件链:
  1.
  2.
  3.
  4.
- 主角本章选择:
- 人物变化:
- 信息释放:
- 结尾钩子:
- 下一章承接:
```

Only after this gate passes should the workflow produce detailed scenes.
## Detailed Plot Handoff

Before writing scene cards, copy or restate the source chapter outline's `本章详细剧情说明` in execution form. Do not replace it with only scene names. Every scene must map to one or more events in that chain, and every event in the chain must have a scene location or an explicit reason for omission. If the detail expansion adds a major event, stop and flag it as a canon decision for author confirmation.

## Expansion Standard

Use `references/14-narrative-readability-standard.md` to keep beats concrete, readable, dialogue-driven, and mobile-friendly.


A scene/beat card is draft-ready only if it includes:

- Location and spatial setup
- Cast present in the scene
- Opening image or first action
- Current pressure
- Protagonist's immediate goal
- Opposition or obstacle
- Concrete plot progression
- Key actions or props
- Key dialogue intent or sample lines
- Information release
- Emotional shift
- Character stage movement
-爽点/reader payoff
- Transition into the next scene
- Attention chain for prose entry

Avoid abstract placeholders like "女主反击", "霸总震惊", "气氛紧张", or "展开冲突" unless followed by concrete behavior.

Do not output broad structural-phase detailed plots for chaptered fiction. Output chapter detailed beats such as `第001章详细剧情` or exact narrative-unit detailed beats. For multi-volume projects, place that chapter section in `大纲/第XX卷/03-章节细纲.md`.

Do not turn a merged chapter outline into one oversized detailed plot. Split first. Each detailed plot file must have one opening pressure, one core chapter conflict, one ending hook, and one next-chapter bridge.


## Output Template

```markdown
## 第 N 章详细剧情: [标题]

### 本章功能
- 字数规则来源:
- 本章最低字数:
- 是否允许自然超出:
- 章节覆盖值:
- 覆盖原因:
- 字数缺失 / 冲突:
- 单元目标:
- 本单元核心冲突:
- 情绪曲线状态: [蓄水期(抑) / 爆发期(扬) / 震荡期(余波)]
- 本单元主要爽点/情绪点:
- 本单元信息释放:
- 本单元伏笔:
- 结尾钩子:
- 禁止写偏:

### 场景 1: [场景名]
- 场景地点:
- 出场人物:
- 开场画面:
- 当前压力:
- 角色目标:
- 阻碍/对抗:
- 具体剧情推进:
  1.
  2.
  3.
- 关键动作/物件:
- 关键对白:
- 信息释放:
- 情绪变化:
- 注意力链:
  - 第一注意物:
  - 打断源:
  - 身体反应:
  - 误判:
  - 确认细节:
  - 下一步动作:
- 人物阶段变化:
  - 本场开始时的性格阶段:
  - 表层情绪:
  - 隐藏情绪:
  - 触发点:
  - 防御动作:
  - 本场结束后的心理/情感变化:
  - 关系姿态变化:
- 爽点落点:
- 转场方式:

### 场景 2: [场景名]
...

### 本单元结尾
- 最后一幕:
- 最后一句/钩子:
- 下一章承接:
```

## Scene Count Guidance

- 1000-2000 words: 2-3 scene cards.
- 3000-5000 words: 3-5 scene cards.
- 6000+ words: 5-8 scene cards, or split the chapter.

Do not add scenes only to fill a quota. Every scene or beat must change pressure, information, relationship, danger, emotion, or choice.

If one source summary contains too many events for a single chapter, split it into multiple chapter outlines before creating scene cards.

If one chapter outline contains both "event that establishes the disaster" and "first intimate confrontation / first kill / first major escape", consider splitting. The first chapter should build the pressure and ending pull; the next chapter should pay it off with its own opening pressure.

## Expansion Pattern

For each broad scene in the chapter outline, expand using:

```text
where -> who -> pressure -> goal -> obstacle -> action -> reveal -> payoff -> transition
```

The scene card is not a paragraph template. It is hidden scaffolding. Prose should enter through POV attention.

For character-driven scenes, expand as:

```text
stage -> surface emotion -> hidden emotion -> trigger -> defense/action -> relationship shift -> next state
```

## Genre Handling

For legal revenge,霸总,重生,穿书,年代,爽文, or other high-concept web fiction:

- Keep the premise's sharp hook visible in every scene.
- Translate abstract revenge into specific legal, social, evidentiary, financial, or relational moves.
- Let power fantasy come from competent choices, not only verbal dominance.
- Give the opposing side visible confidence before the protagonist breaks it.
- Preserve the protagonist's signature method.

## Example: Broad Beat To Scene Card

Broad beat:

```markdown
1. 穿越觉醒，识别处境
```

Expanded scene card:

```markdown
### 场景 1: 手术台醒来
- 场景地点: 私立医院产房
- 出场人物: 苏晚、陆景琛、主刀医生、护士
- 开场画面: 苏晚睁眼时，无影灯刺白，器械盘里手术刀碰出轻响，腹部麻药还没完全退。
- 当前压力: 她刚生产完，身体虚弱，陆景琛控制现场，医生正按他的意思逼近。
- 角色目标: 先确认自己能不能求救，再拖住对方。
- 阻碍/对抗: 身体虚弱、产房被控制、陆景琛默认所有人听他的。
- 具体剧情推进:
  1. 苏晚听见陆景琛说出处理她、留下孩子的霸总式命令。
  2. 她通过台词和环境确认自己穿进原著产房名场面。
  3. 原主记忆与原著剧情同时涌上来，她确认眼前男人就是陆景琛。
  4. 她没有哭闹，先观察门、护士站方向、床头呼叫按钮和座机。
- 关键动作/物件: 她藏在被单下的手往床侧摸，指尖碰到呼叫按钮。
- 关键对白: 苏晚低声说: "你刚才那句话，挺适合做笔录。"
- 信息释放: 苏晚是穿越者，知道原著剧情，也知道陆景琛有税务问题。
- 情绪变化: 恐惧被压下去，职业本能接管。
- 爽点落点: 女主没有按虐文逻辑崩溃，而是第一时间寻找报警条件。
- 转场方式: 她摸到呼叫按钮时，余光看见床头柜上还有一部座机。
```

## Suppression-Release Design Standard (抑扬拉扯设计规范)

To prevent flat pacing or premature release of tension:

1. **Suppression (蓄水/抑) Stage Rules**:
   - Limit the protagonist's direct counter-action: They may observe, plan, or gather evidence, but must not "show their hand" or win yet.
   - Amplify pressure: Highlight the adversary's temporary dominance, the urgency of the threat, or the relational friction. This builds "tension budget" (郁闷感/紧迫度).
   - Do not let the protagonist express emotional defeat; they remain tactically active but physically/socially constrained.

2. **Release (爆发/扬) Stage Rules**:
   - The turning point must be concrete: a hidden contract, a key witness, a recorded call, a sudden skill breakthrough, or an unexpected rule execution.
   - The confrontation must be direct: let the antagonist boast before the reveal.
   - The victory should be definitive: do not leave the target conflict half-resolved in the same unit.

3. **Aftertaste (震荡/余波) Stage Rules**:
   - Emphasize character reactions: show secondary characters' regret, shock, or realization.
   - Describe the adversary's aftermath: panic, silent collapse, or frantic phone calls. This stretches the reader's payoff.

## Quality Gate

Before handing to prewriting instruction generation or prose generation, confirm:

- The unit's emotional suppression-release curve matches its pacing goal.
- Each scene can be written without inventing the next plot step.
- The target is one chapter or one exact narrative unit, not a broad structural phase.
- The source is an independent chapter outline, not a combined heading such as `第002-003章`.
- The chapter has a concrete event chain before scene cards begin.
- For chaptered fiction, the project writing specification is available or the missing rule is explicitly marked; `本章最低字数` is present, and any chapter-level word count override is explicit, author-confirmed, and allowed by the project writing specification.
- Every scene has an action, not only an idea.
- Dialogue intent is present for important confrontations.
- Character stage, surface emotion, hidden emotion, and ending state are visible for important scenes.
- Attention chain is present for scenes that may otherwise become outline-like.
- Information release is distributed across scenes, not dumped at once.




