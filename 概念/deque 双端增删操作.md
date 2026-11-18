---
term: deque 双端增删操作
aliases: [appendleft, popleft, extendleft, append/pop, 双端添加弹出]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# deque 双端增删操作

> 别名：appendleft、popleft、extendleft、append/pop、双端添加弹出

**deque 在左右两端分别添加、弹出元素的一组方法。**

## 解释

append 和 pop 在右端工作，appendleft 和 popleft 在左端工作，extend 和 extendleft 则用于批量插入可迭代对象中的元素。正是这两套对称的方法，让同一个容器既能当栈也能当队列。

## 有什么用

- 在队首插队或优先处理最新任务
- 从两端取数据做 BFS、滑动窗口、撤销栈

## 关键要点

- append(x)/appendleft(x) 添加单个元素，extend(iter)/extendleft(iter) 批量添加
- extendleft 等价于逐个 appendleft，最终左侧顺序与输入顺序相反
- pop()/popleft() 删除并返回该元素，空 deque 调用会报错
- remove(value) 按值删除，值不存在时抛 ValueError；clear() 清空全部
- 同一端添加和弹出即栈，一端进另一端出即队列

## 边界与易混淆

不要与 Pandas 的 DataFrame.append 混淆，它们名字相同但所属对象不同。

## 关联

- [[deque（双端队列）]] — 上位概念
- [[栈与队列]] — 组合使用

## 自测

d = deque([1,2,3])，执行 d.extendleft([4,5]) 后最左边的元素是几？::5。extendleft 相当于连续 appendleft，后加入的元素在最左端。
从空 deque 中调用 popleft() 会发生什么？::抛出 IndexError，因为无元素可弹出。

## 出处

- [Python 双端队列 deque 实战教学！比列表更猛的 O (1) 双端操作，线程安全 + 内存优化全拿捏！](https://www.bilibili.com/video/BV1S8MMzVEJ7) · 2026-11-18
