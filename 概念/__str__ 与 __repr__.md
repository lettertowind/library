---
term: __str__ 与 __repr__
aliases: [__str__, __repr__, 字符串表示方法, str/repr]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# __str__ 与 __repr__

> 别名：__str__、__repr__、字符串表示方法、str/repr

**控制对象被打印和查看时显示文本的两个特殊方法。**

## 解释

__str__ 返回面向用户的易读文本，print(obj) 和 str(obj) 优先用它。__repr__ 返回面向开发者的详细表示，repr(obj) 和交互式查看优先用它。没有 __str__ 时，打印会回退到 __repr__。

## 有什么用

- 让 print(obj) 输出可读内容
- 调试时显示对象的构造参数

## 关键要点

- __str__ 面向用户，__repr__ 面向开发者
- print/str 优先 __str__
- repr 和交互式查看优先 __repr__
- 无 __str__ 时打印回退 __repr__

## 边界与易混淆

默认未定义时通常显示内存地址，不利于阅读；两者不要写成相同内容。

## 关联

- [[dunder 方法]] — 上位概念
- [[对象（实例）]] — 组合使用

## 自测

如果类只定义了 __repr__，print(obj) 会显示什么？::会回退使用 __repr__ 的返回值。

## 出处

- [【中文字幕】最强Python教学-20分钟学会面向对象编程](https://www.bilibili.com/video/BV1m7L1zaEH8) · 2026-11-18
