---
term: head()
aliases: [head, 查看前几行]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
order: 17
---

# head()

> 别名：head、查看前几行

**返回 DataFrame 前 n 行的预览方法，默认 5 行。**

## 解释

head() 用于快速预览数据，默认显示前 5 行，可传参如 head(3)。它只影响显示，不改变变量中已读入的全部数据。

## 有什么用

- 读取后快速预览数据结构
- 检查列名与数据格式

## 关键要点

- 默认 5 行，可传参指定行数
- 只影响显示，不减少内存数据
- 无表头文件预览时行数看似多一行

## 边界与易混淆

head() 不是读取限制；要真正少读数据用 nrows。

## 关联

- [[nrows 参数]] — 对比项
- [[pd.read_csv]] — 组合使用

## 自测

head() 会改变 DataFrame 本身的行数吗？::不会，只影响显示。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
