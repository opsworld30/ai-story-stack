# Project File Organization

Use this when creating, reorganizing, or auditing a narrative project's folder structure, especially when files are flat, mixed by production stage, or named by broad structural phases instead of chapters.

## Core Rule

Project files must support production. Separate settings, outlines, chapter-level AI writing instructions, prose, memory, and final-review records.

For serialized or chaptered fiction, do not use broad structural phases as file categories for prose or AI writing instructions. Structural phases may help pacing internally, but files should be organized by setting category, outline level, volume if needed, and chapter.

## Default Single-Volume Structure

```text
作品名/
  README.md
  设定/
    00-作品定位卡.md
    01-人物系统.md
    02-叙事架构.md
    03-写作风格与禁用项.md
    04-创作规格.md
  大纲/
    00-总纲.md
    01-章节大纲.md
    02-章节细纲.md
  创作指令/
    第001章_标题_AI创作指令.md
    第002章_标题_AI创作指令.md
  正文/
    第001章_标题.md
    第002章_标题.md
  记忆/
    第001章_叙事记忆.md
    第002章_叙事记忆.md
  终审/
    第001章_终审记录.md
```

## Multi-Volume Structure

Use volume folders only when the work truly has separate volume-level arcs, not merely early/middle/late pacing.

```text
作品名/
  README.md
  设定/
  大纲/
    00-总纲.md
    第01卷/
      00-卷纲.md
      01-人物设定.md
      02-章节大纲.md
      03-章节细纲.md
    第02卷/
      00-卷纲.md
      01-人物设定.md
      02-章节大纲.md
      03-章节细纲.md
  创作指令/
    第01卷/
      第001章_标题_AI创作指令.md
  正文/
    第01卷/
      第001章_标题.md
  记忆/
    第01卷/
      第001章_叙事记忆.md
  终审/
    第01卷/
      第001章_终审记录.md
```

## Short Story / Standalone Structure

```text
作品名/
  README.md
  设定/
    00-作品定位卡.md
    01-人物系统.md
    02-叙事架构.md
    04-创作规格.md
  大纲/
    00-故事大纲.md
    01-章节细纲.md
  创作指令/
    单元01_AI创作指令.md
  正文/
    正文.md
  终审/
    终审记录.md
```

## Naming Rules

- Chapter prose: `第001章_标题.md`
- Chapter AI writing instruction: `第001章_标题_AI创作指令.md`
- Chapter memory: `第001章_叙事记忆.md`
- Chapter final review: `第001章_终审记录.md`
- Volume outline folder: `大纲/第01卷/`
- Volume outline: `大纲/第01卷/00-卷纲.md`
- Volume character settings: `大纲/第01卷/01-人物设定.md`
- Volume chapter outline: `大纲/第01卷/02-章节大纲.md`
- Volume chapter details: `大纲/第01卷/03-章节细纲.md`
- Keep numbering width consistent within a project: `第001章` for long works, `第01章` for short works.
- Use clear Chinese folder names for author-facing projects: `设定`, `大纲`, `创作指令`, `正文`, `记忆`, `终审`.

## Migration Rules

When reorganizing a flat project:

1. Move work-positioning, character, worldbuilding, style, and canon files to `设定/`.
2. Move total outline to `大纲/00-总纲.md`; move each volume's outline, volume character settings, chapter outline, and chapter detailed beats to that volume's `大纲/第XX卷/` folder.
3. Rename broad structural-phase prose into chapter files only after splitting it into chapters.
4. Rename broad structural-phase AI writing instructions into chapter-level instructions only after generating chapter detailed beats.
5. Never silently overwrite existing prose. If a target filename exists, preserve both and flag the conflict.

## Quality Gate

Before drafting or continuing prose, confirm:

- The project has clear `设定/`, `大纲/`, `创作指令/`, `正文/`, and `记忆/` locations.
- For multi-volume projects, each volume uses `大纲/第XX卷/00-卷纲.md`, `01-人物设定.md`, `02-章节大纲.md`, and `03-章节细纲.md`; volume planning artifacts are not scattered under `设定/人物/`, `大纲/卷纲/`, or root `大纲/`.
- The target prose file is chapter-level or exact narrative-unit-level.
- The available AI writing instruction is chapter-level or exact narrative-unit-level.
- Broad structural-phase summaries have been converted into chapter outlines and chapter detailed beats.
