---
term: Skill
aliases: [技能, Agent Skill]
kind: concept
domain: AI/智能体
tags: [概念/concept, 领域/AI]

stage: "让 AI 干活"

order: 481
created: 2026-11-17
updated: 2026-11-17
---

# Skill

> 别名：技能、Agent Skill

**把一项任务的完整做法打包成文件夹，含 SKILL.md 说明、模板和脚本。**

## 解释

Skill 把做事的具体方法固化下来，避免每次在提示词里重复交代。关键设计是渐进式加载：平时上下文只放名字和一句简介，用到时才读完整说明，几十个 Skill 也只占很少 Token。

## 有什么用

- 固化任务标准做法
- 让 Agent 按你的标准做事

## 关键要点

- Anthropic 2025 年 10 月推出，现为开放标准
- 含 SKILL.md、模板、参考资料、可运行脚本
- 渐进式加载：平时只占名字和简介的 Token
- 插件通常是把多个 Skill 和 MCP 打包

## 边界与易混淆

Skill 提供方法，MCP 提供工具连接，二者职责不同。

## 关联

- [[MCP]] — 对比项
- [[上下文工程]] — 下位概念
- [[Agent]] — 组合使用

## 自测

渐进式加载为什么重要？::让大量 Skill 平时只占极少上下文，用到时才加载完整内容，节省 Token。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
