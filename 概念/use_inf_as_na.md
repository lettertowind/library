---
term: use_inf_as_na
aliases: [pd.options.mode.use_inf_as_na, inf 视为空值]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 34
stage: "S02E19 · 算数运算与数据对齐"
---

# use_inf_as_na

> 别名：pd.options.mode.use_inf_as_na、inf 视为空值

**Pandas 全局选项，开启后把 inf 和 -inf 视为缺失值。**

## 用法
**语法**：`pd.options.mode.use_inf_as_na = True`

**参数**：
- 该选项是取值 `True` 或 `False` 的布尔选项，通过赋值开启或关闭，没有函数参数。
- `True`：把 `inf` 和 `-inf` 视为缺失值，`fillna`、`isna` 等按空值处理。
- `False`：默认值，保留 `inf` 和 `-inf` 原值。
- 该选项是全局选项，作用于整个会话中的全部 DataFrame/Series。

**示例**：
```python
import pandas as pd, numpy as np
s = pd.Series([1, -1, 0]) / 0
print(s.tolist())          # [inf, -inf, nan]

# 旧版用 pd.options.mode.use_inf_as_na = True，pandas 2.1 起已移除
# 当前写法：先把 inf 替换为 NaN，再填充
s2 = pd.Series([1, -1, 0]) / 0
print(s2.replace([np.inf, -np.inf], np.nan).fillna(0).tolist())  # [0.0, 0.0, 0.0]
```

## 解释

分母为 0 会产生 inf/-inf，而 fillna 只处理 NaN，无法直接替换无穷大。开启该选项后，inf 被当作 NaN，后续 fillna 或 fill_value 才能生效。

## 有什么用

- 除法运算出现 inf/-inf 需要填充时
- 把无穷大统一按缺失值处理

## 关键要点

- 写法：pd.options.mode.use_inf_as_na = True
- 是全局设置，影响整个会话
- 开启后 inf/-inf 可被 fillna 处理
- 新版 Pandas 中该选项已弃用，需注意版本差异

## 边界与易混淆

该选项在新版 Pandas 中已废弃，替代方案是先用 replace([np.inf,-np.inf], np.nan) 再 fillna。

## 关联

- [[fillna]] — 前置知识
- [[inf 与 -inf]] — 上位概念

## 自测

为什么设置 use_inf_as_na 之前 fillna(0) 无法去掉 inf？::因为 fillna 只识别 NaN，inf 不是缺失值，不会被替换。


### 补充 · 2026-11-17

它解决的是 fillna 对无穷大无能为力的问题：先把无穷大“降级”成缺失值，后续的 fillna 或 fill_value 才能接手。写法通常放在 import 语句下方，对之后的所有运算全局生效。

- 设置一次，全局生效，对后续所有计算有效
- 作用是把 inf / -inf 转成 NaN，本身不做填充
- 之后接 fillna(0) 或 fill_value=0 才完成清洗
只写 use_inf_as_na = True 而不加 fillna，除法结果里的 inf 会变成什么？::变成 NaN（空值）。该选项只做转换，不做填充，仍需 fillna 才能变成具体数值。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p34 S02E19.算数运算与数据对齐](https://www.bilibili.com/video/BV1ji4y157uB?p=34) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
