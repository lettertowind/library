---
term: 写回原 Excel 文件
aliases: [ExcelWriter 写回, 覆盖原表, save 与 close]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
order: 40
---

# 写回原 Excel 文件

> 别名：ExcelWriter 写回、覆盖原表、save 与 close

**用 pd.ExcelWriter 打开目标文件，to_excel 写入后 save 并 close。**

## 解释

to_excel 直接给路径会新建/覆盖文件，但要写回原工作簿并控制写入过程，需用 ExcelWriter 作为上下文对象，写完调用 save() 和 close() 落盘。

## 有什么用

- 把处理结果覆盖写回原 Excel
- 一次写入多个工作表

## 关键要点

- writer = pd.ExcelWriter('文件.xlsx') 创建写入器
- to_excel(writer, index=False) 不写行索引
- 必须 writer.save() 再 writer.close() 才真正落盘
- 拼写是 writer 不是 waiter

## 边界与易混淆

新版 Pandas 推荐 with pd.ExcelWriter(...) as writer 上下文写法，自动关闭。

## 关联

- [[pd.ExcelWriter]] — 上位概念
- [[DataFrame.to_excel]] — 组合使用

## 自测

只调用 to_excel(writer) 不 save/close 会怎样？::数据可能没有真正写入文件，文件内容不完整或为空。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
