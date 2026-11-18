---
term: pd.cut
aliases: [cut, 按值分箱, 指定分界点分箱]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 37
stage: "S02E22 · 离散化和分箱"
---

# pd.cut

> 别名：cut、按值分箱、指定分界点分箱

**按指定的分界点或区间把连续一维数据分箱。**


## 用法
**语法**：`pd.cut(x, bins, right=True, labels=None, retbins=False, include_lowest=False)`
**参数**：
- `x`：一维类数组（列表或 Series），不能直接传入整张表，需先用 `df['某列']` 取出。
- `bins`：分界点列表，如 `[1900, 1950, 2000]` 形成两个箱；也可传入整数，表示等宽箱数。
- `right`：默认 `True`，区间右闭，即 `(a, b]`；设为 `False` 则为左闭右开。
- `labels`：箱子名称列表，长度必须等于箱数；传 `False` 返回从 0 开始的整数箱号。
- `retbins`：默认 `False`；设为 `True` 时返回 `(分箱结果, 分界点数组)` 元组。
- `include_lowest`：默认 `False`，设为 `True` 时最左区间包含左端点。
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'year': [1922, 1965, 1999, 2001]})
print(pd.cut(df['year'], bins=[1900, 1950, 2000], labels=['早期', '近期']).tolist())
# ['早期', '近期', '近期', nan]   2001 超出分界点范围成 NaN
print(pd.cut(df['year'], bins=[1900, 1950, 2000], labels=False).tolist())
# [0.0, 1.0, 1.0, nan]   labels=False 即整数箱号
print(pd.cut(df['year'], bins=[1900, 1950, 2000], include_lowest=True, retbins=True)[1].tolist())
# [1900.0, 1950.0, 2000.0]   retbins 取回分界点
```

## 解释

cut 接收一维数据和 bins 分界点列表，把每个值归入对应区间。适合有明确业务边界的场景，如 1950 年前后、分数段评级。

## 有什么用

- 按业务边界划分区间
- 把连续分数转为等级标签

## 关键要点

- 第一个参数 x 必须是一维类数组
- bins 传分界点列表，如 [1900, 1950, 2000] 形成两个箱子
- 默认区间右闭，如 (1900,1950]、(1950,2000]
- labels=False 返回从 0 开始的整数箱号
- labels=名称列表 可给箱子设置业务名称，长度须与箱数一致

## 边界与易混淆

分界点需覆盖数据范围，否则边界外的值会成为 NaN；视频口述的 levels 实为 labels。

## 关联

- [[离散化与分箱]] — 上位概念
- [[pd.qcut]] — 对比项
- [[value_counts]] — 组合使用

## 自测

bins=[1900,1950,2000] 时，年份 1922 落在哪个箱、箱号是多少？::落在 (1900,1950] 区间，箱号为 0。
cut 中 labels=False 与 labels=名称列表 的区别是什么？::labels=False 返回整数箱号；labels=列表 用业务名称替换区间显示。


### 补充 · 2026-11-17

cut 接收一个 Series 和一串分界点，把每个数值归入相应区间，返回每个值所属箱子的区间名。它适合业务阈值已经明确的场景，例如 1950 年前/后、0~15 岁/16~30 岁。结果可再用 value_counts 统计各箱数量。

- 第一个参数必须是一维 Series，不能传整表
- 分界点要用业务逻辑确定，示例中的 1900/1950 只是演示
- 箱子按下标从 0 编号，0 号箱对应第一段区间
把年龄列切成 0~15、16~30、31~45、45 以上四段，为什么不能直接写 pd.cut(df, [...])？::cut 只处理一维数据，df 是二维表，必须先取 df['年龄'] 得到 Series 再分箱。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p37 S02E22.离散化和分箱](https://www.bilibili.com/video/BV1ji4y157uB?p=37) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
