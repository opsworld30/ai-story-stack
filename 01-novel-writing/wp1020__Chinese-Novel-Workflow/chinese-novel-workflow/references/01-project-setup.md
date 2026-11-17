# Project Setup

Use this when the user is opening a new narrative project, choosing a genre, shaping a premise, testing whether an idea can support its intended length, or defining the promise of a short story, scene sequence, serialized web novel, or standalone prose project.

## Required Inputs

If absent, infer conservatively and mark assumptions:

- Form: short story, scene, opening hook, serialized web novel, novella, long-form project, or rewritten concept
- Genre and subgenre
- Target readers
- Core promise to readers
- Protagonist desire
- Main conflict
- Intended length and rhythm
- Project writing specification: prose unit, minimum word count rule, overflow policy, and whether special-unit overrides are allowed
- Tone: light, dark, epic, suspenseful, romantic, comedic, restrained, high-intensity, warm, or realistic

## Project Card Output

Produce a reusable project card:

```markdown
## 作品定位
- 形式:
- 类型:
- 目标读者:
- 核心卖点:
- 阅读爽点 / 情绪承诺:
- 叙事气质:

## 核心故事
- 一句话梗概:
- 主角欲望:
- 主角缺口:
- 外部压力:
- 核心问题:

## 篇幅与节奏策略
- 目标篇幅:
- 开场承诺:
- 中段推进方式:
- 结尾钩子 / 情绪落点:
- 禁止事项:

## 创作规格
- 正文单位:
- 全局最低字数规则:
- 是否允许自然超出:
- 是否设置上限:
- 特殊章节/单元是否允许覆盖:
- 字数规则修改方式:
```

If the user is planning a serialized web novel, add:

```markdown
## 连载策略
- 前 10 章目标:
- 每几章给读者的固定回报:
- 章末钩子风格:
- 长线升级 / 关系 / 秘密推进:
```

## Design Rules

- Make the protagonist's desire concrete enough to generate scenes.
- Define pressure early: enemy, debt, secret, deadline, survival, reputation, family, love, duty, identity, or destiny.
- Avoid a premise that only works for one dramatic moment unless the target form is a very short piece.
- Tie the commercial or emotional hook to repeatable unit-level conflict.
- Define what readers should expect at useful intervals: upgrade, reversal, clue, relationship shift, reveal, confrontation, payoff, irony, dread, warmth, or aftertaste.
- Match the intensity to the form; do not force a short story to carry long-form escalation, and do not leave a serial without repeatable pressure.
- When initializing files for a project, use `references/17-project-file-organization.md` and create separate locations for settings, outlines, chapter-level AI writing instructions, prose, memory, and final-review records.
- For chaptered fiction, do not plan production around broad structural phases. Production should move through chapter outline -> chapter detailed beats -> chapter AI writing instruction -> chapter prose.
- Do not set a default minimum word count from the skill. If the project lacks a writing specification, ask the author to confirm the minimum word count rule and store it under `创作规格` before chapter outlines, detailed beats, AI writing instructions, or prose drafting depend on it.

## File Layout Handoff

When the user asks to create or organize project files, include a recommended layout:

```markdown
## 项目文件结构
- 设定/: 作品定位、人物系统、叙事架构、写作风格与禁用项
- 设定/04-创作规格.md: 正文单位、全局最低字数规则、自然超出策略、特殊章节覆盖规则
- 大纲/: 总纲、章节大纲、章节细纲
- 创作指令/: 按章保存 AI 创作指令
- 正文/: 按章保存正文
- 记忆/: 按章保存叙事记忆
- 终审/: 按章保存终审记录
```

For multi-volume works, put chapter outlines, chapter detailed beats, AI writing instructions, prose, memory, and review records under each volume folder. Do not create broad structural-phase prose files.

## Quality Check

- Can the premise support the user's intended length without repeating the same conflict?
- Does the protagonist have an active reason to move?
- Is there a visible gap between current self and future self?
- Are the early stakes understandable without an encyclopedia of setting?
- Does the tone match the intended genre and audience?
- Does the first narrative unit have a clear pressure, question, or emotional pull?
