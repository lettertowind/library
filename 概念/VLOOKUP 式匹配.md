---
term: VLOOKUP 式匹配
aliases: [VLOOKUP, Excel 查找匹配, 纵向查找]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 44
stage: "S02E29 · vlookup"
---

# VLOOKUP 式匹配

> 别名：VLOOKUP、Excel 查找匹配、纵向查找

**用 merge 左连接从另一张表按关键列取回目标字段，等价 Excel 的 VLOOKUP。**

## 用法
**语法**：`pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, suffixes=('_x', '_y'))`
**参数**：
- `left` / `right`：左表（主表）与右表（查找表），通常是 DataFrame
- `how`：连接方式，做 VLOOKUP 式匹配时固定用 `'left'`，保证主表行一条不少
- `on`：两表同名的连接键列名，如 `on='学号'`
- `left_on` / `right_on`：两表键名不同时分别指定，如 `left_on='学号', right_on='ID'`
- `suffixes`：两表出现同名列时自动加的后缀，默认 `('_x', '_y')`
**示例**：
```python
import pandas as pd

students = pd.DataFrame({'学号': [101, 102, 103], '姓名': ['张三', '李四', '王五']})
scores = pd.DataFrame({'学号': [101, 102], '总分': [590, 610], '班级': ['一班', '二班']})

# 右表只取关键列 + 目标列，再左连接
result = students.merge(scores.loc[:, ['学号', '总分']], on='学号', how='left')
print(result)
#    学号  姓名    总分
# 0  101  张三  590.0
# 1  102  李四  610.0
# 2  103  王五    NaN   <- 右表没匹配到，填空值
```

## 解释

Excel 的 VLOOKUP 按关键列在另一张表查找并返回指定列的值。Pandas 中通过 merge 左连接实现：主表保留全部行，右表只取关键列和目标列，按关键列连接。

## 有什么用

- 跨工作表/跨表补全字段
- 用一张表的数据给另一张表打标签

## 关键要点

- 右表先用 loc[:, ['键','目标列']] 只取需要的列，避免带入无关字段
- how='left' 保证主表记录一条不少
- on='键列' 指定连接键，两表键名不同时用 left_on/right_on
- 匹配结果列默认追加在最后，需要移动时用 insert

## 边界与易混淆

VLOOKUP 只能向右查找且默认近似匹配；merge 无方向限制，但需注意键重复导致的多对多展开。

## 关联

- [[DataFrame 合并]] — 上位概念
- [[how 参数]] — 组合使用
- [[on 参数]] — 组合使用
- [[loc]] — 组合使用

## 自测

为什么右表要先 loc[:, ['学号','总分']] 再 merge，而不是整表连接？::避免把右表无关列全部带入结果，减少冗余字段和列名冲突。
如果主表有而右表没有的学号，how='left' 后该行总分是什么？::NaN，因为左连接保留主表全部行，匹配不到就填空值。


### 补充 · 2026-11-17

Excel 里用 VLOOKUP 干这件事，Pandas 里的标准做法是 pd.merge：左表给基准，右表只留「键 + 目标列」，how='left' 保证左表记录一条不丢。整条链路是：读两张表 → 裁剪右表 → merge → 调整列位置 → 写回。掌握这条链路后，换任何两张表、任何目标列都是同样的写法。

- 核心不是记住函数，而是「按连接键取列」这个套路
- how='left' 才能像 VLOOKUP 一样保留左表全部记录
- 右表目标列用 loc[:, ['键','目标列']] 只取需要的
用 merge 复刻 VLOOKUP 时，how 该选哪个值？为什么？::选 'left'，因为 VLOOKUP 以左表为基准，左表每一行都要保留，右表没有匹配就填 NaN。
如果目标列在右表里位于连接键左边，merge 还能取到吗？::能，merge 不关心列的左右位置，只看连接键，这是它比 VLOOKUP 强的地方。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p44 S02E29.vlookup](https://www.bilibili.com/video/BV1ji4y157uB?p=44) · 2026-11-17

Excel 的 VLOOKUP 在主表每行按关键字去查找表取一列值；pandas 里等价的写法是对多端左表做 how='left' 的 merge，一次带回多个字段，且不受查找列位置限制。

- 对应的就是 left join：主表为左表，查找表为右表
- merge 可一次带回多列，VLOOKUP 每次只能取一列
- 查找表缺键时结果是 NaN，对应 VLOOKUP 的 #N/A
用 VLOOKUP 时查找表有重复键会怎样，换成 merge 左连接呢？::VLOOKUP 只返回第一条匹配；merge 左连接会把每一行匹配都展开，主表行数因此增加。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p22 S02E07.连接查询之Merge](https://www.bilibili.com/video/BV1ji4y157uB?p=22) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
