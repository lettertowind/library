---
term: VBA
aliases: [Visual Basic for Applications, Excel 宏]
kind: tool
domain: 计算机/办公软件/Excel
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# VBA

> 别名：Visual Basic for Applications、Excel 宏

**Excel 内置的宏编程语言，用于自动化 Excel 操作。**

## 解释

VBA 是 Excel 原生工具，能直接操作单元格格式、颜色、合并单元格等对象模型。视频观点是：简单批量读写用 pandas 更短，复杂格式操作 VBA 更方便。

## 有什么用

- 设置单元格格式和颜色
- 处理合并单元格等复杂结构
- Excel 内部自动化

## 关键要点

- Excel 原生，格式与样式控制强
- 简单批量读写不如 pandas 简洁
- 与 pandas 是场景互补而非替代
- 原则：专业工具做专业的事

## 边界与易混淆

跨 Excel 与 PDF 等文件协同处理时不如 pandas 灵活；维护成本较高。

## 关联

- [[Pandas Excel 合并拆分]] — 对比项

## 自测

需要保留原表颜色和合并单元格做批量处理，选 pandas 还是 VBA？为什么？::选 VBA，因为 pandas 读写 Excel 不保留格式样式，VBA 是 Excel 原生工具能操作这些对象。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
