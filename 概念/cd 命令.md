---
term: cd 命令
aliases: [cd, change directory, 进入目录]
kind: method
domain: 计算机/办公软件/Windows
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# cd 命令

> 别名：cd、change directory、进入目录

**DOS/命令行中用于切换当前工作目录的命令。**

## 解释

格式为 `cd 路径`，把命令行当前所在目录切换到指定文件夹。安装库前需 cd 到 pip3.exe 所在目录，否则系统找不到 pip 命令。

## 有什么用

- 切换到 pip3.exe 所在目录
- 在命令行中定位工作路径

## 关键要点

- 格式：cd 空格 + 目标路径
- 路径必须替换为本机真实路径
- 跨盘符需先切换盘符再 cd

## 关联

- [[cmd 命令行]] — 上位概念
- [[pip]] — 前置知识

## 自测

cd 命令的作用是什么？::切换命令行当前所在的工作目录。


### 补充 · 2026-11-17

命令行的所有相对操作都以「当前目录」为基准，cd 就是改变这个基准。本课用它进入 pip3.exe 所在文件夹，使 pip 命令能被找到并执行。

- 写法：cd 空格 路径，路径含空格时需加引号
- 路径因每人 Python 安装位置不同而异，需自行查找 pip3.exe
- 默认安装时容易忘记装在哪，可用文件搜索定位 pip3.exe
为什么 cd 到了 pip3.exe 目录后 pip 就能用，而 cd 到别处又不行？::因为命令行会优先在当前目录查找可执行文件；pip 目录未加入 PATH，所以只有身处该目录时才能按名字调用。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p15 S02E00.安装pandas.numpy.xlrd](https://www.bilibili.com/video/BV1ji4y157uB?p=15) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
