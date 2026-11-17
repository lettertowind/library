---
term: index rindex
aliases: [str.index, str.rindex]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
---

# index rindex

> 别名：str.index、str.rindex

**与 find 类似但找不到目标时会抛出异常的查找方法。**


## 用法
**语法**：`str.index(sub[, start[, end]])` / `str.rindex(sub[, start[, end]])`

**参数**：
- `sub`：要查找的子串，必填
- `start`：查找起始位置，可选，默认为 0
- `end`：查找结束位置（不含），可选，默认为字符串末尾
- 返回值：子串首次出现的下标（rindex 为最后一次出现）；找不到时抛 `ValueError`
- 与 `find`/`rfind` 的唯一差异：找不到时 `index`/`rindex` 报错，`find`/`rfind` 返回 `-1`。数据可能缺失时优先用 `find`

**示例**：
```python
import pandas as pd

s = pd.Series(['a-b-c', 'x-y', 'no-dash-here'])

# 子串必定存在时，用 index 直接定位，缺失即报错
print(s[0].index('-'))        # 1
print(s[0].rindex('-'))       # 3
print(s[1].index('-'))        # 1

# 严格校验：任一元素缺失分隔符就抛出 ValueError
try:
    s.str.index('-')
except ValueError as e:
    print('ValueError:', e)   # ValueError: substring not found
```

## 解释

index 从左往右、rindex 从右往左查找子串位置。与 find 的唯一关键差异是找不到时报错而非返回 -1，适合'必须存在'的断言场景。

## 有什么用

- 确定子串一定存在时定位位置
- 需要失败即报错的校验

## 关键要点

- index 从左往右，rindex 从右往左
- 找不到时抛异常
- 与 find/rfind 形成容错与严格的对比

## 边界与易混淆

数据脏、可能缺失时用 find 更安全。

## 关联

- [[find rfind]] — 对比项

## 自测

什么场景下应优先用 index 而不是 find？::当子串必须存在、希望缺失时立即报错暴露问题时。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
