---
term: 写回原 Excel 文件
aliases: [ExcelWriter 写回, 覆盖原表, save 与 close]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
---

# 写回原 Excel 文件

> 别名：ExcelWriter 写回、覆盖原表、save 与 close

**用 pd.ExcelWriter 打开目标文件，to_excel 写入后 save 并 close。**

## 用法
**语法**：`pd.ExcelWriter(path, engine=None, mode='w', if_sheet_exists=None)`
**参数**：
- `path`：目标 Excel 文件路径，直接给原文件名即表示写回原工作簿
- `engine`：写入引擎，常用 `'openpyxl'`（.xlsx）；不写则由 pandas 按后缀推断
- `mode`：`'w'` 覆盖原文件（默认）；`'a'` 在原有内容上追加，适合保留原表其他工作表
- `if_sheet_exists`：仅 `mode='a'` 时生效，同名工作表可选 `'error'`／`'new'`／`'replace'`／`'overlay'`
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'姓名': ['杨过', '小龙女'], '分数': [90, 95]})
path = 'demo.xlsx'

with pd.ExcelWriter(path, engine='openpyxl') as writer:  # 上下文写法，退出自动 close
    df.to_excel(writer, sheet_name='原表', index=False)
    df.to_excel(writer, sheet_name='备份', index=False)

print(list(pd.read_excel(path, sheet_name=None)))
# 输出：['原表', '备份']

# 旧版写法：writer = pd.ExcelWriter(path); df.to_excel(writer, index=False); writer.save(); writer.close()
# pandas 2.0 起 writer.save() 已移除，用 with 上下文或 writer.close() 落盘
```

## 解释

to_excel 直接给路径会新建/覆盖文件，但要写回原工作簿并控制写入过程，需用 ExcelWriter 作为上下文对象，写完调用 save() 和 close() 落盘。

## 有什么用

- 把处理结果覆盖写回原 Excel
- 一次写入多个工作表

## 关键要点

- writer = pd.ExcelWriter('文件.xlsx') 创建写入器
- to_excel(writer, index=False) 不写行索引
- 必须 writer.save() 再 writer.close() 才真正落盘
- 拼写是 writer 不是 waiter

## 边界与易混淆

新版 Pandas 推荐 with pd.ExcelWriter(...) as writer 上下文写法，自动关闭。

## 关联

- [[pd.ExcelWriter]] — 上位概念
- [[DataFrame.to_excel]] — 组合使用

## 自测

只调用 to_excel(writer) 不 save/close 会怎样？::数据可能没有真正写入文件，文件内容不完整或为空。


### 补充 · 2026-11-17

流程固定四步：writer = pd.ExcelWriter(路径) 打开写入器，df.to_excel(writer, index=False) 写入内容，writer.save() 落盘，writer.close() 释放文件句柄。save 和 close 缺一不可，否则文件可能为空或被占用。index=False 用来避免把行号也写进表格。

- 路径传原文件即为覆盖写回，传新路径则为另存
- index=False 一定要加，否则多出一列无意义的行号
- save() 与 close() 都不能省，两步都执行完才算写完
只调用 save() 不调用 close() 会有什么风险？::文件句柄未释放，文件可能被占用，后续读写异常。
index=False 不加会怎样？::会把 RangeIndex 当成一列写进 Excel，多出无意义的行号列。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p44 S02E29.vlookup](https://www.bilibili.com/video/BV1ji4y157uB?p=44) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
