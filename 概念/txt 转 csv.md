---
term: txt 转 csv
aliases: [txt 转 csv, 文本转 csv, to_csv 转换]
kind: method
domain: Pandas
tags: [概念/method, 领域/Pandas]
created: 2026-11-17
updated: 2026-11-17
order: 17
stage: "S02E02 · 读取txt与csv文件"
---

# txt 转 csv

> 别名：txt 转 csv、文本转 csv、to_csv 转换

**用 read_csv 读 txt 再 to_csv 写出为 csv 的两步转换法。**

## 用法
**语法**：`pd.read_csv(filepath_or_buffer, sep=',', encoding=None)` → `DataFrame.to_csv(path_or_buf, sep=',', index=True, encoding=None)`
**参数**：
- `read_csv` 的 `filepath_or_buffer`：txt 文件路径
- `read_csv` 的 `sep`：分隔符，txt 常见用 `'\t'` 或逗号，默认 `','`
- `read_csv` 的 `encoding`：读入编码，乱码时设 `'utf-8'` 或 `'gbk'`
- `to_csv` 的 `path_or_buf`：输出的 csv 文件路径
- `to_csv` 的 `index`：是否写出索引列，默认 `True`，不需要时设 `False`
- `to_csv` 的 `encoding`：写出编码，同样可设 `'utf-8'`
**示例**：
```python
import pandas as pd

# 先造一个 txt 数据文件（实际使用时换成你自己的 txt 路径）
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('姓名,分数\n杨过,90\n小龙女,95\n')

data = pd.read_csv('data.txt', encoding='utf-8')   # 第一步：读入 txt
data.to_csv('data.csv', index=False, encoding='utf-8')  # 第二步：写出 csv

print(data)
#    姓名  分数
# 0  杨过  90
# 1  小龙女 95
print(pd.read_csv('data.csv'))
#    姓名  分数
# 0  杨过  90
# 1  小龙女 95
```

## 解释

实际大数据分析更推荐 csv 而非 txt。转换只需 read_csv 读入、to_csv 写出两步；若乱码可在读或写时指定 encoding='utf-8'。

## 有什么用

- 把 txt 数据规范为 csv
- 统一数据格式便于后续分析

## 关键要点

- 两步：read_csv 读入 + to_csv 写出
- 乱码时读写都可加 encoding='utf-8'
- 大数据分析优先用 csv 存储

## 边界与易混淆

转换会重写文件，注意不要覆盖原始数据。

## 关联

- [[pd.read_csv]] — 组合使用
- [[DataFrame.to_excel]] — 对比项

## 自测

txt 转 csv 的核心两行代码是什么？::data = pd.read_csv('data.txt')；data.to_csv('data.csv')。

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
