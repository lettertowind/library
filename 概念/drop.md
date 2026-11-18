---
term: drop
aliases: [df.drop, DataFrame.drop, 删除行列]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 30
stage: "S02E15 · 数据删除 drop函数"
---

# drop

> 别名：df.drop、DataFrame.drop、删除行列

**按标签删除 DataFrame 或 Series 的行/列的方法。**

## 用法
**语法**：`DataFrame.drop(labels=None, axis=0, index=None, columns=None, inplace=False, errors='raise')`
**参数**：
- `labels`：要删除的行标签或列标签，可以是单个标签，也可以是列表；删除多行或多列时必须用列表传入
- `axis`：指定删除方向，默认是 `0`，表示按行删除；要删除列时要显式设为 `1` 或 `'columns'`
- `index`：直接指定要删除的行标签，效果等价于 `labels` 配合 `axis=0`，与 `columns` 二选一使用
- `columns`：直接指定要删除的列标签，效果等价于 `labels` 配合 `axis=1`，可读性更好
- `inplace`：默认是 `False`，返回新对象，原数据不变；设为 `True` 时在原对象上直接修改，并返回 `None`
- `errors`：默认是 `'raise'`，标签不存在时就会报错；设为 `'ignore'` 时，即使标签不存在也不会报错

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'语文': [90, 85, 78], '数学': [95, 88, 92]}, index=['小明', '小红', '小刚'])
print(df.drop('小红'))            # 删除行：语文 数学 小明 90 95 / 小刚 78 92
print(df.drop(columns='语文'))     # 删除列：数学 小明 95 / 小红 88 / 小刚 92
print(df.drop(labels=[0], errors='ignore'))  # 标签不存在不报错，原样返回整表
```

## 解释

drop 是 Pandas 中删除数据的核心方法，通过指定行标签或列标签来移除对应数据。默认按行（axis=0）操作，删除列需显式设置 axis=1。它默认返回新对象而不修改原数据，需配合 inplace 或赋值使用。

## 有什么用

- 删除不需要的行记录
- 删除多余的列字段
- 数据清洗时剔除指定标签的数据

## 关键要点

- 删除单行直接写行标签：df.drop(2)
- 删除多行用 labels 列表：df.drop(labels=[1,3])
- 删除列必须设 axis=1，默认 axis=0 按行
- 删除后原索引不会自动重排，保留原标签
- 默认 inplace=False，返回新对象，原数据不变

## 边界与易混淆

drop 按标签删除，不是按位置；要按位置删需先查标签。与 del 语句、pop 方法的区别在于 drop 可批量且返回新对象。

## 关联

- [[axis 参数]] — 组合使用
- [[inplace 参数]] — 组合使用
- [[labels 参数]] — 组合使用
- [[DataFrame]] — 上位概念

## 自测

df.drop(2) 和 df.drop(labels=[2]) 效果一样吗？为什么？::一样。单标签可直接传，多标签必须用 labels 列表；单标签传列表也合法。
执行 df.drop('语文', axis=1) 后直接 print(df)，为什么语文列还在？::因为 inplace 默认 False，drop 返回新对象，原 df 未被修改，需赋值或设 inplace=True。


### 补充 · 2026-11-17

drop 用来从 DataFrame 中剔除不需要的行或列，依据的是索引标签而非物理行号。它能一次删除一个标签，也能通过列表删除多个标签，默认返回删除后的新对象，只有设置 inplace=True 才改动原数据。

- 删单行：data.drop(1)，axis 默认 0 可省略
- 删多行：data.drop(labels=[1, 3])
- 删单列：data.drop('语文', axis=1)，必须写 axis=1
执行 data.drop(1) 后紧接着 print(data)，为什么看不到删除效果？::drop 默认 inplace=False，返回的是新对象，该返回值没被接收，原 data 未变。
要删除“语文”和“英语”两列，写出调用语句并说明为什么不能只写 drop(['语文','英语'])。::data.drop(labels=['语文','英语'], axis=1)；不写 axis=1 时默认按行查找这两个标签，会找不到而报错。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p30 S02E15.数据删除 drop函数](https://www.bilibili.com/video/BV1ji4y157uB?p=30) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
