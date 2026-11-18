---
term: 异常处理（tryexceptfinally）
aliases: [try/except, 异常处理, try except finally, raise]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# 异常处理（tryexceptfinally）

> 别名：try/except、异常处理、try except finally、raise

**用 try 包裹风险代码，except 捕获处理，finally 做收尾的机制。**

## 解释

try 中代码可能抛异常，except 捕获指定异常并处理，finally 无论是否异常都会执行。raise 可主动抛出异常，交给上层处理。它让程序在错误发生时可控降级而不是直接崩溃。

## 有什么用

- 捕获除零、类型转换等运行时错误
- 资源清理与连接关闭
- 主动抛出非法状态

## 关键要点

- except 可指定异常类型并命名
- finally 总执行，适合清理
- raise 主动抛异常
- try 不要包裹过大代码块
- 异常处理不能替代输入校验

## 边界与易混淆

不要用异常处理做普通流程控制；捕获过宽会掩盖 bug。

## 关联

- [[assert 断言]] — 对比项
- [[with 语句（上下文管理）]] — 组合使用

## 自测

finally 与 except 的执行区别？::except 只在捕获到异常时执行；finally 无论是否异常都执行。

## 出处

- [40分钟带你了解Python中所有的关键字](https://www.bilibili.com/video/BV17pLUzdEtw) · 2026-11-18
