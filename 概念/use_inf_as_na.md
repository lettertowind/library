---
term: use_inf_as_na
aliases: [pd.options.mode.use_inf_as_na, inf 视为空值]
kind: method
domain: 计算机/数据分析/Pandas
tags: [概念/method, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# use_inf_as_na

> 别名：pd.options.mode.use_inf_as_na、inf 视为空值

**Pandas 全局选项，开启后把 inf 和 -inf 视为缺失值。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
