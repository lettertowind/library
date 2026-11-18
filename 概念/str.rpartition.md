---
term: str.rpartition
aliases: [rpartition, 从右三分拆分]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# str.rpartition

> 别名：rpartition、从右三分拆分

**从右往左找分隔符，按最后一个分隔符把字符串切成三段。**

## 用法
**语法**：`Series.str.rpartition(pat=' ', expand=True)`
**参数**：
- `pat`：分隔符，默认空格；只从右往左找**最后一个**匹配切一次，找不到时返回 `(原串, '', '')`
- `expand`：默认 `True` 返回三列 DataFrame（前段、分隔符、后段）；设为 `False` 返回元素为三元组的 Series

**示例**：
```python
import pandas as pd

s = pd.Series(['report.final.csv', 'a.b.c', 'no_sep'])

# 默认 expand=True：返回三列 DataFrame，分隔符单独占一列
print(s.str.rpartition('.').values.tolist())
# [['report.final', '.', 'csv'], ['a.b', '.', 'c'], ['no_sep', '', '']]

# 实际常用：直接取最后一段（取文件名、取 @ 后域名）
print(s.str.rpartition('.').iloc[:, 2].tolist())
# ['csv', 'c', '']

# expand=False：返回元组 Series，便于自己解包
print(s.str.rpartition('.', expand=False).tolist())
# [('report.final', '.', 'csv'), ('a.b', '.', 'c'), ('no_sep', '', '')]
```

## 解释

rpartition 与 partition 结构相同、方向相反：partition 从左找第一个分隔符，rpartition 从右找最后一个。适合取路径、邮箱、带后缀编码这类「真正想要的是最后一段」的场景。

## 有什么用

- 按最后一个分隔符拆分，如取路径最后一段、取 @ 后的域名

## 关键要点

- 同样保留分隔符，返回前段、分隔符、后段三段
- 只按最后一个分隔符切一次，前面的分隔符留在第一段
- 找不到分隔符时首段为原串，后两段为空
- 名字里的 r 表示 right，与 rsplit 的 r 含义一致

## 边界与易混淆

与 rsplit 不同：rpartition 只切一次且保留分隔符，rsplit 可全部拆开且丢弃分隔符。

## 关联

- [[str.partition]] — 对比项
- [[str.rsplit]] — 对比项

## 自测

字符串 a.b.c，partition('.') 和 rpartition('.') 的第三段分别是什么？::partition 是 'b.c'，rpartition 是 'c'

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17
