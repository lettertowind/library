---
term: groupby.apply
aliases: [分组应用, groupby(...).apply(...)]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 41
stage: "S02E26 · 分组与聚合 groupby基础部分"
---

# groupby.apply

> 别名：分组应用、groupby(...).apply(...)

**按分组对每个子表调用自定义函数并合并结果。**

## 用法
**语法**：`DataFrameGroupBy.apply(func, *args, include_groups=True, **kwargs)`

**参数**：
- `func`：对每个分组子表调用的函数，接收子 DataFrame 并返回标量、Series 或 DataFrame
- `group_keys`：为 True（默认）时结果外层带分组键索引；设 False 可避免多出索引层
- `include_groups`：pandas 2.2 起新增，默认 True 会把分组列一并传入 func；设 False 则剔除分组列，留空会更安全，因为显式写出该参数也有助于避免未来行为变化的提示
- `*args, **kwargs`：原样透传给 `func`

**示例**：
```python
import pandas as pd

df = pd.DataFrame({
    "city": ["北京", "北京", "北京", "上海", "上海", "上海"],
    "month": [1, 2, 3, 1, 2, 3],
    "sales": [100, 120, 150, 200, 180, 220],
})

def mom(g):
    g = g.copy()                    # 先 copy，避免修改原数据告警
    g["环比"] = g["sales"].pct_change().round(3)
    return g

df = df.sort_values(["city", "month"])          # 先排序，保证组内月份有序
res = df.groupby("city", group_keys=False).apply(mom, include_groups=False)
print(res)
#    month  sales     环比
# 0      1    100    NaN
# 1      2    120  0.200
# 2      3    150  0.250
# 3      1    200    NaN
# 4      2    180 -0.100
# 5      3    220  0.222
```

## 解释

当每组需要多步操作（如组内排序后 shift 再算环比）时，用 groupby(...).apply(函数) 把整段逻辑封装进函数，对每个城市独立执行，避免跨组串行。

## 有什么用

- 多城市分别计算环比
- 每组需要多列多步处理的场景

## 关键要点

- 先 sort_values 排序再 groupby，保证组内顺序
- group_keys=False 可避免多出分组索引层
- 函数内先 copy() 避免修改原数据告警
- 适合组内多步逻辑，单步聚合用 agg 更快

## 边界与易混淆

性能低于向量化操作；仅当组内逻辑复杂时才用。

## 关联

- [[shift]] — 组合使用
- [[环比]] — 组合使用

## 自测

为什么多城市算环比要先排序再分组再 apply？::排序保证每个城市内部月份顺序正确，分组保证各城市独立 shift 不串行。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
