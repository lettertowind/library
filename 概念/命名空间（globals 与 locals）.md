---
term: 命名空间（globals 与 locals）
aliases: [globals(), locals(), 全局命名空间, 局部命名空间]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 命名空间（globals 与 locals）

> 别名：globals()、locals()、全局命名空间、局部命名空间

**变量名到对象的映射关系，Python 分为全局与局部两个层级。**

## 解释

globals() 返回模块级变量的字典，locals() 返回当前局部作用域的字典。在模块顶层两者内容基本相同；进入函数后 locals 只含函数内变量，而 globals 仍是全局那份。

## 有什么用

- 调试时查看当前有哪些变量
- 按键名动态取变量值
- 理解作用域与变量生命周期

## 关键要点

- 两者都以字典形式呈现，可按变量名取值
- 函数内 locals() 不包含全局变量
- 修改 globals() 返回的字典会真实改变全局变量
- 函数内调用 globals() 返回的仍是全局变量

## 边界与易混淆

不要用拼变量名 + globals/locals 动态赋值来替代字典等正常数据结构，代码会难以追踪；对 locals() 写入在不同实现下行为不可靠。

## 关联

- [[字典（dict）]] — 组合使用
- [[内省（dir 与 help）]] — 组合使用

## 自测

在函数内部调用 globals() 能看到该函数的局部变量吗？::不能，globals 只返回模块级全局作用域的名称。
在模块顶层，globals() 与 locals() 有什么区别？::基本一致，此时局部作用域就是全局作用域。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
