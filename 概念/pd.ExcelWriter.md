---
term: pd.ExcelWriter
aliases: [ExcelWriter, Excel 写入对象]
kind: tool
domain: 计算机/数据分析/Pandas
tags: [概念/tool, 领域/计算机]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
order: 40
---

# pd.ExcelWriter

> 别名：ExcelWriter、Excel 写入对象

**pandas 中向同一个 Excel 文件写入多个工作表的写入器对象。**

## 解释

ExcelWriter 打开一个 Excel 文件作为写入目标，之后多次调用 DataFrame.to_excel(writer, sheet_name=...) 可把不同数据写进同一文件的不同 sheet，最后 save/close 落盘。没有它，多次 to_excel 会互相覆盖。

## 有什么用

- 把一个工作表按某列拆成同一文件的多个 sheet
- 向一个 Excel 追加多个数据表

## 关键要点

- 必须先创建 writer，再逐表 to_excel 写入
- sheet_name 参数决定写入哪个工作表
- 最后要 save() 和 close()，新版建议用上下文管理器
- 拆成多个独立工作簿时不需要它

## 边界与易混淆

只管写入，不负责拆分逻辑；新版 pandas 中 writer.save() 已弃用，应使用 close() 或 with 语句。

## 关联

- [[pd.read_excel]] — 对比项
- [[DataFrame.to_excel]] — 组合使用

## 自测

不用 ExcelWriter，循环里直接对同一路径调用 to_excel 会怎样？::后一次写入会覆盖前一次，最终文件只剩最后一个工作表的数据。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
