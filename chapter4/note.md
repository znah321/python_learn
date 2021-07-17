## 第4章 操作列表

### 4.1 遍历整个列表

使用循环可以遍历列表。

假设有这样一个列表：

```python
magicians = ['alice', 'david', 'carolina']
```

使用这样的循环：

```python
for magician in magicians:
```

`magician`代表列表中的**具体值**，而不是**值的索引**，这个`magician`也可以随便写，只要符合变量命名规则就可以。

+ **在使用for循环的时候，需要注意代码缩进。**



### 4.2 range()函数

在python中，使用`range()`函数来生成一系列的数字。

```python
for value in range(a,b):
	print(value)
```

这个for循环将会输出的范围为$[a,b)$，默认的步长为1；也可以指定步长：

```python
for value in range(a,b,step):
```



### 4.3 创建数值列表

可使用函数`list()`将`range()`的结果直接转换为列表：

```python
a = list(range(1,6))
# a = [1, 2, 3, 4, 5]
```

有几个专门用于处理数字列表的Python函数：

+ `min(list)`：列表中的最小值
+ `max(list)`：列表中的最大值
+ `sum(list)`：求和

也可以只用一行代码创建列表：

```python
myList = [value**2 for value in range(1,11)]
```

`value**2`是列表中存储的值，后面的for循环将值1~10提供给表达式`value**2`，且**不需要写括号**。



### 4.4 使用列表的一部分

使用列表索引为$a\sim b$的值：

```python
mylist[a:b-1]
```

如果没有指定左边的索引，则直接从开头进行提取；如果没有指定右边的索引，则直接提取到末尾。

支持反向提取（即使用负数）。



如果要复制列表，可以**同时省略起始索引和终止索引**（即`[:]`）：

```python
list1 = mylist[:]
```



### 4.5 元组

**不可变的列表**称为元组，列表大小和值都不能改变。

```python
dimensions = (200, 50)
```

+ 元组的定义方式也不同，用的是**圆括号**。
+ 访问方式和列表一样，如`dimensions[1]`。
+ 虽然不能更改元组内的值，但可以**把一个变量储存的元组换成另一个元组**。