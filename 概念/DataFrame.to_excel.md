---
term: DataFrame.to_excel
aliases: [to_excel, 写入 Excel]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
order: 40
---

# DataFrame.to_excel

> 别名：to_excel、写入 Excel

**把 DataFrame 写出为 Excel 文件或写入指定工作表的函数。**

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

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
