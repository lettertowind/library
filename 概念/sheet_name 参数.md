---
term: sheet_name 参数
aliases: [sheet_name, 工作表参数]
kind: concept
domain: 数据分析/Pandas
tags: [概念/concept, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
order: 40
---

# sheet_name 参数

> 别名：sheet_name、工作表参数

**read_excel 中用于指定读取哪些工作表的参数。**

## 解释

sheet_name 控制读取范围：默认读第一个表，传名称读指定表，传列表读多个表，传 None 读全部并返回字典。它是多工作表合并任务的前置开关。

## 有什么用

- 读取工作簿中全部工作表
- 只读取指定的几个 sheet
- 按名称或索引定位工作表

## 关键要点

- None = 全部工作表，返回字典
- 可传名称、索引或混合列表，如 [0,1,'Sheet5']
- 工作表索引从 0 开始
- 返回字典时用 keys() 取工作表名列表

## 边界与易混淆

传 None 时返回结构从 DataFrame 变为字典，后续代码要相应调整。

## 关联

- [[pd.read_excel]] — 上位概念
- [[header 参数]] — 组合使用

## 自测

sheet_name=None 和 sheet_name=0 的返回结果有什么本质区别？::None 返回包含全部工作表的字典；0 只返回第一个工作表的单个 DataFrame。


### 补充 · 2026-11-17

一个 Excel 文件可有多个工作表，read_excel 第二个参数即工作表名，可用位置参数或 sheet_name= 关键字传入。不指定时可能读到非预期工作表。

- 第二个参数通常是工作表名
- 可位置传参，也可 sheet_name= 关键字传
- 多工作表文件必须明确指定
read_excel("a.xlsx", "1") 与 read_excel("a.xlsx", sheet_name="1") 有何区别？::前者是位置参数，后者是关键字参数，效果相同但写法不能混用。

一个 Excel 工作簿可含多张工作表，sheet_name 让 Pandas 直接读取指定表，无需先用 VBA 拆分工作簿。可传工作表名称字符串或从 0 开始的索引。

- 可传名称：sheet_name='11'
- 可传索引：sheet_name=1
- 指定不存在的工作表会报错
sheet_name=1 和 sheet_name='1' 有什么区别？::前者按工作表索引（第 2 张表）读取，后者按工作表名称 '1' 读取。

一个 Excel 文件含多个工作表时，read_excel 默认只读第一个。用 sheet_name 指定名称（如 '花名册'）或索引，传列表可一次读多个表返回字典。

- 默认读取第一个工作表
- 可传表名字符串或 0 基索引
- 传列表返回 {表名: DataFrame} 字典
一个 Excel 有两个 sheet，想一次都读进来怎么写？::sheet_name=['花名册','成绩单'] 或 sheet_name=None，返回字典。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
