---
title: Numpy 与 Pandas 学习路线
kind: map
created: 2026-11-17
source: https://www.bilibili.com/video/BV1ji4y157uB
---

# Numpy 与 Pandas 学习路线

> 273 张概念卡 · 按课程顺序从 p2 排到 p46 · 点卡片看定义与自测

这是孙兴华《Python 数据分析三部曲》的概念导航：每一集下面挂着从那集抽出来的卡片，顺着看就是一条完整的学习路径。

- [[孙兴华Python数据分析三部曲-课程地图]] — 79 集完整目录、时长与精简路线
- [[孙兴华 Python 数据分析三部曲]] — 课程总览卡

## 第一季 · Numpy（82 张卡）

数组的地基：创建、计算、索引、统计。

### S01E01 · 参考书籍及安装方法（p2，2 张）

- [[pip3 install numpy]]
- [[数据分析的数学基础]]

### S01E02 · 体验Numpy与for循环的区别（p3，5 张）

- [[import numpy as np]]
- [[range 结束位置不含自身]]
- [[列表推导式]]
- [[向量化计算]]
- [[数组与矩阵的区别]]

### S01E03 · 创建数组（p4，12 张）

- [[dtype 参数]]
- [[ndim 属性]]
- [[np.arange]]
- [[np.array]]
- [[np.full]]
- [[np.ones]]
- [[np.ones_like]]
- [[np.zeros]]
- [[np.zeros_like]]
- [[numpy.ndarray]]
- [[size 属性]]
- [[形状参数]]

### S01E04 · 多维数组（p5，3 张）

- [[Numpy reshape]]
- [[Numpy 多维数组]]
- [[np.full_like]]

### S01E05 · 数组计算（p6，5 张）

- [[三维数组广播]]
- [[列向量广播]]
- [[同形数组运算]]
- [[广播机制]]
- [[数组与标量运算]]

### S01E06 · 基础索引与切片（p7，4 张）

- [[Numpy 二维数组]]
- [[Numpy 切片]]
- [[Numpy 索引]]
- [[负索引]]

### S01E07 · 布尔索引（p8，5 张）

- [[二次切片]]
- [[多条件组合]]
- [[布尔数组]]
- [[条件赋值]]
- [[零一化]]

### S01E08 · 神奇索引（p9，4 张）

- [[Numpy 二维数组双索引]]
- [[一维数组的多维索引返回形状]]
- [[取所有行的指定列]]
- [[神奇索引]]

### S01E09 · 数组的轴和转置（p10，4 张）

- [[axis 参数]]
- [[沿轴切片]]
- [[转置]]
- [[轴转置]]

### S01E10 · random 随机函数【了解即可】（p11，2 张）

- [[Numpy random 随机函数]]
- [[np.random.rand]]

### S01E11 · 通用函数：快速的逐元素数组函数（p12，8 张）

- [[np.add]]
- [[np.exp]]
- [[np.maximum]]
- [[np.minimum]]
- [[np.sqrt]]
- [[一元通用函数]]
- [[二元通用函数]]
- [[通用函数]]

### S01E12 · 数学和统计方法（p13，18 张）

- [[np.argmax np.argmin]]
- [[np.average]]
- [[np.bincount]]
- [[np.cumprod]]
- [[np.cumsum]]
- [[np.max np.min]]
- [[np.mean]]
- [[np.median]]
- [[np.prod]]
- [[np.sum]]
- [[众数]]
- [[分位数]]
- [[协方差]]
- [[方差]]
- [[标准化]]
- [[标准差]]
- [[样本与特征]]
- [[相关系数]]

### S01E13 · 条件计算，排序，深潜拷贝【本季完】（p14，10 张）

- [[argsort]]
- [[ndarray.sort]]
- [[np.all]]
- [[np.any]]
- [[np.in1d]]
- [[np.where]]
- [[unique]]
- [[三目运算]]
- [[布尔数组求和计数]]
- [[浅拷贝与深拷贝]]


## 第二季 · Pandas（191 张卡）

数据处理主场：读写、清洗、连接、分组、透视。

### S02E00 · 安装 pandas.numpy.xlrd（p15，2 张）

- [[import 验证安装]]
- [[pip]]

### S02E01 · 数据类型与新建文件（p16，6 张）

- [[Pandas 写出方法家族]]
- [[dtypes 属性]]
- [[import pandas as pd]]
- [[to_csv]]
- [[to_sql]]
- [[批量处理替代手工]]

### S02E02 · 读取 txt 与 csv 文件（p17，10 张）

- [[encoding 参数]]
- [[head()]]
- [[header 参数]]
- [[names 参数]]
- [[nrows 参数]]
- [[pd.read_csv]]
- [[pd.read_table]]
- [[sep 参数]]
- [[skiprows 参数]]
- [[txt 转 csv]]

### S02E03 · 读取 Mysql 文件（p18，4 张）

- [[SQL 查询语句]]
- [[pd.read_sql]]
- [[pymysql]]
- [[pymysql.connect()]]

### S02E04 · 读取与修改 Excel 文件（p19，3 张）

- [[Excel 无表头文件处理]]
- [[pd.read_excel]]
- [[xlrd]]

### S02E05 · 数据结构之 Series（p20，4 张）

- [[Series]]
- [[index 参数]]
- [[isnull]]
- [[notnull]]

### S02E06 · 数据结构之 DataFrame（p21，6 张）

- [[DataFrame]]
- [[iloc]]
- [[reset_index]]
- [[shape 属性]]
- [[tail]]
- [[字典构造 DataFrame]]

### S02E07 · 连接查询之 Merge（p22，5 张）

- [[how 参数]]
- [[left_on right_on]]
- [[on 参数]]
- [[right_index 参数]]
- [[多对多匹配]]

### S02E08 · 连接查询之 join 与 Merge 总结（p23，3 张）

- [[DataFrame 合并]]
- [[join 方法]]
- [[suffixes 参数]]

### S02E09 · 连接查询之 concat（p24，7 张）

- [[append 方法]]
- [[ignore_index 参数]]
- [[join 参数（concat）]]
- [[join_axes 参数]]
- [[keys 参数]]
- [[pd.concat]]
- [[sort 参数（concat）]]

### S02E10 · 各种数据自动填充（p25，5 张）

- [[datetime 模块]]
- [[dtype 参数（读取时指定列类型）]]
- [[usecols 参数]]
- [[累加月算法]]
- [[自动填充]]

### S02E11 · 列与列之间的计算（p26，7 张）

- [[BMI 计算]]
- [[NumPy 函数在 pandas 中的应用]]
- [[Timedelta]]
- [[dt 访问器]]
- [[lambda 表达式]]
- [[m.name 列名行名判断]]
- [[计算列]]

### S02E12 · 数据排序【已修证】（p27，5 张）

- [[ascending 参数]]
- [[by 参数]]
- [[inplace 参数]]
- [[sort_index]]
- [[sort_values]]

### S02E13 · 数据查询（p28，6 张）

- [[.at 索引器]]
- [[loc]]
- [[列范围切片]]
- [[数据查询]]
- [[数据筛选]]
- [[日期范围查询]]

### S02E14 · 筛选（p29，8 张）

- [[case 参数]]
- [[pd.to_datetime]]
- [[query 方法]]
- [[str.contains]]
- [[truncate]]
- [[布尔索引筛选]]
- [[日期筛选三部曲]]
- [[条件变量化]]

### S02E15 · 数据删除 drop 函数（p30，2 张）

- [[drop]]
- [[labels 参数]]

### S02E16 · 处理缺失值（p31，10 张）

- [[NaN]]
- [[fillna]]
- [[isna]]
- [[limit 参数（fillna）]]
- [[method 参数（fillna）]]
- [[notna]]
- [[subset 参数（dropna）]]
- [[thresh 参数]]
- [[缺失值处理]]
- [[聚合函数 NA 忽略特性]]

### S02E17 · 数学统计函数（p32，3 张）

- [[Pandas 数学统计函数]]
- [[describe()]]
- [[指定列统计]]

### S02E18 · 删除重复和提取重复（p33，5 张）

- [[drop_duplicates]]
- [[duplicated]]
- [[keep 参数]]
- [[subset 参数]]
- [[value_counts]]

### S02E19 · 算数运算与数据对齐（p34，6 张）

- [[inf 与 -inf]]
- [[use_inf_as_na]]
- [[反转方法 r]]
- [[灵活算术方法]]
- [[空值传播]]
- [[索引对齐]]

### S02E20 · 多层索引与多层索引计算（p35，10 张）

- [[index_col 参数]]
- [[is_lexsorted]]
- [[pd.MultiIndex.from_arrays]]
- [[pd.MultiIndex.from_product]]
- [[pd.MultiIndex.from_tuples]]
- [[set_index]]
- [[slice(None)]]
- [[分层索引]]
- [[多层列索引]]
- [[默认索引列]]

### S02E21 · 数据替换（p36，4 张）

- [[regex 参数]]
- [[replace]]
- [[str.replace 正则替换]]
- [[多值替换]]

### S02E22 · 离散化和分箱（p37，5 张）

- [[get_dummies]]
- [[labels 参数（cutqcut）]]
- [[pd.cut]]
- [[pd.qcut]]
- [[离散化与分箱]]

### S02E23 · 字符串操作（上）（p38，19 张）

- [[str.cat]]
- [[str.decode]]
- [[str.encode]]
- [[str.endswith]]
- [[str.get]]
- [[str.join]]
- [[str.lstrip]]
- [[str.pad]]
- [[str.partition]]
- [[str.repeat]]
- [[str.rsplit]]
- [[str.rstrip]]
- [[str.slice]]
- [[str.slice_replace]]
- [[str.split]]
- [[str.startswith]]
- [[str.strip]]
- [[str.zfill]]
- [[字符串乘法]]

### S02E24 · 字符串操作（下）（p39，11 张）

- [[Series.str 访问器]]
- [[astype(str)]]
- [[find rfind]]
- [[index rindex]]
- [[str.extract]]
- [[str.maketrans]]
- [[str.match]]
- [[translate]]
- [[大小写转换方法]]
- [[字符串内容判断方法]]
- [[正则表达式]]

### S02E25 · Excel 文件的拆分与合并（p40，6 张）

- [[DataFrame.to_excel]]
- [[Pandas Excel 合并拆分]]
- [[os.listdir]]
- [[pd.ExcelWriter]]
- [[sheet_name 参数]]
- [[写回原 Excel 文件]]

### S02E26 · 分组与聚合 groupby 基础部分（p41，7 张）

- [[agg]]
- [[axis=1 按列分组]]
- [[groupby]]
- [[groupby.apply]]
- [[level 参数（groupby）]]
- [[通过函数分组]]
- [[遍历分组]]

### S02E27 · 分组对象和创建（p42，6 张）

- [[isin]]
- [[pipe]]
- [[分组对象复用]]
- [[多键分组]]
- [[姓名首字分组]]
- [[布尔分组键]]

### S02E28 · 数据透视表（p43，6 张）

- [[aggfunc 参数]]
- [[crosstab]]
- [[dropna 参数（透视表）]]
- [[fill_value 参数]]
- [[margins 参数]]
- [[pivot_table]]

### S02E29 · vlookup（p44，3 张）

- [[VLOOKUP 式匹配]]
- [[insert 方法]]
- [[列移动三步法]]

### S02E30 · 数据处理的三板斧（p45，3 张）

- [[apply]]
- [[applymap]]
- [[map]]

### S02E31 · 数据的转置、计算环比与同比（p46，4 张）

- [[shift]]
- [[同比]]
- [[数据转置]]
- [[环比]]


## 怎么配合课程地图用

先扫一遍 [[孙兴华Python数据分析三部曲-课程地图]] 里的「精简主干」，按那里标出的重点集数跳到本页对应章节，看完一集就把该集下面的卡片过一遍。

概念卡按课程顺序排列，同名概念只建一张卡、后来学到的内容追加在同一张卡的「补充」小节里，所以不用担心重复。

