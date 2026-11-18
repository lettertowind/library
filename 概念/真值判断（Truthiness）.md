---
term: 真值判断（Truthiness）
aliases: [truthiness, bool(), 假值, truthy/falsy]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 真值判断（Truthiness）

> 别名：truthiness、bool()、假值、truthy/falsy

**Python 判断一个对象在布尔上下文中算真还是算假的规则。**

## 解释

bool() 只是显式地把这套规则的结果取出来；if、and/or、all/any、filter(None, ...) 都会自动套用。空字符串、0、None、空容器等为假，其余为真，这正是 Python 里大量条件写法的底层依据。

## 有什么用

- 写 if 条件判断
- 过滤空值或零值数据
- 理解为什么 if my_list: 可以判空

## 关键要点

- 假值固定为：None、False、0、0.0、空字符串、空容器
- 非空容器、非零数字一律为真，即使内容里有 0
- bool() 无参数时返回 False
- 自定义对象默认恒为真，除非定义了 __bool__ 或 __len__

## 边界与易混淆

真值判断不做数值或类型比较，与 == 是两回事；对多元素 NumPy 数组做真值判断会直接报错。

## 关联

- [[all 与 any]] — 组合使用
- [[None]] — 对比项

## 自测

bool([0]) 的结果是什么？::True，因为 [0] 是非空列表，非空容器为真，与内部元素的值无关。
为什么 if data: 常被用来判断列表是否为空？::空列表是假值，非空列表是真值，等价于 if len(data) > 0 但更简洁。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
