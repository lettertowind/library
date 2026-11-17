---
term: plt.locator_params（刻度数量控制）
aliases: [locator_params, nbins, 坐标轴分段, 刻度个数]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E19 · 坐标轴【下】"
order: 68
created: 2026-11-17
updated: 2026-11-17
---

# plt.locator_params（刻度数量控制）

> 别名：locator_params、nbins、坐标轴分段、刻度个数

**用 nbins 指定坐标轴大约分成几份、显示几个刻度的 Matplotlib 函数。**

## 解释

它按“想分几段”的思路让 Matplotlib 自动挑刻度位置，而不是逐个指定刻度值。传 axis='x' 只改 x 轴，不传则 x、y 轴一起分割。也可先 plt.gca() 取得轴对象，再调用 ax.locator_params，效果完全一致。

## 有什么用

- 刻度太密或太稀时快速调整刻度数量
- 出图前粗调坐标轴分段

## 关键要点

- nbins=5 表示显示约 5 个刻度值，不是固定值列表
- axis='x' 只作用于 x 轴，省略则两轴统一分割
- nbins 只是期望值，Matplotlib 会在取整后的合理位置放置刻度
- 若要指定具体刻度值，应改用 set_xticks/set_yticks

## 边界与易混淆

与 plt.xticks 传具体刻度列表不同，locator_params 只控制“数量/分段”，不控制“具体值”。

## 关联

- [[plt.gca 与 plt.gcf]] — 组合使用
- [[刻度定位器与格式器（Locator Formatter）]] — 上位概念
- [[MultipleLocator]] — 对比项

## 自测

只想让 x 轴出现 4 个左右刻度值，写一行代码？::plt.locator_params(axis='x', nbins=4)
locator_params(nbins=5) 和 xticks([1,2,3]) 的本质区别？::前者只给刻度数量让系统自动定位，后者强制指定每个刻度值。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p68 S03E19.坐标轴【下】](https://www.bilibili.com/video/BV1ji4y157uB?p=68) · 2026-11-17
