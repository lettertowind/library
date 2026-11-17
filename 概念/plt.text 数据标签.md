---
term: plt.text 数据标签
aliases: [text, plt.text(), 数据标签]
kind: method
domain: Matplotlib
tags: [概念/concept, 领域/Matplotlib]
stage: "S03E08 · 折线图"
order: 56
created: 2026-11-17
updated: 2026-11-17
---

# plt.text 数据标签

> 别名：text、plt.text()、数据标签

**在指定坐标处直接绘制一段文字，最常用于标出数据点的数值。**

## 解释

text 只负责“在某个位置写字”，不做箭头和指向关系，因此是加数据标签最轻量的方式。配合 bbox 可以升级为带底色的醒目标签，靠 size 参数控制字号。

## 有什么用

- 给柱子或数据点标注具体数值
- 在图上补充说明性文字

## 关键要点

- 参数顺序为 x, y, 文本内容
- size 控制字号，放大后标签更清楚
- 传入 bbox 字典即可获得带边框背景的标签
- 与 annotate 的区别：text 无箭头指向能力

## 边界与易混淆

需要说明“文字指代哪个对象”时不要用 text，改用 annotate 加箭头，否则读者无法确定文字归属。

## 关联

- [[plt.annotate 文本注释]] — 对比项
- [[bbox 文本边框]] — 组合使用

## 自测

要标出每个点的数值，用 plt.text 还是 plt.annotate 更合适？::plt.text。数据标签只需在点上写字，不需要箭头指向关系。


### 补充 · 2026-11-17

plt.text(x, y, s) 在坐标 (x, y) 处绘制文字 s，常配合 zip 遍历为每个数据点写数值。相比只看折线高度，标签让读者直接读到精确值。文字的位置微调、对齐、字号和旋转都由参数控制。

- 第三个参数是文字内容，数值需用 str(y) 转成字符串
- ha/va 控制水平/垂直对齐，常用 ha='center' 让标签居中于数据点
- fontsize 设置字号，rotation 设置旋转角度（0 表示不旋转）
标签为什么老挡住数据点，怎么解决？::因为直接写在与点相同坐标上，把 y 加一个合适的偏移量上移即可，偏移量需按数据量级试出。
多系列打标签时，为什么用 zip 而不是手写每个坐标？::zip 把时间列与当前系列列自动配对，配合 for 循环即可复用同一套标签逻辑，避免重复代码。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p56 S03E08.折线图](https://www.bilibili.com/video/BV1ji4y157uB?p=56) · 2026-11-17

给条形或柱形标注具体数值。s 是显示内容，ha/va 控制文字相对坐标点的对齐方式，fontsize 与 color 控制外观。图形方向一变，坐标含义随之改变，标签极易接反。

- 堆积条形图中 x 用该层数值或累计和，y 用类别（姓名），与柱形图相反
- ha='center'、va='center' 让文字居中压在条带里
- fontsize 调字号，color='white' 让文字在深色条带上可读
堆积条形图里给数学层加标签，x 应取什么？::data.语文 + data.数学（该层累计末端）再做偏移微调。
照搬柱形图的 x=姓名、y=语文 会出什么问题？::坐标接反，文字跑到图外或看不见，因为条形图纵轴才是类别。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p53 S03E06.叠加条形图](https://www.bilibili.com/video/BV1ji4y157uB?p=53) · 2026-11-17

柱形图默认只给高度不给数字，读者只能估读。plt.text(x, y, s, ...) 把数值文本钉到坐标位置上，配合 for 循环可批量标注。x、y 决定位置，s 是内容，通常要把数值 str() 一下。

- 三个必需参数：x 坐标、y 坐标、要显示的文字（数值需先 str() 转换）
- ha='center' 让文字水平居中对齐到 x 坐标，字号用 fontsize 控制
- 常与 zip 配合：for x1, y1 in zip(x, 数值序列) 批量标注
plt.text 的 y 参数直接传柱子数值会有什么问题？::文字会贴在柱子顶端甚至落进上一层区域，需向下减偏移量才落进柱子内部
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p52 S03E05.叠加柱状图](https://www.bilibili.com/video/BV1ji4y157uB?p=52) · 2026-11-17

plt.text(x, y, s) 在数据坐标 (x, y) 处渲染一段字符串。柱形图、折线图上的「柱子顶上那个数字」就是用它逐点写出来的。它不影响数据本身，只是在图上叠一层文字，因此位置全靠自己算。

- 三个必填参数依次是 x 坐标、y 坐标、要显示的文字
- 每根柱子都要调一次 plt.text，所以必须写在 for 循环里
- 数值需用 str() 转成字符串才能作为文字参数传入
为什么添加柱形图标签要用 for 循环，而不能一次调用搞定？::plt.text 一次只画一段文字，每根柱子位置不同，必须逐根柱子调用一次
柱子高度 y1=8，想让标签浮在柱顶上方 1 个单位，第二个参数写什么？::y1 + 1
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p51 S03E04.添加数据标签](https://www.bilibili.com/video/BV1ji4y157uB?p=51) · 2026-11-17

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p76 S03E27.文本注释](https://www.bilibili.com/video/BV1ji4y157uB?p=76) · 2026-11-17
