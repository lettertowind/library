---
term: maxlen（deque 容量限制）
aliases: [maxlen, 最大长度, 固定容量队列]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# maxlen（deque 容量限制）

> 别名：maxlen、最大长度、固定容量队列

**创建 deque 时指定的长度上限，满员后新元素会挤掉另一端的旧元素。**

## 解释

deque(maxlen=N) 让队列长度永远不超过 N。已满时从右端 append 会挤掉最左元素，从左端 appendleft 会挤掉最右元素，extend 批量添加同样如此。这天然适合保存「最近 N 条」记录，无需自己判断并手动删除。

## 有什么用

- 保存最近 N 条日志、历史操作或滚动窗口数据
- 限制缓冲区大小防止内存无限增长

## 关键要点

- deque(maxlen=4) 后无论怎么添加，长度始终保持最多 4
- append 挤掉左端最旧元素，appendleft 挤掉右端最旧元素
- maxlen 在创建时确定，之后不能修改
- 被挤出的元素不会返回，需要留存就得先手动取出

## 边界与易混淆

只限制长度不限制内存占用，元素本身很大时仍需控制内容；被挤掉的数据无法追溯。

## 关联

- [[deque（双端队列）]] — 上位概念
- [[deque 双端增删操作]] — 组合使用

## 自测

g = deque([1,2,3,4], maxlen=4) 后执行 g.appendleft(0)，队列内容和被挤出的元素分别是什么？::队列变为 deque([0,1,2,3])，右端最旧的 4 被挤出。
maxlen 和手动 if len(d) > N: d.pop() 相比好在哪？::一次操作自动完成插入和淘汰，逻辑更短且不会出现中间状态的越界。

## 出处

- [Python 双端队列 deque 实战教学！比列表更猛的 O (1) 双端操作，线程安全 + 内存优化全拿捏！](https://www.bilibili.com/video/BV1S8MMzVEJ7) · 2026-11-18
