# Pandas 读取 txt 与 csv 文件学习笔记

## 一、课程主题与背景

- 本课属于 Pandas 课程第二节课，主题是：如何使用 Pandas 读取文本文件。
- 主要涉及的文本文件类型包括：
  - `txt`
  - `csv`
  - `tsv`（视频中未用案例演示，但操作方法相同）
- 文本文件的常见特点：
  - 数据可能使用逗号分隔；
  - 可能使用制表符 `tab` 分隔；
  - 可能使用空格分隔；
  - 也可能混合使用空格、制表符等分隔方式。
- 实际大数据分析中，`Excel` 不适合存储大数据，通常使用 `txt` 或 `csv` 文件存储数据。
  - 数据文件小则可能两个 G，大则没有上限。
  - 一次性读取全部大数据可能导致内存承受不了，因此需要控制读取行数或先预览少量数据。
- 上节课讲的是“新建/保存文件”，如 `to_csv`；本节课讲“读取文件”，主要使用 `read_csv`、`read_table`。

## 二、读取文本文件的核心方法

Pandas 中读取文本文件主要有两个方法：

| 方法 | 默认分隔符 | 说明 |
|---|---|---|
| `pd.read_csv()` | 逗号 `,` | 默认按逗号分隔，适合常见 `csv` 文件 |
| `pd.read_table()` | 制表符 `\t` | 默认按制表符分隔，适合 `tsv` 或 tab 分隔文件 |

关键结论：

- `read_csv` 和 `read_table` 都可以读取 `txt`、`csv`、`tsv` 文件，不存在“某个方法只能读某种文件”的限制。
- 两者核心区别是默认分隔符不同：
  - `read_csv` 默认 `sep=','`；
  - `read_table` 默认 `sep='\t'`。
- 如果文件是逗号分隔，但使用 `read_table` 读取，就需要手动指定：
  ```python
  pd.read_table(path, sep=',')
  ```
- 如果文件是制表符分隔，但使用 `read_csv` 读取，也可以手动指定：
  ```python
  pd.read_csv(path, sep='\t')
  ```
- 使用哪个方法主要看个人习惯，但必须注意分隔符是否匹配。

## 三、基础读取演示

导入 Pandas：

```python
import pandas as pd
```

设置文件路径并读取：

```python
path = r"C:\pandas\data.txt"
data = pd.read_csv(path)
print(data)
```

视频中以 `txt` 文件做演示，原因是虽然实际大数据分析中更推荐使用 `csv` 文件，但 `read_csv` 和 `read_table` 都可以读取 `txt` 和 `csv`，因此先用 `txt` 演示读取过程。

- 当 `txt` 文件使用逗号分隔时，`pd.read_csv(path)` 可以直接正常读取。
- 如果改用 `pd.read_table(path)`，由于 `read_table` 默认寻找制表符 `\t`，而该文件使用逗号分隔，读取结果会不正确，不能正常分列。
- 此时需要指定分隔符：
  ```python
  data = pd.read_table(path, sep=',')
  ```

## 四、复杂分隔符与正则表达式

如果文件中既有制表符，又有空格，属于混合分隔情况，可以使用正则表达式作为分隔符。

例如：

```python
import re

data = pd.read_csv(path, sep=r'\s+')
```

说明：

- `\s` 表示匹配空白字符，包括：
  - 换行符；
  - 制表符；
  - 空格等。
- `\s+` 中的 `+` 表示匹配一次或无限次，即一个或多个空白字符。
- 视频提到：如果使用正则表达式相关内容，可以先导入 `re` 模块；正则表达式的基础内容可回顾 Python 爬虫系列前三节课。

## 五、查看数据概况的常用方法

读取数据后，视频演示了多个查看数据基本信息的方法。

### `head()`：查看前几行

```python
data.head()
```

- `head()` 默认显示前 5 行数据。
- 如果写成：
  ```python
  data.head(3)
  ```
  则显示前 3 行。
- 视频中的示例中，表面看起来显示了 6 行，是因为该 `csv` 文件没有表头，Pandas 默认把第一行数据当作表头，然后显示下面的 5 行数据。
- `head()` 写在 `print()` 中只影响显示结果，不改变原始读取的数据变量。视频不推荐长期这样使用，因为容易忘记数据变量仍然包含全部数据，后续再次调用时可能导致内存压力。

### `shape`：查看数据形状

```python
data.shape
```

- 返回数据的行数和列数。
- 视频示例中显示为 6 行 6 列。
- 但实际文件是 7 行 6 列，因为第一行数据被默认当成了表头，没有被当作数据行。
- 这说明“没有表头”时需要正确设置 `header` 和 `names`。

### `columns`：查看列名

```python
data.columns
```

- 默认情况下，第一行数据会被当作列名。
- 设置自定义列名后，再查看 `columns` 就会显示人造列名。

### `index`：查看索引

```python
data.index
```

- 默认索引从 0 开始，到数据行数结束，步长为 1。
- 例如示例中索引从 0 到 6 等。
- 索引是行标签，不是排序结果。

### `dtypes`：查看每列数据类型

```python
data.dtypes
```

- 可以查看每一列的数据类型。
- 视频示例中：
  - 姓名、性别等列显示为 `object`；
  - 年龄列显示为 `int64`。
- `int64` 表示 64 位整型，Numpy 课程中已经讲过。
- 不同列的数据类型可能不同，例如姓名、性别、年龄、手机号等列的类型可能不一样。

## 六、`read_csv` 常用参数详解

### `sep`：指定分隔符

```python
pd.read_csv(path, sep=',')
pd.read_table(path, sep=',')
```

- `sep` 用于指定文件的分隔符。
- 可以是逗号、制表符等，也可以是正则表达式。
- 常见用法：
  ```python
  pd.read_csv(path, sep='\t')   # 制表符分隔
  pd.read_csv(path, sep=r'\s+') # 一个或多个空白字符分隔
  ```

### `header`：指定表头行

```python
pd.read_csv(path, header=None)
```

- `header` 默认值为 `0`，表示把第 0 行，也就是第一行，作为表头。
- 如果文件没有表头，需要告诉 Pandas：
  ```python
  header=None
  ```
- 设置 `header=None` 后，第一行数据不再被当作表头，Pandas 会自动生成 `0, 1, 2, 3, 4, 5` 这样的列名。
- 行号从 0 开始，因此默认表头行是第 0 行。

### `names`：自定义列名

```python
data = pd.read_csv(
    path,
    header=None,
    names=['姓名', '性别', '年龄', '手机', '地址', '入职日期']
)
```

- `names` 用于人工指定列名，需要传入列表。
- 视频示例中有 6 列，所以列表中写 6 个列名。
- `header=None` 与 `names` 一般配合使用：
  - 只写 `header=None` 可以，Pandas 会自动生成数字列名；
  - 只写 `names` 不行，需要同时告诉 Pandas 原文件没有表头。
- 设置后，数据就有了自定义表头。

### `index_col`：指定索引列

```python
data = pd.read_csv(path, index_col='入职日期')
```

- `index_col` 用于指定某一列作为行索引。
- 视频示例中把“入职日期”设置为索引列。
- 索引不是排序，不要把索引和排序混淆。
- 可以指定多个索引列，使用列表形式：
  ```python
  data = pd.read_csv(path, index_col=['姓名', '入职日期'])
  ```
- 多个索引列会形成多级索引。视频提到可回顾 Python 基础课程中 MySQL 索引相关内容，以理解数据库索引列的概念。

### `skiprows`：跳过某些行

```python
data = pd.read_csv(path, skiprows=[2, 3])
```

- `skiprows` 可以跳过指定行。
- 视频示例中传入列表 `[2, 3]`，跳过了“郭靖”“黄蓉”所在的两行。
- 还可以继续添加其他行号，例如 `[2, 3, 5, 6, 7, 8]`，只要文件中有对应行即可。
- 跳过不是删除：
  - 被跳过的行不会出现在读取结果中；
  - 显示结果的索引会重新连续排列，如 `0, 1, 2, 3, 4`；
  - 视频强调“跳过去”与“删除”不同，删除时原索引不会自动变化，而 `skiprows` 是读取时直接忽略这些行。

### `encoding`：指定文件编码

```python
pd.read_csv(path, encoding='utf-8')
```

- 如果 `txt` 文件保存时不是 `utf-8` 编码，在中国大陆地区操作系统上可能出现乱码。
- 此时可以在读取参数中指定编码：
  ```python
  encoding='utf-8'
  ```
- 视频中的示例文件本身是 `utf-8` 编码，因此不需要额外指定。

### `nrows`：限制读取行数

```python
data = pd.read_csv(path, nrows=3)
```

- `nrows` 表示一次只读取前几行，适合大数据文件，避免一次性读取全部数据导致内存不足。
- 视频推荐把行数限制写在 `read_csv` 的参数中，而不是只写在 `print()` 或 `head()` 中。
- 原因：
  - `head()` 只改变显示结果，原始变量仍然包含全部数据；
  - `nrows` 真正限制读取的数据量，变量本身只包含指定行数。
- 例如 `nrows=3` 后，读取结果只包含前 3 行数据。

## 七、将 txt 文件转换为 csv 文件

视频建议：实际大数据分析中尽量不要直接用 `txt` 文件分析，而是转换为 `csv` 文件。转换方法很简单，两行核心代码即可完成，不包括导入库。

示例：

```python
import pandas as pd

data = pd.read_csv('data.txt')
data.to_csv('data.csv')
```

说明：

- 第一步：使用 `pd.read_csv()` 读取 `txt` 文件；
- 第二步：使用 `data.to_csv()` 将数据保存为 `csv` 文件。
- 视频演示中转换成功后，会生成一个新的 `csv` 文件。
- 如果直接打开生成的 `csv` 文件出现乱码，可以在参数中重新指定编码为 `utf-8`：
  ```python
  data.to_csv('data.csv', encoding='utf-8')
  ```
- 也可以在读取时指定编码：
  ```python
  data = pd.read_csv('data.txt', encoding='utf-8')
  ```

## 八、示例代码汇总

```python
import pandas as pd
import re

path = r"C:\pandas\data.txt"

# 1. 直接读取逗号分隔的 txt/csv
data = pd.read_csv(path)
print(data)

# 2. 使用 read_table 读取逗号分隔文件，需要指定 sep
data = pd.read_table(path, sep=',')

# 3. 复杂分隔符：空格、制表符等混合
data = pd.read_csv(path, sep=r'\s+')

# 4. 查看前几行
print(data.head())   # 默认 5 行
print(data.head(3))  # 前 3 行

# 5. 查看数据形状、列名、索引、数据类型
print(data.shape)
print(data.columns)
print(data.index)
print(data.dtypes)

# 6. 没有表头时自定义列名
data = pd.read_csv(
    path,
    header=None,
    names=['姓名', '性别', '年龄', '手机', '地址', '入职日期']
)

# 7. 指定单列索引
data = pd.read_csv(path, index_col='入职日期')

# 8. 指定多列索引
data = pd.read_csv(path, index_col=['姓名', '入职日期'])

# 9. 跳过指定行
data = pd.read_csv(path, skiprows=[2, 3])

# 10. 指定编码
data = pd.read_csv(path, encoding='utf-8')

# 11. 限制读取行数
data = pd.read_csv(path, nrows=3)

# 12. txt 转 csv
data = pd.read_csv('data.txt')
data.to_csv('data.csv')
```

## 九、总结与建议

- 读取 `txt`、`csv`、`tsv` 文件时，可使用 `read_csv` 或 `read_table`。
- `read_csv` 默认逗号分隔，`read_table` 默认制表符 `\t` 分隔。
- 文件既有空格又有制表符时，使用正则表达式 `sep=r'\s+'`。
- 没有表头时：
  - 使用 `header=None` 告诉 Pandas 没有表头；
  - 配合 `names=[...]` 自定义列名。
- 查看数据概况可使用：
  - `head()`：查看前几行；
  - `shape`：查看行数和列数；
  - `columns`：查看列名；
  - `index`：查看索引；
  - `dtypes`：查看每列数据类型。
- 指定索引使用 `index_col`，可以指定单列，也可以传入列表指定多列；索引不是排序。
- 跳过行使用 `skiprows`，跳过不是删除，显示结果的索引会连续排列。
- 文件乱码时使用 `encoding='utf-8'` 指定编码。
- 大数据读取推荐使用 `nrows` 限制读取行数，不建议只在 `print()` 或 `head()` 中限制显示。
- 实际大数据分析中更推荐使用 `csv` 文件；如果拿到的是 `txt` 文件，可用 `read_csv` 读取后再用 `to_csv` 转换为 `csv`。