---
term: import pandas as pd
aliases: [导入 Pandas, pd 别名]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
order: 16
---

# import pandas as pd

> 别名：导入 Pandas、pd 别名

**导入 Pandas 库并约定以 pd 作为简写别名的标准写法。**

## 解释

用 import ... as ... 给库起短别名，避免每次写完整包名。pd 是社区通用约定，与 NumPy 用 np 类似；别名技术上可改，但遵循惯例便于协作。

## 有什么用

- 任何使用 Pandas 的脚本开头
- 统一团队代码风格

## 关键要点

- 标准写法是 import pandas as pd
- 别名可自定义，但建议用 pd
- 与 import numpy as np 是同类约定
- 别名只为少打字，不改变功能

## 边界与易混淆

别名随意改会导致代码可读性下降、与他人代码不一致。

## 关联

- [[DataFrame]] — 前置知识
- [[Series]] — 前置知识

## 自测

把别名改成 import pandas as p 后代码还能跑吗？::能跑，但后续所有 pd.xxx 都要改成 p.xxx，且不符合通用习惯。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
