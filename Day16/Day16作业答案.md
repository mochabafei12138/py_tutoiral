一、复习之前的内容，重点复习if语句，循环，列表、字典和字符串的系统功能

二、总结之前提到的面试题

三、完成下面的测试题

1.简述Python中列表，元组，字典以及集合各自的特点

> | 数据类型  | 是否可变 | 是否有序 |      是否存储重复元素      |        可以存储的数据类型        |
> | :-------: | :------: | :------: | :------------------------: | :------------------------------: |
> | 列表list  |   可变   |   有序   |          可以重复          |             任意类型             |
> | 元组tuple |  不可变  |   有序   |          可以重复          |             任意类型             |
> | 字典dict  |   可变   |   无序   | key:唯一的，value:可以重复 | key:不可变的数据，value:任意类型 |
> |  集合set  |   可变   |   无序   |         不可以重复         |           不可变的数据           |
> | 字符串str |  不可变  |   有序   |          可以重复          |               ----               |

2.简述Python中深拷贝和浅拷贝的区别并举例说明

```Python
# 一、浅拷贝:列表.copy()/ copy.copy() /切片
# 注意：拷贝列表的时候，只会拷贝列表的最外层
import copy
# 1.一维列表
list1 = [345,7,8]
# list2 = list1.copy()
# list2 = list1[:]
list2 = copy.copy(list1)
print(list1 is list2)    # False
list1[0] = 100
print(list1)  # [100,7,8]
print(list2)  # [345,7,8]


# 2.二维列表
list1 = [345,7,8,[45,7]]
list2 = list1.copy()
# list2 = list1[:]
# list2 = copy.copy(list1)
print(list1 is list2)    # False

# a，修改内层列表中的元素，会随着修改
# list1[-1][0] = 100
# print(list1)  # [345,7,8,[100,7]]
# print(list2)  # [345,7,8,[100,7]]

print(list1[-1] is list2[-1])  # True

# b.修改外层列表中的元素，不会随着修改
list1[-1] = 100
print(list1)   # [345,7,8,100]
print(list2)   # [345,7,8,[45,7]]

# 二、深拷贝：copy.deepcopy()
# 结论：无论一个列表如何修改，另一个列表都不受影响
# 1.一维列表
list1 = [345,7,8]
list2 = copy.deepcopy(list1)
print(list1 is list2)    # False
list1[0] = 100
print(list1)  # [100,7,8]
print(list2)  # [345,7,8]

# 2.二维列表
list1 = [345,7,8,[45,7]]
list2 = copy.deepcopy(list1)
print(list1 is list2)    # False

list1[-1][0] = 100
print(list1)  # [345,7,8,[100,7]]
print(list2)  # [345,7,8,[45,7]]

"""
在实际应用中
 对一维列表进行备份，使用 xxx.copy()
 对多维列表进行备份，使用 copy.deepcopy()
"""
```

3.写出下面代码的输出结果并说明原因

```python
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[10:])   
# [],列表切片，不会报错，只是不符合索引规则，得到的结果为[]
```

4.写出下面代码的输出结果并说明原因

```python
str1 = 'hello python'
str1.title()
print(str1)       
# hello python，字符串是不可变的，但凡涉及到修改的操作，都是生成了新的字符串，对原字符串没有任何影响
```

5.写出下面代码执行的结果并说明原因

```Python
list1=[5,3,1,9,12] 
r = (x for x in list1 if x%3==0) 
print(type(r))  
# <class 'generator'> ,这是一个生成器的语法，得到的结果 r 是一个生成器
```

6.在控制台中重复录入在西游记中你喜欢的人物。输入空字符串，打印所有人物。

```Python
like_list= []
while True:
    name = input ("请输入你喜欢的人物:")
    if name:
        like_list.append(name)
    else:
        break
print(like_list)
```

7.在控制台中录入，所有学生名字，如果姓名重复，则提示"姓名已经存在"，不添加到列表中，如果录入空字符串，则倒序打印所有学生

```Python
names_list=[]
while True:
    name_input=input("请输入学生姓名:")
    if name_input == "":
        break
    if name_input not in names_list:
        names_list.append(name_input)
    else:
        print("姓名已经存在")
print(names_list[::-1])
```

8.输入一个数字，转换成中文数字。比如：1 -----> 壹，5 -----> 伍

```Python
num = input("请输入一个数字：")
num_dict = {'1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖','10':'拾'}
if num in num_dict:
    print(num_dict[num])
```

9.有如下商品价格：568，239，368，425，121，219，834，1263，26，请输入随意一个价格区间进行商品的筛选，并能够对筛选出的商品进行从大到小和从小到大进行排序，并求出这个区间的商品的平均价格

```Python
numslist = [568,239,368,425,121,219,834,1263,2]
minprice,maxprice = eval(input("请输入两个数字表示价格区间："))
result_list = []
for num in numslist:
    if num in range(minprice,maxprice):
        result_list.append(num)
# 升序
result_list.sort()
print(result_list)

# 降序
result_list.sort(reverse=True)
print(result_list)

# 平均价格
avg_price = sum(result_list) / len(result_list)
print(avg_price)
```

10.编写程序，使用列表生成式生成一个包含50个随机整数的列表，然后删除其中所有奇数

```Python
import  random
numslist = [random.randint(1,100) for _ in range(50)]
print(numslist)
for num in numslist[:]:
    if num % 2 == 1:
        numslist.remove(num)
print(numslist)
```

