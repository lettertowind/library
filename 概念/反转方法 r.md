---
term: 反转方法 r
aliases: [radd, rsub, rdiv, rpow, r 前缀方法]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 34
stage: "S02E19 · 算数运算与数据对齐"
---

# 反转方法 r

> 别名：radd、rsub、rdiv、rpow、r 前缀方法

**灵活算术方法中带 r 前缀的版本，交换左右操作数顺序。**


## 用法
**语法**：`Series.rsub(other, level=None, fill_value=None, axis=0)`
**参数**：
- `other`：参与运算的标量、Series 或数组；在带 r 前缀的方法里它作为左操作数（被减数、被除数、底数）
- `level`：多层索引下指定对齐的层级，默认 `None`
- `fill_value`：运算前用来补齐缺失值的值，默认 `None` 表示不填充
- `axis`：对齐方向，Series 中默认 `0`
**示例**：
```python
import pandas as pd

s = pd.Series([2, 4, 8])
print(s.rsub(10))   # → 8, 6, 2      （10 - 各自）
print(s.rdiv(16))   # → 8.0, 4.0, 2.0（16 / 各自）
print(s.rpow(2))    # → 4, 16, 256   （2 ** 各自）
print(s.add(10))    # → 12, 14, 18   （加法可交换，r 与否无差别）

t = pd.Series([10, 20], index=[0, 1])
print(t.rsub(s, fill_value=0))  # → -8, -16, 8（对齐后 s - t，索引 2 处补 0）
```

## 解释

add 是左加右，radd 是右加左；div 是左除右，rdiv 是右除左。对加法等交换运算无差别，但对减法、除法、幂次方等非交换运算结果不同。

## 有什么用

- 需要反转操作数顺序时
- 非交换运算中调整被除数/减数位置

## 关键要点

- r 表示 reverse，交换左右操作数
- 对加法、乘法等交换运算无实际影响
- 对减法、除法、幂次方结果不同
- 与 fill_value 可组合使用

## 边界与易混淆

不要误以为 r 是取反或取余，它只是交换操作数顺序。

## 关联

- [[灵活算术方法]] — 上位概念
- [[fill_value 参数]] — 组合使用

## 自测

5 rdiv 3 等价于什么？::等价于 3 / 5，即右操作数除以左操作数。


### 补充 · 2026-11-17

普通方法默认是“调用者在前、参数在后”，加 r 后变成“参数在前、调用者在后”。这是为运算符重载准备的机制，在 a 和 b 地位不对等时决定谁除谁、谁对谁取幂。

- radd/rsub/rmul/rdiv/rfloordiv/rpow 对应六个基本方法
- a.add(b) 是 a+b，a.radd(b) 是 b+a
- 加法、乘法满足交换律，反转后数值不变
a.rdiv(b) 等价于哪个表达式？5 的 rdiv 与 3 得到什么？::等价于 b / a，即 3 / 5 = 0.6。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p34 S02E19.算数运算与数据对齐](https://www.bilibili.com/video/BV1ji4y157uB?p=34) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
