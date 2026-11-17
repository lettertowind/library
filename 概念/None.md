---
term: None
aliases: [Python None, 空值 None, None 关键字]
kind: concept
domain: 数据分析/Python
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
---

# None

> 别名：Python None、空值 None、None 关键字

**Python 内置的空值关键字，必须首字母大写，写成小写会报错。**

## 解释

None 表示“没有值”，在函数参数里常用来关闭某项默认行为，例如 header=None 表示不要把第一行当作表头。它是语言关键字，不是字符串，因此大小写敏感。

## 有什么用

- 作为参数取值关闭默认行为
- 表示缺失或无值

## 关键要点

- None 是关键字，必须大写，写成 none 会触发 NameError
- 多数 IDE 会把正确的 None 高亮成橘红色，可当自检信号
- 与 NaN 不同：None 是 Python 空对象，NaN 是浮点缺失值
- 常作为特殊开关出现在 pandas 参数中，与布尔值、字符串并列

## 边界与易混淆

别和字符串 'None'、numpy 的 np.nan 混淆：前者是普通文本，后者是数值型缺失标记，三者判断方式不同。

## 关联

- [[header 参数]] — 组合使用
- [[NaN]] — 对比项

## 自测

在 pd.read_excel 里写成 header=none 会发生什么？::报 NameError：小写 none 被当成未定义变量，只有大写 None 才是关键字。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17
