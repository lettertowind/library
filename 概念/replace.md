---
term: replace
aliases: [df.replace, 值替换]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 36
stage: "S02E21 · 数据替换"
order: 36
---

# replace

> 别名：df.replace、值替换

**将 DataFrame 中指定旧值全部替换为新值的方法。**

## 解释

replace(old, new) 在整张表中查找匹配的旧值并替换为新值，所有出现位置都会被替换。常用于纠正错误数据、统一命名或做简单映射。

## 有什么用

- 统一同义但写法不同的值
- 批量纠正错误数据

## 关键要点

- 语法 df.replace(旧值, 新值)
- 所有匹配位置都会被替换
- 可传入字典做多组映射
- 与 fillna 不同，它处理的是有效值而非空值

## 边界与易混淆

易与 fillna 混淆：replace 替换已有值，fillna 只填空值；替换范围过大可能误改数据。

## 关联

- [[fillna]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

表中有多个“杨过”，df.replace('杨过','孙兴华') 会替换几个？::全部替换，所有出现的“杨过”都会变成“孙兴华”。
replace 和 fillna 处理的对象有什么不同？::replace 替换已存在的有效值，fillna 只填充 NaN 缺失值。


### 补充 · 2026-11-17

replace 面向“具体值”的替换，可作用于整表或指定列，把某些出现过的值统一换成新值。与 map 的整列映射不同，它不要求覆盖整列所有取值。

- 可对整表或单列操作，范围灵活
- 只替换命中的具体值，未命中的保持原样
- 支持字典形式一次替换多个值
整表多处出现同一个名字要统一改掉，用 map 还是 replace？::replace，它能在整个表范围内替换具体值，map 只能对单列映射。
replace 未命中的值会变成 NaN 吗？::不会，保持原值；map 未命中才会变 NaN。

replace(old, new) 在 DataFrame 或 Series 中查找旧值并替换为新值。默认返回新对象，原数据不变；配合 inplace=True 可原地修改。它解决的是整值替换需求，而非字符串子串替换。

- 不赋值也不设 inplace=True 时，原数据不会改变
- inplace=True 后方法返回 None，不能再用变量接收结果
- 不指定列时在整张表所有列中查找替换
执行 data.replace('A','B') 后直接 print(data)，为什么数据没变？::replace 默认返回新对象，不修改原数据；需要接收返回值或设置 inplace=True。
要把 a、b、c 三个不同旧值分别替换成 1、2、3，用列表还是字典更清晰？::字典，key 为旧值、value 为新值，映射关系一目了然。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
