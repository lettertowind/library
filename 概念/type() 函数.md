---
term: type() 函数
aliases: [type, 对象类型查看]
kind: method
domain: 数据分析/Python
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# type() 函数

> 别名：type、对象类型查看

**Python 内置函数，返回一个对象的类型。**

## 解释

打印数组时输出和列表很像，肉眼难以分辨；type(b) 会返回 <class 'numpy.ndarray'>，这是确认变量到底是不是 NumPy 数组最直接的方式。它看的是整体对象类型，而不是元素类型。

## 有什么用

- 判断变量是列表还是 ndarray
- 调试时确认对象实际类型

## 关键要点

- 写法 type(b)，返回 <class 'numpy.ndarray'>
- 只 print 内容无法区分列表和数组
- 看对象类型用 type()，看元素类型用 dtype
- numpy.ndarray 是 NumPy 独有的数组类型

## 边界与易混淆

不要用 type() 判断元素数据类型；也不要用 dtype 判断对象是不是数组，两者职责不同。

## 关联

- [[numpy.ndarray]] — 组合使用
- [[dtype 参数]] — 对比项

## 自测

打印结果是 [1 2 3]，怎么确认它是数组而不是列表？::用 type() 查看，返回 <class 'numpy.ndarray'> 就是数组；列表会返回 <class 'list'>。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p04 S01E03.创建数组](https://www.bilibili.com/video/BV1ji4y157uB?p=4) · 2026-11-17
