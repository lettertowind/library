---
term: 字典（dict）
aliases: [dict, 字典, 映射类型, 哈希表]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 字典（dict）

> 别名：dict、字典、映射类型、哈希表

**Python 中按键值对存储数据的可变映射类型，靠键的哈希值直接定位。**

## 解释

dict 底层是哈希表，查找、插入、删除的平均复杂度都是 O(1)。键必须可哈希，值任意。从 Python 3.7 起保证按插入顺序迭代，这一点已经成为语言规范而非实现细节。它是 Python 里用得最多的数据结构之一——模块命名空间、函数关键字参数、JSON 对象在内存中都对应字典。

## 有什么用

- 查表映射：名字到数值、ID 到记录
- 计数与分组：`counts[k] = counts.get(k, 0) + 1`
- 缓存（记忆化）
- 表示结构化数据，JSON 解析后就是嵌套 dict
- 接收任意关键字参数 `**kwargs`

## 关键要点

- 键必须可哈希：`str`、`int`、`tuple` 可以，`list`、`dict`、`set` 不行
- `d[k]` 取不存在的键抛 `KeyError`，`d.get(k, default)` 不抛
- `k in d` 判断的是键，不是值
- 字典推导式：`{k: v for k, v in pairs}`
- 合并用 `d1 | d2`（3.9+），同名键取后者

## 边界与易混淆

与 `set` 同族，都依赖哈希；set 只有键没有值。与 `list` 的取舍：需要按位置索引或保持重复元素用 list，需要按键快速查找用 dict。注意 `d.items()` 返回的是视图，原字典改动会反映到视图上。

## 关联

- [[hash 与可哈希]] — 能否作键的判定依据
- [[命名空间（globals 与 locals）]] — 模块和函数命名空间用字典实现
- [[set（集合）]] — 只有键没有值的同类结构

## 自测

为什么 list 不能做 dict 的键？::list 可变且不可哈希，内容一变哈希值就变，哈希表无法定位，因此直接抛 TypeError。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
