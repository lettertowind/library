---
term: import pandas as pd
aliases: [导入 Pandas, pd 别名]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
---

# import pandas as pd

> 别名：导入 Pandas、pd 别名

**导入 Pandas 库并约定以 pd 作为简写别名的标准写法。**

## 用法
**语法**：`import pandas as pd`
**参数**：无
**示例**：
```python
import pandas as pd
import numpy as np   # 与 pd 同类的别名约定

print(pd.__name__)                    # pandas
print(pd.Series([1, 2, 3]).sum())     # 6
print(np.array([1, 2, 3]).mean())     # 2.0

# 旧版写法：import pandas as p 也能运行，但后续 p.Series、p.read_excel 都要跟着改
# 推荐写法：统一用 pd，与社区、教程、同事代码保持一致
```

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


### 补充 · 2026-11-17

直接 import pandas 后每次都要写 pandas.方法名，太啰嗦；用 as pd 起个别名，之后写 pd.方法名即可。点号前代表库，点号后代表方法或对象。

- pd 是社区约定，不是语法强制，别名可以随意改
- 改成中文别名也能运行，但会降低可读性，不建议
- 调用形式统一为 pd.方法名(...)
把别名改成 import pandas as ppp 后，pd.DataFrame(...) 还能用吗？::不能，必须写成 ppp.DataFrame(...)。别名只是代号，改了之后调用名要跟着改。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p16 S02E01.数据类型与新建文件](https://www.bilibili.com/video/BV1ji4y157uB?p=16) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
