---
term: key 参数
aliases: [key=, key function, 比较依据]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# key 参数

> 别名：key=、key function、比较依据

**传给 max/min/sorted 等函数、用来自定义比较依据的函数。**

## 解释

key 函数先把每个元素映射成一个「排序值」，再比较这些值，原元素本身不改变、返回值仍是原元素。常配合内置函数（len、str.lower）或 lambda 使用。

## 有什么用

- 取长度最长的字符串
- 按某字段对字典列表排序
- 忽略大小写排序

## 关键要点

- 只影响比较依据，不改变返回的元素本身
- 可以是任意单参数函数，常用 lambda
- 多关键字比较可让 key 返回元组
- 与老式 cmp 参数不同：key 只做映射，不做两两比较

## 边界与易混淆

key 返回值的类型必须可相互比较，混用数字和字符串会报错；不加 key 时按元素自身比较。

## 关联

- [[lambda 表达式]] — 组合使用
- [[np.max np.min]] — 对比项

## 自测

max(names, key=len) 返回的是什么？::长度最大的那个原始字符串，而不是它的长度值。
如何按「分数降序、名字升序」排序？::sorted(items, key=lambda x: (-x.score, x.name))，用元组让 key 返回多个比较维度。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
