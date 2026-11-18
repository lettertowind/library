---
term: keys 参数
aliases: [keys, 层次索引标识, 来源标识]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 24
stage: "S02E09 · 连接查询之concat"
---

# keys 参数

> 别名：keys、层次索引标识、来源标识

**concat 中用于为每个连接对象添加层次索引标签的参数。**

## 解释

keys 参数接收一个列表，列表元素与传入 concat 的对象顺序一一对应，生成外层索引以标识数据来源。添加后可通过外层索引筛选特定来源的数据，也便于后续分组分析。

## 有什么用

- 合并多张表时标识每行数据来自哪张表
- 为后续按来源筛选或分组提供依据

## 关键要点

- keys 列表顺序与传入对象顺序对应
- 生成 MultiIndex 的外层索引
- 可用字典替代 keys 列表，字典 key 作为分组标识
- 便于按来源表筛选数据

## 边界与易混淆

keys 只增加索引层级，不改变数据内容；与 ignore_index=True 同时使用时，keys 仍会保留外层索引。

## 关联

- [[pd.concat]] — 组合使用
- [[分层索引]] — 组合使用

## 自测

pd.concat([df1, df2], keys=['x','y']) 后，如何取出 df2 对应的数据？::使用 loc 按外层索引 'y' 选取，如 result.loc['y']。


### 补充 · 2026-11-17

读取全部 sheet 后得到 dict，数据.keys() 返回所有键（即 sheet 名），再用 list() 转成列表就能遍历，用 数据[名字] 逐个取 DataFrame。

- keys() 返回的是 dict_keys 视图，遍历前常 list() 落成列表
- 合并时也需要配合 concat 的 keys 参数做来源标识，两者别混
- 数据[列标签] 取出的是整张 sheet 的 DataFrame
数据 = pd.read_excel(路径, sheet_name=None) 之后，怎样遍历每个 sheet 的 DataFrame？::for 名 in list(数据.keys()): 表 = 数据[名]，再对 表 做处理或 concat。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并](https://www.bilibili.com/video/BV1ji4y157uB?p=40) · 2026-11-17


### 补充 · 2026-11-17

concat 中为各来源表指定标签，从而在结果里加一层来源索引的参数。

- 键的数量与顺序要和传入表一一对应
- 键可写 x/y/z，也可直接写真实表名或“表一表二”
- 传字典可代替 keys 列表，效果一致且更直观
- 生成的层可用 loc 或 xs 取出某一张表的数据
## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
