---
term: set_index
aliases: [df.set_index, 设置索引]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# set_index

> 别名：df.set_index、设置索引

**将 DataFrame 的一列或多列设置为行索引的方法。**

## 解释

set_index 在读取数据后调用，传入列名列表即可把多列设为多层行索引。它与读取时用 index_col 指定索引列效果等价，适合先读数据再调整索引结构的场景。

## 有什么用

- 读取后设置单层或多层行索引
- 把普通列转为索引以方便查询

## 关键要点

- 传入列名列表可设置多层索引
- 与 read_excel 的 index_col 效果等价
- 默认返回新 DataFrame，不修改原对象

## 边界与易混淆

与 index_col 的区别只在调用时机：一个读取时设置，一个读取后设置。

## 关联

- [[分层索引]] — 组合使用
- [[index_col 参数]] — 对比项

## 自测

set_index(['班级','学号']) 和 read_excel(index_col=[0,1]) 有什么区别？::效果等价，只是设置时机不同：前者读取后设置，后者读取时直接指定。


### 补充 · 2026-11-17

set_index 将指定业务字段提升为行索引，替代默认的 0、1、2 整数索引。写出文件时默认索引列就不会作为多余的一列出现，常用于让导出结果更干净。

- set 是设置、index 是索引，合起来即设置索引
- 默认返回新对象，需重新赋值或加 inplace
- 设为索引的列不再是普通数据列
导出 Excel 时多出一列 0、1、2，用 set_index 怎么解决？::把某个业务字段设为索引，如 data.set_index('序号')，默认整数索引就不再作为列写出。
set_index 之后原来的那一列还在普通列里吗？::不在了，它变成了行索引，需通过 index 访问。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
