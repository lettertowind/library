---
term: np.array
aliases: [array, 创建数组]
kind: method
domain: 计算机/数据分析/Numpy
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# np.array

> 别名：array、创建数组

**NumPy 中把列表、元组、range 等序列转换为 ndarray 的通用创建函数。**

## 解释

np.array 是 NumPy 最基础的数组创建入口，接收任意可迭代序列并返回 ndarray。它既能包装 range 生成序列，也能直接接收手写列表或元组。相比 np.arange，写法更通用但更啰嗦。

## 有什么用

- 把 Python 列表/元组/range 转成 NumPy 数组
- 需要从已有序列构造数组时

## 关键要点

- 可接收列表、元组、range 或其他序列
- 不指定 dtype 时 NumPy 自动探测元素类型
- np.array(range(1,6)) 与 np.arange(1,6) 效果相同
- 手动写列表较麻烦，一般优先用 np.arange

## 边界与易混淆

np.array 是通用转换函数，不是专门生成等差序列的工具；生成等差序列更推荐 np.arange。

## 关联

- [[np.arange]] — 对比项
- [[Numpy 二维数组]] — 组合使用
- [[dtype 参数]] — 组合使用

## 自测

np.array(range(1,6)) 和 np.arange(1,6) 输出是否相同？为什么？::相同，都是 [1 2 3 4 5]；前者把 range 序列转成数组，后者直接生成等差数组。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
