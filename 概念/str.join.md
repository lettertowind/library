---
term: str.join
aliases: [join, 字符连接]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.join

> 别名：join、字符连接

**用指定字符连接字符串中每个字符的方法。**

## 用法
**语法**：`Series.str.join(sep)`
**参数**：
- `sep`：str，插入到每个字符串**内部相邻字符之间**的连接符；传 `''` 等于原样返回，传 `None` 会报错

**示例**：
```python
import pandas as pd

s = pd.Series(['满血激活', 'abc'])
print(s.str.join('-').tolist())   # 每个字符之间插入 -
# ['满-血-激-活', 'a-b-c']

print(s.str.join('').tolist())    # 连接符为空 = 原样返回
# ['满血激活', 'abc']

# 与 str.cat 对比：cat 拼接的是多个字符串，join 拆分的是单个字符串
print(s.str.join('|').str.cat(sep=','))   # 先逐字连接，再横向拼接
# 满|血|激|活,a|b|c
```
注：元素为 `NaN` 时结果仍为 `NaN`（不报错）；等价于对每个元素执行 `'-'.join(x)`。

## 解释

str.join(sep) 在字符串的每个字符之间插入指定内容，像用胶水把字符粘起来。与 str.cat 不同，它作用于单个字符串内部的字符之间。

## 有什么用

- 给字符之间插入分隔符
- 格式化输出字符串

## 关键要点

- 作用于字符串内部每个字符之间
- 参数是连接符
- 与 str.cat 的拼接对象不同

## 边界与易混淆

易与 str.cat 混淆：cat 拼接多个字符串，join 连接单个字符串内部的字符。

## 关联

- [[str.cat]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

str.join('a') 对“满血激活”的结果是什么？::“满a血a激a活”，每个字符之间插入 a。
str.join 和 str.cat 的核心区别是什么？::join 连接单个字符串内部的字符，cat 拼接多个字符串或序列。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
