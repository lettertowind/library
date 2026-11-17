---
term: str.slice_replace
aliases: [slice_replace, 切片替换]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# str.slice_replace

> 别名：slice_replace、切片替换

**截取指定范围并把该范围替换为指定内容的方法。**

## 解释

str.slice_replace(start, stop, repl) 先按切片取出 start 到 stop 的片段，再用 repl 替换这一段。等价于先 slice 再替换，因此不支持步长。

## 有什么用

- 把字符串中间某段替换成新内容
- 脱敏处理固定位置的字符

## 关键要点

- start 到 stop 的范围被 repl 整体替换
- 不支持 step 步长
- 可理解为 slice 加替换的组合

## 边界与易混淆

不能设置步长；需要隔位替换时应先用其他方式处理。

## 关联

- [[str.slice]] — 前置知识
- [[str.replace 正则替换]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

str.slice_replace(1, 3, '520') 对“满血激活”的结果是什么？::“满520活”，索引 1 到 2 的“血激”被替换为 520。
为什么 slice_replace 不支持 step？::它的本质是截取一段连续范围再整体替换，步长会使范围不连续。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
