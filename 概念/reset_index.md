---
term: reset_index
aliases: [df.reset_index, 重置索引]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
---

# reset_index

> 别名：df.reset_index、重置索引

**将 DataFrame 索引重置为默认 0,1,2… 的方法。**

## 用法
**语法**：`DataFrame.reset_index(drop=False, inplace=False)`
**参数**：
- `drop`：布尔值，默认 `False`；`True` 时丢弃原索引，只保留新的 0,1,2… 默认索引；`False` 时把原索引降为普通列插入最前面
- `inplace`：布尔值，默认 `False`；`True` 时原地修改原 DataFrame 并返回 `None`，`False` 时返回新对象
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'城市': ['北京', '上海', '广州'], '销量': [120, 95, 88]})
df = df.set_index('城市')          # 先把「城市」设为索引，制造非默认索引
print(df)
#       销量
# 城市
# 北京   120
# 上海    95
# 广州    88

print(df.reset_index(drop=True))   # drop=True：原索引丢弃，只剩默认序号
#    销量
# 0  120
# 1   95
# 2   88

print(df.reset_index(drop=False))  # drop=False（默认）：原索引降为普通列
#    城市   销量
# 0  北京  120
# 1  上海   95
# 2  广州   88

print(df.reset_index().shape, df.reset_index(drop=True).shape)  # 多一列，注意列数变化
# (3, 2) (3, 1)
```

## 解释

reset_index() 生成新的默认整数索引，关键参数 drop 决定原索引的去留：drop=True 直接丢弃原索引，drop=False 把原索引降为普通列保留下来。

## 有什么用

- 索引混乱时恢复默认序号
- 把原索引当普通列保留分析

## 关键要点

- drop=True：删除原索引
- drop=False：原索引转为普通列
- 默认 drop=False
- 常与 set_index 配对使用

## 边界与易混淆

drop=False 会多出一列，可能影响后续列数统计；与 set_index 方向相反，勿混。

## 关联

- [[set_index]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

reset_index(drop=True) 和 drop=False 的结果差在哪？::drop=True 丢弃原索引只留新默认索引；drop=False 把原索引保留为普通列。
什么情况下你会选 drop=False？::当原索引本身有信息价值、需要作为一列继续参与分析时。


### 补充 · 2026-11-17

reset_index 处理的是原来那套索引怎么办：drop=True 直接丢掉旧索引，drop=False（默认）把旧索引降级成一个普通列留在表里。两种方式都会得到一个全新的 RangeIndex。

- drop=True：删除旧索引，只留默认整数索引
- drop=False：旧索引变成普通列，同时生成默认索引
- 默认返回新对象，加 inplace=True 才改原表
reset_index(drop=False) 之后，原来的索引去哪了？::变成一个普通数据列保留在表中，同时表获得新的 0 起始默认索引
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p21 S02E06.数据结构之DataFrame](https://www.bilibili.com/video/BV1ji4y157uB?p=21) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
