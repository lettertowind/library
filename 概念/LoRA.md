---
term: LoRA
aliases: [低秩适配, Low-Rank Adaptation]
kind: method
domain: AI/大模型
tags: [概念/method, 领域/AI]

stage: "与模型沟通"

order: 421
created: 2026-11-17
updated: 2026-11-17
---

# LoRA

> 别名：低秩适配、Low-Rank Adaptation

**冻结原模型参数、只额外训练一小部分新参数的低成本微调方法。**

## 解释

LoRA 不动原来的参数，只训练少量新增参数，成本远低于全参数微调。AI 绘画里常见的风格模型很多就是用 LoRA 训练的。

## 有什么用

- 低成本微调
- 训练风格模型

## 关键要点

- 原参数不动，只训练一小部分新参数
- 成本比完整微调低得多
- AI 绘画的风格模型常用它训练

## 边界与易混淆

LoRA 仍是微调的一种，不用于补充实时更新的知识。

## 关联

- [[微调]] — 上位概念

## 自测

LoRA 相比完整微调省在哪里？::冻结原参数，只训练少量新增参数，计算和存储成本都低得多。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
