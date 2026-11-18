---
term: assert 断言
aliases: [assert, 断言语句, AssertionError]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# assert 断言

> 别名：assert、断言语句、AssertionError

**声明程序继续执行前必须成立的条件，不成立则抛 AssertionError。**

## 解释

assert 适合检查内部前置条件和不变量，帮助开发期暴露逻辑错误。它不应替代用户输入验证或正式异常处理，因为断言可能被优化关闭。

## 有什么用

- 检查函数内部前置条件
- 调试时验证不变量
- 快速失败定位逻辑错误

## 关键要点

- 条件为假时抛 AssertionError
- 适合内部检查，不适合用户输入
- 可带错误信息
- 可被 -O 优化移除
- 不能替代 try/except

## 边界与易混淆

生产环境不要依赖 assert 做安全校验或业务规则。

## 关联

- [[异常处理（tryexceptfinally）]] — 对比项
- [[Python 关键字]] — 上位概念

## 自测

为什么不能用 assert 验证用户输入？::断言可能被优化移除，且不适合面向用户的错误处理。

## 出处

- [40分钟带你了解Python中所有的关键字](https://www.bilibili.com/video/BV17pLUzdEtw) · 2026-11-18
