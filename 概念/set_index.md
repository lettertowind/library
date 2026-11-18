---
term: set_index
aliases: [df.set_index, 设置索引]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 35
stage: "S02E20 · 多层索引与多层索引计算"
---

# set_index

> 别名：df.set_index、设置索引

**将 DataFrame 的一列或多列设置为行索引的方法。**

## 用法
**语法**：`DataFrame.set_index(keys, drop=True, inplace=False)`

**参数**：
- `keys`：要设为索引的列名，可以是单个列名或列名列表（传入列表即得到多层索引）
- `drop`：默认 `True`，把设为索引的列从普通数据列中移除；设为 `False` 则保留
- `inplace`：默认 `False` 返回新 DataFrame，设为 `True` 则原地修改原对象

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'班级': ['一班', '一班', '二班'],
                   '学号': [1, 2, 1],
                   '姓名': ['张三', '李四', '王五']})

# 单层索引：把「学号」提升为行索引
print(df.set_index('学号'))
#       班级  姓名
# 学号
# 1     一班  张三
# 2     一班  李四
# 1     二班  王五

# 多层索引：传入列名列表
print(df.set_index(['班级', '学号']))
#         姓名
# 班级 学号
# 一班 1    张三
#      2    李四
# 二班 1    王五

# 原对象未被修改，默认返回新 DataFrame
print(df.index)
# RangeIndex(start=0, stop=3, step=1)
```

## 解释

set_index 在读取数据后调用，传入列名列表即可把多列设为多层行索引。它与读取时用 index_col 指定索引列效果等价，适合先读数据再调整索引结构的场景。

## 有什么用

- 读取后设置单层或多层行索引
- 把普通列转为索引以方便查询

## 关键要点

- 传入列名列表可设置多层索引
- 与 read_excel 的 index_col 效果等价
- 默认返回新 DataFrame，不修改原对象

## 边界与易混淆

与 index_col 的区别只在调用时机：一个读取时设置，一个读取后设置。

## 关联

- [[分层索引]] — 组合使用
- [[index_col 参数]] — 对比项

## 自测

set_index(['班级','学号']) 和 read_excel(index_col=[0,1]) 有什么区别？::效果等价，只是设置时机不同：前者读取后设置，后者读取时直接指定。


### 补充 · 2026-11-17

set_index 将指定业务字段提升为行索引，替代默认的 0、1、2 整数索引。写出文件时默认索引列就不会作为多余的一列出现，常用于让导出结果更干净。

- set 是设置、index 是索引，合起来即设置索引
- 默认返回新对象，需重新赋值或加 inplace
- 设为索引的列不再是普通数据列
导出 Excel 时多出一列 0、1、2，用 set_index 怎么解决？::把某个业务字段设为索引，如 data.set_index('序号')，默认整数索引就不再作为列写出。
set_index 之后原来的那一列还在普通列里吗？::不在了，它变成了行索引，需通过 index 访问。

set 是设置、index 是索引，set_index("序号") 就是拿“序号”这一列当行标签。当导出到 Excel/CSV 时不想要默认的 0 起始索引列，可用它把业务字段设为索引，默认索引列就自然消失。

- 写法 data = data.set_index("序号")，必须重新赋值才生效
- 执行顺序：先 set_index，再 to_excel/to_csv
- 指定业务列做索引后，导出文件不再多出 0 起始索引列
写完 data.set_index("序号") 后直接 to_excel，导出的文件会变化吗？::不会。没有把返回值赋回 data，原 DataFrame 的行索引没变，导出结果照旧带默认索引列。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p16 S02E01.数据类型与新建文件](https://www.bilibili.com/video/BV1ji4y157uB?p=16) · 2026-11-17

默认索引对业务无意义，把「序号」「日期」这类唯一标识设为索引后，就能用业务值直接定位行、做标签切片。默认返回新表，需用赋值接收或加 inplace。它也常用在读取之后补设日期索引的场景。

- 写法 df.set_index('列名')，默认返回新对象，要赋值接收
- 读取阶段可直接用 index_col 参数一步到位
- 设置后原列从列区消失，成为行索引
执行 数据.set_index('序号') 后 print(数据) 发现索引没变，原因是什么？::set_index 默认返回新对象而不改动原表，需要写成 数据 = 数据.set_index('序号') 或加 inplace=True。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p28 S02E13.数据查询](https://www.bilibili.com/video/BV1ji4y157uB?p=28) · 2026-11-17

自动填充完成后用 数据.set_index('序号', inplace=True)，序号列变成行标签，表格更接近 Excel 的呈现。它只改索引，不新增也不删除数据列（默认 drop=True 时原列移入索引）。

- 必须放在 for 循环之外，否则循环依据的索引被改掉，结果错乱
- inplace=True 表示原地修改，不返回新对象
- 默认 drop=True，该列从数据列中移走，成为索引
为什么不能在填充循环之前就 set_index('序号')？::循环依赖 数据.index 的行号，索引被换成序号后 i 的取值逻辑全变了，容易报错或填错
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p25 S02E10.各种数据自动填充](https://www.bilibili.com/video/BV1ji4y157uB?p=25) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
