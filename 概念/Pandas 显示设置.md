---
term: Pandas 显示设置
aliases: [pd.options.display, max_columns, max_rows, 显示全部行列]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# Pandas 显示设置

> 别名：pd.options.display、max_columns、max_rows、显示全部行列

**通过 pd.options.display 控制 DataFrame 在控制台显示多少行多少列的设置。**

## 用法
**语法**：`pd.options.display.max_columns = None`、`pd.options.display.max_rows = None`
**参数**：
- `max_columns`：DataFrame 最多显示的列数，设为 `None` 时显示全部列
- `max_rows`：DataFrame 最多显示的行数，设为 `None` 时显示全部行
- `width`：单行显示宽度（字符数），超过宽度时会换行折段显示
**示例**：
```python
import pandas as pd

df = pd.DataFrame({f'col{i}': range(3) for i in range(20)})

print(df.shape)              # (3, 20)
print(pd.options.display.max_columns)   # 默认值，如 20

pd.options.display.max_columns = None    # 全部列都显示，不再出现省略号
print(df.columns.tolist()[-1])           # col19，确认最后一列可见

pd.options.display.max_columns = 20      # 看完结构后还原默认
print(pd.options.display.max_columns)    # 20
```

## 解释

Pandas 默认只显示部分列，列多时用省略号代替，容易误判数据内容。把 pd.options.display.max_columns 或 max_rows 设为 None 就能显示全部列或全部行，方便查看数据结构。但这只是显示层的临时调试手段。

## 有什么用

- 初次读入数据、想确认有哪些列时
- 排查列被省略号隐藏导致的误判

## 关键要点

- 显示全部列：pd.options.display.max_columns = None
- 显示全部行：pd.options.display.max_rows = None
- 数据量大时不要设 None，展开几十万行会浪费 Pandas 的性能优势
- 看完结构后应及时取消该设置，只读需要的列
- 显示全部列时，较长的一行会被折成多段展示

## 边界与易混淆

这是全局显示选项，不影响实际数据和计算；不要与读取时的 usecols、dtype 等参数混淆。

## 关联

- [[NaN]] — 组合使用
- [[head()]] — 对比项

## 自测

数据显示有 48 列，但控制台只看到十几列加省略号，怎么解决？::设置 pd.options.display.max_columns = None，查看完记得还原。
为什么有几十万行数据时不建议设置 max_rows = None？::强制展开全部数据会消耗大量性能，违背 Pandas 按需读取、按需查看的设计思路。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p65 S03E16.散点图](https://www.bilibili.com/video/BV1ji4y157uB?p=65) · 2026-11-17
