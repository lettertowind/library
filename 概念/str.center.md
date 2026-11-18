---
term: str.center
aliases: [center, 两端填充]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# str.center

> 别名：center、两端填充

**把字符串两端补到指定宽度，等价于 pad(side='both')。**

## 用法
**语法**：`Series.str.center(width, fillchar=' ')`
**参数**：
- `width`：补齐后的总宽度（int）；小于原字符串长度时保持原串不变
- `fillchar`：填充字符，只能是单个字符，默认空格 `' '`
**示例**：
```python
import pandas as pd

s = pd.Series(['ab', 'abcd', 'x'])
print(s.str.center(6).tolist())
# ['  ab  ', ' abcd ', '  x   ']
print(s.str.center(6, fillchar='*').tolist())
# ['**ab**', '*abcd*', '**x***']
print(s.str.center(2).tolist())   # 宽度不足时原样返回
# ['ab', 'abcd', 'x']
```
左右补数不平衡时，优先补在左侧，即左少右多；功能等价于 `str.pad(width, side='both', fillchar=...)`。

## 解释

center 只接受宽度和填充字符两个参数，不用再写 side，直接两端补齐。左右补几个自动平衡，通常先左后右。适合让文本在定宽展示中对齐美观。

## 关键要点

- 参数为 center(width, fillchar='*')，省去 side 设置
- fillchar 只能是单个字符，默认空格
- 左右补数不平衡时优先补左侧
- 宽度小于原字符串长度时保持原串不变

## 边界与易混淆

功能已被 pad(side='both') 覆盖，记不住时用 pad 即可。

## 关联

- [[str.pad]] — 上位概念
- [[str.ljust]] — 对比项
- [[str.rjust]] — 对比项

## 自测

pad(5, side='both', fillchar='*') 和哪个方法等价？::str.center(5, fillchar='*')

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
