# 孙兴华中文讲Python数据分析三部曲入门篇 Numpy教程 Pandas教程 Matplotlib教程 p40 S02E25.Excel文件的拆分与合并

## 课程定位与讲师观点

- 本课主题：使用 `pandas` 实现 Excel 文件的拆分与合并。
- 讲师观点：`pandas` 拥有 Excel 文件拆分与合并功能；在简单操作上，`pandas` 比 VBA 更方便；但复杂操作以后，VBA 可能更方便。
- 讲师建议：专业工具做专业的事。操作 Excel 时建议使用 VBA；`pandas` / Python 在与 PDF、Excel 互相工作等场景中可能更友好。
- VBA 是 Excel 原生工具，操作 Excel 很方便，但用 VBA 操作 Word、PPT 的教程较少；大多数人用 VBA 操作 Excel。讲师推荐可参考其《Excel VBA 第一季》。
- 本课用简单几行代码演示 Excel 拆分与合并，忽略了一些特殊情况；若把特殊情况全部考虑进去，代码会越写越复杂。
- 第一个案例会用到 `os` 模块；后面的拆分案例不涉及文件夹遍历，不需要 `os`。

## 一、多个工作簿合并为一张总表

### 1. 场景与默认前提

- 场景：从一个文件夹下读取多个工作簿进行合并。
- 默认前提：每个工作簿中只有一个工作表。
- 后续再讲同一工作簿中多个工作表如何合并。

### 2. 合并思路

- 先准备一张空表。
- 假设文件夹中有 1、2、3 三个文件：
  - 第一次：空表连接 1 号文件。
  - 第二次：空表连接完 1 号文件后的总表，再连接 2 号文件。
  - 第三次：连接完 1、2 号文件后的总表，再连接 3 号文件。
  - 以此类推，循环累加。
- 空表可以直接用 `pd.DataFrame()` 创建；也可以建立空白 Excel 再用 `read_excel` 读下来，但后者较麻烦，讲师建议直接写 `pd.DataFrame()`。

### 3. 关键代码与步骤

导入库并准备路径、空表：

    import os
    import pandas as pd

    path = r"C:\...\pandas\课件\025"
    merged = pd.DataFrame()

使用 `os.listdir(path)` 获取目录下所有文件和文件夹名称，返回一个列表。讲师说明 `os.listdir` 在 Python 基础篇第 122 页讲过，用于获取某个文件夹下所有文件和文件夹的名字。

    for 文件名 in os.listdir(path):
        print(文件名)

课堂演示目录中有 `1`、`2`、`3` 三个文件，打印验证成功。

循环读取每个文件并合并：

    for 文件名 in os.listdir(path):
        table = pd.read_excel(path + 文件名)
        merged = pd.concat([merged, table])

    print(merged)

关键点：
- `pd.read_excel(...)` 用于读取 Excel 文件。
- 仅有目录路径读不出文件，必须让路径和文件名拼成完整文件路径。
- 课堂中用字符串加号 `+` 拼接路径和文件名；讲师强调两个字符串连接用加号，不要用 `&` 连接符。
- 每次循环读取不同文件，第一次读第 1 张表，第二次读第 2 张表，第三次读第 3 张表。
- `pd.concat([merged, table])` 将当前累计总表与本次读取的表进行连接。
- 打印 `merged` 后可以看到索引；取消索引的方法在第一节课讲过，写回 Excel 时也可以设置。

### 4. 将合并结果写回 Excel

合并表 `merged` 只是一个变量，最后需要用 `to_excel` 写到指定盘符和文件名：

    merged.to_excel(r"C:\合并.xlsx")

关键点：
- `merged` 是内存中的变量，不是文件名。
- 最终保存到哪个盘、哪个文件，由 `to_excel` 的路径参数决定。
- 讲师说明：知道怎么把表搞到内存里，就知道怎么把表存到 Excel 里。
- 打印时出现的索引，可以参考第一课“新建文件往前写东西”的方法取消；`to_excel` 里也可以设置索引相关参数。

## 二、同一工作簿中多个工作表 sheet 合并

### 1. 读取所有工作表

- 同一个工作簿中多个 `sheet` 合并，本质上是在读取时增加参数。
- 在 `pd.read_excel` 中增加 `sheet_name=None`，即可读取所有工作表。
- 如果工作簿中还有其他 sheet，也会被读取出来。

示例：

    数据 = pd.read_excel(路径, sheet_name=None)

读取后打印数据，可以看到所有 sheet 工作表都被读出来。打印结果看起来可能较乱，先不用管，只需确认读取成功。

### 2. 获取所有 sheet 名称并循环合并

准备空表：

    合并表 = pd.DataFrame()

查看读取结果中的 sheet 名称：

    数据.keys()

课堂中将 `data.keys()` 的结果转成列表，变量名为“字段名”或“列标签”：

    字段名 = list(数据.keys())

循环取出每个 sheet 的 DataFrame 并合并：

    for 列标签 in 字段名:
        新数据 = 数据[列标签]
        合并表 = pd.concat([合并表, 新数据])

    print(合并表)

关键点：
- 课堂中变量名称为“字段名”“列标签”，但这里 `list(data.keys())` 得到的是 sheet 名称列表。
- `数据[列标签]` 取出的是对应 sheet 的 DataFrame。
- 每个 sheet 内都有相同字段：序号、姓名、电话。
- 每次取出一个 sheet 的数据，再与空表或累计合并表进行 `concat`。
- 最后打印 `合并表`，成功将所有 sheet 连接起来。

### 3. 重要提醒

- 操作多个 sheet 时，想让它识别全部 sheet，必须加 `sheet_name=None`。
- 不要忘记如何把 sheet 名称取出为列表，再遍历该列表。
- 每次拿到一个 sheet 数据后，使用 `pd.concat` 进行合并。

### 4. `read_excel` 的 `sheet_name` 参数补充

讲师说明已将 `read_excel` 和 `to_excel` 的详细方法放入笔记，参数不熟时随时查询。示例：
- `sheet_name=None`：所有表都作为数据文件读取。
- `sheet_name="Sheet1"` 或 `sheet_name=1`：读取第一页数据。
- `sheet_name=[0, 1, "Sheet5"]`：读取第一页、第二页和第五页作为数据。
- 具体用到时再查询，不可能一次全部记住。

## 三、多表头读取与合并

### 1. 多表头场景

- 课件使用 `025-2` 文件夹，里面都是多表头文件。
- 多表头时，需要在 `read_excel` 后面增加 `header` 参数。

### 2. `header` 参数用法

示例：

    pd.read_excel(路径, header=[0, 1])

说明：
- 表头默认是第 0 行；我们通常看到的第一行在 pandas 中默认为第 0 行。
- 如果第 0 行和第 1 行都是表头，就设置 `header=[0, 1]`。
- 多表头时加 `header` 参数即可；自己是几行表头，就默认到几。
- 如果不加 `header`，表头会乱，读取结果不正确。
- 多表头场景下，只需要改这一点知识，没有别的地方。

## 四、将一个工作表拆分成同一工作簿中的多个工作表

### 1. 场景

- 示例文件位于 `pandas` 下的“拆分”文件。
- 当前是一个工作表，想按照某一列拆分成多个工作表。
- 示例按照“部门”列拆分，部门中有：办公室、销售部、保洁部。
- 目标：生成“办公室”“销售部”“保洁部”等多个 sheet，让对应部门的数据进入对应 sheet。
- 实际工作中部门可能很多，拆分出的 sheet 也会更多。

### 2. 引入 ExcelWriter

`pd.ExcelWriter` 是一个写入小插件，可以向同一个 Excel 中的不同工作表写入数据。

标准保存 pandas 数据到多个 sheet 的形式：
- 先创建 `ExcelWriter` 对象。
- 创建时传入路径 / 文件名，告诉它保存到哪里。
- 再用 `df.to_excel(writer, sheet_name=工作名)` 写入不同 sheet。
- 最后不要忘记保存和关闭 writer 对象。

讲师提醒：
- 如果 Excel 中有格式，例如单元格颜色等已经设置好，用 pandas 操作会很麻烦。
- 如果涉及格式操作，需要查看笔记中的代码再操作。

### 3. 拆分步骤与代码

读取 Excel：

    import pandas as pd

    路径 = r"C:\...\pandas\拆分.xlsx"
    数据 = pd.read_excel(路径)

获取“部门”列的唯一值列表。由于部门列中会有重复的办公室、销售部、保洁部，需要先去重：

    分割列 = list(数据["部门"].drop_duplicates())

说明：
- `drop_duplicates()` 用于删除重复值。
- 讲师提到该知识点在笔记相关章节中讲过，可用于删除重复值。
- 如果列中本来没有重复，可以直接转列表；现在有重复，必须先 `drop_duplicates()` 再转列表。

创建 `ExcelWriter`：

    writer = pd.ExcelWriter(r"C:\孙兴华.xlsx")

循环按部门拆分并写入不同 sheet：

    for i in 分割列:
        数据一 = 数据[数据["部门"] == i]
        数据一.to_excel(writer, sheet_name=i)

    writer.save()
    writer.close()

关键点：
- `数据[数据["部门"] == i]` 是双重切片：筛选“部门”列等于当前遍历值 `i` 的数据。
- 条件判断必须用 `==`，不能写成 `=`；课堂中曾写错，后改为 `==`。
- `to_excel(writer, sheet_name=i)` 中 `sheet_name=i` 指定工作表名称。
- 变量名注意：课堂中 `writer` 对象可能被命名为“新数据”，但它的实际作用是 `ExcelWriter` 对象。
- 最后必须执行 `save()` 和 `close()`。
- 运行后 C 盘生成 `孙兴华.xlsx`，打开后办公室、销售部、保洁部三个部门 sheet 都存在，数据正确。

### 4. 取消索引

- 拆分出的表可能带索引列。
- 讲师说明第一节课讲过如何取消索引：可以在 `to_excel` 中设置，也可以单独设置。
- 示例可设置 `index=False`，具体参考第一课和 `to_excel` 参数笔记。

## 五、将一个工作表拆分成多个工作簿

### 1. 场景

- 前面是拆分成同一工作簿中的多个 sheet。
- 现在要将一个工作表拆分成多个工作簿，即生成多个 Excel 文件。

### 2. 步骤与代码

仍然读取“拆分”文件，并按“部门”列去重得到分割列表：

    import pandas as pd

    路径 = r"C:\...\pandas\拆分.xlsx"
    数据 = pd.read_excel(路径)
    分割列 = list(数据["部门"].drop_duplicates())

循环筛选数据并分别写入多个 Excel 文件：

    for i in 分割列:
        数据一 = 数据[数据["部门"] == i]
        数据一.to_excel("C:/" + i + ".xlsx")

关键点：
- 拆分多个工作簿时，不需要 `ExcelWriter`，因为每个部门要保存成独立文件。
- 保存路径不是固定唯一文件，而是由字符串拼接生成不同文件名。
- 路径拼接形式：`"C:/" + i + ".xlsx"`。
- 运行后会生成类似：
  - `办公室.xlsx`
  - `销售部.xlsx`
  - `保洁部.xlsx`
- 课堂演示中 C 盘成功生成办公室、销售部、保洁部三个文件。
- 索引设置 / 取消索引与前面相同，可参考第一课时和 `to_excel` 参数。

## 六、本课涉及函数与参数速查

- `os.listdir(path)`：获取某个文件夹下所有文件和文件夹名称，返回列表。
- `pd.DataFrame()`：创建空 DataFrame，即空表。
- `pd.read_excel(path)`：读取 Excel 文件。
- `pd.read_excel(path, sheet_name=None)`：读取工作簿中所有 sheet，返回字典形式数据；键为 sheet 名称，值为对应 DataFrame。
- `data.keys()`：获取读取结果中的所有 sheet 名称。
- `pd.concat([df1, df2])`：将多个 DataFrame 连接合并。
- `pd.read_excel(path, header=[0, 1])`：指定第 0 行和第 1 行作为多表头。
- `df.drop_duplicates()`：删除重复值。
- `pd.ExcelWriter(path)`：创建 Excel 写入器对象，用于向同一个 Excel 的不同 sheet 写入数据。
- `df.to_excel(writer, sheet_name=i)`：将 DataFrame 写入指定 writer 的指定 sheet。
- `writer.save()`：保存 ExcelWriter 对象。
- `writer.close()`：关闭 ExcelWriter 对象。
- `df.to_excel(path)`：将 DataFrame 写入单个 Excel 文件。
- `index=False`：写 Excel 时取消默认索引，具体参考第一课和 `to_excel` 参数。

## 七、踩坑与结论清单

- 路径和文件名必须拼接完整；只有目录读不出文件。
- 字符串拼接用 `+`，讲师强调不要用 `&` 连接符。
- 多个工作簿合并默认每个工作簿只有一个工作表；多 sheet 需要 `sheet_name=None`。
- 多 sheet 读取后得到的是多个 sheet 的数据集合；课堂通过 `list(data.keys())` 取 sheet 名称列表，再循环 `data[列标签]` 取出对应 DataFrame。
- 多表头读取必须设置 `header`；默认第 0 行是表头，多表头可设 `header=[0,1]`。
- 拆分前如果目标列有重复值，必须先 `drop_duplicates()` 去重，再转成列表遍历。
- 拆分筛选条件必须用 `==`，不能误写成 `=`。
- 拆分到同一工作簿多个 sheet 时，用 `ExcelWriter`，最后 `save()` 和 `close()` 不能漏。
- 拆分到多个工作簿时，用字符串拼接生成不同文件名，如 `"C:/" + i + ".xlsx"`。
- 打印结果带索引；取消索引可在 `to_excel` 中设置，也可参考第一课方法。
- 本课演示的是理想状态；实际 Excel 中可能有空行、表头、格式等问题，需要结合 `read_excel` 参数和笔记处理。
- 若 Excel 中有复杂格式，pandas 操作麻烦；涉及格式操作时查看讲师笔记中的代码。
- 讲师建议：操作 Excel 可用 VBA；pandas 适合与 PDF、Excel 互相工作等场景，简单拆分合并很方便。