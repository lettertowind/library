---
term: str.zfill
aliases: [zfill, 零填充]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.zfill

> 别名：zfill、零填充

**用字符 0 从左侧把字符串填充到指定宽度的方法。**

## 用法
**语法**：`Series.str.zfill(width)`
**参数**：
- `width`：填充后的目标总宽度（int）。原字符串长度不足时在左侧补 0，长度已达或超过 width 时原样返回，不截断。

**示例**：
```python
import pandas as pd

s = pd.Series(['7', '42', '2024', '张三'])
print(s.str.zfill(5).tolist())
# ['00007', '00042', '02024', '000张三']
print(s.str.zfill(5).str.len().tolist())
# [5, 5, 5, 5]  —— 长度按字符数计，中文同样算 1 位
print(s.str.zfill(2).tolist())
# ['7', '42', '2024', '张三']  —— 已超宽则原样保留
```
> 只能补 0、只能左补；要自定义填充字符或方向请改用 `str.pad(width, side='left', fillchar='x')`。

## 解释

str.zfill(width) 是 str.pad 的特例：只能用 0 填充，且只能从左侧填充。常用于编号补零对齐。

## 有什么用

- 工号、编号补零到固定位数
- 生成定长数字字符串

## 关键要点

- 只能用 0 填充
- 只能从左侧填充
- 相当于 pad(side='left', fillchar='0')

## 边界与易混淆

不能自定义填充字符或方向；需要其他字符时用 str.pad。

## 关联

- [[str.pad]] — 上位概念
- [[Series.str 访问器]] — 上位概念

## 自测

str.zfill(10) 对“张三”的结果是什么？::左侧补 8 个 0 到 10 位，即“00000000张三”。
zfill 和 pad 的关系是什么？::zfill 是 pad 的特例，固定用 0 从左侧填充。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
