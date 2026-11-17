---
term: str.decode
aliases: [decode, 解码转换]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.decode

> 别名：decode、解码转换

**把编码后的字节按指定格式解码为字符串的方法。**

## 解释

str.decode('utf-8') 将字节内容按指定字符集还原为字符串，是 str.encode 的逆操作。常用于读取乱码数据后还原。

## 有什么用

- 还原编码后的文本
- 修复乱码列

## 关键要点

- 参数为解码格式
- 与 encode 配对使用
- 格式不匹配会乱码或报错

## 边界与易混淆

解码格式必须与编码格式一致。

## 关联

- [[str.encode]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

解码时格式与编码时不一致会怎样？::会得到乱码或直接报错。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
