---
term: pip3 install numpy
aliases: [安装 NumPy, pip3 安装, pip3 install]
kind: method
domain: 数据分析/Python
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
stage: "S01E01 · 参考书籍及安装方法"
order: 2
---

# pip3 install numpy

> 别名：安装 NumPy、pip3 安装、pip3 install

**用 pip3 包管理器从网络下载并安装 NumPy 库的命令。**

## 解释

安装思路与安装 PyMySQL 类似：先找到 pip3.exe 所在目录，在命令行中 cd 进入该目录，再执行 pip3 install numpy。安装过程必须联网，因为需要下载安装包。

## 有什么用

- 首次在电脑上配置 NumPy 环境
- 重装或修复 NumPy 安装

## 关键要点

- 先定位 pip3.exe 所在文件夹并复制路径
- Win+R 输入 cmd 打开命令行，cd 加空格粘贴路径
- 在目标目录执行 pip3 install numpy
- 安装必须联网下载安装包
- 也可在已能调用 pip3 的环境中直接执行

## 边界与易混淆

若系统有多个 Python 版本，pip3 可能装到非目标解释器；此时需用对应解释器的 pip 或虚拟环境。

## 关联

- [[pip]] — 上位概念
- [[cmd 命令行]] — 前置知识
- [[cd 命令]] — 前置知识
- [[import 验证安装]] — 组合使用

## 自测

为什么安装前要先 cd 到 pip3.exe 所在目录？::因为命令行默认可能找不到 pip3 命令，进入其所在目录后系统才能定位并执行该程序。


### 补充 · 2026-11-17

在 cmd 中、pip3.exe 所在目录下执行该命令即可安装 NumPy；执行时要按回车、保持联网并等待下载安装完成。安装后必须验证：进入 Python 交互环境执行 import numpy，无报错才算成功，报错则重装一遍。

- 命令结构：pip3（工具）+ install（子命令）+ numpy（包名）
- 必须先 cd 到 pip3.exe 所在目录再执行
- 安装依赖网络，需要等待下载完成
安装完成后怎么确认真的装好了？::进入 Python 交互环境执行 import numpy，无报错即成功；报错说明需重新安装。
安装命令报“找不到 pip3”，最可能的原因是什么？::当前命令行目录不是 pip3.exe 所在目录，也没有把其路径加入环境变量。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p02 S01E01.参考书籍及安装方法](https://www.bilibili.com/video/BV1ji4y157uB?p=2) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
