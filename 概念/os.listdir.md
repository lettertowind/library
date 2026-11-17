---
term: os.listdir
aliases: [listdir, 遍历文件夹]
kind: method
domain: 数据分析/Python
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E25 · Excel文件的拆分与合并"
order: 40
---

# os.listdir

> 别名：listdir、遍历文件夹

**返回指定文件夹下所有文件和文件夹名称列表的函数。**

## 解释

os.listdir(路径) 把目录内容列成一个列表，配合 for 循环即可逐个读取文件夹中的 Excel 文件。它是多工作簿批量合并的入口。

## 有什么用

- 批量读取同一文件夹下的多个 Excel
- 遍历目录中的文件

## 关键要点

- 返回文件名列表，不含完整路径
- 需与路径字符串用 + 拼接成完整路径
- 结果包含子文件夹名，必要时需过滤
- 属于 os 模块，需先 import os

## 边界与易混淆

只列一层，不递归子目录；结果顺序不保证，需要顺序时应排序。

## 关联

- [[pd.read_excel]] — 组合使用
- [[pd.concat]] — 组合使用

## 自测

os.listdir 返回的是完整路径还是文件名？读取文件前还要做什么？::返回文件名，需要与文件夹路径用 + 拼接成完整路径再传给 read_excel。


### 补充 · 2026-11-17

合并一个文件夹内的多个 Excel 时，用 os.listdir(目录) 拿到文件名列表再逐个循环读取。它只返回名字，不含目录本身。

- 拿到的是文件名列表，需要与目录拼成完整路径才能打开
- 字符串拼接用 +，不能用 & 连接符
- 结果包含子文件夹名，必要时先过滤或判断后缀
直接 pd.read_excel(目录路径) 为什么读不出文件？::目录不是文件，必须把目录和 os.listdir 得到的文件名用 + 拼成完整文件路径。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并](https://www.bilibili.com/video/BV1ji4y157uB?p=40) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
