---
term: insert 方法
aliases: [DataFrame.insert, 指定位置插入列]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 44
stage: "S02E29 · vlookup"
---

# insert 方法

> 别名：DataFrame.insert、指定位置插入列

**在 DataFrame 指定列位置插入一列，原地修改不返回新表。**

## 用法
**语法**：`DataFrame.insert(loc, column, value, allow_duplicates=False)`
**参数**：
- `loc`：整数，新列插入的列位置，从 0 开始计；0 表示最前面，原列依次右移
- `column`：新列的列名，不能与已有列重名，否则报 ValueError
- `value`：新列的数据，可以是标量、Series、数组或列表，长度与行数一致
- `allow_duplicates`：默认 False，设为 True 时允许列名重复，一般保持默认

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'姓名': ['张三', '李四'], '语文': [80, 90], '数学': [75, 88]})
df.insert(1, '总分', df['语文'] + df['数学'])  # 原地插入，返回值是 None
print(df)
#    姓名  总分  语文  数学
# 0  张三  155   80   75
# 1  李四  178   90   88

# 移动列：取出 → drop 原列 → insert 到指定位置
s = df['数学']
df.drop(columns='数学', inplace=True)
df.insert(1, '数学', s)
print(df.columns.tolist())
# ['姓名', '数学', '总分', '语文']
```

## 解释

insert(loc, column, value) 把一列插到第 loc 个列位置，原有列依次右移。它是原地操作，返回值是 None，不能写成 df = df.insert(...)。

## 有什么用

- 调整列顺序，把某列移到指定位置
- 在固定位置补充新字段

## 关键要点

- loc 是列位置整数，0 表示最前面
- 原地修改，不要赋值接收返回值
- 常与「取出列→drop 原列→insert」配合实现列移动
- 插入列名不能与已有列重名，否则报错

## 边界与易混淆

insert 只能插列不能插行；插行需用 concat 或 loc 赋值。

## 关联

- [[drop]] — 组合使用
- [[DataFrame]] — 上位概念

## 自测

把总分列插到第二列位置，loc 应传几？::1（0 基位置，第二列即索引 1）。
写 结果 = 结果.insert(0,'总分',s) 会有什么问题？::insert 原地修改且返回 None，结果变量会被赋成 None，原表其实已改好但变量丢了。


### 补充 · 2026-11-17

df.insert(loc, column, value) 把一列数据塞进指定序号的位置，原本该位置及之后的列整体右移。它是「调整列顺序」的最后一步，与 drop 配合使用。因为是原地修改，调用后不需要重新赋值。

- 参数顺序是 (位置序号, 列名, 列数据)
- 位置从 0 开始，0 表示插到最前面
- 原地修改，不要写 df = df.insert(...)（会得到 None）
df.insert 的返回值是什么？为什么不能写成 df = df.insert(...)？::返回 None，它是原地方法；赋值会把 df 变成 None。
对已存在同名列的 DataFrame 调用 insert 会发生什么？::抛 ValueError，需先 drop 原列再插入。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p44 S02E29.vlookup](https://www.bilibili.com/video/BV1ji4y157uB?p=44) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
