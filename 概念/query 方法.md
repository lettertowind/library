---
term: query 方法
aliases: [df.query, query, 字符串查询]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 29
stage: "S02E14 · 筛选"
---

# query 方法

> 别名：df.query、query、字符串查询

**用字符串表达式筛选 DataFrame 行的方法，语法接近 SQL。**

## 用法
**语法**：`DataFrame.query(expr, inplace=False, **kwargs)`
**参数**：
- `expr`：字符串形式的筛选条件，支持 `and`、`or`、`in`、`not in` 等 SQL 风格语法
- 条件中引用外部变量时，写成 `@变量名`
- `inplace`：布尔值，为 `True` 时直接在原 DataFrame 上修改并返回 `None`，默认 `False` 返回新对象
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'姓名': ['张三', '李四', '王五', '赵六'],
                   '城市': ['北京', '上海', '北京', '广州'],
                   '年龄': [23, 35, 28, 41]})
城市列表 = ['北京', '广州']
# 列名不加引号，外部变量用 @ 引用
print(df.query("城市 in @城市列表 and 年龄 > 25"))
#    姓名  城市  年龄
# 2  王五  北京  28
# 3  赵六  广州  41
```

## 解释

query 接收一个字符串条件，内部解析列名和比较表达式，避免反复写 数据['列']。支持 and/or/in 等 SQL 风格语法，条件多时比布尔索引更清晰。

## 有什么用

- 多条件组合筛选
- 用 in 匹配多个指定值
- 日期范围叠加类别条件

## 关键要点

- 条件写成字符串，外层双引号内层单引号避免冲突
- 支持 and、or、in 等 SQL 风格语法
- 引用外部变量用 @变量名
- 日期条件写在 query 里时不要把日期设为索引
- 条件多时比布尔索引可读性更好

## 边界与易混淆

条件少时布尔索引同样可行；日期列若设为索引会导致 query 日期条件报错。

## 关联

- [[布尔索引筛选]] — 对比项
- [[数据筛选]] — 上位概念
- [[dt 访问器]] — 组合使用

## 自测

query 中要引用外部变量 数据，字符串里应该怎么写？::用 @数据 引用外部变量。
为什么用 query 写日期条件时不能把出生日期设为索引？::日期作为索引时 query 无法按列名解析日期条件，会报错；应保持默认索引或序号索引。


### 补充 · 2026-11-17

支持 and/or/in 等逻辑，可直接写列名，条件多时比布尔索引更简洁。还可用 @ 引用外部变量。

- 使用小括号，区别于 loc 的中括号
- 支持 and、or、in 运算符
- @ 可引用外部 DataFrame 变量如 @数据.出生日期.dt.year
query 中引用外部 DataFrame 变量用什么符号？::@ 符号，例如 @数据.出生日期.dt.year。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p29 S02E14.筛选](https://www.bilibili.com/video/BV1ji4y157uB?p=29) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
