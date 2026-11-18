---
term: strftime 日期格式化
aliases: [strftime, strftime(), 日期格式化, 时间转字符串]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
---

# strftime 日期格式化

> 别名：strftime、strftime()、日期格式化、时间转字符串

**把 Timestamp/datetime 对象按格式符转成自定义字符串的方法。**

## 用法

**语法**：`Timestamp.strftime(format)`（datetime 对象同此法）

**参数**：
- `format`：格式字符串，定义输出的日期文本样式；`%Y` 表示四位年份、`%m` 表示月份、`%d` 表示日期，这三位必须用大写 Y 和小写 m、d，且可在字符串中直接夹入普通字符（如「年」「月」「日」）

**示例**：

```python
import pandas as pd

d = pd.Timestamp('2020-12-01')
print(d.strftime('%Y年%m月%d日'))  # 2020年12月01日
print(d.strftime('%m-%d'))         # 12-01

df = pd.DataFrame({'日期': pd.to_datetime(['2020-12-01', '2020-12-02'])})
labels = [x.strftime('%m-%d') for x in df['日期']]  # 列表推导式批量处理整列
print(labels)          # ['12-01', '12-02']
print(df['日期'].dtype)  # datetime64[ns]，原始日期列未被修改
```

## 解释

strftime 是 Timestamp 和 datetime 对象自带的方法，接收一个格式字符串，返回排版好的日期文本。它解决的是「数据里存的是日期类型，图上却要显示成特定写法」的问题，比反复调图表参数更直接、更可控。

## 有什么用

- 把日期列转成「2020年12月1日」「12-01」等自定义文本
- 作为 plt.plot 的 x 轴数据，控制坐标轴上日期的显示样式

## 关键要点

- %Y 四位年份、%m 月份、%d 日期，大小写不可混用
- 格式串中可夹普通字符：年、月、日、-、*
- %m-%d 得 12-01；%Y年%m月%d日 得 2020年12月01日
- 转换后元素由 Timestamp 变为 str，原始日期列不被修改
- 常配合列表推导式一次性处理整列日期

## 边界与易混淆

只改显示文本，不保留时间轴语义；x 轴变成字符串分类轴后，原生日期刻度（间隔、定位器）不再生效，需要真正的时间轴控制时应改用 DateFormatter + Locator。

## 关联

- [[Timestamp]] — 前置知识
- [[列表推导式]] — 组合使用
- [[DateFormatter]] — 对比项
- [[刻度标签旋转]] — 组合使用

## 自测

为什么格式化后的日期列表要作为 plt.plot 的第一个参数传入，而不是继续用 data['日期']？::因为 Matplotlib 默认按原始数据形式显示刻度；传入字符串列表后，x 轴按列表中的文本显示，格式才生效。
想把 2020-12-01 显示成「2020年12月01日」，格式字符串该怎么写？其中哪个字母必须大写？::用 %Y年%m月%d日；%Y 的 Y 必须大写，m 和 d 用小写。

## 出处

- [孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p63 S03E14.坐标轴上面的日期格式](https://www.bilibili.com/video/BV1ji4y157uB?p=63) · 2026-11-17
