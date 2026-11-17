---
term: Pandas Excel 合并拆分
aliases: [Excel 拆分与合并, 多工作簿合并, 按列拆分]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
order: 40
---

# Pandas Excel 合并拆分

> 别名：Excel 拆分与合并、多工作簿合并、按列拆分

**用 pandas 批量合并多个 Excel 或按某列拆成多表/多文件的套路。**

## 解释

包含四类任务：多工作簿合并、多工作表合并、按列拆成多个 sheet、按列拆成多个工作簿。合并靠空表加 concat 累积，拆分靠去重取分组键加循环筛选写出。

## 有什么用

- 月度报表汇总
- 按部门/地区分发数据
- 批量整理分散的 Excel 文件

## 关键要点

- 合并：空表 + for + concat 累积
- 拆 sheet：ExcelWriter + to_excel(sheet_name=分组)
- 拆工作簿：动态拼接文件名 + to_excel
- 分组键先 drop_duplicates 再 list

## 边界与易混淆

示例为理想数据，忽略空行、合并单元格、格式颜色；复杂格式操作应改用 VBA。

## 关联

- [[pd.concat]] — 组合使用
- [[pd.ExcelWriter]] — 组合使用
- [[VBA]] — 对比项

## 自测

拆成同一文件的多个 sheet 与拆成多个独立工作簿，关键区别在哪一步？::拆 sheet 需要 ExcelWriter 并指定 sheet_name；拆工作簿直接对每个分组调用 to_excel 写独立路径。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
