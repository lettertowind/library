---
term: inplace 参数
aliases: [inplace, inplace=True, 原地修改参数]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
