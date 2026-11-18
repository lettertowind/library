---
term: eval 与 exec
aliases: [eval(), exec(), 动态执行代码, 字符串求值]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# eval 与 exec

> 别名：eval()、exec()、动态执行代码、字符串求值

**把字符串当作 Python 表达式（eval）或代码块（exec）直接执行。**

## 解释

eval 只接受单个表达式并返回其结果，适合算数值；exec 可执行多行语句、循环和赋值，返回 None，其中定义的变量会进入当前作用域。二者本质都是「把数据当代码跑」，因此有代码注入风险。

## 有什么用

- 实现简单计算器
- 动态运行拼接出来的代码片段
- 教学演示与调试

## 关键要点

- eval 有返回值，exec 永远返回 None
- exec 中定义的变量会留在当前命名空间，造成污染
- 绝不对用户输入或不可信来源使用，可被注入任意代码
- eval 可传入 globals/locals 字典限制可用名称

## 边界与易混淆

只解析字面量时应用 ast.literal_eval，它安全但不支持运算与函数调用。

## 关联

- [[命名空间（globals 与 locals）]] — 组合使用
- [[真值判断（Truthiness）]] — 对比项

## 自测

为什么不能把用户输入直接交给 eval？::用户可输入任意 Python 表达式，被当作代码执行，造成安全漏洞；解析字面量应改用 ast.literal_eval。
exec 执行后，代码块里的变量还存在吗？::存在，会进入当前作用域，可直接访问。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
