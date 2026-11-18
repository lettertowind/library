# Python 面向对象编程（OOP）课程笔记

> 说明：以下代码为根据视频讲解整理出的结构示例，变量名统一为视频中的 `smeg`、`bosch`；打印文案按讲解含义整理，不是逐字转录。视频转录中个别品牌名/变量名存在口误或识别误差，笔记按上下文统一。

## 1. 类的核心概念：蓝图与对象（00:00-00:45）

- **类 class**：一个对象应该“长什么样”以及“如何运作”的蓝图。
- 类比：建房子前先画蓝图，蓝图说明房子的外观和功能；真正建造出来的房子才是具体对象。
- 类包含一个对象应该做什么的所有相关信息。
- 本课场景：假设我们是微波炉制造商。
  - 第一步：设计微波炉的蓝图，即定义 `Microwave` 类。
  - 第二步：使用蓝图实际创建微波炉，即创建类的实例/对象。
- **对象/实例 instance**：按照类这个蓝图创建出来的具体微波炉。

## 2. 定义类与命名规范（00:45-01:27）

- 使用 `class` 关键字定义类，后面跟类名。
- 类名遵循**驼峰命名法/PascalCase**：
  - 类名首字母大写。
  - 每个额外单词的首字母也大写。
  - 示例：`BlueCar`。
- 本课定义微波炉类，类名可写为 `Microwave`。
- 初始空类示例：

```python
class Microwave:
    pass
```

- 目前这个类还是空的，但已经可以基于它创建对象。
- 空类本身没有有用的信息和功能，因此后续需要添加初始化器和方法。

## 3. 实例化对象（01:27-02:31）

- 在类名后加括号，就会创建该类的一个实例：

```python
smeg = Microwave()
```

- `smeg` 是一个变量名，表示一台具体的微波炉；视频中也用品牌/类型来命名实例。
- 类名后的括号表示调用构造函数，创建一个该类的实例。
- 每次使用括号实例化，都会创建一个独特的对象。
- 如果直接打印这个实例，会得到一个唯一的 id/内存地址，指向这个微波炉实例。
- 此时类仍然比较无用，因为它不包含任何有用的数据或功能。

### 类型注解/type hints

- 可以写类型注解：

```python
smeg: Microwave = Microwave()
```

- 类型注解只是给代码编辑器看的，帮助编辑器提示和检查。
- 类型注解不影响程序运行；不喜欢可以安全忽略。
- 讲师在视频中全程使用类型注解，因为认为它们很有用，但是否使用取决于个人。

## 4. 初始化器 `__init__`（02:57-04:27）

- 为了让每个微波炉具有个性化信息，需要使用初始化器。
- 初始化方法名为 `__init__`。
- `__init__` 是一个 **dunder 方法**，即双下划线方法。
- 默认情况下，`__init__` 返回 `None`。
- 可以不显式写返回 `None`，但讲师喜欢写出来，让代码更明确。
- 初始化器负责初始化类：当创建实例时，如果有额外信息要传给类，这些代码会在实例化后立即运行。
- 参数设计：
  - `self`
  - `brand: str`：品牌，字符串类型。
  - `power_rating: str`：功率等级，字符串类型。
- 在初始化器中赋值：
  - `self.brand = brand`
  - `self.power_rating = power_rating`

示例结构：

```python
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
```

- 因为 `__init__` 现在要求额外参数，实例化时必须传入这些信息：

```python
smeg = Microwave("smeg", "B")
bosch = Microwave("bosch", "C")
```

- 视频中品牌/功率示例存在口误和识别误差，核心是：创建实例时传入品牌与功率等级。
- 实例化后可以访问属性：

```python
print(smeg.brand)
print(smeg.power_rating)
```

- 打印结果会返回创建实例时插入的品牌和功率信息。
- 也可以创建第二个微波炉，例如 `bosch`，并打印它的品牌和功率设置。
- 由于 `__init__` 要求参数，缺少参数时编辑器会出现语法高亮/警告，提示需要提供这些信息。

## 5. `self` 是什么（04:53-06:22）

- `self` 是类的实际实例，也就是当前正在使用的对象。
- `self` 确保所有数据都绑定到正确的实例/对象上。
- 创建 `smeg` 时，`__init__` 中的 `self` 指向 `smeg`。
- 创建 `bosch` 时，`__init__` 中的 `self` 指向 `bosch`。
- 因此调用 `bosch.brand` 时，会返回 `bosch` 这个实例自己的品牌数据。
- `self` 只是当前实例的引用。
- 可以将 `self` 改名：
  - 改成 `this`：在 Java 中很流行。
  - 改成 `instance`。
  - 甚至改成 `s`。
- 改名字后代码仍然可以以相同方式工作。
- 但不建议这样做，因为 Python 社区惯例是使用 `self`；在线文档和其他教程通常都写 `self`。
- 结论：`self` 只是惯例名称，指代当前实例；不是必须叫 `self`，但强烈建议遵循惯例。

## 6. 给类添加方法（06:22-09:25）

- 现在微波炉有数据，但还没有行为，不会工作。
- 需要给类添加方法，让对象可以执行操作。
- 讲师先保留 `smeg` 实例，删除多余示例，然后添加方法。
- 还要在初始化器中增加一个状态属性，用于跟踪微波炉是打开还是关闭。

### 6.1 增加 `turned_on` 状态属性

- 在 `__init__` 中增加：

```python
self.turned_on: bool = False
```

- `turned_on` 是布尔类型，初始值为 `False`。
- 含义：创建微波炉时默认是关闭的。
- 讲师用生活类比说明：打开装有微波炉的盒子时，微波炉不应已经处于开启状态。

### 6.2 定义打开方法 `turn_on`

- 方法名：`turn_on`。
- 返回 `None`，因为它只执行代码。
- 逻辑：
  - 如果 `self.turned_on` 已经为 `True`，打印提示：微波炉已经打开，不能重复打开。
  - 否则将 `self.turned_on` 设置为 `True`。
  - 通知用户已成功打开。

示例结构：

```python
def turn_on(self) -> None:
    if self.turned_on:
        print(f"Microwave {self.brand} is already on")
    else:
        self.turned_on = True
        print(f"Microwave {self.brand} is now on")
```

### 6.3 定义关闭方法 `turn_off`

- 方法名：`turn_off`。
- 返回 `None`。
- 逻辑：
  - 如果微波炉已打开，则将 `self.turned_on` 设置为 `False`。
  - 打印提示：微波炉已关闭。
  - 如果微波炉已经关闭，则提示：微波炉已经关闭。

示例结构：

```python
def turn_off(self) -> None:
    if self.turned_on:
        self.turned_on = False
        print(f"Microwave {self.brand} is now off")
    else:
        print(f"Microwave {self.brand} is already off")
```

### 6.4 定义运行方法 `run`

- 方法名：`run`。
- 参数：
  - `self`
  - `seconds: int`：运行秒数，整数类型。
- 返回 `None`。
- 逻辑：
  - 首先检查 `self.turned_on` 是否为 `True`。
  - 如果没有打开，则不能运行微波炉；打印提示，要求先开启微波炉。
  - 如果已打开，则打印正在运行 `self.brand`，持续 `seconds` 秒。

示例结构：

```python
def run(self, seconds: int) -> None:
    if self.turned_on:
        print(f"Running {self.brand} for {seconds} seconds")
    else:
        print("Please turn on your microwave first")
```

- 视频中把未开启时的提示描述为“神秘的力量低语”，实际含义是：必须先开启微波炉才能运行。
- 到这里，类已经包含：
  - 数据：`brand`、`power_rating`、`turned_on`。
  - 功能：`turn_on()`、`turn_off()`、`run()`。
- 类成了完整蓝图，说明微波炉应该长什么样、应该如何工作。

## 7. 使用对象及其方法（09:25-11:26）

- 使用点符号 `.` 访问对象的方法。
- 示例：对 `smeg` 执行打开、运行、关闭：

```python
smeg.turn_on()
smeg.turn_on()
smeg.run(30)
smeg.turn_off()
smeg.run(10)
```

- 控制台行为：
  - 第一次 `smeg.turn_on()`：成功打开微波炉。
  - 第二次 `smeg.turn_on()`：提示微波炉已经打开，避免重复打开。
  - `smeg.run(30)`：运行 30 秒。
  - `smeg.turn_off()`：关闭微波炉。
  - 关闭后再 `smeg.run(10)`：提示需要先开启微波炉。
- 这说明类中有安全机制：
  - 不能重复打开。
  - 不能重复关闭。
  - 未打开时不能运行。

- 同样可以对 `bosch` 执行相同操作：

```python
bosch.turn_on()
bosch.turn_off()
bosch.run(2)
```

- 视频中演示了对 `bosch` 打开、关闭、运行等操作，行为与 `smeg` 完全相同。
- 这体现了类的复用价值：只要按蓝图创建实例，所有数据和功能都可以直接复用。

## 8. dunder 方法/魔术方法（11:26-12:43）

- 背景：尝试执行对象相加，例如：

```python
smeg + bosch
```

- 如果类中没有定义 `+` 操作符的行为，会立即报错：该类型不支持此操作。
- 要定义对象相加行为，需要在类中定义 **dunder 方法**。
- dunder 方法名称前后各有两个下划线，因此称为“双下划线方法”。
- 也可能被称为 **magic methods/魔术方法**。
- 加法对应的方法名是 `__add__`。
- `__add__` 接收：
  - `self`：当前实例。
  - `other`：另一个实例。

示例结构：

```python
def __add__(self, other):
    return self.brand + other.brand
```

- 定义 `__add__` 后，语法高亮和警告会消失。
- 如果方法体不返回任何内容，脚本可以运行，但相加不会有实际效果。
- 在方法中可以返回任意想要的内容。
- 视频示例中，两个微波炉相加可以返回一个“融合”字符串，例如 `self.brand + other.brand`。
- 同样道理适用于其他操作符：
  - `*` 星号。
  - `|` 管道符。
  - 其他操作符都可以在类中定义。
- 乘法对应 `__mul__`，示例中返回与前面类似的内容，只是带有一个星号。

示例结构：

```python
def __mul__(self, other):
    return self.brand + " * " + other.brand
```

- 不必只返回字符串，也可以返回任意对象，甚至返回类的另一个实例。

## 9. `__str__` 与 `__repr__`（14:01-16:59）

### 9.1 默认打印对象

- 如果没有定义 `__str__`，直接打印对象通常会看到类的内存地址或默认表示。
- 例如打印 `smeg` 或 `bosch`，默认输出不直观。

### 9.2 字符串表示 `__str__`

- `__str__` 用于返回一个用户友好的字符串表示。
- 定义后，`print(obj)` 和 `str(obj)` 会使用它。
- 示例结构：

```python
def __str__(self) -> str:
    return f"{self.brand}\nPower rating set to {self.power_rating}"
```

- 定义后再次打印 `smeg` 或 `bosch`，会得到可读内容，而不是内存地址。
- 如果类中没有定义 `__str__`，打印对象时会退回到表示方法/默认表示。

### 9.3 开发者表示 `__repr__`

- `__repr__` 用于返回对开发者更有用的信息。
- 可以覆盖默认的对象表示。
- 示例结构：

```python
def __repr__(self) -> str:
    return f"Microwave(brand='{self.brand}', power_rating='{self.power_rating}')"
```

- `repr(obj)` 会使用这个方法。
- 讲师演示了 `__repr__` 中字符串参数应带引号，且引号应放在括号内，这样开发者能清楚看到：
  - 这是一个 `Microwave` 对象。
  - `brand` 是字符串。
  - `power_rating` 是字符串。
- 默认情况下，如果没有定义 `__repr__`，会得到类的默认表示，例如内存地址。
- 打印对象时，如果找不到 `__str__`，会使用 `__repr__`；因此 `__str__` 和 `__repr__` 的默认回退关系需要理解。

### 9.4 `__str__` 与 `__repr__` 的区别

- `__str__`：
  - 应返回用户友好的内容。
  - 目标是“你奶奶都能读懂”。
  - 例如显示品牌和功率设置的易读文本。
- `__repr__`：
  - 应返回对开发者有用的内容。
  - 目标是说明对象具体是什么、参数是什么。
  - 例如 `Microwave(brand='smeg', power_rating='B')`。
- 总结：
  - `print(obj)` / `str(obj)` 偏向 `__str__`。
  - `repr(obj)` / 交互式查看对象偏向 `__repr__`。
  - 如果没有 `__str__`，打印对象会回退到 `__repr__`。

## 10. 类的组织价值与复用（17:01-18:00）

- 类可以被视为组织代码的最佳方式之一，因为所有功能都与类耦合在一起。
- 这样可以在一个地方找到所需的数据和方法。
- 创建新对象时，几乎不需要额外努力就能让功能工作。
- 视频最后新增第三个微波炉 `Samsung`：
  - 品牌设置为 `Samsung`。
  - 功率等级按构造参数传入。
  - 创建后可以直接使用所有功能：

```python
samsung.turn_on()
samsung.run(1)
samsung.turn_off()
```

- `Samsung` 微波炉“开箱即用”，不需要重新实现打开、关闭、运行等逻辑。
- 如果没有使用类，每个微波炉都要单独创建数据和函数，需要付出很多重复劳动。
- 类的优势：
  - 数据和功能集中管理。
  - 新实例复用同一套行为。
  - 降低重复代码。
  - 容易扩展新的对象。

## 11. 关键结论与易错点清单

- 类名使用 PascalCase，例如 `Microwave`、`BlueCar`。
- 类名后加括号才会创建实例，例如 `Microwave()`。
- 实例化时如果 `__init__` 有参数，必须传入对应参数。
- 类型注解可选，只影响编辑器和可读性，不影响运行。
- `__init__` 是初始化器，创建实例后立即执行。
- `__init__` 默认返回 `None`，通常不需要返回其他值。
- `self` 指当前实例；可以改名，但惯例是 `self`。
- 属性必须通过 `self.xxx` 绑定到实例，否则不会成为该实例的数据。
- 方法第一个参数通常是 `self`，调用时不需要手动传入。
- 操作符默认不支持自定义对象；需要定义对应 dunder 方法，例如 `__add__`、`__mul__`。
- `__str__` 面向用户，`__repr__` 面向开发者。
- 打印对象时优先使用 `__str__`；没有 `__str__` 时会回退到 `__repr__`。
- 类的核心价值：把数据和功能封装在一起，创建新对象时可复用全部功能。