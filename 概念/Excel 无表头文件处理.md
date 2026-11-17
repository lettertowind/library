---
term: Excel 无表头文件处理
aliases: [无表头读取, header=None 组合写法, Excel 表头修复]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 19
stage: "S02E04 · 读取与修改Excel文件"
order: 19
---

# Excel 无表头文件处理

> 别名：无表头读取、header=None 组合写法、Excel 表头修复

**用 header=None + names + index_col 一次性把无表头 Excel 读成规范表的写法。**

## 解释

无表头 Excel 直接读取会导致首行数据被当列名、索引错位。标准解法是在 read_excel 中同时声明“没有表头”“列名叫什么”“哪列作索引”，读入即得到带表头带索引的干净 DataFrame。

## 有什么用

- 读取导出系统生成的裸数据 Excel
- 批量修复结构不规范的工作簿

## 关键要点

- 三步：header=None 关自动表头、names 给列名、index_col 定索引
- 顺序无关，但三者需同时给全才不产生冗余列
- 参数名大小写必须正确
- 处理后可直接 to_excel 写回原路径

## 边界与易混淆

仅解决结构问题，不解决数据类型和日期格式问题。

## 关联

- [[header 参数]] — 组合使用
- [[names 参数]] — 组合使用
- [[index_col 参数]] — 组合使用
- [[pd.read_excel]] — 上位概念

## 自测

只设 header=None 不设 index_col，读出来会多出什么？::会多出一列 0、1、2… 的默认索引，而原本的序号列仍作为普通数据列存在。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
