# Narrative Unit Prewriting Instruction Generator

Use this when the user asks for AI 创作指令, 写作前指令, 叙事单元创作指令, 正文生成前约束, 写章提示词, or wants a narrative-unit instruction document before drafting.

## Purpose

Create a narrative-unit AI writing contract before prose generation.

This workflow turns project notes, unit outline, scene/beat cards, character files, readability rules, style rules, and red lines into a clear instruction document that another AI can follow to draft the narrative unit without drifting.

It sits between scene/beat expansion and prose drafting:

```text
11-chapter-detail-expansion -> 12-prewriting-instruction-generator -> 05-chapter-generation
```

## Core Rule

The instruction must constrain the draft, not replace the story.

Do not invent major canon, hidden motives, world rules, character arcs, legal facts, relationship changes, or reveal timing that are not present in the source material.

For serialized or chaptered fiction, AI writing instructions must be generated per chapter. Do not generate broad structural-phase AI writing instructions for prose drafting. If the source material is only a broad summary, first create chapter outlines, then chapter detailed beats, then one AI writing instruction for the target chapter.

Lock narrative person separately from POV. Third-person limited POV may stay close to the protagonist's perception, but it must not convert the protagonist's narration into first-person "I" unless the user explicitly asks for first-person narration.

## Required Inputs

Before generating a chapter-level AI writing instruction, read the source files needed to build continuity. Do not rely on the target chapter outline alone.

For chapter N, required source reading is:

1. Target chapter detail / scene-card source: for multi-volume projects, use the target chapter section inside `大纲/第XX卷/03-章节细纲.md`; for single-volume projects, use the project's equivalent chapter-detail source
2. Target chapter outline entry: for multi-volume projects, use `大纲/第XX卷/02-章节大纲.md`; otherwise use `大纲/01-章节大纲.md` or the equivalent chapter outline entry for chapter N
3. Optional chapter-detail index: `大纲/02-章节细纲索引.md`, only if the project actually maintains this file
4. Project writing specification: `设定/04-创作规格.md` or the author-confirmed equivalent
5. Previous chapter narrative memory: `记忆/第N-1章_叙事记忆.md`
6. Recent narrative memories when continuity depends on ongoing state: usually the latest 2-3 chapter memories
7. Global lore database or setting files if available: character state, relationship state, timeline, location state, organization changes, foreshadowing state, and canon constraints

If the target chapter is the opening chapter, explicitly mark that no previous chapter memory exists and use project setup, character files, and opening pressure instead. If an expected memory file is missing, state the missing source and mark the affected continuity items as needing author confirmation instead of inventing them.

If `大纲/02-章节细纲索引.md` does not exist and the project does not use a chapter-detail index, do not list it as a missing required source. Use the target chapter outline entry plus the target chapter section in `03-章节细纲.md`.

If the project uses volume folders under `大纲/第XX卷/`, do not look for root-level `大纲/章节细纲/` or a target volume `03-章节细纲/` folder as the required detail location. Their absence is normal; use the target volume's `03-章节细纲.md` file and extract the target chapter section.

## Word Count Source Gate

Before writing the instruction, determine the chapter's minimum word count from source files:

1. Read the target chapter detail / scene-card section and inherit its `本章最低字数` if present.
2. Read the target chapter outline entry in `大纲/01-章节大纲.md` or the equivalent chapter outline/index to verify the inherited value.
3. Read `设定/04-创作规格.md` for the project-level prose unit, global minimum word count, overflow policy, whether chapter-level overrides are allowed, and how word count changes are approved.
4. If the chapter detail section and chapter outline agree, use that value as the final adopted minimum word count.
5. If the chapter detail section lacks the field but the chapter outline has it, inherit from the chapter outline.
6. If both detail and outline lack the field, use the project-level minimum word count.
7. If a valid chapter-level override exists and overrides are allowed by the project writing specification, use the override as the final adopted minimum word count.
8. If the project writing specification is missing or does not define a minimum word count, do not invent a number. Mark `本章最低字数: 需要作者确认` and state the missing source.
9. If the chapter detail, chapter outline, and project writing specification conflict, flag the conflict and use `需要作者确认` unless the author-confirmed override clearly resolves it.

The generated AI writing instruction must include:

Word count is a drafting constraint and review datum, not prose content. The instruction may state `本章最低字数` and `字数规则来源`, but must explicitly forbid printing chapter word count, counting method, or bookkeeping metadata inside正文 output.

```markdown
### 字数规则来源
- 项目创作规格:
- 章节大纲字数规则:
- 目标章细纲字数规则:
- 章节大纲字数覆盖:
- 是否允许章节覆盖:
- 本章最低字数:
- 自然超出规则:
- 字数缺失 / 冲突:
```

Extract or infer from available material:

- Unit identifier, chapter number if relevant, and title
- For chaptered fiction: exact chapter number, chapter title, and target prose file if known
- Volume name, only if relevant
- Project writing specification, including the global minimum word count rule and any confirmed chapter-level override
- Unit position in the book, arc, sequence, or standalone story
- Narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift
- Project/volume style rules
- Unit goal and opening pressure
- Source chapter outline's complete `本章详细剧情说明`, which is the authoritative chapter event-chain handoff
- Source files actually read for this instruction
- Previous chapter narrative memory used for continuity
- 本章详细剧情说明
- 上一章已完成事件
- 本章必须新增的事件
- 本章禁止重演的事件
- 本章必须把剧情推进到哪里
- Recent chapter memories used for ongoing state, if any
- Global lore / character / relationship / foreshadowing entries used, if any
- Previous unit/chapter ending image
- Previous unit/chapter final line or final action
- Opening continuity bridge
- Protagonist current body state from previous unit/chapter
- Protagonist current mental state from previous unit/chapter
- Key characters positions, relationships, and attitudes from previous unit/chapter
- Released information readers already know
- Unresolved suspense and pressure
- Foreshadowing that this unit must inherit
- Previous information that must not be repeated as exposition
- 本章详细剧情说明（必须完整引用或准确压缩，不得改写成空泛摘要）
- Scene cards or detailed plot beats
- Character state anchors
- Character stage anchors from `references/15-character-depth-arc.md`, if available
- Required information release
- Foreshadowing and payoff requirements
- Red lines and forbidden drift
- Desired unit hook, payoff, or aftertaste
- Output format required by the user

If source files are listed, include them under "统一依据". If no file paths are provided, cite the available source names generically without fabricating paths.

## Chapter Difference Gate

Before generating the instruction, compare the target chapter against the previous chapter's ending and against the target chapter detail section.

The instruction must state:

- 本章详细剧情说明
- 上一章已完成事件
- 本章必须新增的事件
- 本章禁止重演的事件
- 本章必须把剧情推进到哪里

Generation self-check before prose drafting:

- Is this chapter only retelling the previous chapter in different words?
- Does it add a new conflict escalation, viewpoint change, information release, relationship change, decision, or consequence?
- Does the opening inherit pressure without summarizing the full previous event chain?
- If the answer is no, send the material back to chapter outline or chapter detail expansion before drafting.

## Detailed Plot Fidelity Gate

Before generating the instruction, compare the chapter outline `本章详细剧情说明` with the chapter-detail section. Confirm:

- every major event in the outline is represented in the detail scenes;
- the protagonist''s action, key choice, and direct result remain unchanged;
- the detail does not add a major event, reveal, relationship change, or ending result absent from the outline;
- the chapter remains one independent chapter and does not merge another chapter''s event chain.

If the source field is missing, vague, or conflicts with the chapter detail, stop and list the exact missing or conflicting items. Do not generate the AI writing instruction or prose until the author confirms or revises the chapter plan.

## Output Structure

Use this structure by default:

```markdown
# 叙事单元 AI 创作指令：[标题]

## 1. 【AI 创作者人格设定】

## 2. 统一依据

## 3. 本单元基础信息

## 4. 前文衔接包

## 5. 前后章差异检查

## 6. 本单元核心任务

必须先列出：

### 本章详细剧情说明
- 开场压力与事件触发:
- 主角行动与主要阻碍:
- 冲突升级与关键选择:
- 直接结果与结尾状态:

这部分是剧情事实底稿，不是正文，不得用场景标题或一句话摘要替代。

## 7. 人物状态锚点

## 8. 本单元设定红线

## 9. 本单元情绪曲线

## 10. 注意力链写法

## 11. 场景拆解

## 12. 关键台词功能

## 13. 写作风格要求

## 14. 本单元真人作者化微调

## 15. 禁用项

## 16. 单元钩子 / 情绪落点

## 17. 生成前自检

## 18. 正文输出要求

Must include this red line:

```text
正文输出不得在叙述、人物心理或普通对白中写入章节/卷/大纲/未来剧情结构语言，如“第几卷”“第几章”“本卷”“下一章”“后续剧情”“阶段收束”“主线节点”“读者会看到”“本章真正的冲突”。这些词只可作为故事内可见文本、系统界面、档案名、书名、公告、任务面板、卷宗标题，或作者明确允许的元叙事。
```
```

## Section Guidance

### 1. AI Creator Persona

Define:

- Project or volume-level inheritance.
- Genre-specific author identity.
- Unit lens identity.
- Style pressure: speed, coldness, comedy, legal precision, emotional restraint, dread, warmth, etc.
- Sensory priority.
- Psychological writing rule.
- Extra unit taboos.

For example, legal revenge comedy may use:

- Cold legal precision under bodily pressure.
- Anti-overbearing-CEO romance logic.
- Competence fantasy through evidence, procedure, and calm tactical choices.

### 2. Unified Sources

List source materials the draft must obey:

- Project framework
- Character file
- Volume rules
- Unit outline or chapter outline
- Scene cards
- Target chapter detail / scene-card section
- Target chapter outline entry
- Optional chapter-detail index, only if the project maintains one
- Previous chapter narrative memory
- Recent chapter memories used for continuity
- Global lore database entries used for character, relationship, timeline, location, organization, foreshadowing, or canon constraints
- Legal or setting notes
- Style/soul document

State conflict priority:

```markdown
> 若本单元内容与统一依据冲突，一律以统一依据为准；若单元指令与用户最新要求冲突，以用户最新要求为准。
```

### 3. Basic Unit Info

Include:

- Volume, only if relevant
- Unit identifier and chapter number if relevant
- Unit title
- Word count rule inherited from the project writing specification, with any confirmed chapter-level override
- Final adopted minimum word count and its source
- Unit position
- Point of view
- Narrative person
- POV character
- Protagonist naming form
- Allowed protagonist pronouns
- Forbidden pronoun drift

Use this structure when relevant:

```markdown
### 叙事人称锁定
- 叙事人称:
- POV 角色:
- 主角称谓:
- 正文主角代词:
- 禁止代词漂移:
```

For third-person limited POV, write explicitly:

```markdown
- 禁止代词漂移: 不得把“[主角名] / 他 / 她”改写成“我”；“我”只能出现在角色对白、直接心理引语或作者明确要求的第一人称片段中。
```

### 4. Previous-Text Continuity Package

Always include this section. It prevents narrative-unit openings from feeling disconnected.

Build this section from the previous chapter narrative memory first. Use recent chapter memories and global lore to resolve ongoing injuries, emotional states, relationship posture, known information, unresolved pressure, and foreshadowing. Do not fill these fields from the target chapter outline alone unless the unit is an opening chapter or no memory source exists.

Use this structure:

```markdown
## 4. 前文衔接包

### 4.1 上一单元收束点
- 上一单元最后画面：
- 上一单元最后一句 / 最后动作：
- 上一单元遗留压力：
- 读者此刻最关心的问题：

### 4.2 本单元开场承接
- 开场时间：
- 开场地点：
- 主角身体状态：
- 主角心理状态：
- 场面未解决问题：

### 4.3 连续性硬约束
- 不能跳过：
- 不能重复解释：
- 不能突然改变：
- 必须自然接上的动作 / 情绪 / 信息：

### 4.4 前文伏笔与本单元关系
- 已埋伏笔：
- 本单元推进方式：
- 暂不揭示内容：
```

If no previous unit exists, explicitly write “本单元为开篇 / 独立篇，无前文承接”, then define the opening pressure and initial reader question instead.

### 5. Core Tasks

Split into:

- Must-complete main tasks
- Must-advance information points
- Results that cannot be skipped

### 6. Character State Anchors

For each important character:

- Current body state
- Current mental state
- Current personality stage
- Current emotional state
- Surface emotion vs hidden emotion
- Current relationship posture toward other key characters
- Trigger that may make the character attack, retreat, soften, lie, or lose control
- Current resources/power
- What this character can do in this unit
- What this character absolutely cannot do in this unit
- What psychological or emotional change is allowed by the end of this unit
- What stage jump is forbidden
- Dialogue/behavior notes

### 7. Setting And Logic Red Lines

Use categories suited to the project:

- Ability red lines
- Legal logic red lines
- Worldbuilding red lines
- Character red lines
- Relationship red lines
- Reveal timing red lines

### 8. Emotion Curve

Use a compact curve:

```text
opening state -> disturbance -> pressure rise -> decision/action -> payoff/hook
```

Make it unit-specific, not generic.

### 9. Attention Chain Writing

Define how prose should enter and move without exposing outline structure:

- First attention point
- First interruption
- Body reacts before thought
- Misread / uncertainty
- Recognition detail
- Delayed emotion
- What should remain unsaid or unexplained
- Allowed one-line paragraphs / unfinished thoughts
- Formatted paragraph pattern to avoid
- Floating gesture guard: any close-up action such as a hand pause, breath catch, eye movement, finger tightening, or step stopping must have pressure, object, impulse, consequence, or next-choice function.

### 10. Scene Breakdown

Convert each scene card into writing instructions:

- Word range
- Action chain
- Character reactions
- Information purpose
- Sensory anchors
- Required dialogue or dialogue function
- Transition

### 11. Key Dialogue Function

Do not only list lines. Explain each line's function:

- Establish power relation
- Break trope expectation
- Plant legal evidence
- Expose arrogance
- Create hook
- Show character voice

### 12. Writing Style Requirements

Specify:

- Rhythm
- Sentence density
- Dialogue style
- Exposition rules
- Sensory order
- Humor/irony intensity
- Unit pacing

### 13. Human-Author Micro-Adjustment

Add unit-level anti-AI controls and apply `references/14-narrative-readability-standard.md`: 

- Avoid neat explanatory paragraphs.
- Add small physical discomfort, object handling, timing, and interrupted speech.
- Avoid fake restraint details: do not add small gestures only to look subtle or literary.
- Keep short sentences, but make sure their action chain stays connected through pressure, attention, consequence, or choice.
- Preserve useful roughness in dialogue.
- Let the scene show before narration explains.

### 14. Forbidden Items

List concrete no-go items. Avoid vague "do not write badly" rules.

### 15. Unit Hook Or Payoff

Define:

- Last scene
- Last line or last image
- Reader question, hook, emotional aftertaste, or next-unit pull

### 16. Pre-Generation Self-Check

Use 5-10 check questions that directly guard against this unit's failure modes.

Always include continuity questions:

- 生成本指令前是否读取了上一章叙事记忆？
- 若人物状态、关系变化或伏笔跨越多章，是否读取了最近 2-3 章叙事记忆？
- 是否读取了可用的全局设定库 / 人物状态 / 关系状态 / 伏笔状态？
- 本单元开场是否承接了前文最后画面？
- 主角身体 / 心理状态是否连续？
- 核心人物当前性格阶段是否连续？
- 核心人物的表层情绪和隐藏情绪是否清楚？
- 本单元是否出现了未经铺垫的心软、黑化、动摇、原谅或告白？
- 是否跳过了前文留下的压力？
- 是否重复解释了读者已经知道的信息？
- 本单元第一场是否能从前文自然滑入，而不是像重启？
- 正文是否按人物注意力进入，而不是按大纲字段进入？
- 是否避免了“环境-动作-心理-解释”的固定循环？
- 是否保留了情绪滞后、误判、打断和不完整念头？
- 是否在生成正文前使用了 `<thought_anchor>`（定义首个注意点、压力和性格约束）以对齐注意力链？若用户要求只给正文，或正文将保存到 `正文/` 文件夹，是否已改为内部执行，并确认不会写入正文文件？
- 是否明确禁止把字数统计、番茄计字法、本章最低字数、章节备注、创作说明等元信息写入正文？
- 叙事人称是否已锁定？
- 若为第三人称有限视角，是否明确禁止把主角称谓从“角色名 / 他 / 她”漂移成“我”？
- 正文中的“我”是否只允许出现在对白、直接心理引语或作者明确允许的第一人称片段中？

- Are close-up gestures functional rather than decorative?
- Do short standalone sentences still connect through pressure, attention, object, consequence, or choice?

### 17. Prose Output Requirements

Define:

- Before generating prose, execute a `<thought_anchor>` to define the POV first attention point, current pressure, and active character stage constraint. The anchor may be shown in chat as a prewriting note by default, but it must not be written into the prose file. If the user explicitly requests prose-only output or the result will be saved under `正文/`, apply this anchor internally and output only narrative prose.
- Before generating prose, execute a narrative person check: confirm narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift. If narrative person is third-person limited, do not convert the protagonist into first-person "I" narration.
- For third-person limited POV, the prose may follow the POV character's perception, misreading, reaction, and judgment closely, but narration must still use character name / he / she / omitted subject. "I" is allowed only in dialogue, direct inner quotation, or author-confirmed first-person passages.
- Output only正文 or include title
- Follow the final adopted minimum word count listed in `### 字数规则来源`. Allow natural overflow; do not compress scenes, skip transitions, or delete character reactions to control word count.
- No outline headings in the prose unless requested
- 正文元信息输出门控: 字数规则只作为内部约束执行。正文中不得输出 `本章字数`、`字数统计`、`番茄计字法`、`本章最低字数`、`字数规则`、`章节备注`、`创作说明`、`以下是正文`、生成说明或任何非故事元信息。
- Preserve unit hook, payoff, or aftertaste
- No explanation after prose unless requested

## Genre-Specific Instruction Notes

### Legal Revenge / Anti-CEO Romance

Use legal procedure as power fantasy:

- Evidence, police, tax, contracts, medical records, surveillance, witness, and procedure should matter.
- The protagonist wins first by identifying the violation and preserving proof.
- Do not let the overbearing CEO be softened into a romantic savior.
- Do not turn legal logic into a lecture; embed it in action, phone calls, wording, and evidence handling.

### Rebirth / Transmigration / Book-Transmigration

- The protagonist may know future or source-plot information, but must still be limited by body, location, and evidence.
- Release original-plot memory only when it changes the immediate choice.
- Do not dump the whole novel premise in the opening scene.

### High-Pressure Opening Unit

- Open with pressure, not encyclopedia setup.
- Anchor the body first, then memory, then tactical choice.
- Let the first win define the protagonist's method.


Do not transfer names, settings, legal facts, tropes, or plot examples from the sample skeleton into unrelated works. The example shows structure only.
## Example Mini Skeleton

```markdown
# 叙事单元 AI 创作指令：重生产房

## 1. 【AI 创作者人格设定】
- 你是一位擅长反套路霸总文、法律爽文、女性复仇文的成熟网文作者。
- 本单元不是虐恋开局，不是霸总救赎，不是女主崩溃独白。
- 本单元核心质感是：疼、冷、准、狠、合法反击。

## 4. 前文衔接包
- 本单元为开篇，无前文承接。
- 开场必须直接承接“产房手术台上的身体危机”，不要先解释世界观。
- 读者初始问题：苏晚如何在失血、疼痛和被控制状态下保住自己？
- 禁止一开章回忆原著全貌；只释放会影响报警动作的信息。

## 5. 前后章差异检查

## 6. 本单元核心任务

必须先列出：

### 本章详细剧情说明
- 开场压力与事件触发:
- 主角行动与主要阻碍:
- 冲突升级与关键选择:
- 直接结果与结尾状态:

这部分是剧情事实底稿，不是正文，不得用场景标题或一句话摘要替代。
1. 让苏晚在产房醒来并迅速识别处境。
2. 展示陆景琛的霸总式违法控制。
3. 让苏晚不哭闹、不求饶，而是寻找报警条件。
4. 完成 110 报警。
5. 埋下陆景琛税务问题伏笔。

## 17. 生成前自检
- 苏晚是否始终保持法治执行者逻辑？
- 陆景琛是否仍是违法控制者，而非深情男主？
- 产房压迫是否具体？
- 本单元是否自然承接上一单元 / 开篇压力？
- 报警动作是否清楚？
- 税务伏笔是否自然埋入？
- 结尾钩子 / 情绪落点是否保留？
```

## Quality Gate

Before handing the instruction to prose generation, confirm:

- It includes enough constraints to prevent trope drift.
- It does not invent new canon.
- It names the unit's author persona and lens identity.
- For chaptered fiction, it is bound to one exact chapter, not a broad structural phase.
- It locks character stage, psychological state, emotional state, relationship posture, and forbidden behavior.
- It locks narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift.
- It gives scene-by-scene writing instructions, not only a plot summary.
- It includes the complete `本章详细剧情说明` and the detail section agrees with it event by event.
- It does not proceed when the detailed plot is missing, vague, merged across chapters, or materially inconsistent.
- It includes a 前文衔接包 or explicitly marks the unit as an opening / standalone unit.
- It lists the source files actually read, including the target chapter section in the volume chapter-detail file, previous chapter narrative memory, relevant recent memories, and global lore entries when available.
- It lists `设定/04-创作规格.md` and the target chapter outline entry when generating chapter-level instructions, or states the missing source explicitly.
- Its 前文衔接包 is built from narrative memory and lore sources, not only from the target chapter outline.
- It includes `### 字数规则来源` and a final adopted minimum word count inherited from the target chapter detail section, verified against the chapter outline and project writing specification; missing or conflicting rules are marked as needing author confirmation.
- It defines final output requirements.













