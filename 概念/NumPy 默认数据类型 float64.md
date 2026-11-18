---
term: NumPy 默认数据类型 float64
aliases: [float64, 默认浮点型, 64 位浮点数]
kind: concept
domain: Numpy
tags: [概念/concept, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
---

# NumPy 默认数据类型 float64

> 别名：float64、默认浮点型、64 位浮点数

**ones、zeros 等创建函数在不指定 dtype 时生成的元素类型，为 64 位浮点数。**

## 解释

用 np.ones、np.zeros 建数组时，即使形状里全是整数，元素默认也是浮点型 float64，打印结果会带小数点。np.full 则不同，它按填充值推断类型（填 520 得到整型）。所以不能凭直觉假设类型，要用 .dtype 实际查看。

## 有什么用

- 判断数组能否直接参与整型相关运算
- 控制内存占用与数值精度时
- 排查计算结果出现小数点的原因

## 关键要点

- ones/zeros 不传 dtype 时，元素类型固定为 float64
- full 的类型由填充值推断，填整数会得到整型，与 ones/zeros 不同
- 打印时带小数点是最直观的浮点标志
- 需要固定类型就显式写 dtype=int 或 dtype=np.float32，不要靠猜

## 边界与易混淆

这是 NumPy 的类型推断规则，不是所有创建函数都统一为 float64；np.array 由列表元素推断，np.full 由填充值推断。

## 关联

- [[np.ones]] — 组合使用
- [[np.zeros]] — 组合使用
- [[dtype 参数]] — 前置知识

## 自测

np.ones((3,3)) 的元素是什么类型？为什么不是整型？::float64；ones 在不指定 dtype 时按浮点默认类型创建，与形状里的数字是否为整数无关。
如果想让元素全为 1 且是整型，该怎么写？::np.ones((3,3), dtype=int)，显式覆盖默认的 float64。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p05 S01E04.多维数组](https://www.bilibili.com/video/BV1ji4y157uB?p=5) · 2026-11-17
