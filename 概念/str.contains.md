---
term: str.contains
aliases: [contains, 包含判断]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 29
stage: "S02E14 · 筛选"
---

# str.contains

> 别名：contains、包含判断

**判断每个字符串是否包含指定内容并返回布尔值的方法。**

## 用法
**语法**：`Series.str.contains(pat, case=True, flags=0, na=None, regex=True)`
**参数**：
- `pat`：要查找的字符序列或正则表达式；默认按正则解释
- `case`：默认 True 区分大小写；设为 False 则忽略大小写
- `flags`：传给正则引擎的标志位，如 `re.IGNORECASE`
- `na`：空值处填什么，默认 None 保留 NaN；常设 `na=False`
- `regex`：默认 True 把 pat 当正则；只想按纯文本匹配时设 False
**示例**：
```python
import pandas as pd

s = pd.Series(['河南省信阳市', '信阳市', '郑州市', None])
print(s.str.contains('信阳市').tolist())
# [True, True, False, nan]

print(s.str.contains('信阳市', na=False).tolist())
# [True, True, False, False]

print(s.str.contains('^信阳市', regex=True).tolist())
# [False, True, False, nan]

df = pd.DataFrame({'地址': s})
print(df[df['地址'].str.contains('信阳市', na=False)])
#           地址
# 0  河南省信阳市
# 1      信阳市
```

## 解释

str.contains('血') 对每个元素判断是否包含指定子串，返回 True 或 False。空值默认返回 NaN，可用 na 参数指定空值结果。

## 有什么用

- 筛选包含关键词的行
- 标记数据中是否出现某内容

## 关键要点

- 返回布尔型结果
- 空值默认返回 NaN
- na 参数可设为 False、True 或自定义值
- 常与布尔索引筛选组合使用

## 边界与易混淆

默认按子串匹配；需要正则匹配时需注意参数设置。

## 关联

- [[布尔索引筛选]] — 组合使用
- [[str.startswith]] — 对比项
- [[正则表达式]] — 前置知识

## 自测

str.contains 遇到空值默认返回什么？::NaN。
如何让空值在 contains 结果中显示为 False？::设置 na=False。


### 补充 · 2026-11-17

contains 用于“包含”匹配，弥补 startswith/endswith 只能匹配首尾的不足。第一个参数可为普通字符串或正则表达式，配合 case 控制大小写。

- 写法：数据['地址'].str.contains('信阳市')
- 参数可为字符串或正则表达式
- 默认区分大小写，case=False 忽略
地址有“河南省信阳市”和“信阳市”两种写法，该用 startswith 还是 contains？::用 contains，因为“河南省信阳市”不以“信阳市”开头。

默认按正则表达式处理，可用于文本包含筛选。支持大小写敏感控制。

- 第一个参数 pat 可以是普通字符串或正则表达式
- case=True 默认大小写敏感，case=False 不敏感
- 默认按正则处理，普通文本含特殊字符需转义
str.contains 默认是否区分大小写？::是，case 默认为 True。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p29 S02E14.筛选](https://www.bilibili.com/video/BV1ji4y157uB?p=29) · 2026-11-17

返回的布尔序列可以直接作为筛选掩码使用，是文本条件过滤的主力方法。参数默认按正则解释，空值位置的取值由 na 参数决定。

- 返回布尔 Series，可直接用于 df[...] 过滤
- case 参数控制是否区分大小写
- na 参数指定空值处返回 True 还是 False
空值行默认会让 contains 报错吗？怎么处理？::不报错，可用 na 参数指定这些位置返回 True 还是 False
contains 与 startswith 的差别在哪？::contains 匹配任意位置，startswith 只匹配开头
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
