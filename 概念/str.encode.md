---
term: str.encode
aliases: [encode, 编码转换]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 38
stage: "S02E23 · 字符串操作（上）"
---

# str.encode

> 别名：encode、编码转换

**把字符串按指定格式编码为字节的方法。**

## 用法

**语法**：`str.encode(encoding='utf-8', errors='strict')`
**参数**：
- `encoding`：目标字符集，默认 `'utf-8'`，中文场景常用 `'utf-8'`、`'gbk'`
- `errors`：编码出错时的处理策略，默认 `'strict'` 直接抛异常，也可用 `'ignore'`、`'replace'`
**示例**：

```python
import pandas as pd

s = pd.Series(['张三', '李四'])
b = s.str.encode('utf-8')
print(b)
# 0    b'\xe5\xbc\xa0\xe4\xb8\x89'
# 1    b'\xe6\x9d\x8e\xe5\x9b\x9b'
# dtype: object
print(b.str.decode('utf-8').tolist())
# ['张三', '李四']

# 编码与解码格式不一致会报错或乱码，必须配对
print(s.str.encode('gbk').str.decode('gbk').tolist())
# ['张三', '李四']
```

## 解释

str.encode('utf-8') 将字符串编码为指定字符集，常用于处理 CSV 中文乱码问题。与 str.decode 配对使用，一编一解。

## 有什么用

- 处理中文乱码
- 把文本转为字节流

## 关键要点

- 参数为编码格式，如 utf-8
- 与 decode 方向相反
- 本课了解即可，遇到转码问题再查

## 边界与易混淆

编码与解码必须配对，格式不一致会乱码或报错。

## 关联

- [[str.decode]] — 对比项
- [[Series.str 访问器]] — 上位概念

## 自测

encode 和 decode 的方向区别是什么？::encode 把字符串编码为字节，decode 把字节解码回字符串。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
