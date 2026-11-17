---
term: PATH 环境变量
aliases: [环境变量 PATH, 系统路径变量, path 配置]
kind: concept
domain: 计算机/办公软件/Windows
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# PATH 环境变量

> 别名：环境变量 PATH、系统路径变量、path 配置

**操作系统按其中列出的目录顺序查找可执行程序的全局路径列表。**

## 解释

当你在命令行输入一个命令名而不是完整路径时，系统会依次到 PATH 列出的各个目录里找同名可执行文件。找不到就报「不是内部或外部命令」。本课要求先 cd 到 pip3.exe 所在目录，本质就是绕过 PATH 未配置的问题。

## 有什么用

- 理解命令为什么能直接调用或报「找不到命令」
- 判断该配 PATH 还是该 cd 进目录

## 关键要点

- 命令输入后先在当前目录找，再按 PATH 目录顺序找
- pip 命令报「不是内部或外部命令」通常是 Scripts 目录没进 PATH
- 根治办法是把 pip 所在目录加入 PATH，一次性解决
- 课程采用的临时办法是 cd 到 pip3.exe 目录再执行

## 边界与易混淆

PATH 只影响「按名字找程序」，不影响 Python 内部 import 模块的搜索路径（那是 sys.path）。

## 关联

- [[cd 命令]] — 对比项
- [[pip]] — 前置知识
- [[cmd 命令行]] — 前置知识

## 自测

教程让你先 cd 进 pip3.exe 目录再执行 pip，这解决了什么根本问题？它的局限是什么？::解决的是 pip 所在目录不在 PATH 中、系统按名字找不到命令的问题；局限是换目录或换终端后又要重新 cd，治本应把目录加入 PATH。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p15 S02E00.安装pandas.numpy.xlrd](https://www.bilibili.com/video/BV1ji4y157uB?p=15) · 2026-11-17
