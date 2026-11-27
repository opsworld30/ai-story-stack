# 音频与声音

本分类收录配音、声音设计、对白表演、音乐生成、音效和音频后期。

## 实际收录统计

- **10 个完整 Skill 包 / 10 个 Skill 入口**。
- **6 个上游来源仓库**：Emily2040/seedance-2.0、Runware/runware-skills、NanmiCoder/creator-pipeline、awesome-genmedia/skills、AlterLab-IEU/AlterLab-FC-Skills、calesthio/generative-media-skills。

## Skill 清单

| Skill 入口 | 功能 | 上游来源 | 许可证 |
|---|---|---|---|
| [seedance-audio](./Emily2040__seedance-2.0/seedance-audio/SKILL.md) | Seedance 音频生成与声音提示词 | Emily2040/seedance-2.0 | MIT |
| [voiceover](./Runware__runware-skills/voiceover/SKILL.md) | 单人配音、旁白、情绪和语速控制 | Runware/runware-skills | MIT |
| [dialogue-audio](./Runware__runware-skills/dialogue-audio/SKILL.md) | 双人对白、访谈与多说话人对话 | Runware/runware-skills | MIT |
| [voice-cloning](./Runware__runware-skills/voice-cloning/SKILL.md) | 定制音色设计与声音克隆 | Runware/runware-skills | MIT |
| [music](./Runware__runware-skills/music/SKILL.md) | 歌曲、纯音乐、配乐和 Jingle | Runware/runware-skills | MIT |
| [add-audio-to-video](./Runware__runware-skills/add-audio-to-video/SKILL.md) | 为视频补充同步音效、旁白或音乐 | Runware/runware-skills | MIT |
| [voice-clone-tts](./NanmiCoder__creator-pipeline/voice-clone-tts/SKILL.md) | 用户授权参考音频驱动的配音与音色克隆，输出音频、字幕和时间轴 | NanmiCoder/creator-pipeline | MIT |
| [music-generation](./awesome-genmedia__skills/music-generation/SKILL.md) | 按场景、流派、情绪、BPM 与乐器生成器乐和配乐 | awesome-genmedia/skills | MIT |
| [alterlab-genai-voice-designer](./AlterLab-IEU__AlterLab-FC-Skills/alterlab-genai-voice-designer/SKILL.md) | ElevenLabs 音色设计、情绪表演与语音导演 | AlterLab-IEU/AlterLab-FC-Skills | MIT |
| [elevenlabs-tts](./calesthio__generative-media-skills/elevenlabs-tts/SKILL.md) | TTS 生产、发音、分段/流式生成、质量与权利检查 | calesthio/generative-media-skills | MIT |

## 运行依赖

Runware 的五个结果型 Skill 依赖 [Agent Tools 分类中的基础 Skill](../10-agent-tools/README.md)：runware-run、runware-models 和 runware-prompting。需要 Runware 账号、API Key 和可用模型。仓库只完成静态镜像，没有调用付费服务。

## 新增 Skill 的运行说明

`music-generation` 的上游目录只包含 `SKILL.md`；公开包同时保留仓库根目录 MIT LICENSE 与 `UPSTREAM.md`。该 Skill 使用远程 each::sense 音乐生成服务，使用者需自行配置服务访问与凭据；本仓库没有包含凭据，也未调用远程生成服务。

## 新增语音 Skill 说明

- 两个新包分别覆盖音色身份/表演设计与 TTS 生产工程；上游根 MIT LICENSE 与各自 UPSTREAM.md 已保留。
- ElevenLabs TTS 的评估者专用 `EVAL.md` 未公开发布；上游 Skill 的模型和 API 信息需以当前官方文档为准。
