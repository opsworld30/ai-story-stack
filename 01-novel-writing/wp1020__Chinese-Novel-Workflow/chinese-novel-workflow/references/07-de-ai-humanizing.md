# Naturalization And De-AI Residue Scan

Use this when the user asks for 自然化顺读润色, 文章自然化, 自然表达修正, 语句别扭, 段落衔接, 读起来不顺, 生硬表达, 润顺一点, 轻修, Gemini 已写得不错只做轻修, 去 AI 痕迹扫描, 去 AI 味, 降低 AI 感, 人味化精修, 改得不像 AI, 去模板腔, 改对白里的 AI 腔, or medium-intensity prose polishing.

## Core Rule

Make prose read naturally as fiction while preserving plot, point of view, relationships, timeline, foreshadowing, ending pull, character intent, and genre promise.

Change expression, rhythm, paragraph order, dialogue movement, action bridges, and concrete details. Do not change story facts or add major events unless the user explicitly asks.

Default intensity: medium.

Default fiction mode is conservative polishing. If the prose is already strong, especially when the user says Gemini wrote it well, run a naturalization pass first and do not run full de-AI rewriting by default. De-AI work should be a residue scan plus local fixes unless the user explicitly asks for stronger cleanup.

Conservative polishing may change wording, sentence order, paragraph rhythm, action bridges, dialogue naturalness, and sensory precision. De-AI residue scanning may only change the specific lines where AI residue is found. Neither mode may change event order, event result, character motive, relationship posture, character knowledge, foreshadowing, reveal timing, or ending hook.

Use `references/14-narrative-readability-standard.md` as the shared standard for sentence rhythm, dialogue interaction, mobile paragraphing, and reader immersion. Use `references/16-attention-driven-prose.md` when prose reads like outline execution or has visible paragraph formatting.

For 极致去AI化, 硬核流畅度润色, 网文金牌责编式重构, 终稿级强去AI, severe machine-flavor cleanup, or mobile端强顺读重构, use `references/13-hardcore-de-ai-line-edit.md` instead.

## Mode Selection

| User symptom | Use mode |
| --- | --- |
| Gemini 写得不错、只做轻修、润顺一点 | Naturalization pass only, then optional residue scan if obvious issues remain |
| 语句别扭、段落跳、衔接硬、读起来不顺 | Naturalization pass |
| 对白像说明书、心理太直白、场景动作像清单 | Naturalization pass; fix only the affected lines |
| 去 AI 痕迹扫描、查 AI 味、看看哪里像 AI | De-AI residue scan report first; local fixes only if requested |
| 去 AI 味、降低 AI 感、模板腔 | De-AI residue scan + local fixes |
| 自然化去 AI 润色 | Naturalization pass -> De-AI residue scan -> local fixes only |
| 机器味很重、伪深刻旁白、大段需要重构 | Escalate to `13-hardcore-de-ai-line-edit.md` |


## Audience And Tone Gate

Before polishing, identify the polishing profile:

- Text type: fiction prose, dialogue, synopsis, author note, article, speech, report, marketing copy, or mixed text
- Target reader: genre readers, ordinary public readers, professional readers, platform editors, or internal project users
- Intended tone: restrained, sharp, comic, warm, formal, plain, suspenseful, intimate, or public-facing humorous
- Purpose: immerse, explain, persuade, summarize, introduce, sell, comfort, or entertain
- Allowed intimacy: direct reader address, first-person commentary, rhetorical questions, jokes, and colloquial turns are allowed only when the text type permits them

For fiction prose, map the profile to genre, POV, character stage, relationship pressure, and reader expectation. Do not default to "ordinary public + humorous".

For article-like or auxiliary prose, the profile may allow more direct explanation, reader address, first-person reflection, and light humor, but the edit must still preserve facts and avoid hollow enthusiasm.

## Story Lock Gate

Before polishing fiction prose, extract the story state that must survive the edit:

- Fixed plot facts:
- Event order and event results:
- Character body / mental / emotional state:
- Relationship posture:
- Character knowledge boundaries:
- Foreshadowing and unrevealed information:
- Ending hook / aftertaste:
- Allowed edit scope:

Allowed edit scope depends on the selected mode:

- Naturalization pass: wording, sentence order, paragraph rhythm, action bridges, dialogue naturalness, sensory precision.
- De-AI residue scan: diagnose AI residue first; only locally revise the exact lines or short passages where residue is found.
- Combined pass: run naturalization first, then scan residue; do not rewrite clean passages just to make the whole text "less AI".

If the prose cannot be improved without changing character behavior, motive, relationship posture, reveal timing, or event result, stop and report it as a story-editing decision instead of silently changing it.

## Naturalization Pass

Use this as the default fiction polish when the prose is already good. Focus on flow, sentence order, paragraph transitions, scene continuity, emotional pacing, and readability. Do not actively chase AI residue during this pass.

Typical symptoms:

- Sentences are grammatically correct but feel awkward.
- Paragraphs jump without emotional or action bridges.
- Dialogue carries information but lacks conversational movement.
- Psychological narration explains too much or arrives too early.
- Scene actions are listed rather than staged.
- Small gestures feel stylish but float without cause, consequence, object, or next choice.
- Tone shifts too suddenly.
- Paragraph order weakens tension.
- Prose has useful content but lacks breath.

Revision sequence:

1. Identify the scene function: conflict, transition, reveal, emotional beat, setup, payoff, or ending pull.
2. Mark fixed facts that must not change.
3. Smooth paragraph order before polishing individual sentences.
4. If prose reads like outline execution, rebuild paragraph order around the POV character's attention chain instead of only polishing sentences.
5. Add or adjust minimal action bridges when transitions feel abrupt.
6. Move explanation after action when readers can first infer emotion.
7. Keep dialogue incomplete when natural speech would be incomplete.
8. Preserve genre rhythm and reader expectation.
9. Stop before adding new plot events, new characters, or new canon.

## De-AI Residue Scan

Use this as a scan-and-local-fix pass, not a full rewrite pass. First list the exact residue found. If little or no residue is found, say so and avoid unnecessary rewriting.

Remove or weaken only where these patterns actually appear:

- Summary voice: 这一切、显然、事实上、实际上、毫无疑问、无可否认
- Explanation voice: 其实、说白了、换句话说、简单来说、通俗点讲
- Template transitions: 然后（作为无因果的纯时间连接）、与此同时、紧接着、就在这时、恰在此时、正当此刻
- Hollow adjectives / empty inflation: 复杂、微妙、深刻、独特、特殊、极其、无比、前所未有、难以形容等词，只有在空泛、无动作支撑、无人物声线、无场景后果时才算病灶。正常网文允许夸张形容、强情绪、重复强调和戏剧化表达。
- Repeated turns: 然而、但是、不过、可是 in every paragraph
- Overused similes: 似乎、仿佛、如同、宛如、犹如
- Mechanical phrases: 目光交汇的瞬间、空气仿佛凝固、心中五味杂陈、眼神变得坚定
- Humanizer-zh style generic AI vocabulary when used as empty emphasis: 此外、至关重要、深入、彰显、展现、赋予、承载、格局、关键、核心、宝贵、充满活力、无缝、直观、强大
- Westernized syntax / Translation-ese (西式长定语与翻译腔): 冗余代词（无必要的主语他/她/它）、多重"的"字长定语、不自然被动句（无谓、欧化、削弱动作链或被动感官中介的"被"字句；不得因出现"被"字就自动修改）、英文式逻辑词堆砌（事实上、关于这一点、正如我们所知）
- Three-step negation-explanation template (三段式否定解释模板): "现象 → 然后 → 不是A → 而是B"。这是AI写作中极强的指纹——作者跳出来先排除读者的"错误理解"，再给出"正确理解"，本质是教学而非叙事。修复方式：将"不是A"直接删除，将"而是B"转换为POV人物的直接感知结果。如果A是读者不会产生的误解，则"不是A"连存在的必要都没有。
- Quote-like golden sentences: "这不是X，而是Y", "这一刻，某某终于明白", "真正的X从来不是Y". Keep only if it is a character's distinct voice, a deliberate hook, or genre-required爽点台词.
- Generic positive or concluding summaries: "一切都会好起来", "新的篇章即将开启", "命运的齿轮开始转动", "这只是开始". Replace with a concrete hook, object, decision, or unresolved pressure.
- Overqualified hedging: 某种程度上、可以说、似乎有些、或许可能、潜在地. Keep uncertainty only when it belongs to POV misread or character knowledge limits.
- Neat three-item rhythm: three adjectives, three abstract nouns, or three balanced actions used only to sound complete. Use two, four, or an uneven action sequence unless the character is intentionally speaking in a formal/listing style.

Method:

1. Identify text function: narration, dialogue, psychology, scene, action, emotional burst, suspense, chapter ending.
2. Mark only the exact words, sentences, or short passages that show AI residue.
3. Delete filler that does not move plot, character, atmosphere, or rhythm.
4. Replace abstract emotion with action, sensory detail, dialogue, silence, object handling, or choice only in the marked location.
5. Break overly balanced sentence patterns only where the pattern is visible.
6. Make dialogue less complete and more relationship-specific only when the original line is exposition-like.
7. Leave clean passages untouched.
8. Before revising a 被字句, run the be-sentence protection check: keep it if it carries pressure, victimhood, restraint, being forced/trapped, unknown actor, POV limit, idiom, or character voice; revise only if it is unnecessary passive voice, westernized passive syntax, or passive sensory mediation.
9. Before weakening an exaggerated adjective, repeated emphasis, or dramatic phrase, run the rhetorical intensity protection check: keep it if it serves genre intensity, character voice, pressure, humor, humiliation, suspense,爽点, emotional payoff, rhythm, or relationship tension. Revise only if it is empty emphasis with no scene function.

## Fiction-Adapted Humanizer Rules

Borrow Humanizer-zh as a lesion scanner, not as a prose goal.

- Directness: scene prose should show the object, action, pressure, or choice directly. Do not announce significance before the reader sees what happened.
- Rhythm: vary sentence and paragraph length by pressure, not by decorative "literary" balance.
- Trust: delete explanations that only prove what the reader already understands.
- Authenticity: make the line sound like this POV character or this relationship, not like a neutral article.
- Precision: remove filler, but do not compress away suspense buildup, reaction beats, aftertaste, or necessary web-fiction release.

When applying these rules to fiction, always ask:

- Is this sentence moving plot, pressure, relationship, information, atmosphere, or character state?
- Is this "human" detail functional, or just decoration?
- Is this line a narrator slogan, or would this character actually notice/say/think it now?


## Article-Like Polishing Mode

Use this mode only for non-fiction or auxiliary text such as essays, public-facing articles, book introductions, author notes, summaries, speeches, reports, or platform copy. Do not apply it blindly to chapter prose.

Revision sequence:

1. Clarify purpose, reader, and tone before rewriting.
2. Diagnose the top 2-3 AI traits: rigid sentence pattern, emotional flatness, stiff transition, redundant listing, generic conclusion, hollow enthusiasm, or over-formal phrasing.
3. Preserve core meaning, facts, names, data, and argument order unless the user asks for restructuring.
4. Reshape structure only when paragraph order blocks comprehension.
5. Vary sentence rhythm with natural Chinese flow, not decorative inversion or forced rhetoric.
6. Replace abstract neutral wording with concrete verbs, grounded details, and context-appropriate emotion.
7. Remove mechanical list markers and stock transitions such as "首先/其次/总之/值得注意的是/基于以上分析" when prose would flow better without them.
8. Add reader interaction, rhetorical questions, first-person perspective, or humor only when the polishing profile allows it.
9. Read once as the target reader and remove new AI flavor introduced by over-polishing.

Article-like polishing output may include:

```markdown
## 原文 AI 特征分析
- 

## 核心优化策略
- 

## 优化后的文章
[revised text]
```

If the user says "只给正文" or "只给结果", run the analysis internally and output only the revised text.
## Revision Directions

| Problem | Revision direction |
| --- | --- |
| Sentence is correct but stiff | Reorder clauses, shorten overloaded lines, vary rhythm. |
| Paragraph jump feels abrupt | Add a small action, sensory cue, or reaction bridge. |
| Dialogue sounds like exposition | Cut known information, add evasion, interruption, or relationship pressure. |
| Emotion is over-explained | Let action, silence, object handling, or delayed reply carry it. |
| Scene feels flat | Clarify pressure, choice, and consequence without adding new plot. |
| Transition feels mechanical | Replace summary transition with concrete movement or time cue. |
| 气氛紧张 | Use sound, pause, interrupted action, or a small object. |
| 他很犹豫 | Show a half-finished action, repeated choice, or self-denial. |

| Floating gesture / fake restraint detail | Tie the gesture to pressure, object, hidden impulse, next choice, or another character's reaction; delete it if it only decorates mood. |
| Broken short-sentence chain | Keep the short rhythm, but restore why this sentence follows the last and what it changes next. |

## Dialogue Rules

- Shorten lines when emotion is high.
- Let familiar characters omit background.
- Let conflict create interruption, evasion, repetition, or misdirection.
- Different characters must not share the same rhythm.
- Do not make dialogue serve as an exposition manual.
- Do not flatten rough, local, childish, cold, arrogant, or comedic voice into polished neutrality.


## Two-Pass Naturalization And Residue Scan

Use a two-pass process adapted for simplified Chinese web fiction. For Gemini-first workflows, the second pass is a scan, not a second full rewrite.

### First Pass

Revise for natural flow, dialogue movement, paragraph rhythm, scene continuity, and reader immersion. Apply `references/14-narrative-readability-standard.md` during this pass. Do not rewrite clean prose just to lower AI flavor.

### Second Pass

- 是否出现正文内结构元叙事：`第几卷` / `第几章` / `本卷` / `下一章` / `后续剧情` / `阶段收束` / `主线节点` / `读者会看到` 等作者规划语言？如不是故事内可见文本或批准的元叙事，必须改成角色当下可感知的动作、压力、信息或判断。

Before final output, scan the revised prose again and ask:

- 哪些句子还像总结？
- 哪些段落还像说明书？
- 哪些对白不像人在当场说话？
- 是否出现整齐排比、三段式、万能转折？
- 是否出现 Humanizer-zh 常见病灶：AI高频词、三段式列举、通用积极结论、金句式总结、过度限定？
- 是否能看出大纲字段顺序？
- 是否每段都太完整、太均匀？
- 是否缺少打断、迟滞、误判、半句话？
- 是否有"这一刻 / 显然 / 事实上 / 不仅……更是……"等 AI 痕迹？
- 是否残留了英文式翻译腔句式、多重"的"字定语、无谓/欧化/感官中介型被动句？正常承担受害、压迫、状态承接、信息隐藏或人物口吻功能的被字句不得列为病灶。
- 是否把正常网文需要的夸张、强情绪、戏剧化形容、重复强调误判为 AI 味？只有空泛、无动作支撑、无人物声线、无场景后果的夸张才需要修改。
- 是否有重复解释前文信息，导致章节衔接变钝？

- Are there floating close-up gestures such as a hand pausing, eyes moving, breath catching, or fingers tightening without function?
- Do short standalone sentences connect through pressure, attention, object, consequence, or choice?
If residue is found, revise only the affected lines or short passages before delivering the final prose. Output only the final version unless the user asks for process notes.

## Drift Audit

After polishing fiction prose, compare the revised prose against the original. If any locked story item changed, revise again and restore the original story state unless the user explicitly requested story rewriting.

| Check | Changed? | Required action |
| --- | --- | --- |
| Event order | No | Revert if changed |
| Event result | No | Revert if changed |
| Character motive | No | Revert if changed |
| Character stage / state | No | Revert if changed |
| Character relationship posture | No | Revert if changed |
| Character knowledge boundary | No | Revert if changed |
| Foreshadowing / reveal timing | No | Revert if changed |
| Ending hook / aftertaste | No | Revert if changed |

## Output Modes

Default (To prevent single LLM cognitive drift, force diagnostics and plan before the prose):

```markdown
## 润色排查与策略
- 当前模式：自然化顺读润色 / 去 AI 痕迹扫描 / 自然化后局部去 AI
- 识别出的顺读问题：
- 识别出的 AI 痕迹（仅列命中项）：
- 段落与衔接调整策略：
- 不可改剧情事实：
- 不可改事件顺序 / 事件结果：
- 不可改人物状态：
- 不可改人物关系：
- 不可改角色认知：
- 不可改伏笔 / 结尾钩子：
- 本次只允许修改：

## 润色修正版
[revised prose]

## 润色后漂移审计
| 检查项 | 是否改变 | 处理 |
| --- | --- | --- |
| 事件顺序 / 结果 | 否 |  |
| 人物动机 / 阶段 / 状态 | 否 |  |
| 人物关系姿态 | 否 |  |
| 角色认知边界 | 否 |  |
| 伏笔 / 揭示时机 / 结尾钩子 | 否 |  |
```

If the user says "只给正文" or "只给结果", run the story lock gate, second pass, and drift audit internally, then output only revised prose.

## What Not To Do

- Do not rewrite the story into a different plot.
- Do not add major events just to make the prose exciting.
- Do not make a character wiser, softer, crueler, calmer, more romantic, or more decisive than the original stage allows.
- Do not repair plot logic by changing character motive or relationship posture during polishing.
- Do not add new information a character did not know in the original.
- Do not turn conservative polishing into editor-style rewriting unless the user asks.
- Do not run full de-AI rewriting when the user only asked for naturalization, light polish, or Gemini-first touch-up.
- Do not rewrite clean passages during a de-AI residue scan.
- Do not make every sentence literary or ornate.
- Do not remove useful genre directness from web fiction.
- Do not explain every edit unless the user asks.
- Do not compress the chapter unless the user asks.
- Do not treat polishing as academic editing or marketing copywriting.
- Do not use public-facing article habits in fiction unless allowed by POV or genre: direct reader address, first-person editorial comments, rhetorical questions to the reader, cheerful humor, and speech-like persuasion can break immersion.
- Do not add metaphors, personification, inversion, or parallelism just to look human; in fiction, action chain, attention chain, and character voice matter more than decorative rhetoric.

## Final Checklist

- Plot facts preserved.
- Event order and results preserved.
- Character motive, stage, body/mental/emotional state preserved.
- Relationship posture and character knowledge boundaries preserved.
- Foreshadowing, reveal timing, and ending hook preserved.
- Character intent and voice preserved or sharpened.
- Paragraph transitions are readable.
- Paragraph order follows attention chain rather than outline-field order.
- Dialogue sounds like people in relationship, not exposition delivery.
- Emotion arrives through scene movement before explanation.
- Close-up gestures are functional, not decorative.
- Short sentences preserve rhythm without breaking the action chain.
- AI-style template residue is reduced.
- Prose is smoother without becoming generic.
- Ending pull and foreshadowing remain intact.
- Humanizer residue scan passes: no empty emphasis, slogan-like summary, generic conclusion, or decorative three-part rhythm remains unless intentionally used for character voice.
- Polishing profile respected: the revised text matches its text type, target reader, intended tone, and allowed intimacy level.







