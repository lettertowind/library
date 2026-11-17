---
term: pd.concat
aliases: [concat, pandas 连接, 纵向连接]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
order: 24
---

# pd.concat

> 别名：concat、pandas 连接、纵向连接

**pandas 中沿指定轴把多个 DataFrame 拼接成一个的方法。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
