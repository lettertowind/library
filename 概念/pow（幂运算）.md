---
term: pow（幂运算）
aliases: [pow, pow(), 模幂运算, pow(base, exp, mod)]
kind: method
domain: 计算机/编程/Python
tags: [概念/method, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# pow（幂运算）

> 别名：pow、pow()、模幂运算、pow(base, exp, mod)

**计算 base 的 exp 次方，可附加模数一步完成取模。**

## 解释

pow(base, exp) 等价于 base ** exp；第三个参数 mod 让它变成模幂运算，返回 base**exp % mod。模幂在密码学（如 RSA）里非常重要，因为它能在大数上高效计算而不必先算出巨大的幂。

## 有什么用

- 普通幂运算
- 大数取模、密码学算法

## 关键要点

- pow(2, 3) 返回 8，等价于 2 ** 3
- pow(5, 2, 3) 返回 1，即 25 % 3
- 带 mod 时比先算幂再取模更高效

## 边界与易混淆

mod 只能传整数；浮点参与模幂会报错。

## 关联

- [[地板除与取余（ 与 %）]] — 组合使用

## 自测

pow(5, 2, 3) 为什么不是先算出 25 再取模这么简单？::它内部用快速模幂算法，指数很大时也不会先构造出天文数字的中间结果。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
