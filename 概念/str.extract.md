---
term: str.extract
aliases: [extract, 分组捕获, 捕获组提取]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 39
stage: "S02E24 · 字符串操作（下）"
order: 39
---

# str.extract

> 别名：extract、分组捕获、捕获组提取

**用正则括号分组从字符串中提取目标内容为多列的方法。**

## 解释

Series.str.extract(pattern) 只提取正则中括号（捕获组）内的内容，每个括号对应一列结果。常用于从日期等复合字符串中拆出年、月、日。

## 有什么用

- 从日期列拆出年月日
- 从复合文本中抽取字段

## 关键要点

- 只有括号内的内容会被提取
- 每个捕获组对应一列
- 日期列需先 .astype(str)
- 正则需匹配实际分隔符（- 或 年月日）

## 边界与易混淆

不匹配的行对应位置为 NaN；模式写错会整列提取失败。

## 关联

- [[str.match]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

正则 (\d{4})-(\d{2})-(\d{2}) 用 extract 会得到几列？::三列，分别是年、月、日。
如果只给月份加括号，extract 结果是什么？::只提取月份一列。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
