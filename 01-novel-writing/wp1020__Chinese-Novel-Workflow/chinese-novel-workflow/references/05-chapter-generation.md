# Narrative Prose Generation

Use this when drafting, continuing, expanding, rewriting, or filling any narrative unit: chapter, scene, short story, opening hook, serialized episode, or plot-driven prose fragment.

If the user provides only a broad unit outline, first use `references/11-chapter-detail-expansion.md` to create scene cards unless the user explicitly asks for a rough draft.

Before drafting any prose, continuing a narrative unit, expanding scene/beat cards into prose, or rewriting outline material into正文, always check whether a narrative-unit AI writing instruction exists.

- If it exists and includes a 前文衔接包, load it and treat it as the unit's execution contract.
- If it exists but lacks a 前文衔接包, add that section before drafting.
- If it does not exist, generate it with `references/12-prewriting-instruction-generator.md` before drafting.
- Do not draft prose directly unless the user explicitly says: “不生成创作指令，直接写”.
- For serialized or chaptered fiction, the instruction must be chapter-level or exact narrative-unit-level. Do not draft prose from broad structural-phase instructions.

## Drafting Gate

Use this branch exactly:

1. User asks only for AI 创作指令: output only the instruction.
2. User asks to write prose and provides a valid instruction: draft the prose directly.
3. User asks to write prose but no instruction exists: generate the instruction first, then draft from it if the request implies a full writing workflow.
4. User asks to write prose but the instruction lacks 前文衔接包: add the continuity package first, then draft.
5. User explicitly opts out of instruction generation: lock fixed facts and continuity, then draft without the instruction.
6. User provides only a broad structural summary or broad-phase instruction for chaptered fiction: do not draft yet. First split it into chapter outlines, expand the target chapter into detailed beats with `references/11-chapter-detail-expansion.md`, then generate the chapter AI writing instruction.

If generating the instruction and drafting in the same response would exceed available context or cause low-quality output, stop after the instruction and say the prose should be generated from that contract next.

## Before Drafting

Extract:

- Current unit identifier, title, and goal
- Chapter number and chapter title, when writing chaptered fiction
- Point of view
- Narrative person lock
- POV character
- Protagonist naming form
- Allowed protagonist pronouns
- Forbidden pronoun drift
- Previous scene ending
- Previous unit ending image
- Previous unit final line or final action
- 上一章已完成事件
- 本章禁止重演的事件
- 本章必须新增的事件或结果
- Unresolved tension from previous unit
- Continuity bridge required for this unit opening
- Fixed facts
- Character knowledge limits
- Required foreshadowing
- Desired unit ending, hook, payoff, or aftertaste
- Available scene cards or detailed plot beats
- Attention chain, if provided
- Available AI writing instruction / prewriting contract, if provided
- Style or soul document, if provided

Ask only if a missing answer would force an irreversible story choice.

## Chapter Overlap Ban

Do not let chapter prose repeat the previous chapter's finished event chain.

Forbidden patterns:

- Retelling the previous chapter's opening pressure in summary form
- Replaying the previous chapter's climax
- Repeating the same conflict in two chapters without a new escalation or new result
- Starting with a recap of what readers just watched happen

A chapter opening must enter through at least one of these:

- 新压力
- 新动作
- 新信息
- 新误判
- 新决策
- 新后果

The first scene may echo the previous chapter's final pressure, but it must immediately convert that pressure into a new obstacle, choice, information, consequence, or misread.

## Draft Structure

A narrative unit should usually contain:

1. Immediate pressure or unresolved motion.
2. Scene action, not abstract setup.
3. Character choice under constraint.
4. Consequence or new information.
5. Relationship, status, or danger shift.
6. Ending pull: hook, payoff, reversal, question, or emotional aftertaste.

## Scene Beat Pattern

Use this internally, not as visible headings unless requested:

```text
pressure -> action -> friction -> choice -> consequence -> ending pull
```

## Using Prewriting Instructions

The AI writing instruction is mandatory for prose drafting unless the user explicitly opts out.

When an AI writing instruction exists:

- Treat it as the unit's execution contract.
- Confirm it is for the exact target chapter or narrative unit.
- Confirm it states narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift. If these are missing and the source does not clearly establish them, ask for confirmation before drafting instead of guessing.
- Follow its creator persona, lens identity, sensory priorities, red lines, scene order, output format, and self-check.
- Follow the 前文衔接包 before writing the opening; do not restart the situation as if the previous unit did not exist, and do not replay the previous unit's completed event chain.
- If it conflicts with higher-level canon or user instructions, follow the higher-level canon/user instruction and state the conflict briefly if needed.
- Do not add new story mechanisms, character motives, or reveal timing outside the instruction.

## Using Scene Cards

When scene cards are available:

- Follow the scene order unless the user asks to restructure.
- Convert each scene card into prose with action, dialogue, sensory detail, and transition.
- Keep key dialogue intent, but make the final wording sound like the character.
- Preserve the scene's information release and payoff.
- Do not skip the transition bridge between scenes.
- Do not add new canon just to fill length.
- Do not draft in scene-card field order.
- Treat scene cards as hidden structure, then write through the POV character's attention chain.
- Convert location, pressure, goal, obstacle, and reveal into lived perception, interruption, reaction, and choice.
- Do not treat "write through the POV character" as permission to change narrative person. Third-person limited POV keeps close perception while preserving character name / he / she narration.

## Attention-Driven Drafting

Before drafting, use `references/16-attention-driven-prose.md` when prose may become outline-like, evenly paragraphed, too logical, or too formatted.

Before writing each important scene, choose:

- First attention point
- First interruption
- Body reaction
- Misread or uncertainty
- Recognition detail
- Pressured choice
- Emotion delay
- What must remain unexplained

## Prose Rules

Apply `references/14-narrative-readability-standard.md` for sentence rhythm, dialogue function, scene presence, and mobile reading layout.

- Start with a concrete action, image, line of dialogue, or problem.
- Keep exposition tied to what a character needs now.
- Make dialogue carry relationship pressure, not only information.
- Let emotion leak through behavior, timing, and omission.
- Vary paragraph length.
- Preserve genre expectations: momentum, readable conflict, visible reward, emotional aftertaste, or suspense.



## In-Prose Structure Meta Ban

Do not write author-planning, outline, table-of-contents, platform, or future-chapter language inside narrative prose.

Forbidden in narration, character psychology, and ordinary dialogue:

```text
这是第X卷的开始
到了第X章
本卷主线
卷末
下一章
后续剧情
阶段收束
主线节点
这一章的重点
本章真正的冲突
读者会看到
剧情推进到这里
```

Prose must only write what characters can perceive, say, do, infer, read in-world, or experience now.

Allowed only when the phrase is visible inside the story world, such as system UI, archive/file name, case file title, book title, announcement, task panel, or author-approved metafiction.

Before returning prose, scan narration, psychology, and ordinary dialogue for `第几卷` / `第几章` / `本卷` / `下一章` / `后续剧情` / `阶段收束` / `主线节点` / `读者会看到`. If found without in-world justification, replace it with current action, pressure, information, character inference, or consequence.
## Prose Metadata Output Gate

When generating, continuing, expanding, or rewriting prose, word count and counting method are internal constraints only.

If the target output is narrative prose, especially when saving under `正文/` or when the user says "只给正文", output only story text.

Forbidden in prose output:

```text
本章字数
字数统计
番茄计字法
本章最低字数
字数规则
章节备注
创作说明
以下是正文
正文如下
本章完成
生成说明
```

Allowed locations for word count metadata:

- `设定/04-创作规格.md`
- chapter outline / chapter detail
- AI writing instruction
- continuity review / finalization report
- author-facing diagnostic notes outside the prose file

Before returning prose, scan the first and last paragraphs and remove any non-story bookkeeping line.
## Output Defaults

- If the user asks to write prose and a valid instruction is available, use a `<thought_anchor>` before generation to align focus (defining: 1. POV first attention point; 2. Current conflict pressure; 3. Active character stage constraints). It may be shown in chat as a prewriting note by default, but it must never be written into prose files. If the user explicitly asks for prose-only output or the result will be saved under `正文/`, apply the anchor internally and output only narrative prose.
- Before prose output, verify the narrative person lock. If the instruction says third-person limited POV, use character name / he / she / omitted subject in narration; do not write the protagonist as "I" except in dialogue, direct inner quotation, or author-confirmed first-person passages.
- If the user asks only for the instruction, do not draft prose.
- Do not append word count, counting method, generation notes, or chapter bookkeeping before or after prose. Word count compliance is handled internally and in review outputs, not printed in正文.
- Do not put chapter/volume/outline/future-plot structure language into narration, psychology, or ordinary dialogue. Terms like `第几卷`, `第几章`, `本卷`, `下一章`, `后续剧情`, `主线节点`, or `读者会看到` are allowed only as in-world visible text or approved metafiction.
- For chaptered fiction, do not accept a new target word count at prose drafting time. Use the minimum word count rule inherited from the project writing specification or a confirmed chapter-level override in the AI writing instruction. If the user provides a conflicting word count, stop and ask whether to revise the project writing specification or the chapter-level override first.
- If context is sparse, produce a strong first-pass draft and mark assumptions briefly before the text only when necessary.
- If asked to rewrite, preserve the original plot beats unless the user asks for structural change.
- If the available planning material is broader than one chapter or exact narrative unit, stop and request or generate chapter-level detailed beats before drafting.

## Narrative Unit Self-Check

- Did the generation use a `<thought_anchor>` to align the single LLM's attention chain before generating prose? If the user requested prose-only output or the result is saved under `正文/`, was the anchor kept internal and excluded from the prose file?
- Did the draft exclude word count metadata, counting-method notes, chapter bookkeeping, and workflow labels such as `本章字数` or `番茄计字法`?
- Did the draft keep the locked narrative person?
- If the draft is third-person limited POV, did it avoid turning the protagonist's narration into "I"?
- Is every narrative "我" justified as dialogue, direct inner quotation, or author-confirmed first-person passage?
- Did something change by the end?
- Does the protagonist act instead of only react?
- Does the scene respect character knowledge?
- Does the ending create forward pull, payoff, or aftertaste?
- Did the draft obey the mandatory prewriting instruction?
- Was the instruction tied to the exact target chapter or exact narrative unit?
- Did the opening inherit the 前文衔接包 instead of restarting the scene?
- Did the opening enter through 新压力 / 新动作 / 新信息 / 新误判 / 新决策 / 新后果 instead of summarizing the previous chapter?
- Did the chapter avoid replaying the previous chapter climax or repeating the same conflict without escalation?
- Did the draft avoid summary-heavy AI phrasing?
- Did the prose follow the character's attention chain instead of the outline field order?
- Are paragraph lengths uneven in a purposeful way?
- Did any paragraph explain what the scene already showed?
- Is there enough interruption, delay, misread, silence, or unfinished thought?
- Did it follow `references/14-narrative-readability-standard.md` for sentence rhythm, dialogue function, paragraph focus, and mobile readability?




