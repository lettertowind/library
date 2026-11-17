---
term: level 参数（groupby）
aliases: [level, 按索引层级分组, groupby(level=...)]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
---

# level 参数（groupby）

> 别名：level、按索引层级分组、groupby(level=...)

**groupby 中 level 指定按多层索引的某一层级分组，而非按列值分组。**

## 用法
**语法**：`DataFrame.groupby(level=None, axis=0)` / `DataFrame.groupby(level='层名')[列子集].聚合函数()`
**参数**：
- `level`：索引层级名（字符串）或层级位置编号（整数），也可传列表按多层分组；只认索引层级，不认普通列名
- `axis`：分组方向，`0`（默认）按行索引分组；按列层级汇总在 pandas 2.x 中写 `df.T.groupby(level=...)`（旧版 `axis=1` 已废弃）
**示例**：
```python
import pandas as pd

df = pd.DataFrame({
    '班级': ['一班', '一班', '二班', '二班'],
    '性别': ['男', '女', '男', '女'],
    '语文': [90, 85, 78, 92],
    '数学': [88, 95, 80, 86],
})
df = df.set_index(['班级', '性别'])          # 先提升为索引层级

print(df.groupby(level='班级')[['语文', '数学']].median())
#       语文    数学
# 班级
# 一班  87.5  91.5
# 二班  85.0  83.0

print(df.T.groupby(level=0).median())        # 按列层级汇总，等价旧版 axis=1
#        (一班, 男)  (一班, 女)  (二班, 男)  (二班, 女)
# 语文        90        85        78        92
```
注意：若「班级」仍是普通列，`groupby(level='班级')` 会报错，需先 `set_index` 或改用 `groupby('班级')`；整表聚合时剩余列须全为数值。

## 解释

当「班级」「性别」已被 set_index 提升为索引层级后，用 level='班级' 即可按班级聚合，无需再引用列名。它让分组键与索引结构解耦，是多层索引数据分析的关键写法。

## 有什么用

- 按多层索引的某一层汇总
- 配合 axis=1 按列层级汇总季度
- 避免重复把索引层还原成列

## 关键要点

- 必须先用 set_index 把分组列提升为索引层级
- 写法：df.groupby(level='班级').median()
- 可显式选列：groupby(level='班级')[['语文','数学']].median()
- 未设索引直接用 level 会报错或结果异常
- 整体聚合时所有剩余列必须是数值列

## 边界与易混淆

level 只认索引层级名，不认普通列名；若分组列还在列里，需先 set_index 或改用列名分组。

## 关联

- [[分层索引]] — 前置知识
- [[set_index]] — 前置知识
- [[groupby]] — 组合使用

## 自测

df 中「班级」还是普通列，能直接 groupby(level='班级') 吗？::不能，需先 set_index(['班级','性别']) 把它提升为索引层级。
level 分组出错时首先该检查什么？::索引是否已正确设置、参与聚合的列是否都是数值列。


### 补充 · 2026-11-17

当分组字段本身就是索引（或索引的一层）时，用 level 指定层级名或序号即可分组。常见于 set_index 之后，或对多层列索引按列层级聚合。

- 使用前必须先用 set_index 把该字段设为索引
- 写法：数据.set_index(["班级","性别"]); 数据.groupby(level="班级").median()
- 多层列索引按列层级聚合：数据.groupby(level="季度", axis=1).sum()
直接对未设为索引的“班级”列写 groupby(level="班级") 会怎样？::报错，索引中没有名为“班级”的层级；需要先 set_index(["班级"])。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p41 S02E26.分组与聚合 groupby基础部分](https://www.bilibili.com/video/BV1ji4y157uB?p=41) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
