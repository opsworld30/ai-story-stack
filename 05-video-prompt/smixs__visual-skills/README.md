# Video｜AI 视频导演、分镜与提示词

**上游作者：Serge Shima。** 本 Skill 将导演、编剧与剪辑视角结合，用于把已有创意、剧本或场景转化为可执行的 AI 视频生成提示词。

## 适用能力

- 生成、拆分和审查 AI 视频提示词，覆盖 Seedance、Kling、Veo、Runway、Luma、Pika、Sora 等视频生成流程
- 设计分镜、镜头清单、导演阐述、多片段叙事与动态蒙太奇
- 控制机位、镜头运动、灯光、场面调度、节奏、人物连续性、对白和声音
- 根据任务读取相应参考文件，并在输出前执行戏剧结构与镜头细节检查

## 文件结构

- `video/SKILL.md`：主 Skill 与任务路由
- `video/references/`：12 份按需加载的导演、分镜、模型语法、镜头、灯光与修复参考资料
- `LICENSE`：原始 CC BY 4.0 许可证
- `NOTICE`：作者署名与第三方致谢
- `UPSTREAM.md`：来源提交、许可证、同步版本和文件范围

## 使用边界

此包只包含上游的 `video` Skill，不包含同仓库的 `image` Skill、营销页面、图片/Logo 资产或安装器。它负责视频生成提示词与导演/分镜工作，不替代完整剧本开发，也不用于既有素材的剪辑、调色或组装。

## 署名

Serge Shima — https://t.me/aimastersme · https://sergeshima.com · https://aimasters.me  
来源：https://github.com/smixs/visual-skills

授权：CC BY 4.0。再分发或改编时请保留署名、许可证链接，并说明本地说明文件与打包结构为本仓库新增。
