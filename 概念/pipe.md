---
term: pipe
aliases: [DataFrame.pipe, 管道方法, 表格函数]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 42
stage: "S02E27 · 分组对象和创建"
---

# pipe

> 别名：DataFrame.pipe、管道方法、表格函数

**把 DataFrame 作为第一个参数传入指定函数，实现链式调用。**

## 用法
**语法**：`df.pipe(func, *args, **kwargs)`
**参数**：
- `func`：可调用对象，接收当前 DataFrame 作为第一个位置参数
- `*args`：原样传给 `func` 的额外位置参数，如 `'班级'`
- `**kwargs`：原样传给 `func` 的额外关键字参数

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'班级': ['一班', '一班', '二班'], '分数': [90, 80, 95]})

def add_total(data, bonus):
    data = data.copy()
    data['分数'] = data['分数'] + bonus
    return data

result = (df.pipe(add_total, bonus=5)
            .pipe(pd.DataFrame.groupby, '班级')
            .sum())
print(result)
#       分数
# 班级
# 一班   175
# 二班   100
```

## 解释

pipe 让「函数式」操作也能接入 Pandas 的链式写法。它把当前对象传给任意函数，适合把自定义函数或 groupby 这类类方法串进流水线。

## 有什么用

- 链式调用中插入自定义函数
- 把 groupby 等类方法接入管道
- 提高多步处理的可读性

## 关键要点

- df.pipe(pd.DataFrame.groupby, '班级').sum() 等价于 df.groupby('班级').sum()
- pipe 传的是整个 DataFrame，apply 传的是行或列，map 传的是元素
- 适合把复杂处理拆成可复用的函数步骤
- 后续可接 .sum() 等聚合完成链式调用

## 边界与易混淆

简单操作直接用方法链更直观；pipe 的价值在接入外部函数时体现。

## 关联

- [[groupby]] — 组合使用
- [[apply]] — 对比项
- [[map]] — 对比项

## 自测

pipe、apply、map 三者的作用对象分别是什么？::pipe 作用于整个 DataFrame，apply 作用于行/列，map 作用于单个元素。
df.pipe(pd.DataFrame.groupby, '班级').sum() 等价于什么？::df.groupby('班级').sum()。


### 补充 · 2026-11-17

pipe 本身不做计算，它只是把当前对象塞进你给的函数里，让代码能以“数据 → 函数 → 函数”的管道形式书写。例如 data.pipe(pd.DataFrame.groupby, '班级').sum() 等价于 data.groupby('班级').sum()。适合把复杂逻辑封装成函数后串起来，保持链式可读性。

- pipe 会把调用它的对象作为函数的第一个参数。
- data.pipe(pd.DataFrame.groupby, '班级').sum() 等价于按班级分组求和。
- Pandas 三大方法：pipe 处理表格级、apply 处理行列级、map 处理元素级。
data.pipe(pd.DataFrame.groupby, '班级') 里 data 被传到了哪个参数？::作为 groupby 的第一个参数，相当于 data.groupby('班级')。
pipe、apply、map 的作用粒度分别是什么？::pipe 管整张表，apply 管行或列，map 管单个元素。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p42 S02E27.分组对象和创建](https://www.bilibili.com/video/BV1ji4y157uB?p=42) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
