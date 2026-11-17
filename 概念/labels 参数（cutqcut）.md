---
term: labels 参数（cutqcut）
aliases: [labels, labels=False, 箱子名称参数]
kind: concept
domain: 计算机/数据分析/Pandas
tags: [概念/concept, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
---

# labels 参数（cutqcut）

> 别名：labels、labels=False、箱子名称参数

**cut/qcut 中用于替换箱子显示名称或返回整数箱号的参数。**

## 解释

labels 传名称列表时用业务名称替换区间显示；传 False 时只返回从 0 开始的整数箱号，便于后续计算或建模。

## 有什么用

- 给分箱结果设置可读的业务标签
- 返回箱号用于数值计算

## 关键要点

- labels=名称列表 长度必须与箱数一致
- labels=False 返回整数箱号，从 0 开始
- 箱子名称建议单独定义成列表再传入，多箱场景更清晰
- 视频口述的 levels 实为 labels

## 边界与易混淆

名称列表长度与箱数不匹配会报错。

## 关联

- [[pd.cut]] — 组合使用
- [[pd.qcut]] — 组合使用

## 自测

想让分箱结果直接显示“50年代前/50年代后”，应怎么传参？::定义名称列表并传入 labels，如 pd.cut(x, bins=bins, labels=['50年代前','50年代后'])。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
