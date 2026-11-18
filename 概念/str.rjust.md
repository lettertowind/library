---
term: str.rjust
aliases: [rjust, 右侧对齐左侧填充]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# str.rjust

> 别名：rjust、右侧对齐左侧填充

**把字符串右对齐、在左侧补齐到指定宽度。**

## 用法
**语法**：`Series.str.rjust(width, fillchar=' ')`
**参数**：
- `width`：目标最小宽度（int）。如果原字符串长度已经达到或超过它，就原样返回，不会截断
- `fillchar`：填充字符，只能是一个字符，默认是空格 `' '`；它会被加在左侧，效果等同于 `str.pad(width, side='left')`
- 缺失值 `NaN` 原样保留，不会参与填充
**示例**：
```python
import pandas as pd

s = pd.Series(['7', '42', '2020'])
print(s.str.rjust(6, '0').tolist())
# ['000007', '000042', '002020']

# 不写 fillchar 时用空格填充，等价于 str.pad(6, side='left')
print(s.str.rjust(6).tolist())
# ['     7', '    42', '  2020']

print(s.str.rjust(2).tolist())   # 已够宽，原样返回
# [' 7', '42', '2020']
```

## 解释

rjust 等价于 pad(..., side='left')：内容靠右，填充加在左边。这是 pad 的默认方向，所以平时直接用 pad 不写 side 效果相同。常用于数字/编号对齐。

## 关键要点

- rjust(width, fillchar='*')，无需写 side
- 内容靠右，填充加在左侧
- 等价于 pad(..., side='left')，即 pad 默认行为
- 填充字符只能是单个字符

## 边界与易混淆

只补 0 时用 zfill 更直接；rjust 的 r 表示 right 对齐，不是「右边填充」，容易记反。

## 关联

- [[str.pad]] — 上位概念
- [[str.ljust]] — 对比项
- [[str.zfill]] — 对比项

## 自测

rjust 的填充字符加在左边还是右边？为什么？::加在左边，因为它是右对齐，内容靠右，剩余空间留在左侧

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
