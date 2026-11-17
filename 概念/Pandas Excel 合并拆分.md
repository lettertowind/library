---
term: Pandas Excel 合并拆分
aliases: [Excel 拆分与合并, 多工作簿合并, 按列拆分]
kind: method
domain: 数据分析/Pandas
tags: [概念/method, 领域/数据分析]
created: 2026-11-17
updated: 2026-11-17
order: 40
stage: "S02E25 · Excel文件的拆分与合并"
---

# Pandas Excel 合并拆分

> 别名：Excel 拆分与合并、多工作簿合并、按列拆分

**用 pandas 批量合并多个 Excel 或按某列拆成多表/多文件的套路。**

## 用法

**语法**：`pd.concat(objs, ignore_index=True)`；`pd.ExcelWriter(path)` + `df.to_excel(writer, sheet_name=键)`
**参数**：
- `objs`：待合并的 DataFrame 列表，通常由 for 循环逐个 append 进空列表
- `ignore_index`：True 时重置合并后的行索引，避免原索引重复
- `ExcelWriter(path)`：一次性写多个 sheet 的上下文管理器，配合 `with` 使用
- `sheet_name`：目标工作表名，拆分时传入分组键
- `index=False`：to_excel 常用参数，写出时不带行号

**示例**：
```python
import pandas as pd

df = pd.DataFrame({'部门': ['A', 'A', 'B', 'B'], '金额': [10, 20, 30, 40]})

# 拆成同一文件的多个 sheet
with pd.ExcelWriter('out.xlsx') as writer:
    for key, g in df.groupby('部门'):
        g.to_excel(writer, sheet_name=key, index=False)

# 拆成多个独立工作簿
for key in df['部门'].drop_duplicates().tolist():
    df[df['部门'] == key].to_excel(f'{key}.xlsx', index=False)

# 合并回来：空列表 + for + concat
frames = []
for key in df['部门'].drop_duplicates().tolist():
    frames.append(pd.read_excel(f'{key}.xlsx'))
merged = pd.concat(frames, ignore_index=True)
print(len(merged))  # 4
```

## 解释

包含四类任务：多工作簿合并、多工作表合并、按列拆成多个 sheet、按列拆成多个工作簿。合并靠空表加 concat 累积，拆分靠去重取分组键加循环筛选写出。

## 有什么用

- 月度报表汇总
- 按部门/地区分发数据
- 批量整理分散的 Excel 文件

## 关键要点

- 合并：空表 + for + concat 累积
- 拆 sheet：ExcelWriter + to_excel(sheet_name=分组)
- 拆工作簿：动态拼接文件名 + to_excel
- 分组键先 drop_duplicates 再 list

## 边界与易混淆

示例为理想数据，忽略空行、合并单元格、格式颜色；复杂格式操作应改用 VBA。

## 关联

- [[pd.concat]] — 组合使用
- [[pd.ExcelWriter]] — 组合使用
- [[VBA]] — 对比项

## 自测

拆成同一文件的多个 sheet 与拆成多个独立工作簿，关键区别在哪一步？::拆 sheet 需要 ExcelWriter 并指定 sheet_name；拆工作簿直接对每个分组调用 to_excel 写独立路径。


### 补充 · 2026-11-17

共四种形态：多工作簿合并成总表（os.listdir 遍历 + 循环累加 concat）、多 sheet 合并（sheet_name=None + 遍历 sheet 名）、一张表按列拆成同一工作簿多个 sheet（ExcelWriter）、按列拆成多个独立文件（to_excel 路径拼接）。

- 合并侧关键：路径要目录加文件名拼完整，用 + 不用 &
- 合并前提是各表结构一致、每簿默认只有一张表
- 拆分侧先对目标列 drop_duplicates 再转 list 遍历
拆成同一工作簿的多个 sheet 和拆成多个独立文件，代码上最本质的差别是什么？::前者需要 ExcelWriter 承接同一个文件并最后 save/close；后者每次 to_excel 直接写一个由字符串拼接生成的新路径。
- 出处：[孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并](https://www.bilibili.com/video/BV1ji4y157uB?p=40) · 2026-11-17

## 出处

- 孙兴华《Python 数据分析三部曲》p2–p46（B站）· https://www.bilibili.com/video/BV1ji4y157uB · 2026-11-17
