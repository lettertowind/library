---
term: str.pad
aliases: [pad, 填充对齐]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
order: 38
---

# str.pad

> 别名：pad、填充对齐

**用指定字符把字符串填充到指定宽度的方法。**

## 解释

str.pad(width, side, fillchar) 把每个字符串补到指定宽度。side 控制填充方向：left 右对齐、right 左对齐、both 两端填充。fillchar 只能是一个字符。

## 有什么用

- 统一字符串宽度
- 生成定长编码
- 对齐显示文本

## 关键要点

- width 为目标宽度
- side 可取 left、right、both
- fillchar 只能是一个字符
- center、ljust、rjust 是它的演变方法

## 边界与易混淆

fillchar 多字符会报错；记住 pad 即可，其余方法了解为主。

## 关联

- [[str.zfill]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

side='right' 时填充方向是哪边，效果相当于什么对齐？::从右侧填充，相当于左对齐。
str.pad 的 fillchar 能传多个字符吗？::不能，只能是一个字符。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
