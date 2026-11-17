---
term: xlrd
aliases: [xlrd 库, Excel 读取库]
kind: tool
domain: 数据分析/Python
tags: [概念/tool, 领域/数据分析]
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


### 补充 · 2026-11-17

read_excel 只是外壳，真正解析 Excel 二进制结构的是引擎库。缺少 xlrd 时某些读取方式会直接抛 ImportError，所以建议提前装好。

- pandas 的 Excel 读取依赖它作为引擎
- 未安装时调用某些读取方法会直接报错
- 新版 xlrd 已不再支持 .xlsx，读 xlsx 需 openpyxl
为什么课程建议先安装 xlrd 再练 read_excel？::read_excel 只是封装，底层解析 Excel 要靠引擎库，缺库时某些读取方式会直接报错。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17

pandas 的 read_excel 自身不解析二进制表格，而是调用 xlrd 之类的引擎完成读取。因此即使 pandas 装好了，缺 xlrd 仍会在读 .xls 时报错。安装命令为 pip install xlrd。

- 安装命令：pip install xlrd，与 pandas 同样走网络
- 只负责读，不负责写；写 Excel 用 to_excel 等另一套机制
- 验证方式是在解释器里 import xlrd 不报错
pandas 已经装好，为什么读某个 Excel 文件仍报缺少引擎的错？::因为 read_excel 依赖第三方解析引擎，该文件是 .xls 却未安装 xlrd（或 .xlsx 未装 openpyxl）。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p15 S02E00.安装pandas.numpy.xlrd](https://www.bilibili.com/video/BV1ji4y157uB?p=15) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
