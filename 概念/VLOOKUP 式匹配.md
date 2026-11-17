---
term: VLOOKUP 式匹配
aliases: [VLOOKUP, Excel 查找匹配, 纵向查找]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 44
stage: "S02E29 · vlookup"
order: 44
---

# VLOOKUP 式匹配

> 别名：VLOOKUP、Excel 查找匹配、纵向查找

**用 merge 左连接从另一张表按关键列取回目标字段，等价 Excel 的 VLOOKUP。**

## 解释

Excel 的 VLOOKUP 按关键列在另一张表查找并返回指定列的值。Pandas 中通过 merge 左连接实现：主表保留全部行，右表只取关键列和目标列，按关键列连接。

## 有什么用

- 跨工作表/跨表补全字段
- 用一张表的数据给另一张表打标签

## 关键要点

- 右表先用 loc[:, ['键','目标列']] 只取需要的列，避免带入无关字段
- how='left' 保证主表记录一条不少
- on='键列' 指定连接键，两表键名不同时用 left_on/right_on
- 匹配结果列默认追加在最后，需要移动时用 insert

## 边界与易混淆

VLOOKUP 只能向右查找且默认近似匹配；merge 无方向限制，但需注意键重复导致的多对多展开。

## 关联

- [[DataFrame 合并]] — 上位概念
- [[how 参数]] — 组合使用
- [[on 参数]] — 组合使用
- [[loc]] — 组合使用

## 自测

为什么右表要先 loc[:, ['学号','总分']] 再 merge，而不是整表连接？::避免把右表无关列全部带入结果，减少冗余字段和列名冲突。
如果主表有而右表没有的学号，how='left' 后该行总分是什么？::NaN，因为左连接保留主表全部行，匹配不到就填空值。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
