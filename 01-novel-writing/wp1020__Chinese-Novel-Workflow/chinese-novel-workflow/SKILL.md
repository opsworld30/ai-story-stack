---
name: chinese-novel-workflow
description: Use when creating, planning, drafting, reviewing, revising, polishing, organizing, or finalizing Chinese narrative writing, including web novels, short stories, chapters, scenes, opening hooks, plot-driven prose, chapter-level prewriting AI instruction prompts, continuity checks, natural expression revision, de-AI prose humanization, hardcore final-pass line editing, file organization, and memory-oriented writing workflows.
version: 0.6.26
---

# Chinese Narrative Writing Workflow

## Version

- Current version: `0.6.26-chapter-detailed-plot-gate`
- Date: 2026-07-21
- Version focus: requires a complete 本章详细剧情说明 as the factual event-chain handoff from chapter outline to chapter detail, while preserving independent chapter boundaries and preventing outline, volume, or future-plot structure language from leaking into prose.
- Compatibility principle: Humanizer-zh is treated as a general AI-writing lesion dictionary, not as a replacement for novel craft. All borrowed rules must be converted into fiction terms: POV attention, scene pressure, dialogue relationship, character voice, and plot movement.

## Core Principle

Preserve story truth before improving expression. Treat every task as a narrative unit, whether it is a chapter, scene, short story, opening hook, continuation, rewritten fragment, or plot-driven prose passage.

Do not change fixed plot facts, point of view, relationships, timeline, canon rules, foreshadowing, character knowledge, unit function, or ending pull unless the user explicitly asks.

Prose polishing is expression editing, not plot editing. Before de-AI polishing, lock fixed plot facts, character state, relationship posture, character knowledge, foreshadowing, and ending pull; after polishing, audit whether any of them changed.

## Shared Terms

- Narrative unit: chapter, scene, short story, opening hook, continuation, rewritten fragment, serialized episode, or any prose passage with story movement.
- Previous-text continuity package: last image/action/line, unresolved pressure, body state, mental state, known information, inherited foreshadowing, and what must not be repeated.
- AI writing instruction: an executable prewriting contract for the next narrative unit. It constrains style, facts, scene order, voice, red lines, continuity, character stage, readability, and output requirements.
- Memory source gate: before generating a chapter-level AI writing instruction, read the target chapter detail/scene cards, the immediately previous chapter memory, relevant recent chapter memories, and global lore entries needed to build the continuity package.
- Optional chapter detail index: `大纲/02-章节细纲索引.md` is optional. If the project does not maintain this file, do not report it as a missing required source; use the target chapter outline file plus the target chapter's section inside the volume chapter-detail file instead. In multi-volume projects, those usually live in `大纲/第XX卷/02-章节大纲.md` and `大纲/第XX卷/03-章节细纲.md`.
- Volume outline folder gate: for multi-volume projects, every volume-level planning artifact must live under `大纲/第XX卷/`: `00-卷纲.md`, `01-人物设定.md`, `02-章节大纲.md`, and `03-章节细纲.md`. `03-章节细纲.md` is the single canonical chapter-detail file for the volume; each chapter detail must be stored as an independent heading/section inside it. Do not create `03-章节细纲/` folders or `第XXX章_标题_细纲.md` per-chapter detail files for multi-volume projects. Do not scatter volume character settings under `设定/人物/`, `设定/第XX卷/`, or duplicate them outside the canonical `大纲/第XX卷/01-人物设定.md`.
- Narrative person lock: before generating chapter-level AI writing instructions or prose, identify the narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift. Third-person limited POV may stay close to the POV character's perception, but it must not convert the protagonist's narration from character name / he / she into first-person "I" unless the user explicitly asks.
- Memory position gate: before generating chapter memory, read the chapter prose, target chapter detail/scene cards, AI writing instruction, chapter outline, optional chapter detail index only if the project maintains one, total outline or volume outline, previous chapter memory, and relevant lore so the memory can distinguish chapter-level closure from volume-level or book-level closure.
- Memory template integrity gate: before outputting chapter memory, verify that every required memory section, field, and table from `references/09-memory-update.md` is present. Missing sections must be output as empty but explicit fields, not silently omitted.
- Lore ingestion position gate: before merging chapter memory into the global lore database, verify the memory's chapter-position section against chapter outline, optional chapter detail index if maintained, volume, total-outline, or author evidence; reject or downgrade unsupported volume, arc, or book ending claims to "未确认".
- Project writing specification: an author-confirmed project setting for prose unit, minimum word count rule, overflow policy, special-unit exceptions, and whether chapter-level overrides are allowed.
- Word count source gate: before generating a chapter-level AI writing instruction, read `设定/04-创作规格.md` and the target chapter's chapter outline entry. The instruction must state the global minimum word count, any chapter-level override, the final adopted minimum word count, and the source used.
- Outline/detail word count gate: before generating chapter outlines or chapter detail expansions, read `设定/04-创作规格.md`; every chapter outline and chapter detail file must state the final adopted minimum word count, whether chapter override is allowed, any override value, and missing/conflict status.
- Prose word count review gate: during chapter prose continuity review, read the chapter prose, AI writing instruction, chapter detail, chapter outline entry, and `设定/04-创作规格.md`; compare actual prose word count with `本章最低字数`. Output a scene-by-scene expansion plan only when actual prose word count is below the chapter minimum. If word count passes, do not output an expansion plan. If the minimum word count is missing or conflicting, ask for author confirmation instead of outputting an expansion plan.
- Prose meta-leak review gate: during continuity review, scan prose for outline-only structure labels such as volume number, current volume, volume ending, next chapter, later plot, arc closure, mainline node, or author-planning language. Treat them as issues unless they are legitimate in-world text, titles, UI/system messages, archive names, or explicitly allowed metafiction.
- Prose metadata output gate: chapter word count, counting method, writing specification, review bookkeeping, source labels, and workflow notes are internal metadata. They may appear in settings, outlines, chapter details, AI writing instructions, reviews, and finalization records, but must never be written into `正文/` prose files. Examples to exclude from prose: `本章字数`, `番茄计字法`, `字数统计`, `本章最低字数`, `字数规则`, `章节备注`, `创作说明`, `以下是正文`.
- In-prose structure meta leak gate: prose narration, character psychology, and ordinary dialogue must not mention chapter number, volume number, current volume, next chapter, later plot, arc stage, outline node, reader-facing future preview, or author-planning language. Terms such as `第几卷`, `第几章`, `本卷`, `下一章`, `后续剧情`, `阶段收束`, `主线节点`, `读者会看到`, and `本章真正的冲突` are allowed only when they are legitimate in-world visible text, archive names, system UI, file names, book titles, case files, announcements, task panels, or explicitly approved metafiction.
- Chapter overlap guard: chapter N must inherit the pressure left by chapter N-1, but it must not repeat chapter N-1's completed event chain, climax beat, or final hook. Every new chapter must add a new event, new information, new decision, or new result.
- Detailed plot handoff gate: every independent chapter outline and chapter-detail section must contain `本章详细剧情说明`. It must describe the complete chronological event chain from opening pressure, event trigger, protagonist action, obstacle, escalation, key choice, and direct result to ending state. A one-line summary, keyword list, scene-title list, or merged multi-chapter description is not sufficient. If the field is missing, vague, or cannot show what changes through the chapter, stop before generating chapter detail, AI writing instructions, or prose and request the missing information.
- Be-sentence protection gate: do not treat every `被` sentence as AI residue. Keep natural 被字句 when they express pressure, victimhood, restraint, humiliation, being forced/trapped, unknown actors, POV-limited knowledge, character voice, or a smoother Chinese idiom. Only revise unnecessary passive voice, westernized passive syntax, or passive sensory mediation.
- Rhetorical intensity protection gate: do not treat exaggerated adjectives, strong emotion, dramatic phrasing, repetition, or heightened genre language as AI residue by default. Chinese web fiction often needs intensity. Only revise inflated wording when it is empty, generic, unsupported by scene action, not character-voiced, or does not move pressure, relationship, information, atmosphere, rhythm, humor, humiliation, suspense,爽点, or consequence.
- Review boundary gate: review tasks must stop at issue confirmation, evidence, impact, and revision direction. Do not recommend archiving, memory generation, finalization, publishing, next-chapter preparation, or other workflow progression unless the user explicitly asks for next-step planning.
- Humanizing: improve rhythm, action, dialogue, paragraphing, sensory texture, and reader immersion without changing story facts.
- Character stage: a character's current personality expression, psychological state, emotional state, relationship posture, and permitted change within a narrative unit.
- Attention chain: the order in which a POV character notices, misreads, reacts, recognizes, and chooses inside a scene.
- Sensory synergy: a technique ensuring that any major environmental shift (e.g., rule invasion, power failure, explosion) triggers multiple interacting senses (sound, light, temperature, tactile state) rather than a single isolated mechanical description.
- Chapter-level production: for serialized or chaptered fiction, planning, detailed beats, AI writing instructions, prose drafting, memory updates, and final checks must be bound to a specific chapter, not to a broad structural phase.
- Independent chapter outline: for chaptered fiction, each chapter outline item must describe exactly one chapter with its own number, title, opening pressure, 本章详细剧情说明, event chain, character change, information release, ending hook, and next-chapter bridge. Combined headings such as `第002-003章` are migration problems, not valid default output.
- Structural phase: an internal planning span used only for pacing or escalation. Do not use it as a file category, prose unit, or AI writing instruction target.
- Naturalization pass: a conservative readability pass that smooths sentence flow, paragraph transitions, action bridges, dialogue movement, and POV attention without actively chasing AI residue.
- De-AI residue scan: a local scan-and-fix pass for generic AI-writing residue such as filler transitions, slogan-like claims, neat three-part rhythm, false profundity, generic positive conclusions, overqualified statements, and quote-like summaries. Use it only after locking story facts, and only rewrite the lines where residue is found.
- Polishing profile: the text type, target reader, intended tone, purpose, and allowed intimacy level before revision. For fiction, translate this into genre, POV, character stage, relationship pressure, and reader expectation; do not default to public-article friendliness.

## Workflow Router

Load only the reference file needed for the current stage.

| User intent | Required reference |
| --- | --- |
| 开新书、短故事、叙事项目定位、题材定位、卖点设计、项目基调 | `references/01-project-setup.md` |
| 项目文件夹分类、作品目录结构、按卷归档、设定/大纲/正文/创作指令分类、整理项目文件 | `references/17-project-file-organization.md` |
| 世界观、力量体系、势力结构、冲突链 | `references/02-story-architecture.md` |
| 人物卡、主角弧光、反派、配角、角色声线 | `references/03-character-system.md` |
| 人物立体化、性格阶段、心理变化、情感变化、人物弧光深化、避免人物跑偏 | `references/15-character-depth-arc.md` |
| 总纲、分卷大纲、章节细纲、叙事单元大纲、节奏规划 | `references/04-outline-workflow.md` |
| 写正文、写章节、写场景、写叙事单元、续写、扩写、改写 | `references/05-chapter-generation.md` |
| 正文太规整、段落格式感、写得像大纲、缺少真人写作流动感、注意力驱动写法、人物注意力链、去格式化正文 | `references/16-attention-driven-prose.md` |
| 审稿、查崩坏、查设定冲突、查伏笔、查叙事衔接 | `references/06-continuity-review.md` |
| 自然化顺读润色、语句别扭、段落衔接、生硬表达、读起来不顺、轻修、Gemini 已写得不错只做轻修、去 AI 痕迹扫描、降低 AI 感、模板腔、人味化精修、文章润色、普通大众向文本润色、幽默风趣润色 | `references/07-de-ai-humanizing.md` |
| 定稿、保存前检查、发布前检查、入库前检查 | `references/08-finalization-checklist.md` |
| 叙事单元记忆、章节记忆、人物状态、伏笔、时间线沉淀 | `references/09-memory-update.md` |
| 叙事单元详细剧情、章节详细剧情、场景卡、节拍拆解、把大纲扩成可写正文 | `references/11-chapter-detail-expansion.md` |
| AI 创作指令、写作前指令、叙事单元创作指令、正文生成前约束、给 AI 的写作提示词 | `references/12-prewriting-instruction-generator.md` |
| 极致去AI化、硬核流畅度润色、网文金牌责编式重构、强去AI腔终稿 | `references/13-hardcore-de-ai-line-edit.md` |
| 中文叙事顺读标准、网感、句式、对白、移动端排版、读者留存自查 | `references/14-narrative-readability-standard.md` |
| 全局设定库维护、Lore Book、记忆合并、背景设定冲突、滑动窗口检索、长线设定管理 | `references/10-lore-database-maintenance.md` |

## Default Workflow

1. Identify the user's current stage and load the matching reference.
2. Extract fixed facts before generating or revising.
3. Before drafting prose, require a narrative-unit AI writing instruction; generate it with `references/12-prewriting-instruction-generator.md` if missing, unless the user explicitly opts out. Before generating that instruction, apply the memory source gate, word count source gate, and narrative person lock: read the target chapter detail/scene cards, target chapter outline entry, `设定/04-创作规格.md`, previous chapter narrative memory, relevant recent 2-3 chapter memories when continuity depends on them, and global lore/person/relationship/foreshadowing entries if available; then explicitly state narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift.
4. If an AI writing instruction exists but lacks a previous-text continuity package, add that package before drafting.
5. For serialized or chaptered projects, reject structural-phase prose generation, merged chapter outline items, and chapter-to-chapter plot repetition: if the available material is only a broad phase/volume summary, a combined chapter entry, or a target chapter that only replays the previous chapter, first split or revise it into an independent chapter outline, then chapter detailed beats, then chapter-level AI writing instructions.
6. For new projects or projects missing a writing specification, confirm the project-level minimum word count rule with the author and store it in settings before later creative stages depend on it.
7. Before generating chapter outlines or chapter detail expansions, apply the outline/detail word count gate and detailed plot handoff gate. Do not output a chapter outline or target chapter detail section without explicit `本章最低字数` and `本章详细剧情说明` fields.
8. Ask only when missing information would cause a risky story change.
9. Produce the requested artifact directly.
10. For review tasks, list blocking issues first with concrete evidence and apply the review boundary gate and prose meta-leak review gate. Do not add "next stage", "archive", "generate memory", "finalize", "publish", or "start next chapter" suggestions unless explicitly requested.
11. During chapter prose continuity review, apply the prose word count review gate and the in-prose structure meta leak gate. If actual prose word count is below the chapter minimum, mark it as a blocking or high-priority issue and provide an expansion plan that preserves plot facts, scene order, character state, and ending hook. If word count passes or the minimum is unconfirmed, do not output an expansion plan.
12. For prose revision, separate naturalization from de-AI cleanup. If the draft is already strong, especially when the user says Gemini wrote it well, default to a light naturalization pass first. Use de-AI residue scanning only when requested or when obvious residue remains. Always extract a story lock list before either pass, revise expression only, and run a drift audit after revision. If drift is found, revert that part unless the user explicitly requested story rewriting. If the user explicitly asks for prose-only output, apply the lock list and drift audit internally and output only the revised prose.
13. During prose drafting, apply the prose metadata output gate and the in-prose structure meta leak gate. If the output target is `正文/` or the user asks for prose-only output, return only narrative prose; do not output word count lines, counting-method notes, chapter bookkeeping, prefaces, after-notes, workflow labels, or author/outline/table-of-contents structure language inside narration.
14. Before finalizing, check continuity, character voice, pacing, ending pull, actual prose word count, AI-flavor residue, and whether chapter-position / volume-status claims are supported before memory ingestion.
15. Before generating chapter memory, apply the memory position gate and memory template integrity gate. Do not infer volume ending, arc ending, or book ending from prose tone alone; require explicit support from chapter outline, chapter index, volume outline, total outline, or author instruction. Keep all required memory headings, fields, and tables even when content is empty or unconfirmed.
16. Before merging chapter memory into the global lore database, apply the lore ingestion position gate. Do not write unsupported "本卷结束", "阶段收束", "主线告一段落", "全书进入尾声", or "最终结局临近" into long-term lore.

## Drafting Gate

When the user asks to draft, continue, expand, or rewrite prose:

- If the user provides an AI writing instruction with a previous-text continuity package, draft from it. Before generating prose, use a `<thought_anchor>` to align the POV attention point, current pressure, and active character constraints. It may be shown in chat as a prewriting note by default, but it must never be written into prose files. If the user asks for prose-only output or the result will be saved under `正文/`, apply the anchor internally and output only narrative prose.
- For chaptered fiction, the instruction must be tied to a specific chapter or exact narrative unit. Do not draft from a broad structural-phase instruction.
- If the instruction exists but the continuity package is missing, add the package first, then draft.
- If no instruction exists, generate the instruction with `references/12-prewriting-instruction-generator.md` first, then draft if the user requested the full writing workflow.
- If the user only asks for the instruction, output only the instruction.
- If the user explicitly says “不生成创作指令，直接写”, skip the instruction but still lock fixed facts, continuity, and the `<thought_anchor>` before drafting; hide the anchor when prose-only output is requested or when writing to `正文/`.
- Check absolute quantifiers (e.g., 'all', 'completely') against immediate downstream scene actions. If sub-elements (like a character's phone) must remain active or unaffected, do not apply absolute coverage to the group.

## Recommended Narrative Production Chain

Use this order for narrative prose production when enough planning material exists:

```text
17-project-file-organization (when creating or reorganizing project files)
-> 04-outline-workflow
-> 10-lore-database-maintenance (to recall settings and active character wikis)
-> 15-character-depth-arc (when characters feel functional or stage changes are unclear)
-> 11-chapter-detail-expansion (when outline is broad)
-> 12-prewriting-instruction-generator
-> 16-attention-driven-prose (before drafting prose or when prose risks becoming outline-like)
-> 05-chapter-generation
-> 06-continuity-review
-> 07-de-ai-humanizing (naturalization pass by default; de-AI residue scan only when needed)
-> 13-hardcore-de-ai-line-edit (optional, only for extreme final-pass cleanup)
-> 08-finalization-checklist
-> 09-memory-update
-> 10-lore-database-maintenance (to merge narrative-unit changes to the global database)
```

## Output Defaults

- Planning: use compact structured sections that can be reused as project notes.
- Chapter outlines and chapter detail expansions: include `字数规则来源`, `本章最低字数`, and a complete `本章详细剧情说明` for every chapter. The detailed plot is inherited from the chapter outline and expanded into scene-level action without inventing major canon.
- Project file organization: separate settings, outlines, chapter-level AI writing instructions, prose, memory, and final-review files. Use volume folders only for genuinely multi-volume works; when using them, put volume outline, volume character settings, volume chapter outline, and volume chapter details under `大纲/第XX卷/` with fixed names `00-卷纲.md`, `01-人物设定.md`, `02-章节大纲.md`, and `03-章节细纲.md`.
- Character design: define surface role, inner mechanism, stage changes, emotional leakage, relationship triggers, and red lines.
- Scene/beat expansion: turn broad outlines into concrete scenes or beats with location, pressure, action, dialogue, information release, emotional turn, and transition.
- Prewriting instruction: mandatory before prose drafting unless the user explicitly says “不生成创作指令，直接写”; produce a narrative-unit AI writing contract that locks style, tasks, red lines, scene/beat order, previous-text continuity, voice, readability standards, and output requirements.
- Prewriting narrative person: state the narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift. If the project uses third-person limited POV, explicitly forbid converting the protagonist into first-person "I" narration.
- Prewriting word count: include the final adopted minimum word count in the AI writing instruction's basic information and prose output requirements, with evidence from `设定/04-创作规格.md` and any target chapter outline override.
- Drafting: output usable narrative prose from the AI writing instruction, not process explanation; hide outline structure and write through POV attention chain.
- Drafting metadata boundary: word count rules guide generation internally. Do not print `本章字数`, `番茄计字法`, `字数统计`, `本章最低字数`, `字数规则`, source notes, or any chapter bookkeeping inside正文 output.
- Reviewing: output issue severity, evidence, impact, and fix direction.
- Review boundary: stop at current-text issue confirmation. Do not infer that few issues means the work can be archived, memorized, finalized, published, or advanced to the next chapter.
- Continuity review word count: report the minimum word count, actual prose word count, gap, source, and pass/fail result. Output an expansion plan only when the draft is short.
- Continuity review meta-leak: report any outline-only or table-of-contents structure language that leaks into narration, character psychology, or ordinary dialogue, including `第几卷`, `第几章`, `本卷`, `卷末`, `下一章`, `后续剧情`, `阶段收束`, `主线节点`, `读者会看到`, or author-planning language, unless the wording is a valid in-world title, visible text, UI/system message, archive name, or explicitly allowed metafiction.
- Prose revision and de-AI polishing: preserve plot while improving sentence flow, paragraph transitions, rhythm, readability, dialogue, mobile reading texture, and template-like AI residue.
- Hardcore de-AI line editing: use only for final-pass, high-intensity editorial reconstruction that removes machine flavor, fake profundity, passive perception, and paragraph bloat while preserving canon.
- Memory update: output structured Markdown/JSON-like bullets suitable for later storage, with chapter-position validation before any volume/arc/book status claim, and with every required memory template section retained. Empty content must be written as "无"; unsupported or source-missing content must be written as "未确认".
- Lore merge: ingest only supported local memory facts; unsupported volume/arc/book status claims must be flagged, downgraded to "未确认", or sent back for author confirmation before entering the global database.

## Hard Limits

- Do not overwrite the user's authorial intent with generic "better story" ideas.
- Do not merge all characters into one voice.
- Do not reduce a character to role function, trope label, or plot tool when a scene depends on their psychology or emotional change.
- Do not expose outline structure in prose by writing in scene-card field order.
- Do not make every paragraph equally complete, balanced, or explanatory.
- Do not explain every emotion when the scene can carry it.
- Do not remove foreshadowing, ending pulls, intentional hooks, or intentional ambiguity.
- Do not treat scene-card expansion as permission to add major plot events outside the outline.
- Do not let Chapter N repeat Chapter N-1's completed plot. Chapter N may inherit the previous pressure, but it must introduce a new change, new obstacle, or new result.
- Do not treat prewriting instructions as permission to invent canon beyond supplied planning material.
- Do not write `<thought_anchor>` into chapter prose files. It is a prewriting alignment note for chat display or internal execution, not narrative text.
- Do not draft, continue, expand, or rewrite prose before checking for an AI writing instruction and its 前文衔接包 / context bridge, unless the user explicitly opts out.
- Do not set a default minimum word count inside this skill. Minimum word count must come from the author-confirmed project writing specification, with optional explicit chapter-level overrides.
- Do not generate chapter outlines or chapter detail expansions that omit `本章最低字数`, `字数规则来源`, or `本章详细剧情说明` with missing/conflict status.
- Do not generate a chapter-level AI writing instruction that omits the final adopted minimum word count, its source, or whether a chapter-level override exists. If `设定/04-创作规格.md` is missing, mark the word count rule as needing author confirmation instead of guessing.
- Do not generate a chapter-level AI writing instruction that omits narrative person, POV character, protagonist naming form, allowed protagonist pronouns, and forbidden pronoun drift. If the project or chapter narrative person is missing, mark `叙事人称: 需要作者确认` instead of guessing or converting perspective.
- Do not accept a new target word count during chapter prose drafting. If the word count rule changes, revise the project writing specification or an explicit chapter-level override before drafting.
- Do not write chapter word count, counting method, or bookkeeping metadata into `正文/` files. Forbidden prose lines include but are not limited to: `本章字数：3086字（番茄计字法）`, `字数统计`, `番茄计字法`, `本章最低字数`, `字数规则`, `章节备注`, `创作说明`, `以下是正文`, and postscript-style generation notes. Word count may be reported only in review/finalization outputs, never as part of narrative prose.
- Do not let author, outline, table-of-contents, platform, or future-chapter structure language enter narration, character psychology, or ordinary dialogue. Replace `第几卷`, `第几章`, `本卷`, `下一章`, `后续剧情`, `阶段收束`, `主线节点`, `读者会看到`, `本章真正的冲突`, or similar planning terms with in-world action, pressure, information, character inference, or visible consequences unless the phrase is legitimate in-world text or approved metafiction.
- Do not change narrative person. Third-person limited POV means close perception distance, not first-person pronoun conversion. Do not rewrite the protagonist's narration from character name / he / she into "I" unless the user explicitly asks for first-person narration. "I" is allowed only in dialogue, direct inner quotation, or a source-confirmed first-person passage.
- Do not omit required chapter memory sections, fields, or tables. If a field has no confirmed content, write "无" or "未确认"; do not delete the heading, table, or field. Do not merge memory sections or convert required tables into prose summaries.
- Do not report `大纲/02-章节细纲索引.md` as a missing required source unless the project explicitly maintains and depends on a chapter detail index. Its absence is normal for projects that use a chapter outline file plus chapter sections inside the volume chapter-detail file; for multi-volume projects, use `大纲/第XX卷/02-章节大纲.md` and `大纲/第XX卷/03-章节细纲.md`.
- Do not scatter volume-level planning artifacts across unrelated folders. For a multi-volume project, do not save `第XX卷` character settings to `设定/人物/`, `设定/第XX卷/`, or any duplicate path; the only canonical volume character file is `大纲/第XX卷/01-人物设定.md`. Do not save volume outlines to `大纲/卷纲/`, volume chapter outlines to root `大纲/`, chapter details to root `大纲/章节细纲/`, chapter details to `大纲/第XX卷/03-章节细纲/`, or chapter details as separate `第XXX章_标题_细纲.md` files. Use `大纲/第XX卷/00-卷纲.md`, `01-人物设定.md`, `02-章节大纲.md`, and chapter sections inside `03-章节细纲.md`.
- Do not approve chapter prose continuity if actual prose word count is below `本章最低字数`. Do not output expansion plans when word count passes or the minimum is unconfirmed. Do not pad with repeated exposition, empty scenery, generic introspection, or summary; when the draft is short, propose functional expansion tied to action, pressure, dialogue, character reaction, sensory detail, information release, or transition.
- Do not allow outline-only structure labels to leak into prose narration. Terms such as "第几卷", "本卷", "卷末", "下一章", "后续剧情", "阶段收束", or "主线节点" must be flagged during continuity review unless they are legitimate in-world text, titles, UI/system messages, archive names, or explicitly allowed by the author.
- Do not turn review results into workflow progression advice. Do not say "可以归档", "生成记忆", "进入下一章", "推进下一阶段", "可以定稿", or similar next-step recommendations unless the user explicitly asks for those recommendations.
- Do not use broad structural phases as default file categories, AI writing instruction targets, or prose drafting units.
- Do not generate phase-level正文 or phase-level AI writing instructions for chaptered fiction; split to chapter outline -> chapter detailed beats -> chapter AI writing instruction -> chapter prose.
- Do not output combined chapter outline headings such as `第002-003章`, `第004/005章`, `第006章-第008章`, `第010章及后续`, or `上半章/下半章` for chaptered fiction. Split them into independent chapter outline items before detailed beats or drafting.
- Do not treat a one-sentence chapter event summary as detailed plot. Every chapter outline must first state `本章详细剧情说明` as a chronological chain of actions, obstacles, choices, and results. If it is missing or too thin, enrich the chapter outline before using `references/11-chapter-detail-expansion.md` for scene cards.
- Do not treat prose revision or de-AI polishing as plot rewriting, compression, academic editing, or marketing copywriting.
- Do not impose public-article, speech-script, first-person commentary, direct reader address, or humorous-friendly tone on fiction prose unless the project POV, narrator style, or user request explicitly allows it.
- Do not treat hardcore de-AI line editing as permission to change plot, genre, POV, canon, or unit function.
- Do not bypass the POV character's cognitive delay (cognitive damping) to deliver instant objective truths. Always follow the attention chain order: physical sensation -> misread/uncertainty -> close observation of anomalies -> final logical recognition.
- Do not use chronologically inconsistent physical properties or outdated technology details that clash with the story's contemporary setting (e.g., modern LCD/OLED screens experiencing a CRT-style center-point shrink effect upon powering off), unless explicitly mandated by magic/canon rules.
- Do not describe major environmental shifts with a single isolated sense (e.g., only "the AC hummed once") without immediate surrounding sensory feedback (e.g., wind stopping, ambient light shifting, body reaction).
- Do not write textbook-style or dictionary-like explanations of common physics, tech, or daily operations to justify an anomaly (e.g., explaining how a screen normally powers off to prove it went black incorrectly). Trust the reader's common sense; show only the immediate sensory contrast or anomalous state directly.
- Do not construct paragraphs using rigid three-part logical contrasts (e.g., "Statement of anomaly -> Normal baseline explanation -> Present abnormal state"). Break this symmetrical logical flow with sensory delay, uneven paragraph rhythm, or scattered physical reactions.
- Do not mechanically delete or rewrite normal `被` sentences during de-AI review. Before changing a 被字句, verify that it is unnecessary, westernized, or a passive sensory mediation. If `被` carries pressure, victimhood, restraint, hidden actor, POV limit, idiom, or character voice, preserve it.
- Do not flatten genre intensity during de-AI editing. Do not delete exaggerated adjectives, strong emotion, repetition, or dramatic phrasing merely because they are forceful. First check whether the wording serves character voice, genre promise, pressure, humor, humiliation, suspense,爽点, rhythm, or emotional payoff. If it does, preserve it.
- Do not use cold, generic pronouns (e.g., "这个/那个" as direct translations of "this/it") to refer to key abnormal objects or central props. Refer to them using sensory adjectives, concrete nouns (e.g., "那块灰亮的荧幕" instead of "这个"), or omit the subject entirely where the flow allows.
- Do not place subjective judgment conclusions before sensory inputs when describing anomalies (e.g., writing "The way the screen went black was wrong" before describing the screen's visual state). Always place the physical perception first (what the POV character physically sees/hears) and let the logical realization lag behind.



