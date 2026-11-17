---
term: Benchmark
aliases: [基准测试, 跑分, benchmark]
kind: metric
domain: 计算机/AI/大模型
tags: [概念/metric, 领域/计算机]
stage: "评价与未来"
order: 501
created: 2026-11-17
updated: 2026-11-17
---

# Benchmark

> 别名：基准测试、跑分、benchmark

**一套固定的测试题，用同样题目考不同模型得到的分数即跑分。**

## 解释

Benchmark 用统一题目衡量模型能力，不同基准考不同方面：数学推理、编程（如 SWE-bench）、综合知识（如 HLE）。看跑分要注意测试方、测试条件和数据污染。

## 有什么用

- 横向比较模型能力
- 评估模型在特定任务上的水平

## 关键要点

- SWE-bench 考修复真实代码仓库问题
- HLE 被称为“人类最后的考试”
- 看跑分三要点：谁测的、测试条件、有无数据污染

## 边界与易混淆

跑分受 Harness、测试条件影响，不能直接等同于实际使用体验。

## 关联

- [[SOTA]] — 组合使用
- [[Harness]] — 组合使用

## 自测

为什么看跑分要注意数据污染？::测试题若提前出现在训练数据里，模型等于看过答案，分数会虚高。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
