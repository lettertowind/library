---
term: names 参数
aliases: [names, 自定义列名]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
---

# names 参数

> 别名：names、自定义列名

**读取文件时人工指定列名的参数，传入列名列表。**

## 解释

names 接收与列数等长的列表，用于给无表头文件命名列。通常与 header=None 一起用，否则 Pandas 仍可能把首行当表头。

## 有什么用

- 无表头文件自定义列名
- 统一规范列名便于后续分析

## 关键要点

- 传入列表，长度需与列数一致
- 一般配合 header=None 使用
- 设置后 columns 显示自定义列名

## 边界与易混淆

只写 names 不写 header=None 时，首行数据可能仍被当表头而丢失。

## 关联

- [[header 参数]] — 组合使用
- [[pd.read_csv]] — 组合使用

## 自测

6 列无表头文件，names 列表应写几个元素？::6 个，与列数一致。


### 补充 · 2026-11-17

names=[...] 让读取阶段就带上正确列名，避免读进来再改 columns。列名个数需与数据列数一致，常与 header=None 配合处理无表头文件。

- 传入列表，顺序对应数据列顺序
- 列表长度应与实际列数一致
- 与 header=None 组合是处理无表头文件的标准写法
names 列表长度和实际列数不一致会怎样？::列名与数据对不齐，通常报错或产生错位的列名，必须先确认列数。

当原文件没有表头或表头不规范时，用 names=[...] 直接给出规范列名，一步得到可用 DataFrame，不必读入后再改 columns。

- 传入列表，长度要与数据列数一致
- 与 header=None 是标准搭配：先声明无表头，再给新列名
- 会覆盖文件原有的列名
names 与 header 各自管什么？::header 指定哪一行当表头（或声明没有表头），names 指定最终列名叫什么。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
