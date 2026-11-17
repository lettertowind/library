---
term: cmd 命令行
aliases: [命令提示符, cmd, 命令行窗口]
kind: tool
domain: 计算机/办公软件/Windows
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# cmd 命令行

> 别名：命令提示符、cmd、命令行窗口

**Windows 系统自带的文本命令交互界面，用于执行 DOS 风格命令。**

## 解释

通过 Win+R 输入 cmd 打开，可在其中执行 cd、pip 等命令。数据分析入门阶段常用它来安装库、启动 Python 解释器。

## 有什么用

- 执行 pip 安装命令
- 进入目录、启动 Python

## 关键要点

- Win+R 输入 cmd 快速打开
- cd 命令用于切换当前目录
- 路径需替换为本机真实路径

## 关联

- [[pip]] — 组合使用

## 自测

在 cmd 中如何进入 D 盘的 Python 目录？::先输入 D: 切换盘符，再 cd 到具体路径。


### 补充 · 2026-11-17

按 Win + R 打开“运行”窗口，输入 cmd 回车即可打开。它有个“当前目录”的概念，很多命令只在本目录下生效，所以执行前要先用 cd 切到目标目录。

- Win + R → 输入 cmd → 回车，是通用打开方式
- cd 空格 路径：切换当前目录
- 先 cd 到 pip3.exe 所在文件夹，再执行 pip3 install
为什么装包前要先 cd 到 pip3.exe 所在目录？::因为 pip3 不是全局可用命令，只有在它所在目录（或已加入环境变量）执行，系统才找得到它。
Win + R 打开的是什么？和 cmd 什么关系？::打开的是“运行”窗口，在其中输入 cmd 才会启动命令提示符。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p02 S01E01.参考书籍及安装方法](https://www.bilibili.com/video/BV1ji4y157uB?p=2) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
