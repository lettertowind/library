---
term: dtype 参数
aliases: [dtype, 数据类型参数, 元素数据类型]
kind: concept
domain: 计算机/数据分析/Numpy
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 4
stage: "S01E03 · 创建数组"
order: 4
---

# dtype 参数

> 别名：dtype、数据类型参数、元素数据类型

**创建数组时用于指定或查看元素数据类型的参数/属性，如 int32、float64。**

## 解释

dtype 既可作为创建函数的参数（dtype=float、dtype=np.int32）指定元素类型，也可作为数组属性（a.dtype）查看当前类型。不指定时 NumPy 自动探测，整数可能得到 int32 或 int64。

## 有什么用

- 控制数组元素是整数还是浮点、多少位
- 查看已有数组的元素类型

## 关键要点

- 作为参数：np.arange(1,8,dtype=float)
- 作为属性：a.dtype 返回元素类型
- 常见形式为类型名加位数：int32、int64、float32、float64
- 不指定时自动探测，结果可能与预期不完全一致

## 边界与易混淆

dtype 描述元素类型，type(a) 描述对象类型（numpy.ndarray），两者不要混淆。

## 关联

- [[np.array]] — 组合使用
- [[shape 属性]] — 对比项

## 自测

a.dtype 和 type(a) 分别返回什么？::a.dtype 返回元素数据类型（如 int64）；type(a) 返回对象类型 <class 'numpy.ndarray'>。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
