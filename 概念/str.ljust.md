---
term: str.ljust
aliases: [ljust, 左侧对齐右侧填充]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# str.ljust

> 别名：ljust、左侧对齐右侧填充

**把字符串左对齐、在右侧补齐到指定宽度。**

## 用法
**语法**：`Series.str.ljust(width, fillchar=' ')`
**参数**：
- `width`：目标总宽度（按字符数计），小于原字符串长度时原样返回、不截断
- `fillchar`：填充字符，默认空格 `' '`，只能是单个字符，填充加在右侧
**示例**：
```python
import pandas as pd

s = pd.Series(['ab', 'python', '数据分析'])
print(s.str.ljust(8, fillchar='*'))
# 0    ab******
# 1    python**
# 2    数据分析****
# dtype: object
```
等价写法（课程中的 pad 形式）：`s.str.pad(8, side='right', fillchar='*')`；若只需补 0 到定宽、左侧填充，用 `s.str.zfill(8)` 更直接。

## 解释

ljust 是 pad 的衍生写法，等价于 pad(..., side='right')：内容靠左，空白（或指定字符）加在右边。常用于生成定宽编码、对齐报表输出。

## 关键要点

- ljust(width, fillchar='*')，无需写 side
- 内容靠左，填充加在右侧
- 等价于 pad(..., side='right')
- 填充字符只能是单个字符

## 边界与易混淆

只补 0 且固定左填时用 zfill；任意方向任意字符用 pad。

## 关联

- [[str.pad]] — 上位概念
- [[str.rjust]] — 对比项

## 自测

要让姓名靠左、星号补在右边到 5 位，用 pad 和用 ljust 分别怎么写？::pad(5, side='right', fillchar='*')；ljust(5, fillchar='*')

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
