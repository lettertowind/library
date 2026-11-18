---
term: reversed（反转迭代器）
aliases: [reversed, reversed(), 反转迭代]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# reversed（反转迭代器）

> 别名：reversed、reversed()、反转迭代

**返回一个按相反顺序遍历原序列的迭代器，不复制原数据。**

## 解释

reversed(seq) 不生成新列表，只给出反向迭代器，因此内存效率高，需要具体结果时用 list() 收拢。它与切片 seq[::-1] 效果相似，但切片会复制整个序列。

## 有什么用

- 倒序遍历序列
- 需要低内存反转时

## 关键要点

- 返回迭代器，需 list() 才能看到全部元素
- 不复制数据，内存开销小
- seq[::-1] 是等价但会复制列表的写法

## 边界与易混淆

要求对象支持反向访问（有 __len__ 和 __getitem__ 或 __reversed__），普通生成器不能直接反转。

## 关联

- [[负索引]] — 前置知识
- [[range 范围对象]] — 组合使用

## 自测

为什么处理超大列表时 reversed 优于 seq[::-1]？::reversed 只是惰性反向遍历，切片会立刻复制一份完整的新列表占内存。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
