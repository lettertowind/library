---
term: map
aliases: [Series.map, 映射方法]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 45
stage: "S02E30 · 数据处理的三板斧"
---

# map

> 别名：Series.map、映射方法

**对 Series 每个元素按字典或函数做一对一映射，返回同长度新 Series。**

## 用法
**语法**：`Series.map(arg, na_action=None)`
**参数**：
- `arg`：字典（键为原值）或单参数函数，也可是 Series；按原值查找映射
- `na_action`：`None`（默认，NaN 也传入）或 `'ignore'`（跳过 NaN，保留缺失）
**示例**：
```python
import pandas as pd

s = pd.Series(['男', '女', '男', '未知'])
print(s.map({'男': '先生', '女': '女士'}).tolist())
# ['先生', '女士', '先生', nan]

grade = pd.Series([60, 75, 90])
print(grade.map(lambda x: x + 5).tolist())
# [65, 80, 95]
```

## 解释

map 是 Series 专属方法，把整列的每个值逐个传入字典或函数，得到映射后的新值并按原位置返回。适合分类转换、编码替换等整列统一处理。

## 有什么用

- 把性别列男/女映射为先生/女士
- 用字典把编码列翻译成中文标签
- 对整列套用简单单参数函数

## 关键要点

- 只作用于 Series，不能直接对 DataFrame 调用
- 可接收字典（键为原值）或函数（单参数）
- 映射不到的值返回 NaN，需注意缺失
- 单参数场景优先用 map，多参数改用 apply
- 赋值回原列即覆盖修改，赋给新列则保留原值

## 边界与易混淆

与 replace 易混：map 是整列逐值映射，replace 是表内具体值替换；map 不支持多参数。

## 关联

- [[Series]] — 上位概念
- [[apply]] — 对比项
- [[replace]] — 对比项

## 自测

性别列用字典 map 后出现 NaN，最可能的原因是什么？::原列中存在字典里没有的键，映射不到就返回 NaN。
要给整列成绩统一加 5 分，用 map 还是 apply 更合适？为什么？::单参数可用 map；若函数还需第二个参数（误差值），则必须用 apply 的 args 传参。


### 补充 · 2026-11-17

map 只作用于单列，值逐个作为参数交给字典查找或函数计算，结果按原行位置对齐返回。它是把一列编码值翻译成另一种表述的最省事写法，也可直接覆盖原列。

- 可接收字典：df["性别"].map({ "男": "先生", "女": "女士"})
- 可接收函数或 lambda，函数必须有 return
- 结果可赋给新列，也可写回原列覆盖（保留最后一次赋值）
df["性别"].map(dic) 中 dic 里没出现过的取值会变成什么？::变成 NaN，因为字典查不到对应键
同一个需求既能用 map 也能用 replace，怎么判断用哪个？::针对一整列的映射转换用 map；针对表里某个具体值的批量替换用 replace
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p45 S02E30.数据处理的三板斧](https://www.bilibili.com/video/BV1ji4y157uB?p=45) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
