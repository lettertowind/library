---
term: sorted（排序）
aliases: [sorted, sorted(), key 排序, reverse]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# sorted（排序）

> 别名：sorted、sorted()、key 排序、reverse

**对任意可迭代对象排序并返回新的有序列表，原数据不变。**

## 解释

sorted 接受 key 指定排序依据（如 key=len 按长度排），reverse=True 反向。它与列表方法 list.sort 的区别是：sorted 不修改原对象，可用于元组、字符串、字典键等任何可迭代对象。

## 有什么用

- 对任意可迭代对象排序
- 按某个属性或长度自定义排序

## 关键要点

- 返回新列表，原对象保持不变
- key 接受函数，决定按什么排序
- reverse=True 实现降序
- 不传 key 时字符串按 Unicode 编码顺序排

## 边界与易混淆

sorted 返回列表而非原类型；若想原地排序且对象是列表，用 list.sort 更省内存。

## 关联

- [[ndarray.sort]] — 对比项
- [[lambda 表达式]] — 组合使用

## 自测

sorted(t) 能对元组用，而 t.sort() 会报错，原因是什么？::sorted 是内置函数，任何可迭代对象都能吃进来并返回新列表；sort 是列表的方法，只有列表才有。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
