---
term: RLHF
aliases: [人类反馈强化学习, Reinforcement Learning from Human Feedback]
kind: method
domain: 计算机/AI/大模型
tags: [概念/method, 领域/计算机]
stage: "AI 基础"
order: 251
created: 2026-11-17
updated: 2026-11-17
---

# RLHF

> 别名：人类反馈强化学习、Reinforcement Learning from Human Feedback

**用人类对回答的评分作为奖励信号来调整模型参数的强化学习方法。**

## 解释

RLHF 是后训练中强化学习的一种形式，打分来自人而非自动指标。模型生成回答后由人评分，再按分数调整参数，使其更倾向给出人类认可的回答。

## 有什么用

- 让模型回答更符合人类偏好
- 提升回答的有用性和安全性

## 关键要点

- 属于后训练中的强化学习环节
- 奖励信号来自人类评分
- 与自动打分相对

## 关联

- [[后训练]] — 上位概念

## 自测

RLHF 和普通强化学习的关键区别是什么？::奖励信号来源不同：RLHF 的分数由人来打，普通强化学习用自动计算的奖励。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
