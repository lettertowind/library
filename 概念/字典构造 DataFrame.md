---
term: 字典构造 DataFrame
aliases: [dict 建表, pd.DataFrame(dict)]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 21
stage: "S02E06 · 数据结构之DataFrame"
order: 21
---

# 字典构造 DataFrame

> 别名：dict 建表、pd.DataFrame(dict)

**用字典的键作列名、值作列数据来创建 DataFrame 的写法。**

## 解释

pd.DataFrame({...}) 接收字典时，键自动成为列名，值（通常是列表）成为该列各行数据。这是手工造小表最直观的方式，数值不加引号、字符串加引号。

## 有什么用

- 快速构造演示或测试用的小型二维表
- 把已有字典数据转成表格

## 关键要点

- 键是列名，值通常是列表表示一列数据
- 数值不加引号，字符串必须加引号
- 键名应唯一，列表内的值可以重复
- 各列列表长度应一致，否则会补缺失值

## 边界与易混淆

只适合小数据量手工构造，大批量数据应从文件读取。

## 关联

- [[DataFrame]] — 上位概念
- [[Series]] — 组合使用
- [[set_index]] — 组合使用

## 自测

pd.DataFrame({'序号':[1,2],'姓名':['叶问','李小龙']}) 生成的表有几列几行？::两列（序号、姓名）两行。
如果字典里两个列表长度不同会怎样？::Pandas 会按最长列对齐，短列缺失位置补 NaN。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
