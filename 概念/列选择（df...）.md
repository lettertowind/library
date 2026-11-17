---
term: 列选择（df...）
aliases: [中括号选列, df[['列名']], 多列选择]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# 列选择（df...）

> 别名：中括号选列、df[['列名']]、多列选择

**用中括号传入列名从 DataFrame 取列，单列返回 Series，传入列表返回 DataFrame。**

## 用法
**语法**：`df['列名']` / `df[['列名1', '列名2', ...]]`
**参数**：
- `'列名'`：单个列名（字符串），返回 Series
- `['列名1', '列名2']`：列名列表，返回只含这些列的新 DataFrame，列顺序即列表顺序
**示例**：
```python
import pandas as pd
df = pd.DataFrame({'语文': [90, 80], '数学': [85, 95], '英语': [70, 60]})
print(df[['语文', '英语']])        # DataFrame，两列，顺序同列表
print(df['语文'])                  # Series
print(type(df[['语文']]))          # <class 'pandas.core.frame.DataFrame'>
print(df[['语文', '数学']].mean())  # 只对所选两列求均值
print(df[['语文', '数学']].describe())  # 统计范围限定为这两列
```

## 解释

df['语文'] 取一列得到 Series，可以直接使用 .str、.dt 等访问器；df[['语文','数学']] 传列表得到只含这些列的新 DataFrame。它是控制后续分析范围最基础的手段——先选列再统计，就相当于给 describe()、mean() 等方法划定了作用域。

## 有什么用

- 只需分析部分字段时缩小计算范围
- 把单列转成 Series 以便使用字符串或时间访问器
- 宽表（几百列）中先选列再统计，避免全表 describe 输出过长

## 关键要点

- 单列用字符串取，返回 Series；多列用列表取，返回 DataFrame
- 列表中的列名顺序即结果列的顺序
- 可与 describe()、mean() 等统计方法直接串联
- df[['语文']] 与 df['语文'] 结果类型不同，容易踩坑

## 边界与易混淆

这套写法只选列不选行；按条件筛选行要用布尔索引或 loc/iloc，不要混用。

## 关联

- [[describe()]] — 组合使用
- [[Series]] — 组合使用
- [[iloc]] — 对比项

## 自测

df[['语文']] 和 df['语文'] 有什么区别？::前者返回只含一列的 DataFrame，后者返回 Series。
为什么 df[['语文','数学']].describe() 只输出两列的统计？::因为选列已经把传入的数据限定为这两列，describe() 只对拿到的数据做统计。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p32 S02E17.数学统计函数](https://www.bilibili.com/video/BV1ji4y157uB?p=32) · 2026-11-17
