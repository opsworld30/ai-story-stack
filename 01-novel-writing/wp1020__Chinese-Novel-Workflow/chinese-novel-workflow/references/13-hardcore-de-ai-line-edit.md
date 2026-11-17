# Hardcore De-AI Line Edit

Use this when the user asks for 极致去 AI 化, 硬核流畅度润色, 网文金牌责编, 终稿级重构, 强去 AI 腔, 机器味很重, 逻辑断层, 伪深刻旁白, or 番茄移动端顺读式润色.

## Core Rule

Preserve story truth first: plot facts, POV, timeline, relationships, canon rules, foreshadowing, ending pull, character intent, unit function, and genre promise must remain fixed unless the user explicitly asks to change them.

Use `references/14-narrative-readability-standard.md` as the baseline for readability, dialogue, paragraphing, and anti-AI lesions.

This is a high-intensity final-pass line edit. It may restructure sentences, split paragraphs, sharpen action chains, replace abstract narration, and strengthen physical texture. It must not invent major events, new canon, new relationships, or a different unit function.

Before hardcore line editing, lock story state: fixed plot facts, event order/results, character stage, body/mental/emotional state, relationship posture, character knowledge, foreshadowing, reveal timing, and ending pull. High-intensity editing may restructure sentences and paragraphs, but not story state. If improving flow requires changing character behavior, relationship posture, event result, reveal timing, or ending pull, stop and report it as an author decision instead of silently editing it.

## Intensity Boundary

Use this after `07-de-ai-humanizing.md` when normal prose revision and medium de-AI polishing are not enough.

Use `07-de-ai-humanizing.md` for natural expression revision and medium de-AI cleanup. Use this file when the text needs hard editorial reconstruction.

## Scan For AI Lesions

Remove or rebuild these patterns:

| Lesion | Replace with |
| --- | --- |
| 中介性感官 / 被动感官中介: 脚底的触感、耳边传来、令人反胃的感觉、被他的脚底感知到 | Direct body contact, object friction, sound source, pain point, movement result. This does not target normal 被字句. |
| 作者上帝视角哲思: 这一刻他明白、命运齿轮、普通人的尊严 | Scene-local action, silence, interrupted movement, concrete choice. |
| "不是 A，而是 B" explanation pattern | Observation progression, visible consequence, abrupt result. Its compound form "现象→然后→不是A→而是B" is a classic AI teacher-voice: the author interrupts the scene to correct the reader's presumed misinterpretation. In most cases, delete "不是A" entirely and ground "而是B" as the POV character's direct perceptual result. |
| "然后" as mechanical temporal connector | Replace with sensory consequence, object feedback, or body reaction. If two beats are merely sequential with no causal pressure, merge or cut the weaker one. |
| 系统 / 医学 / 学术术语泄漏 | Character-level perception, physical reaction, role-based judgment. |
| 伪深刻旁白 | Cut it or convert it into a decision under pressure. |
| 高频风格词: 死死、瞳孔骤缩、歪着脖子、仿佛、像是、宛如 | Specific hand force, breath, object deformation, gaze behavior, environmental feedback. |
| 大段心理 / 环境堆砌 | Break into action beats and pressure beats. |
| 对话动作挤在一段 | Separate dialogue, action, reaction, and environment. |
| Outline-execution prose | Rebuild around attention chain: perception, interruption, body reaction, recognition, choice. |
| Balanced paragraph machine rhythm | Vary paragraph length by pressure; allow single-line beats and unfinished thoughts. |

## Rewrite Method

1. Lock fixed facts and unit function before editing.
2. Mark each scene's pressure source: threat, temptation, humiliation, deadline, reveal, or emotional collapse.
3. Rewrite action before explanation. Let the reader see what changes before naming why it matters.
4. If prose exposes outline-field order, use `references/16-attention-driven-prose.md` and rebuild through POV attention chain.
5. Convert abstract emotion into body movement, object handling, delayed speech, failed composure, or tactical choice.
6. Replace passive sensory mediation with direct physical contact, but do not mechanically rewrite normal 被字句. Preserve 被 when it carries pressure, victimhood, restraint, hidden actor, POV limit, idiom, or character voice.
7. Break balanced AI sentence patterns; vary sentence length by scene pressure.
8. Keep genre directness. Do not turn readable fiction into literary essay prose.
9. Preserve or sharpen the ending pull. Do not summarize after it.

## Mobile Reading Formatting

- No first-line indentation.
- Use blank lines between paragraphs.
- Keep paragraphs sparse; aim for each paragraph under 80 Chinese characters when possible.
- Split after 2-3 short sentences.
- Put dialogue on its own paragraph.
- Put action, physical reaction, and environment feedback in separate paragraphs when tension is high.
- Do not merge report, analysis, and prose unless the user asks.

## Texture Rules

Use concrete, scene-bound texture:

- Object response: chair legs scrape, door panel dents, phone screen flashes, fabric sticks, water pulls at soles.
- Body response: breath catches, fingers fail, ribs seize, throat burns, knees soften, blood taste rises.
- Environment response: light stutters, corridor noise cuts off, heat presses down, metal chills the palm.
- Tactical thought: short, pressured, tied to immediate choice.

Avoid decorative pain for its own sake. Physical detail must serve danger, desire, conflict, shame, suspense, payoff, intimacy, warmth, comedy, or aftertaste.

## Mandatory Second Audit

Never stop after the first rewrite.

After the first line edit, scan again for:

- passive sensory mediation, while protecting normal 被字句 that carry pressure, victimhood, restraint, hidden actor, POV limit, idiom, or character voice
- author summary
- fake profound sentences
- neat parallel structure
- generic positive conclusion
- over-explained emotion
- repeated style tokens
- broken continuity with the previous unit
- accidental character-stage drift
- changed relationship posture
- changed character knowledge boundary
- changed event order or event result
- added, removed, or moved foreshadowing / reveal timing
- softened, redeemed, blackened, romanticized, or villainized a character beyond the original stage
- accidental loss of ending pull or foreshadowing
- visible outline-field order
- overly complete paragraph symmetry
- missing attention chain
- "然后……不是……而是……" compound template
- over-explained scene meaning
- violations of `references/14-narrative-readability-standard.md`: hard transitions, black-block paragraphs, weak dialogue function, vague shadows, overloaded sensation, and slogan-like summaries
- Humanizer-zh residue: generic AI vocabulary, empty emphasis, neat three-part listing, quote-like maxim, generic positive conclusion, overqualified hedging, and inflated symbolic meaning
- accidental flattening of genre intensity: exaggerated adjectives, strong emotion, repetition, or dramatic phrasing were removed even though they served character voice, pressure,爽点, suspense, comedy, humiliation, rhythm, or emotional payoff
- audience/tone drift: fiction prose accidentally turns into public article, speech script, motivational copy, or direct-to-reader commentary
- word-count metadata leak: lines such as `本章字数`, `番茄计字法`, `字数统计`, `本章最低字数`, `字数规则`, `章节备注`, or generation notes remain inside prose

Only output the second-pass version. If the user asks for a report, mention what changed in the second audit briefly after the prose.

## Fiction Humanizer Score

Use this as an internal final-pass score when the user requests hardcore de-AI editing or publication-level polish. Do not output the score unless the user asks for a report.

| Dimension | Fiction-specific question |
| --- | --- |
| Directness | Does the paragraph show the pressure/action/result directly before explaining meaning? |
| Rhythm | Do sentence and paragraph lengths vary because of scene pressure rather than template balance? |
| Reader trust | Does the prose avoid proving, summarizing, or over-explaining what the scene already shows? |
| Character authenticity | Does each thought, line, and reaction sound like this POV character in this relationship and stage? |
| Precision | Is filler removed without deleting suspense buildup, reaction beats, foreshadowing, or emotional aftertaste? |
| Polishing-profile fit | Does the final text match its text type, target reader, intended tone, and allowed intimacy level without importing the wrong genre voice? |

If any dimension fails, revise again before delivery.

## Output Modes

Default output (To prevent single LLM cognitive drift, force diagnostics and check reports BEFORE generating the polished text):

```markdown
## 去AI痕迹终审自检与排查
- 固定剧情保留：
- 人物状态 / 关系 / 认知锁定：
- 清除的主要 AI 病灶（如被动感官、伪深刻旁白等）：
- 段落与移动端顺读重构策略：
- 仍需作者确认：

## 硬核去AI润色版
[revised prose]

## 硬核润色后漂移审计
| 检查项 | 是否改变 | 处理 |
| --- | --- | --- |
| 事件顺序 / 结果 | 否 |  |
| 人物动机 / 阶段 / 状态 | 否 |  |
| 人物关系姿态 | 否 |  |
| 角色认知边界 | 否 |  |
| 伏笔 / 揭示时机 / 结尾钩子 | 否 |  |
```

If the user says "只给正文", run the story-state lock and drift audit internally, then output only revised prose.

If the user provides outline plus draft, preserve the outline's required scenes and key lines. If the draft is under target length and the user asks for expansion, add density through action chain, tactical calculation, physical texture, environmental pressure, and relationship reaction, not filler summary.

## Hard Prohibitions

- Do not preserve or smooth in-prose structure meta language. Replace `第几卷`, `第几章`, `本卷`, `下一章`, `后续剧情`, `阶段收束`, `主线节点`, `读者会看到`, or similar planning terms with in-world action, pressure, information, character inference, or visible consequence unless it is visible in-world text or approved metafiction.

- Do not add a preface, apology, or chatty explanation before the revised prose.
- Do not flatten character voice into polished neutrality.
- Do not overuse violent metaphors when the genre is not hard action, apocalypse, crime, or combat.
- Do not force male-frequency hardness onto female-frequency, romance, family, slice-of-life, or comedic units; adapt texture to genre.
- Do not delete intentional foreshadowing, ambiguity, hooks, ending pulls, or emotional aftertaste.
- Do not report word counts unless the user requests a self-check report.
- Do not copy project-specific names, settings, or examples from a sample prompt into unrelated works.
- Do not turn fiction prose into public-facing article, speech script, motivational essay, or direct reader conversation unless the narrative form explicitly uses that voice.
- Do not preserve word-count lines, counting-method notes, chapter bookkeeping, or generation notes in the polished prose. Delete them from正文; report word count only outside prose when requested.
- Do not treat every `被` sentence as a de-AI target. Only rewrite 被字句 when they are unnecessary passive voice, westernized passive syntax, or passive sensory mediation; preserve natural Chinese 被字句 when rewriting would damage meaning, pressure, character posture, or idiomatic flow.
- Do not make prose plain merely to make it look less AI. Strong adjectives, heightened emotion, repetition, and dramatic phrasing are allowed when they are functional and genre-appropriate.

## Final Checklist

- Plot facts and unit function preserved.
- AI-style abstract explanation removed or grounded in scene action.
- Passive perception converted to direct sensation or visible event.
- Humanizer-style residue removed or justified as deliberate character voice: generic AI vocabulary, false depth, three-part listing, quote-like maxim, and generic positive conclusion.
- Genre intensity preserved where it serves pressure, character voice, suspense, comedy, humiliation,爽点, rhythm, or emotional payoff.
- Repeated style tokens reduced.
- Paragraphs are mobile-readable.
- Paragraph order follows POV attention chain rather than visible outline structure.
- Dialogue, action, and reaction are separated where needed.
- The ending lands on a hook, payoff, question, or aftertaste, not an author summary.



