---
term: inplace 参数
aliases: [inplace, inplace=True, 原地修改参数]
kind: concept
domain: Pandas
tags: [概念/concept, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 27
stage: "S02E12 · 数据排序【已修证】"
---

# inplace 参数

> 别名：inplace、inplace=True、原地修改参数

**控制方法是在原对象上直接修改还是返回新对象的布尔参数。**

## 解释

inplace 是 Pandas 多个方法（drop、fillna、reset_index 等）共有的参数。默认 False，方法返回新对象、原数据不变；设为 True 则直接在原对象上修改且返回 None。理解它可避免“删除/填充不生效”的常见困惑。

## 有什么用

- 决定是否原地修改数据
- 避免不必要的对象复制
- 解释操作后原数据为何没变

## 关键要点

- 默认 False：返回新对象，原数据不变
- True：原地修改，方法返回 None
- 只写 df.drop(...) 不赋值也不设 True，操作无效
- print(df.drop(...)) 打印的是新对象，原 df 不变

## 边界与易混淆

inplace=True 会丢失链式调用能力（返回 None），且不利于回溯；数据分析中常倾向返回新对象以保留原始数据。

## 关联

- [[drop]] — 组合使用
- [[fillna]] — 组合使用
- [[reset_index]] — 组合使用

## 自测

df.drop(2, inplace=True) 的返回值是什么？::None。inplace=True 时原地修改，不返回新对象。
为什么说 inplace 参数能解释“删除没生效”？::因为默认 False 时 drop 只返回新对象，若既不赋值也不设 True，原 df 不变，看起来就像没删。


### 补充 · 2026-11-17

inplace=True 时方法直接修改调用对象本身并返回 None；默认 False 时返回新对象、原数据不变。它影响所有替换/填充类操作是否生效，是初学者最常见的踩坑点。

- inplace=True 后方法返回 None，不能用变量接收结果
- 默认 False 时原数据不变，需接收返回值
- 整表替换与单列替换都受此参数影响
df.replace('A','B', inplace=True) 的返回值是什么？::None，因为原地修改不返回新对象。

inplace=True 时直接在原 DataFrame 上修改并返回 None；inplace=False（默认）返回新对象，原数据不变。判断是否改原表看 inplace，而不是看有没有赋值给新变量。

- True 直接改原数据，返回 None
- False 返回新对象，原数据不变
- 即使赋值给新变量，inplace=True 仍会改原表
data2 = data.sort_values(by='语文', inplace=True) 后 data 变了吗？data2 是什么？::data 被修改了；data2 是 None

inplace=False 时方法返回一个新对象，原数据保持不变；inplace=True 时直接在原数据上改动并返回 None。是否设置它，决定了“写了一句删除却没生效”这类问题是否出现。

- 默认 False：返回新对象，原数据不变
- True：原地修改，方法返回 None
- 不接收返回值又不设 True，操作等于白写
为什么说“data.drop(1)”单独一行是无效代码？怎样改成有效？::它返回新对象却没人接收，原数据不变；可改成 data = data.drop(1) 或 data.drop(1, inplace=True)。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p30 S02E15.数据删除 drop函数](https://www.bilibili.com/video/BV1ji4y157uB?p=30) · 2026-11-17

设为 True 时方法直接在原 DataFrame 上生效并返回 None，可以省内存但会丢掉原始数据；保持默认则返回副本，原表不动。sort_values、drop、fillna、rename 等方法都支持它。

- inplace=True 的方法返回 None，不能写 df = df.drop(..., inplace=True)
- 默认 False，返回副本，便于链式调用和回滚
- 删除类操作开了 inplace 后原数据无法恢复
执行 df.drop(columns='x', inplace=True) 之后，df 和这条语句的返回值分别是什么？::df 已被修改，'x' 列被删除；该语句返回 None。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p49 S03E02.条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=49) · 2026-11-17


### 补充 · 2026-11-17

控制 Pandas 操作是否直接修改原对象的布尔参数

- 默认 False，操作返回新对象，原数据保持不变。
- 设为 True 后直接修改原对象，无需再赋值。
- 可与 regex=True 等参数同时使用。
- 不是所有 Pandas 方法都支持 inplace，使用前需确认。
## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
