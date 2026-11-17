---
term: find rfind
aliases: [str.find, str.rfind, 查找字符位置]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
---

# find rfind

> 别名：str.find、str.rfind、查找字符位置

**返回子串首次出现位置的字符串方法，找不到返回 -1。**

## 用法

**语法**：`Series.str.find(sub, start=0, end=None)` 和 `Series.str.rfind(sub, start=0, end=None)`
**参数**：
- `sub`：要查找的子串
- `start`：开始查找的位置，默认 0（含该位置）
- `end`：结束查找的位置，默认 None 表示一直查到末尾（不含该位置）
- 返回：整数 Series，是子串首次出现的索引；找不到时返回 `-1`，不会报错

**示例**：
```python
import pandas as pd

s = pd.Series(['2020-05-01', '2021-12', 'no-dash'])
print(s.str.find('-').tolist())      # [4, 4, 2]  从左往右，首次出现
print(s.str.rfind('-').tolist())     # [7, 4, 2]  从右往左，最后一次出现
print(s.str.find('-', 5).tolist())   # [7, -1, -1] 从位置 5 起找，找不到返回 -1
print('2020-05-01'.find('-', 5))     # 7  纯字符串用法与 str 方法一致
```

## 解释

find 从左往右查找，rfind 从右往左查找，均可指定起始和结束位置。找不到时返回 -1 而不报错，适合需要容错判断的场景。

## 有什么用

- 定位日期中横杠的位置
- 判断子串是否存在

## 关键要点

- 索引从 0 开始
- 可指定起始/结束位置控制查找范围
- 找不到返回 -1，不报错
- rfind 从右往左找

## 边界与易混淆

与 index/rindex 区别：后者找不到会抛异常。

## 关联

- [[index rindex]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

'2020-05-01' 中 str.find('-', 5) 返回什么？::返回 7，即第二个横杠的位置。
find 找不到目标时返回什么？::返回 -1。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
