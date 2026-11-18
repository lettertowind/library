---
term: import numpy as np
aliases: [导入 NumPy, np 别名, import numpy]
kind: method
domain: Numpy
tags: [概念/method, 领域/Numpy]
created: 2026-11-17
updated: 2026-11-17
order: 3
stage: "S01E02 · 体验Numpy与for循环的区别"
---

# import numpy as np

> 别名：导入 NumPy、np 别名、import numpy

**导入 NumPy 库并约定俗成地简写为 np。**

## 用法

**语法**：`import numpy as np`

**参数**：无（`as np` 是导入别名，不是函数参数，可换成其他别名，但社区约定用 `np`）

**示例**：

```python
import numpy as np

a = np.arange(5)
print(a)          # [0 1 2 3 4]
print(a.mean())   # 2.0
print(type(a))    # <class 'numpy.ndarray'>
```

## 解释

NumPy 的标准导入写法，np 是社区通用别名，便于后续调用 np.arange、np.array 等。Pandas 对应简写为 pd。

## 有什么用

- 使用 NumPy 前的第一步
- 统一代码风格便于阅读

## 关键要点

- 标准写法：import numpy as np
- np 是约定俗成的别名，不是强制
- Pandas 对应简写为 pd
- 导入后才能调用 np.arange 等函数

## 关联

- [[pip3 install numpy]] — 前置知识
- [[import pandas as pd]] — 对比项

## 自测

为什么大家习惯把 NumPy 导入为 np？::这是社区通用约定，统一别名便于代码阅读和复用。


### 补充 · 2026-11-17

导入后即可用 np.xxx 调用 NumPy 的函数。写不带别名的 import numpy 也合法，最常用于安装后的验证：没有报错说明库已正确安装且能被解释器找到。

- as np 是行业惯例，几乎所有教程统一使用
- 验证安装时可直接写 import numpy，无报错即成功
- 导入报错通常是未安装或装到了别的 Python 环境
import numpy 没报错，能说明什么、不能说明什么？::能说明 NumPy 已装好且被当前 Python 解释器找到；不能说明版本合适或依赖完整。
为什么要写 as np？::缩短调用名，且与主流教程和代码库保持一致，便于阅读和协作。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p02 S01E01.参考书籍及安装方法](https://www.bilibili.com/video/BV1ji4y157uB?p=2) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
