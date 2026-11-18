---
term: Series.str 访问器
aliases: [.str, str 访问器, 字符串方法访问器]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
---

# Series.str 访问器

> 别名：.str、str 访问器、字符串方法访问器

**Pandas 中用于对 Series 逐元素调用字符串方法的访问器。**


## 用法
**语法**：`Series.str.<method>(...)`
**参数**：访问器本身无参数，参数由所调用的字符串方法决定，常用几项如下：
- `pat`：匹配模式，供 `contains`/`replace`/`extract` 等方法使用
- `regex`：是否把 `pat` 当正则解析；`contains` 默认 True，`replace` 自 pandas 2.0 起默认 False
- `na`：缺失值位置的返回值，默认 None（保留 NaN），如 `contains` 里常设为 False
- `case`：`startswith`/`endswith` 是否区分大小写，默认 True
- `expand`：`extract`/`split` 是否展开为 DataFrame，默认 False
**示例**：
```python
import pandas as pd

s = pd.Series(['Apple pie', 'banana', None])
print(s.str.lower().tolist())                   # ['apple pie', 'banana', None]
print(s.str.contains('an', na=False).tolist())  # [False, True, False]
print(s.str.replace('an', 'AN', regex=False).tolist())  # ['Apple pie', 'bANANa', None]

d = pd.Series(pd.to_datetime(['2020-01-02', '2021-03-04']))
# d.str.find('-')  # 报错：Can only use .str accessor with string values
print(d.astype(str).str.find('-').tolist())     # [4, 4]
```

`.str` 只负责把字符串方法向量化调用，不改变列类型；日期列、数值列要先 `.astype(str)` 再调用，取子串、拆分、匹配后返回的仍是 Series，可以继续链式处理。

## 解释

通过 Series.str.xxx() 可以把 Python 字符串方法（如 lower、find、replace）向量化应用到整列。它只做方法调用，不做类型转换；非字符串列必须先 .astype(str) 才能使用。

## 有什么用

- 批量清洗文本列
- 对整列做查找、替换、正则提取

## 关键要点

- .str 是访问器，不是类型转换函数
- 日期/数值列需先 .astype(str) 再调用 .str
- 支持大部分 Python 字符串方法和部分正则方法
- 返回结果仍是 Series，可继续链式操作

## 边界与易混淆

易与 .astype(str) 混淆：后者才是类型转换；对非字符串列直接 .str 会报错或行为异常。

## 关联

- [[Series]] — 上位概念
- [[astype(str)]] — 前置知识

## 自测

为什么日期列不能直接 .str.find('-')？::因为日期列是 datetime 类型，.str 只对字符串生效，需先 .astype(str) 转换。
.str 和 .astype(str) 的本质区别是什么？::.str 是字符串方法访问器，.astype(str) 是类型转换。


### 补充 · 2026-11-17

在字符串 Series 上加 .str，就能把 Python 字符串方法批量作用到每个元素上，包括按位置取字符 str[0]、str[1]，以及 find、contains 等。取出的字符可以直接作为分组键，实现按姓氏这类“字符串片段”分组。

- str[0] 取首字符，str[1] 取第二个字符，可分别作为分组键。
- 想一次取多个字符用 str[:2]，但在分组场景下分别取更可靠。
- 返回仍是 Series，可直接传给 groupby。
要按姓氏给成绩分组汇总，分组键怎么写？::data.groupby(data['姓名'].str[0])[['语文','数学','英语']].sum()。
这种取首字的方法对“司马光”会得到什么？::得到“司”，复姓被错误拆分，这是该方法的局限。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p42 S02E27.分组对象和创建](https://www.bilibili.com/video/BV1ji4y157uB?p=42) · 2026-11-17

.str 不是类型转换，它只是把 Python 的字符串方法批量映射到 Series 每个元素上。数据是日期型、数值型时直接加 .str 会报错或行为异常，必须先 astype(str) 转成字符串再调用，形成固定流程 Series.astype(str).str.方法()。

- .str 是方法访问器，astype(str) 才是类型转换，两者别混为一谈
- 日期/数值列做字符串操作前必须先 astype(str)
- 固定写法：Series.astype(str).str.方法(...)
对日期列直接写 df['日期'].str.find('-') 为什么可能出问题？::该列是日期 dtype 不是字符串，.str 访问器无法作用于日期元素；应先 astype(str)。
.str 会把日期转成字符串吗？::不会，它只提供字符串方法的调用入口；转换由 astype(str) 完成。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p39 S02E24.字符串操作（下）](https://www.bilibili.com/video/BV1ji4y157uB?p=39) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
