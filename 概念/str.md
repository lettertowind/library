---
term: str
aliases: [字符串, 字符串类型, Python 字符串]
kind: concept
domain: 计算机/编程/Python
tags: [概念/concept, 领域/计算机]
created: 2026-11-18
updated: 2026-11-18
---

# str

> 别名：字符串、字符串类型、Python 字符串

**Python 中表示文本的不可变序列类型，元素是 Unicode 码点。**

## 解释

str 是 Python 3 的内置文本类型。它不可变——任何"修改"操作都会返回新对象，原对象不变。下标访问 `s[i]` 取单个字符，切片 `s[a:b:step]` 取子串，`len(s)` 返回码点数量。文本与字节严格分离：网络和文件里的是 `bytes`，需要用 `encode` / `decode` 互转。

## 有什么用

- 处理一切文本：日志、网页、CSV、用户输入
- 拼接、格式化、查找、替换、切分
- 与 bytes 互转，处理编码问题（UTF-8、GBK）

## 关键要点

- 不可变：`s += x` 实际新建对象，大量拼接用 `"".join(parts)`
- `len()` 数的是码点，不是显示宽度，emoji 和组合字符会与直觉不符
- 优先用 f-string 格式化：`f"{name} 共 {n} 条"`
- 三个引号 `'''...'''` 保留换行，适合多行文本
- `str` 与 `bytes` 不能直接相加，必须先 encode 或 decode

## 边界与易混淆

与 `bytes` 的核心区别：str 是码点序列，bytes 是字节序列。`"中".encode("utf-8")` 是 3 个字节，`len` 却是 1。用错误的编码 decode 会得到乱码或 `UnicodeDecodeError`。

## 关联

- [[ord（字符转码点）]] — 取单字符的码点
- [[chr]] — 由码点生成字符
- [[slice（切片对象）]] — 切片语法
- [[原始字符串]] — 不转义的字面量写法

## 自测

Python 3 里 str 和 bytes 的关键区别是什么？::str 是 Unicode 码点序列，bytes 是字节序列；两者必须用 encode / decode 互转，不能直接拼接。

## 出处

- [【中文字幕】Python必须会的49个内置函数](https://www.bilibili.com/video/BV1bbGyzsECP) · 2026-11-18
