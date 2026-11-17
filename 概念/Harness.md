---
term: Harness
aliases: [智能体框架, Agent 框架, harness]
kind: concept
domain: 计算机/AI/智能体
tags: [概念/concept, 领域/计算机]
stage: "让 AI 干活"
order: 461
created: 2026-11-17
updated: 2026-11-17
---

# Harness

> 别名：智能体框架、Agent 框架、harness

**包在模型外面、负责组织上下文和执行工具的一整套程序。**

## 解释

Harness 负责组织上下文、提供工具清单、执行工具调用、判断任务是否完成、压缩过长上下文、危险操作前征求同意。模型只负责思考和决策。原意是马具：模型是马，Harness 是让它干活的装备。

## 有什么用

- 支撑 Agent 运行
- 决定同一模型的实际任务能力

## 关键要点

- 公式：Agent = 模型 + Harness
- Claude Code 是 Harness，Claude 是里面的模型
- 同一模型配不同 Harness，能力差别可能很大
- Agent 框架、Agent 平台基本都指这一层

## 边界与易混淆

Harness 本身不是模型；DeepSeek Harness 是框架，里面接入的才是模型。

## 关联

- [[Agent]] — 组合使用
- [[工具调用]] — 上位概念
- [[MCP]] — 组合使用
- [[上下文工程]] — 上位概念

## 自测

为什么厂商公布 Agent 成绩时要注明用的 Harness？::同一模型配不同 Harness 表现差别很大，不注明就无法公平比较。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
