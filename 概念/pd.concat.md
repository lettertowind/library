---
term: pd.concat
aliases: [concat, pandas 连接, 纵向连接]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
---

# pd.concat

> 别名：concat、pandas 连接、纵向连接

**pandas 中沿指定轴把多个 DataFrame 拼接成一个的方法。**

## 用法
**语法**：`pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None)`
**参数**：
- `objs`：待拼接对象的列表或字典，如 `[df1, df2]`，不是两个位置参数
- `axis`：拼接方向，`0` 表示纵向堆叠（默认），`1` 表示横向按行索引对齐
- `join`：索引对齐方式，`'outer'` 保留并集（默认），`'inner'` 只保留交集
- `ignore_index`：为 `True` 时重建 0..n-1 连续索引，默认 `False` 保留原索引
- `keys`：传入列表可为结果增加层次索引，标识每块数据来源
**示例**：
```python
import pandas as pd

df1 = pd.DataFrame({'城市': ['北京', '上海'], '销量': [100, 200]})
df2 = pd.DataFrame({'城市': ['广州', '深圳'], '销量': [300, 400]})

# 纵向堆叠，列名需一致
print(pd.concat([df1, df2], ignore_index=True))
#    城市   销量
# 0  北京  100
# 1  上海  200
# 2  广州  300
# 3  深圳  400

# 横向拼接：行索引对齐，不匹配处填 NaN
df3 = pd.DataFrame({'总计': [300, 600]})
print(pd.concat([df1, df3], axis=1))
#    城市   销量   总计
# 0  北京  100  300.0
# 1  上海  200  600.0

# keys 标识来源
print(pd.concat([df1, df2], keys=['一店', '二店']).loc['一店'])
#    城市   销量
# 0  北京  100
# 1  上海  200
```

注意：如果列名不一致，纵向拼接会产生 NaN 列；如果只需要按键匹配，应改用 `pd.merge`。

## 解释

pd.concat 接收一个 DataFrame 列表，默认按行（axis=0）纵向堆叠，把结构相同的多张表接成一张总表。它是合并多个工作簿、多个工作表的核心操作，配合空表和 for 循环即可实现累积合并。

## 有什么用

- 合并同一文件夹下多个 Excel 工作簿
- 合并同一工作簿中多个 sheet
- 把分批读取的数据累积成一张总表

## 关键要点

- 参数是列表：[表1, 表2]，不是两个位置参数
- 默认 axis=0 纵向堆叠，列名需一致
- 常配合空表 pd.DataFrame() 做累积合并
- ignore_index=True 可重建连续索引

## 边界与易混淆

只做结构拼接，不做按键匹配；按键对齐合并要用 pd.merge。列不一致时会产生 NaN 列。

## 关联

- [[DataFrame]] — 组合使用
- [[pd.read_excel]] — 组合使用

## 自测

要把三个结构相同的表纵向接成一张总表，用 pd.concat 还是 pd.merge？为什么？::用 pd.concat，因为只是按行堆叠、不需要按键匹配；pd.merge 用于按键横向对齐。


### 补充 · 2026-11-17

pd.concat 可按行（axis=0）或按列（axis=1）拼接多个对象。横向拼接时要求行索引对齐，常用于把计算结果（如总计列）追加到原数据旁边。

- axis=1 表示横向拼接，axis=0 表示纵向
- 横向拼接要求行索引对齐
- 列索引结构一致时拼接结果更规整
把总计列拼到原销售表右侧，pd.concat 的 axis 应设为什么？::axis=1，表示横向拼接。

pd.concat 是 Pandas 数据合并的核心工具，通过 axis 参数控制纵向堆叠（axis=0）或横向拼接（axis=1）。它支持 keys、join、ignore_index 等参数，能处理索引对齐、来源标识和缺失值填充。相比 join 方法，concat 参数更丰富、适用范围更广。

- axis=0 纵向首尾相连，axis=1 横向按行索引对齐
- keys 参数可增加层次索引标识数据来源
- join 参数控制对齐方式：inner 交集，outer 并集
pd.concat([df1, df2], axis=1) 时，如果两个 DataFrame 的行索引不完全相同，结果会怎样？::按行索引对齐，不匹配的位置填充 NaN。
concat 的 join='inner' 和 join='outer' 有什么区别？::inner 只保留共同索引（交集），outer 保留所有索引（并集），缺失处填 NaN。

默认 axis=0 做纵向首尾相接（类似 Excel 上下拼表）；axis=1 做横向拼接并按行索引对齐，索引不一致处补 NaN。它按轴工作而非按键匹配，这是与 merge 的根本区别。

- 默认 axis=0，等价于把第二张表放到第一张下面
- axis=1 按行索引对齐，索引不同处补 NaN
- keys 参数加一层来源索引；也可直接传字典，字典键即分组键
pd.concat([s1, s2]) 与 pd.concat([s1, s2], axis=1) 结果差在哪？::前者纵向首尾相接、索引可能重复；后者横向并排、按索引对齐并出现 NaN。
为什么建议写成 frames = [df1, df2, df3]; pd.concat(frames)？::表列表集中在一个变量里，便于后续增删、复用和排查问题。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p24 S02E09.连接查询之concat](https://www.bilibili.com/video/BV1ji4y157uB?p=24) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
