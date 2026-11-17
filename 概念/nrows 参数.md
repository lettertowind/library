---
term: nrows 参数
aliases: [nrows, 限制读取行数]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# nrows 参数

> 别名：nrows、限制读取行数

**读取时只读前 n 行的参数，用于控制内存占用。**

## 解释

nrows 在读取阶段就限制进入内存的行数，适合大文件预览或内存有限场景。与 head() 不同，head() 只改变显示，变量仍含全部数据。

## 有什么用

- 大数据文件先预览
- 避免一次性读入导致内存不足

## 关键要点

- nrows=3 只读前 3 行
- 真正减少内存数据量
- 优于只在 print/head 中限制显示

## 边界与易混淆

nrows 只取前 n 行，不能随机采样；需要抽样应另用其他方法。

## 关联

- [[pd.read_csv]] — 组合使用

## 自测

为什么大数据读取推荐 nrows 而不是 head()？::nrows 读取阶段就限制行数，head() 已把全部数据读进内存。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
