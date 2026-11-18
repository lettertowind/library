---
term: to_csv
aliases: [DataFrame.to_csv, 写出 CSV]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 16
stage: "S02E01 · 数据类型与新建文件"
---

# to_csv

> 别名：DataFrame.to_csv、写出 CSV

**把 DataFrame 写出为逗号分隔纯文本文件的 Pandas 方法。**

## 用法
**语法**：`DataFrame.to_csv(path_or_buf, sep=',', index=True, encoding=None, header=True)`
**参数**：
- `path_or_buf`：输出路径或文件名，如 `'data.csv'`；不传则返回字符串
- `sep`：分隔符，默认 `','`，存 Tab 分隔文本可设为 `'\t'`
- `index`：是否把行索引写成一列，默认 `True`，通常设为 `False`
- `header`：是否写出列名，默认 `True`
- `encoding`：文件编码，中文内容建议 `'utf-8-sig'`，方便 Excel 打开
**示例**：
```python
import pandas as pd

data = pd.DataFrame({'姓名': ['张三', '李四'], '分数': [90, 85]})
data.to_csv('score.csv', index=False, encoding='utf-8-sig')
print(pd.read_csv('score.csv'))
#    姓名  分数
# 0  张三  90
# 1  李四  85
```
注意调用形式是 `data.to_csv(path)`，不是 `pd.to_csv`；与 `to_excel` 只差方法名和文件后缀。

## 解释

to_csv 是 DataFrame 的写出方法，将二维表保存为 CSV 纯文本，默认逗号分隔。它与 to_excel 写法几乎一致，只改方法名和文件后缀即可切换格式。

## 有什么用

- 把清洗后的数据保存为 CSV 供后续读取
- 批量导出多张表为纯文本格式

## 关键要点

- 调用形式是 data.to_csv(path)，不是 pd.to_csv
- CSV 本质是纯文本，可用逗号或 Tab 等分隔符
- 与 to_excel 只差方法名和文件后缀
- 默认会把索引也写成一列，需要时可关闭

## 边界与易混淆

CSV 不保存格式、公式和多工作表，只适合纯数据交换。

## 关联

- [[DataFrame.to_excel]] — 对比项
- [[pd.read_csv]] — 对比项
- [[DataFrame]] — 上位概念

## 自测

已有 data 这个 DataFrame，要生成 CSV 文件，代码和生成 Excel 的写法差在哪？::只把 data.to_excel(path) 换成 data.to_csv(path)，并把路径后缀改为 .csv。
为什么说 CSV 文件可以用记事本打开查看？::因为 CSV 本质是逗号分隔的纯文本，不含二进制格式信息。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
