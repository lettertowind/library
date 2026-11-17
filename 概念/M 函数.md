---
term: M 函数
aliases: [Power Query M, M 语言, M formula language]
kind: tool
domain: 计算机/办公软件/Excel
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# M 函数

> 别名：Power Query M、M 语言、M formula language

**Power Query 中用于数据转换的公式语言，去重等操作需手写代码实现。**

## 解释

Power Query 的每一步操作背后都是一段 M 代码，界面点选可完成常见操作，但复杂逻辑（如保留最后一次重复、提取重复行）要写 M 函数。相比 Pandas 的一行方法调用，M 语言学习门槛更高、中文资料也少。

## 有什么用

- 在 Excel Power Query 中做复杂去重与数据转换
- 需要把清洗流程固化为可刷新步骤时

## 关键要点

- Power Query 每个操作步骤都对应一段 M 代码
- 同等去重需求，Pandas 一行方法即可，M 需自行编写逻辑
- 中文 M 函数资料相对稀缺，学习成本较高
- 与 Excel 单元格公式不是一回事，不能混用

## 边界与易混淆

只在 Power Query 编辑器中生效，不能写进普通单元格

## 关联

- [[Power Query 追加查询]] — 上位概念
- [[drop_duplicates]] — 对比项

## 自测

同样是「只保留最后一次出现的重复记录」，Pandas 和 Power Query 的实现成本差在哪？::Pandas 用 keep='last' 一个参数即可；Power Query 需自行编写 M 函数逻辑，门槛和资料成本都更高

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p33 S02E18.删除重复和提取重复](https://www.bilibili.com/video/BV1ji4y157uB?p=33) · 2026-11-17
