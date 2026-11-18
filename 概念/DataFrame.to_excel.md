---
term: DataFrame.to_excel
aliases: [to_excel, 写入 Excel]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
---

# DataFrame.to_excel

> 别名：to_excel、写入 Excel

**把 DataFrame 写出为 Excel 文件或写入指定工作表的函数。**

## 用法
**语法**：`DataFrame.to_excel(excel_writer, sheet_name='Sheet1', index=True, columns=None)`
**参数**：
- `excel_writer`：文件路径字符串，或 `pd.ExcelWriter` 对象；传路径生成独立文件，传 writer 则写入该文件的一个 sheet
- `sheet_name`：工作表名，默认 `'Sheet1'`；传 writer 时用它区分多个 sheet
- `index`：是否把行索引写成一列，默认 `True`，一般设为 `False`
- `columns`：指定要写出的列，默认 `None` 表示全部列
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'部门': ['A', 'B'], '销量': [10, 20]})

# 传路径：生成独立文件，变量名不影响输出位置
df.to_excel('out.xlsx', index=False)

# 传 writer：同一文件写多个 sheet（现代写法，用 with 自动关闭）
with pd.ExcelWriter('multi.xlsx') as writer:
    df.to_excel(writer, sheet_name='全部', index=False)
    df[df['部门'] == 'A'].to_excel(writer, sheet_name='A部', index=False)

# 读回验证：index=False 时不会多出 Unnamed: 0 列
print(pd.read_excel('out.xlsx').columns.tolist())  # ['部门', '销量']
print(pd.ExcelFile('multi.xlsx').sheet_names)      # ['全部', 'A部']
```

## 解释

to_excel 的第一个参数可以是文件路径，也可以是 ExcelWriter 对象。传路径时生成独立工作簿，传 writer 时写入该文件的指定 sheet。index=False 可去掉默认行索引。

## 有什么用

- 把合并结果保存为新 Excel
- 配合 ExcelWriter 写入多个 sheet
- 按部门动态生成多个工作簿

## 关键要点

- 传路径=独立文件，传 writer=同一文件的一个 sheet
- index=False 取消默认索引列
- 输出位置由参数路径决定，与变量名无关
- 动态文件名用字符串拼接：路径 + 名称 + '.xlsx'

## 边界与易混淆

不保留原 Excel 的格式与样式；文件名含特殊字符时需先做合法性处理。

## 关联

- [[pd.ExcelWriter]] — 组合使用
- [[pd.read_excel]] — 对比项

## 自测

变量名叫“合并表”，to_excel('c:/out.xlsx') 后文件叫什么？变量名影响输出吗？::文件叫 out.xlsx，变量名只是内存中的名字，不影响输出路径。


### 补充 · 2026-11-17

df.to_excel(路径) 将内存中的表落盘为 xlsx；若路径与源文件相同则直接覆盖原文件，因此可用“读入—修正结构—写回”的方式原地修复 Excel。

- 写回原路径即覆盖原文件，操作前建议备份
- 默认会把索引也写成一列
- 多表写入需配合 pd.ExcelWriter
为什么说 to_excel 写回原路径能“修复”原文件？::因为写出会覆盖原文件，读入时用 header/names/index_col 修正的结构会随写出一并落到磁盘。

传入文件路径则新建文件，传入 ExcelWriter 对象则写入该写入器管理的文件（可继续追加其他 sheet）。index=False 控制不写行索引，sheet_name 控制落到哪个工作表。它属于 to_* 写出方法家族，与 to_csv 等用法同构。

- 第一个参数可以是路径字符串，也可以是 ExcelWriter 对象
- index=False 是导出报表几乎必加的选项
- 用 ExcelWriter 时必须配合 save() 与 close() 才会落盘
to_excel 传路径和传 ExcelWriter 有什么区别？::传路径直接生成一个文件；传 ExcelWriter 只是把数据交给写入器，还需 save/close 才真正写盘，且可写多个 sheet。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p44 S02E29.vlookup](https://www.bilibili.com/video/BV1ji4y157uB?p=44) · 2026-11-17

它是数据处理闭环的最后一环：读入、清洗、改表头设索引之后，用 to_excel 把结果落盘。因为会静默覆盖同名文件，路径写错就可能毁掉原始数据。

- DataFrame → Excel，与 read_excel 方向相反
- 路径相同即覆盖原文件，运行前先确认路径与文件名
- 默认会把行索引一起写入，成为首列
为什么用 to_excel 写回同一路径有风险？::它会静默覆盖同名文件，路径或文件名写错就会丢掉原始数据，且无法撤销。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p19 S02E04.读取与修改Excel文件](https://www.bilibili.com/video/BV1ji4y157uB?p=19) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
