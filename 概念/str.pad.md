---
term: str.pad
aliases: [pad, 填充对齐]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.pad

> 别名：pad、填充对齐

**用指定字符把字符串填充到指定宽度的方法。**

## 用法
**语法**：`Series.str.pad(width, side='left', fillchar=' ')`
**参数**：
- `width`：目标总宽度，若原字符串长度已不小于该值，则原样返回
- `side`：填充方向，`'left'` 表示在左侧填充（右对齐），`'right'` 表示在右侧填充（左对齐），`'both'` 表示两端填充
- `fillchar`：填充字符，只能是一个字符，默认空格，多字符会报错
**示例**：
```python
import pandas as pd

s = pd.Series(['ab', 'abc', 'a'])
print(s.str.pad(5, side='left', fillchar='*').tolist())
# ['***ab', '**abc', '****a']
print(s.str.pad(5, side='right', fillchar='0').tolist())
# ['ab000', 'abc00', 'a0000']
print(s.str.pad(5, side='both', fillchar='-').tolist())
# ['--ab-', '-abc-', '--a--']
print(s.str.pad(2, side='left').tolist())  # 宽度不足时原样返回
# ['ab', 'abc', 'a']
```

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


### 补充 · 2026-11-17

定义宽度和填充字符后自动补足长度，side 参数决定补在哪一侧。center、ljust、rjust 都是它的衍生写法，记住 pad 一个即可覆盖。

- width 指补齐后的总宽度，fillchar 只能是单个字符
- side 取 left（默认）、right 或 both
- center、ljust、rjust 是衍生方法，优先记 pad
想让填充出现在两端，side 传什么？::'both'
zfill 与 pad 的关键差别是什么？::zfill 只能用 0 从左侧补，pad 可指定填充字符和方向
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p38 S02E23.字符串操作（上）](https://www.bilibili.com/video/BV1ji4y157uB?p=38) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
