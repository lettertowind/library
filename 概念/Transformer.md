---
term: Transformer
aliases: [Transformer 架构]
kind: model
domain: 计算机/AI/大模型
tags: [概念/model, 领域/计算机]
stage: "AI 基础"
order: 281
created: 2026-11-17
updated: 2026-11-17
---

# Transformer

> 别名：Transformer 架构

**谷歌 2017 年提出、以注意力机制为核心、当前几乎所有大模型采用的结构。**

## 解释

Transformer 是现在几乎所有大模型都在使用的模型结构，由谷歌在 2017 年的一篇论文中提出。它的核心是注意力机制：预测下一个 Token 时回头看前面所有 Token，判断哪些最相关并重点参考。

## 有什么用

- 理解大模型的底层结构
- 理解长上下文为何有效

## 关键要点

- 2017 年由谷歌论文提出
- 核心是注意力机制
- 是当前大模型的通用底座

## 关联

- [[注意力机制]] — 下位概念
- [[大语言模型]] — 上位概念

## 自测

Transformer 靠什么机制决定该重点参考前文的哪些部分？::注意力机制，它计算当前 Token 与前面各 Token 的相关性并加权参考。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
