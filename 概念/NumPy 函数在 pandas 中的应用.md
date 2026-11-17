---
term: NumPy 函数在 pandas 中的应用
aliases: [np.sqrt, NumPy 函数, 整表计算]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 26
stage: "S01E11 · 通用函数：快速的逐元素数组函数"
order: 12
---

# NumPy 函数在 pandas 中的应用

> 别名：np.sqrt、NumPy 函数、整表计算

**把 NumPy 的逐元素函数直接用于 Series 或 DataFrame 做整表计算。**

## 解释

NumPy 函数如 np.sqrt 是逐元素通用函数，可直接作用于 pandas 对象，也可作为 apply 的回调。整张表做数学计算时优先用 NumPy，单列自定义逻辑时用 Series + apply。

## 有什么用

- 整表开方、取对数等数学变换
- apply 中传入 np.sqrt 等

## 关键要点

- NumPy 函数需写 np. 前缀，内置函数直接写名
- 整表计算优先 NumPy，单列常用 Series+apply
- np.sqrt 可作 apply 回调，逐列或逐行计算
- 先学 NumPy 再学 pandas 的原因之一

## 边界与易混淆

NumPy 函数是逐元素数学运算，不含业务逻辑；条件分支需 lambda 包裹。

## 关联

- [[np.sqrt]] — 组合使用
- [[apply]] — 组合使用
- [[通用函数]] — 上位概念

## 自测

为什么 apply 里写 np.sqrt 要带 np. 前缀，而 len 不用？::np.sqrt 属于 NumPy 库需模块前缀，len 是 Python 内置函数直接写名。
整张表做数学计算时优先用什么？::优先用 NumPy 函数，而不是逐列 Series 操作。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
