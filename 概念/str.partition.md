---
term: str.partition
aliases: [partition, 三分拆分]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.partition

> 别名：partition、三分拆分

**按第一个分隔符把字符串拆成“前、分隔符、后”三部分的方法。**


## 用法
**语法**：`s.str.partition(pat, expand=True)`

**参数**：
- `pat`：分隔符字符串，只按第一个匹配处分割
- `expand`：默认 `True` 返回三列 DataFrame（左段、分隔符、右段）；`False` 返回三元素元组 Series

**示例**：
```python
import pandas as pd

s = pd.Series(["a-b-c", "hello", "x-y"])
print(s.str.partition("-"))
#     0  1     2
# 0   a  -   b-c
# 1  hello
# 2   x  -     y

print(s.str.rpartition("-"))     # 从右往左找分隔符
```

## 解释

str.partition 固定返回三个部分：分隔符之前的内容、分隔符本身、分隔符之后的内容。与 split 不同，它保留分隔符，且只按第一个分隔符分割。

## 有什么用

- 需要保留分隔符本身时
- 把字符串拆成前缀、标记、后缀三段

## 关键要点

- 固定返回三部分，保留分隔符
- 只按第一个分隔符分割
- 分隔符不存在时返回原字符串和两个空串
- rpartition 从右向左查找分隔符

## 边界与易混淆

多个分隔符时只处理第一个；找不到分隔符不会报错，而是返回原串加两个空值。

## 关联

- [[str.split]] — 对比项
- [[str.rsplit]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

str.partition 和 str.split 对分隔符的处理有什么本质区别？::partition 保留分隔符作为中间部分，split 不保留分隔符。
字符串中有多个分隔符时 partition 怎么处理？::只按第一个分隔符分割，其余部分整体归入第三部分。


### 补充 · 2026-11-17

与 split 最大区别是保留分隔符本身，且即使有多个分隔符也只按第一个切一次，剩余内容整段放进第三部分。找不到分隔符时第三部分为空，首段即原串。

- 固定返回三段：分隔符前、分隔符本身、分隔符后
- 多个分隔符时只按第一个分割，后续不再继续拆
- 找不到分隔符时：首段为原串，后两段为空
字符串里有多个 b，str.partition('b') 会切成几段？后面那些 b 去哪了？::切成三段；第一个 b 之后的所有内容（含后续 b）整体放进第三段
partition 找不到指定字符时，三段分别是什么？::原字符串、空、空
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
