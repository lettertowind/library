---
term: pip
aliases: [pip3, pip install, 包管理器]
kind: tool
domain: 数据分析/Python
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S02E00 · 安装pandas.numpy.xlrd"
order: 15
---

# pip

> 别名：pip3、pip install、包管理器

**Python 的官方包管理工具，用于从网络下载并安装第三方库。**

## 解释

pip 是 Python 生态中安装第三方库的标准入口，通过 `pip install 包名` 从 PyPI 下载并安装。Windows 下常以 pip3.exe 形式存在于 Python 安装目录的 Scripts 文件夹中，需先 cd 到该目录或将其加入 PATH 才能直接调用。

## 有什么用

- 安装 pandas、numpy、xlrd 等第三方库
- 升级或卸载 Python 包

## 关键要点

- 命令格式：pip install 包名
- 需先定位 pip3.exe 所在目录，或配置环境变量
- 安装失败多因网络问题，可重复执行重试
- 安装是否成功可用 import 语句验证

## 边界与易混淆

pip 只管 Python 包，不负责系统级依赖；conda 环境下应优先用 conda install 避免冲突。

## 关联

- [[import pandas as pd]] — 组合使用
- [[孙兴华 Python 数据分析三部曲]] — 上位概念

## 自测

为什么在命令行直接输入 pip install pandas 可能提示找不到命令？::因为 pip3.exe 所在目录不在系统 PATH 中，需要先 cd 到该目录或配置环境变量。


### 补充 · 2026-11-17

基本语法是 pip install 库名，例如 pip install pandas、pip install numpy、pip install xlrd。安装需要联网，成功率和速度受网速与运营商影响，失败属常见现象。

- 固定句式：pip install + 库名，一次装一个库
- 安装走网络下载，慢或失败多为网络原因，不一定是命令写错
- 失败最实用的处理是原命令反复重试，直到成功
执行 pip install pandas 卡住并报错，第一步应该判断是命令问题还是网络问题？怎么判断？::先看报错类型：若是「不是内部或外部命令」是路径/环境问题；若是超时、连接失败、下载中断则属网络问题，重试或换源即可。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p15 S02E00.安装pandas.numpy.xlrd](https://www.bilibili.com/video/BV1ji4y157uB?p=15) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
