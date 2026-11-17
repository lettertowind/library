---
term: xlrd
aliases: [xlrd 库, Excel 读取库]
kind: tool
domain: 计算机/数据分析/Python
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E04 · 读取与修改Excel文件"
order: 19
---

# xlrd

> 别名：xlrd 库、Excel 读取库

**Python 中用于读取旧版 .xls 格式 Excel 文件的第三方库。**

## 解释

xlrd 是 pandas 早期读取 Excel 的底层依赖，专门解析 .xls（Excel 97-2003）格式。新版 xlrd 已不再支持 .xlsx，读取 .xlsx 需改用 openpyxl。安装 pandas 后仍需单独安装 xlrd 才能读取 Excel。

## 有什么用

- 配合 pd.read_excel 读取 .xls 文件
- 作为 pandas Excel 读取的底层引擎

## 关键要点

- 只支持 .xls，不支持 .xlsx
- 需单独 pip install xlrd
- 是 pd.read_excel 的默认引擎之一
- 新版 pandas 读 .xlsx 改用 openpyxl

## 边界与易混淆

易与 openpyxl 混淆：xlrd 读 .xls，openpyxl 读写 .xlsx。

## 关联

- [[pd.read_excel]] — 前置知识
- [[pip]] — 组合使用

## 自测

用 pd.read_excel 读取 .xlsx 文件报错提示缺少引擎，应该装 xlrd 还是 openpyxl？::openpyxl，因为新版 xlrd 已不支持 .xlsx。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
