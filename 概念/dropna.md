---
term: dropna
aliases: [df.dropna, 删除缺失值, 丢弃空值行, 删除空值行列]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-23
updated: 2026-11-23
order: 31
stage: "S02E16 · 处理缺失值"
---

# dropna

> 别名：df.dropna、删除缺失值、丢弃空值行

**把含缺失值的行或列整条删掉，是缺失值处理里「不补、直接丢」的那条路。**

## 用法

**语法**：

```python
DataFrame.dropna(*, axis=0, how=<默认 'any'>, thresh=None, subset=None, inplace=False, ignore_index=False)
```

Series 也可用 `s.dropna()`，没有 `axis`/`subset` 参数。

**参数**：
- `axis`：`0`/`'index'`（默认，删行）或 `1`/`'columns'`（删列）
- `how`：`'any'`（默认，有一个缺失就删）或 `'all'`（整行/整列全空才删）
- `thresh`：保留非空值个数 ≥ 该值的行/列，优先级高于 `how`
- `subset`：只看指定列是否缺失，其他列的缺失不影响判断
- `inplace`：默认 `False` 返回新对象，`True` 原地修改
- `ignore_index`：删完后重排索引为 0,1,2…

**示例**：

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "姓名": ["张三", "李四", "王五", "赵六"],
    "语文": [90, np.nan, np.nan, 85],
    "数学": [88, 92, np.nan, np.nan],
})
print(df)
#    姓名    语文    数学
# 0  张三  90.0  88.0
# 1  李四   NaN  92.0
# 2  王五   NaN   NaN
# 3  赵六  85.0   NaN

print(df.dropna())               # 默认 how='any'：只要有一个空值就删行
#    姓名    语文    数学
# 0  张三  90.0  88.0          ← 只剩完整的一行

print(df.dropna(how="all"))      # 整行全空才删（王五姓名非空，所以一行都没删）
#    姓名    语文    数学
# 0  张三  90.0  88.0
# 1  李四   NaN  92.0
# 2  王五   NaN   NaN
# 3  赵六  85.0   NaN

print(df.dropna(subset=["语文"]))   # 只看语文列是否缺失
#    姓名    语文    数学
# 0  张三  90.0  88.0
# 3  赵六  85.0   NaN

print(df.dropna(thresh=2))       # 至少 2 个非空值才保留
#    姓名    语文    数学
# 0  张三  90.0  88.0
# 1  李四   NaN  92.0
# 3  赵六  85.0   NaN

print(df.dropna(axis=1))         # 按列删：语文、数学都有空值，只剩姓名
#    姓名
# 0  张三
# 1  李四
# 2  王五
# 3  赵六
```

## 解释

`dropna` 逐行（或逐列）检查 NaN，满足删除条件就整条丢弃。默认条件是「任一位置为空」（`how='any'`），所以最严格；真要宽松些就换 `how='all'`、用 `subset` 限定检查范围，或用 `thresh` 按有效值数量放行。它和 `fillna` 是互补的两条路：一个丢、一个补。

## 有什么用

- 缺失比例极低、且缺失本身无意义时，直接删比乱补更安全
- 分析前先剔除关键字段缺失的记录，避免后续统计被污染
- 清洗宽表时按列剔除整列都不可用的字段

## 关键要点

- 默认 `how='any'` 最严格，稍不留神就删掉大半数据
- `thresh` 与 `how` 同时给时，`thresh` 生效
- `subset` 只决定「看哪些列判断」，不改变 `how` 的语义
- 默认返回新对象，原表不动；要原地改加 `inplace=True`
- 删完索引会留空档，用 `ignore_index=True` 重排
- 删除是不可逆的，删前先用 `isnull().sum()` 看看会删多少

## 边界与易混淆

和 `fillna` 方向相反：`fillna` 补值保留数据量，`dropna` 删行牺牲样本量。数据量小、缺失分散时用 `dropna` 容易把有效样本删干净，这时应优先考虑填充。

注意 `pivot_table` 里也有一个叫 `dropna` 的**参数**，含义是「是否丢弃全空的分组列」，与这里的 `dropna()` **方法**不是一回事，别混淆。

## 关联

- [[fillna]] — 对比项：填充而非删除
- [[how 参数（dropna）]] — 删除条件：any / all
- [[subset 参数（dropna）]] — 限定判断范围
- [[thresh 参数]] — 按非空值个数阈值保留
- [[isnull]] — 删除前先统计缺失分布
- [[NaN]] — 处理对象
- [[缺失值处理]] — 上位主题
- [[dropna 参数（透视表）]] — 易混淆：同名但是参数

## 自测

`df.dropna()` 默认会删掉哪些行？::任何一个单元格为 NaN 的行（`how='any'`），要求整行完全没有缺失才留下。

想只在「成绩列缺失」时才删行，其他列缺失不管，用哪个参数？::`subset=['成绩']`，它把判断范围限定在指定列上。

`dropna(thresh=2)` 和 `dropna(how='all')` 有什么区别？::thresh 按非空值个数放行（≥2 个非空才保留），how='all' 只在整行全空时才删，前者更严格。

删完行后索引出现 0、3 这样的空档，怎么让它重新连续？::加 `ignore_index=True`，结果索引会重排为 0,1,2…

## 出处

- 孙兴华《Python 数据分析三部曲》p31 · S02E16 处理缺失值（B站）· https://www.bilibili.com/video/BV1ji4y157uB?p=31 · 2026-11-17
