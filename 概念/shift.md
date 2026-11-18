---
term: shift
aliases: [shift(), 数据位移, 向下移动]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 46
stage: "S02E31 · 数据的转置、计算环比与同比"
---

# shift

> 别名：shift()、数据位移、向下移动

**把序列整体上下移动若干行，用于构造上期/前期数据。**

## 用法
**语法**：`DataFrame.shift(periods=1, freq=None, axis=0, fill_value=None)` / `Series.shift(periods=1, fill_value=None)`

**参数**：
- `periods`：移动的行数，正数表示向下移动（取上期），负数表示向上移动，默认 1
- `freq`：只用于时间索引，按时间频率整体平移索引；普通的构造上期列场景不用传
- `axis`：0 或 'index' 表示沿行移动，默认 0；不要传 1
- `fill_value`：移位后空出来的位置用该值填充，默认留空（NaN）

**示例**：
```python
import pandas as pd

df = pd.DataFrame({
    "city": ["北京", "北京", "北京", "上海", "上海", "上海"],
    "month": [1, 2, 3, 1, 2, 3],
    "amount": [100, 120, 150, 200, 180, 210],
})

# 整列 shift 会跨组错位：上海 1 月会对应到北京 3 月
print(df["amount"].shift(1).tolist())
# [nan, 100.0, 120.0, 150.0, 200.0, 180.0]

# 正确做法：先 groupby 再组内 shift
df["prev_amount"] = df.groupby("city")["amount"].shift(1)
print(df)
#   city  month  amount  prev_amount
# 0   北京      1     100          NaN
# 1   北京      2     120        100.0
# 2   北京      3     150        120.0
# 3   上海      1     200          NaN
# 4   上海      2     180        200.0
# 5   上海      3     210        180.0

# 环比 = 本期 / 上期 - 1，首行无上期为 NaN
df["mom"] = (df["amount"] / df["prev_amount"] - 1).round(4)
print(df["mom"].tolist())
# [nan, 0.2, 0.25, nan, -0.1, 0.1667]
```

## 解释

shift(1) 把整列向下移一格，使每行对应上一行数据，是计算环比的标准手段。首行移动后为空，正好对应没有上期。多组数据时须在组内 shift，不能整列直接移。

## 有什么用

- 构造上期金额列
- 计算环比、差分、滞后特征

## 关键要点

- shift(1) 向下移一格，shift(-1) 向上移
- 首行移位后为空，对应无上期
- 多分组数据要先 groupby 再在组内 shift
- 常配合 astype(float) 处理空值类型

## 边界与易混淆

整列 shift 会跨组错位，多城市/多分组时必须组内使用。

## 关联

- [[环比]] — 组合使用
- [[groupby]] — 组合使用

## 自测

多城市数据直接对整列 shift(1) 会出什么问题？::会把上海 1 月与北京 12 月错误对应，产生跨城市的假环比。


### 补充 · 2026-11-17

shift() 默认向下移动一行，原第一行位置变为 NaN。在环比中用它构造“上期金额”，再用本期减 shift 后的上期。多城市计算时需先分组，在组内 shift 才不会串城市。

- 默认 periods=1，向下移动一行
- 移动后首行出现 NaN，表示没有上期
- 多组数据先 groupby 再 shift，避免串组
多城市数据直接对整个表 shift 会有什么问题？::可能把上一个城市的最后一行当成下一个城市的第一行上期，导致串组。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p46 S02E31.数据的转置、计算环比与同比](https://www.bilibili.com/video/BV1ji4y157uB?p=46) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
