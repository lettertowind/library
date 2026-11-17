---
term: range 结束位置不含自身
aliases: [range 左闭右开, range(1, n+1)]
kind: concept
domain: 数据分析/Python
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S01E02 · 体验Numpy与for循环的区别"
order: 3
---

# range 结束位置不含自身

> 别名：range 左闭右开、range(1, n+1)

**range 的结束参数不包含在序列内，取到 n 需写 n+1。**

## 解释

range(1, n+1) 才能取到 1 到 n。省略起始位置默认从 0 开始。np.arange 遵循同样的左闭右开规则。

## 有什么用

- 写循环边界
- 生成 1 到 n 的序列

## 关键要点

- 左闭右开：包含起始，不包含结束
- 取 1 到 n 必须写 n+1
- 省略起始默认从 0 开始
- np.arange 同样适用此规则

## 关联

- [[np.arange]] — 组合使用
- [[列表推导式]] — 组合使用

## 自测

range(1, 4) 包含哪些数？::1、2、3，不包含 4。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
