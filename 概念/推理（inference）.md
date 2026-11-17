---
term: 推理（inference）
aliases: [inference, 模型推理]
kind: concept
domain: 计算机/AI/大模型
tags: [概念/concept, 领域/计算机]
stage: "AI 基础"
order: 261
created: 2026-11-17
updated: 2026-11-17
---

# 推理（inference）

> 别名：inference、模型推理

**用训练好的参数计算一次并生成回答的过程，与训练相对。**

## 解释

推理指训练完成后，你每发一次消息，模型就用训练好的参数计算一次并生成回答。训练是造模型，推理是用模型。它与「推理（reasoning）」中文同名但含义完全不同。

## 有什么用

- 理解 API 调用成本来源
- 区分训练与使用阶段

## 关键要点

- 训练是造模型，推理是用模型
- 每次对话都触发一次推理
- 推理成本按 Token 计费

## 边界与易混淆

易与「推理（reasoning，思考过程）」混淆，两者中文同名但无关。

## 关联

- [[推理模型]] — 对比项
- [[预训练]] — 对比项

## 自测

「推理」在 AI 语境下可能指哪两件完全不同的事？::一是指用模型计算生成回答（inference），二是指模型先思考再回答的思考过程（reasoning）。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
