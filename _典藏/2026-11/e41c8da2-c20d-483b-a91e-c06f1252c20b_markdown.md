# Pandas 数据排序（p27 S02E12）

## 学习目标

本节围绕 Pandas 中的数据排序展开，依次讲解：

- 单字段排序：`DataFrame.sort_values()`
- 多字段排序：`by` 与 `ascending` 传入列表
- 按索引排序：`DataFrame.sort_index()`
- 指定轴排序：`axis=1` 的横向排序场景
- 关键参数：`by`、`inplace`、`ascending`、`axis`

---

## 0. 数据准备

课程开始先完成数据读取的常规步骤：

- 导入所需库。
- 指定数据文件路径。
- 读取数据，并把“序号”列设置为索引。
- 后续排序使用的 `data` 为课程中的 DataFrame 变量。

读取并设置索引后，才可以进行后续的列值排序与索引排序。尤其 `sort_index()` 是直接针对已经设置好的索引进行排序。

---

## 1. 单字段排序：`DataFrame.sort_values()`

### 1.1 方法说明

对某一列的值进行排序，使用：

```python
data.sort_values(...)
```

视频语音中提到的 `soft their videos` 实际对应 Pandas 的 `sort_values`。该方法按“值”排序，而不是按索引排序。

### 1.2 关键参数

`sort_values()` 本节重点讲三个参数：

- `by`
  - 表示按哪个字段进行排序。
  - 单字段排序时，用引号把字段名写进去，例如：`by='语文'`。
- `inplace`
  - 表示是否创建新对象。
  - `inplace=True`：不创建新对象，直接修改原始数据。
  - `inplace=False`：创建新的对象，不修改原始数据。
- `ascending`
  - 表示升序或降序。
  - `ascending=False`：降序。
  - `ascending=True`：升序。

### 1.3 示例一：按“语文”降序，并修改原数据

代码结构：

```python
data.sort_values(by='语文', inplace=True, ascending=False)
```

执行后：

- 按“语文”列排序。
- `inplace=True` 表示直接修改原始 `data`。
- `ascending=False` 表示降序。
- 排序结果中，“语文”成绩从大到小排列。

### 1.4 示例二：`inplace=False` 创建新对象

将 `inplace` 设置为 `False`，并把排序结果赋给新对象：

```python
data2 = data.sort_values(by='语文', inplace=False, ascending=True)
```

执行后：

- `data2` 是升序排序后的新对象。
- 原始 `data` 不会被修改。
- 再查看原始 `data` 时，顺序保持不变。

### 1.5 重要结论：`inplace` 的作用

- `inplace=True`：直接修改原始数据。
- `inplace=False`：不修改原始数据，而是生成新对象。
- 即使把 `inplace=True` 的排序结果重新命名或赋值，原始 `data` 仍然会被修改。
- 因此，是否需要保留原数据，必须通过 `inplace` 控制。

---

## 2. 多字段排序：`sort_values()` 传入列表

### 2.1 使用场景

当需要按多个字段依次排序时，仍然使用 `sort_values()`，但 `by` 需要写成列表形式。

### 2.2 参数写法

- `by` 用列表按优先级顺序写入多个字段：

```python
by=['语文', '数学', '英语']
```

- `ascending` 也要用列表对应每个字段的升序/降序：

```python
ascending=[False, True, False]
```

示例表示：

- 语文：降序
- 数学：升序
- 英语：降序

### 2.3 示例代码

```python
data.sort_values(
    by=['语文', '数学', '英语'],
    inplace=True,
    ascending=[False, True, False]
)
```

### 2.4 多字段排序的执行逻辑

多字段排序不是让每一列都同时保持全局升序或降序，而是按字段列表的顺序逐级排序：

- 先按“语文”降序排序。
- 在“语文”相同或同一排序层级内，再按“数学”升序排序。
- 再在更细层级内按“英语”降序排序。

因此，看到“数学”中某个较小值出现在特定位置时，不应误认为数学列整体没有升序；这是因为最终结果首先受“语文”降序控制。

### 2.5 易错点

- `by` 必须是列表，不能只写一个字段名，否则不是多字段排序。
- `ascending` 也要用列表，并与 `by` 中字段顺序一一对应。
- 多字段排序的优先级从左到右，前一个字段决定主要顺序，后一个字段只在前一个字段相同或分组内起作用。
- `inplace` 的作用与单字段排序相同。

---

## 3. 按索引排序：`DataFrame.sort_index()`

### 3.1 方法区别

- `sort_values()`：按“值”排序。
- `sort_index()`：按“索引”排序。

视频语音中的 `salt.index` 实际对应 `sort_index`。

### 3.2 使用前提

前面读取数据时已经把“序号”设置为索引：

- 索引已经确定。
- 因此按索引排序时，不需要再使用 `by` 指定字段。
- 也不需要再告诉 Pandas 谁是索引，因为索引已经设置好了。

### 3.3 示例代码

```python
data.sort_index(inplace=True)
```

执行后：

- 直接按索引排序。
- `inplace=True` 表示不创建新对象，直接修改原始数据。
- 示例中数据按照“序号”索引重新排列。

### 3.4 结论

- 按索引排序使用 `sort_index()`。
- 按列值排序使用 `sort_values()`。
- `sort_index()` 不需要 `by` 参数。
- 本节演示中只设置了 `inplace`，方法本身已经明确按索引进行排序。

---

## 4. 进阶排序：指定 `axis` 的排序

### 4.1 场景说明

常规二维表格排序，多数是按某列字段给行排序，例如按“语文”或“数学”排序。这种场景使用默认的 `axis=0` 即可。

但有时需要针对一行数据进行横向排序，或者说按某一行的值来调整列的顺序，此时需要指定 `axis=1`。

### 4.2 数据准备步骤

课程中为了演示 `axis=1` 排序，先做了以下操作：

- 打开下一个数据文件。
- 调整或交换部分数据位置。
- 保存修改后的数据。
- 读取数据并先打印原始数据，确认当前顺序。
- 再将排序代码写入并运行。

### 4.3 示例代码结构

按讲师示例，排序时需要注意：

- `by` 中写的是用于排序的行索引/行标签。
- `inplace` 控制是否修改原数据。
- `ascending=False` 表示降序。
- 必须显式设置 `axis=1`。

代码结构如下：

```python
data.sort_values(
    by='一金牌',
    inplace=True,
    ascending=False,
    axis=1
)
```

说明：示例中的 `'一金牌'` 为行索引/行标签示例，实际使用时替换为对应行索引名称。

### 4.4 示例结果

讲师示例中，“一金牌”这一行原来的值类似：

```text
4 6 2
```

设置 `ascending=False` 并指定 `axis=1` 后，排序结果为：

```text
6 4 2
```

即按该行中的数值进行降序横向排列。

### 4.5 关键结论与踩坑点

- `axis` 默认是 `0` 轴。
- 如果按列字段给行排序，使用默认 `axis=0`。
- 如果要对行进行横向排序，必须把 `axis` 改为 `1`。
- 在 `axis=1` 的场景下，`by` 写的是行索引/行标签。
- 这种排序方式在实际分析中很少使用。
- 常规的普通表格排序、字段排序一般用不到 `axis=1`。
- 如果遇到行方向排序，一定要检查：
  - `by` 是否写的是行索引；
  - `axis` 是否已经改为 `1`；
  - `ascending` 是否符合升序/降序要求；
  - `inplace` 是否需要修改原数据。

---

## 5. 本节速查总结

| 需求 | 方法 | 关键参数 |
|---|---|---|
| 按单个字段排序 | `DataFrame.sort_values()` | `by='字段名'`、`ascending`、`inplace` |
| 按多个字段排序 | `DataFrame.sort_values()` | `by=['字段1', '字段2']`、`ascending=[True/False, ...]`、`inplace` |
| 按索引排序 | `DataFrame.sort_index()` | `inplace` |
| 按指定轴/行方向排序 | `DataFrame.sort_values()` | `by=行索引`、`axis=1`、`ascending`、`inplace` |

### 最终结论

- 单字段排序：`by` 写字段名。
- 多字段排序：`by` 和 `ascending` 都写成列表，排序优先级从左到右。
- `inplace=True` 修改原数据；`inplace=False` 创建新对象。
- `ascending=False` 降序；`ascending=True` 升序。
- 按索引用 `sort_index()`，按值用 `sort_values()`。
- 对行进行横向排序时必须设置 `axis=1`；默认 `axis=0`。
- `axis=1` 的排序场景较少，二维表常规字段排序通常不需要使用。