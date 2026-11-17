---
term: labels 参数（cutqcut）
aliases: [labels, labels=False, 箱子名称参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 37
stage: "S02E22 · 离散化和分箱"
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


### 补充 · 2026-11-17

cut 默认输出每个值所属的区间文本，可读但不便再计算；labels=False 改为输出从 0 开始的整数箱号，适合后续数值运算；labels 传列表则用业务名称替换区间，如「50年代前」「50年代后」。

- 不写 labels：返回区间，如 1950~2000
- labels=False：返回整数箱号，0 号箱对应第一段
- labels=列表：返回自定义箱名，便于报表展示
用 [1900, 1950, 2000] 分箱并传 labels=['50年代前','50年代后']，若写成三个标签会怎样？::标签数多于箱子数，参数校验不通过会报错；标签必须与两个箱子的数量对齐。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p37 S02E22.离散化和分箱](https://www.bilibili.com/video/BV1ji4y157uB?p=37) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
