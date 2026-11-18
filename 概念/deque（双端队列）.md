---
term: deque（双端队列）
aliases: [deque, collections.deque, 双端队列, double-ended queue]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# deque（双端队列）

> 别名：deque、collections.deque、双端队列、double-ended queue

**collections 模块中支持两端高效增删的队列容器。**

## 解释

deque 是 Python 标准库 collections 提供的容器，可视为栈与队列的泛化：左右两端都能以接近 O(1) 的代价添加和弹出元素。相比 list 的头部插入需要整体搬移元素，deque 在两端操作上更省时，并具备线程安全与内存回收方面的优势。适合做任务队列、滑动窗口、最近记录等场景。

## 有什么用

- 需要频繁在两端增删元素时替代 list
- 实现栈、队列、生产者-消费者缓冲、滑动窗口

## 关键要点

- 导入：from collections import deque，可用 deque([1,2,3]) 从可迭代对象初始化
- 支持索引 d[2]、insert、count、reverse，但不支持切片，需先转成 list(d)[1:3]
- 作为栈用 append + pop，作为队列用 append + popleft
- 视频称双端操作性能大致相同、线程安全、内存高效，但内存收益依场景而定
- 可用类型提示 deque[Any] 标注元素类型，只是提示不影响运行

## 边界与易混淆

不支持切片；在中间插入删除仍需移动元素，不能完全替代 list。

## 关联

- [[栈与队列]] — 上位概念
- [[deque 双端增删操作]] — 下位概念
- [[rotate（deque 旋转）]] — 下位概念
- [[maxlen（deque 容量限制）]] — 下位概念
- [[时间复杂度 O(1)]] — 组合使用
- [[线程安全]] — 组合使用

## 自测

为什么把 list 改成 deque 来实现队列会更快？::list 的 pop(0) 需要把后面所有元素前移，是 O(n)；deque 的 popleft 是两端操作，代价接近 O(1)。
想把 deque 中间的一段元素取出来，该怎么做？::deque 不支持切片，先 list(d)[1:3] 转成列表再切。

## 出处

- [Python 双端队列 deque 实战教学！比列表更猛的 O (1) 双端操作，线程安全 + 内存优化全拿捏！](https://www.bilibili.com/video/BV1S8MMzVEJ7) · 2026-11-18
