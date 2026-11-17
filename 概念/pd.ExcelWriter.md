---
term: pd.ExcelWriter
aliases: [ExcelWriter, Excel 写入对象]
kind: tool
domain: 数据分析/Pandas
tags: [概念/tool, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
---

# pd.ExcelWriter

> 别名：ExcelWriter、Excel 写入对象

**pandas 中向同一个 Excel 文件写入多个工作表的写入器对象。**

## 用法
**语法**：`pd.ExcelWriter(path, engine=None, mode='w', if_sheet_exists=None)`
**参数**：
- `path`：目标 Excel 文件路径，或类文件对象
- `engine`：写入引擎，常用 `'openpyxl'`、`'xlsxwriter'`；不填则按扩展名自动推断
- `mode`：`'w'` 覆盖重建（默认），`'a'` 向已有文件追加
- `if_sheet_exists`：仅在 `mode='a'` 时生效，同名工作表处理方式为 `'error'`（默认）/`'new'`/`'replace'`/`'overlay'`
**示例**：
```python
import pandas as pd

df = pd.DataFrame({'城市': ['北京', '上海'], '销量': [120, 95]})
with pd.ExcelWriter('out.xlsx', engine='openpyxl') as writer:  # 新版用 with，勿用已弃用的 save()
    df.to_excel(writer, sheet_name='总表', index=False)
    df[df['销量'] > 100].to_excel(writer, sheet_name='筛选', index=False)

print(pd.read_excel('out.xlsx', sheet_name=None).keys())
# dict_keys(['总表', '筛选'])
```

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


### 补充 · 2026-11-17

直接 to_excel 会覆盖整个文件，无法把多张表写进同一个工作簿。ExcelWriter 先打开一个文件句柄，再用 df.to_excel(writer, sheet_name=名) 逐张写入，最后 save() 与 close() 落盘。

- 标准形式：writer = pd.ExcelWriter(路径)
- 写入用 df.to_excel(writer, sheet_name=工作表名)
- 结尾必须 writer.save() 加 writer.close()，漏了文件不完整
要把数据拆成办公室.xlsx、销售部.xlsx 三个独立文件，需要用 ExcelWriter 吗？::不需要。每个部门是独立文件，循环里直接 df.to_excel("C:/" + 部门 + ".xlsx") 即可。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并](https://www.bilibili.com/video/BV1ji4y157uB?p=40) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
