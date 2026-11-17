---
term: MCP
aliases: [模型上下文协议, Model Context Protocol]
kind: concept
domain: 计算机/AI/智能体
tags: [概念/concept, 领域/计算机]
stage: "让 AI 干活"
order: 471
created: 2026-11-17
updated: 2026-11-17
---

# MCP

> 别名：模型上下文协议、Model Context Protocol

**Anthropic 开源的、统一 AI 应用与外部工具连接方式的标准协议。**

## 解释

MCP 规定 AI 应用和外部工具之间统一的连接方式。软件方按 MCP 做一个 MCP 服务器，所有支持 MCP 的 AI 应用都能直接连接使用，不必为每个软件单独开发接入。

## 有什么用

- 让 AI 统一接入 Notion、数据库、文件等外部工具

## 关键要点

- Anthropic 2024 年 11 月开源
- 软件方做 MCP 服务器，AI 应用直接连接
- “安装一个 MCP”实际是连接一个 MCP 服务器
- MCP 连 Agent 和工具，A2A 连 Agent 和 Agent

## 边界与易混淆

MCP 与 API 不同：API 是各软件自己的接口、格式各异；MCP 统一了 AI 连接这些接口的方式。

## 关联

- [[API]] — 对比项
- [[Harness]] — 组合使用
- [[A2A 协议]] — 对比项
- [[Skill]] — 对比项

## 自测

MCP 解决了什么重复劳动？::每个 Harness 接入每个软件都要单独开发一次的问题。

## 出处

- [全网最详细的 AI 入门课：一期视频搞懂 58 个 AI 术语，从大模型到 Agent、MCP、Skill](https://www.bilibili.com/video/BV1VQWb6eEeo?p=1) · 2026-11-17
