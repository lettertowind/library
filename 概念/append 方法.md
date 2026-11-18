---
term: append 方法
aliases: [append, 追加, DataFrame.append, Series.append]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
---

# append 方法

> 别名：append、追加、DataFrame.append、Series.append

**Series 和 DataFrame 的方法，将新数据追加到原对象下方并按列对齐。**


## 用法
**语法**：`df.append(other, ignore_index=False, verify_integrity=False, sort=False)`（pandas 2.0 起已移除，以下函数签名属于旧版写法；现在推荐改用 `pd.concat([df, other], ignore_index=...)`）
**参数**：
- `other`：要追加的 Series、字典或 DataFrame，按列名对齐，缺失的列自动填 NaN
- `ignore_index`：为 True 时忽略原索引，按追加后的顺序生成新的连续索引（默认 False）
- `verify_integrity`：为 True 时检查追加后索引是否重复，如果重复则报错（默认 False）
- `sort`：为 True 时对列名排序（默认 False）
**示例**：
```python
import pandas as pd

df1 = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
row = pd.Series({'a': 5})                    # 该 Series 缺少 b 列
# 旧版写法：df1.append(row, ignore_index=True)  # pandas 2.0 起已移除
# 推荐写法：改用 pd.concat 进行纵向拼接
res = pd.concat([df1, row.to_frame().T], ignore_index=True)
print(res)
#    a    b
# 0  1  3.0
# 1  2  4.0
# 2  5  NaN
```

## 解释

append 用于在 DataFrame 或 Series 末尾追加行，按列名对齐，缺失字段填 NaN。效果类似 concat 的纵向连接，但语法更简洁。注意 append 在新版 Pandas 中已被弃用，推荐使用 pd.concat。

## 有什么用

- 向现有表追加一行或多行数据
- 快速合并两个结构相似的表

## 关键要点

- 按列名对齐，缺失字段自动填 NaN
- 可追加 Series、字典或 DataFrame
- ignore_index=True 可忽略原索引生成新索引
- 新版 Pandas 已弃用，建议改用 pd.concat

## 边界与易混淆

append 不是 concat 的方法，而是 DataFrame/Series 的方法；新版 Pandas 中已弃用。

## 关联

- [[pd.concat]] — 对比项
- [[ignore_index 参数]] — 组合使用

## 自测

df1.append(s2, ignore_index=True) 中 ignore_index=True 的作用是什么？::忽略原索引，按追加后的顺序生成新的连续索引。


### 补充 · 2026-11-17

效果接近 concat 默认 axis=0 的纵向追加，默认按列名对齐。它还能把一条索引为列名的 Series 追加成 DataFrame 的新行。

- 是对象方法，不是 pd 顶层函数，写法 s1.append(s2)
- 按列对齐，缺的列补 NaN
- 可用 Series 构造一行：索引设为 df 的列名再 append
要把一条新记录加到 df 末尾，Series 的索引该怎么设？::设为 df 的列名，才能按列对齐插入。
append 与 concat 默认行为的主要差别是什么？::行为基本一致（纵向追加），差别在于 append 是对象方法、已弃用且性能差。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p24 S02E09.连接查询之concat](https://www.bilibili.com/video/BV1ji4y157uB?p=24) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
