1.调用python列表操作中常用函数，实现以下功能：

```
1)    创建一个空列表lst；

2)    在lst列表中依次追加10个数值[8, 93, 66, 83, 100, 95, 77, 93, 85, 98]

3)    输出lst列表中第7个元素的数值；

4)    输出lst列表中第1~5个元素的数值；

5)    在lst列表第7个元素之前添加数值59；

6)    利用变量num保存数值93，调用count()函数，查询num变量值在lst列表中出现的次数；

7)    查询lst列表中是否有num = 10；

8)    查询lst列表中100的序号；

9)    找出lst列表中数值为59的元素，并加1；

10) 删除lst列表中的第1个元素；

11) 获得lst列表中元素的个数；

12) 对列表中所有元素进行排序，输出列表中最高分和最低分；

13) 反转lst列表中元素的顺序；

14) 删除lst列表中尾部的元素，返回删除的元素；

15) 向lst列表中追加数值83，并输出。调用remove()函数删除lst列表中第一个数值83；

16) 创建2个列表lst1和lst2，lst1中包含2个元素值：78，91，lst2中包含3个元素值：84，92，65，合并这两个列表，并输出全部元素；

17) 创建lst1列表，其中包含数值2个元素值：78，91，将lst1中元素赋值5遍保存在lst2列表中，输出lst2列表中全部元素;

18) 清空lst列表，将lst2列表复制给lst列表，将lst列表中第2个元素变为2，并分别输出lst列表、lst2列表全部元素
```
```Python
lst=[]

lst +=[78,93,66,83,100,95,77,93,85,98]
lst.extend([78,93,66,83,100,95,77,93,85,98])

lst[6]

lst[0:5]

lst.insert(6,59)

num=93
lst.count(num)

num in lst

lst.index(100)

i=lst.index(59)
lst[i] += 1

del lst[0]

len(lst)


lst.sort()
print(lst[-1],lst[0])


lst.reverse()


lst.pop(9)


lst.append(83)

lst.remove(83)


lst1=[78,91]
lst2=[84,92,65]
lst1+lst2


lst1=[78,91]
lst2=lst1*5


lst=[]
lst=lst2
lst[1]=2

lst[1]=91
lst[1]=2
```

2.根据列表推导式完成下面的题目

a. 生成一个存放1-100之间个位数为3的数据列表

```
结果为 [3, 13, 23, 33, 43, 53, 63, 73, 83, 93]
```

```Python
list_a = [n for n in range(1,101) if n % 10 == 3]
print(list_a)
```

b. 利用列表推导式将已知列表中的整数提取出来

```python
例如：[True, 17, "hello", "bye", 98, 34, 21] --- [17, 98, 34, 21]
```

```Python
list_b = [True, 17, "hello", "bye", 98, 34, 21]
new_list_b = [ele for ele in list_b if type(ele) == int]
print(new_list_b)
```

c.利用列表推导式存放指定列表中字符串的长度

```
例如 ["good", "nice", "see you", "bye"] --- [4, 4, 7, 3]
```

```Python
list_c =  ["good", "nice", "see you", "bye"]
# len()
new_list_c = [len(s) for s in list_c]
print(new_list_c)
```

d.生成一个列表，其中的元素为'0-1'，'1-2'，'2-3'，'3-4'，'4-5'

```Python
list_d1 = [str(n) + '-' + str(n + 1) for n in range(5)]
print(list_d1)
list_d2 = [f'{n}-{n + 1}' for n in range(5)]
print(list_d2)
```

3.根据products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号,
就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。注意：本题可以自由发挥

```
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
```

```Python
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
# print('============','欢迎进入xxx自助购物超市','============')
# 扩展：xxx.center(width,ch):将xxx字符串居中显示，两端用ch填充，最终字符串的长度为width
print('欢迎进入xxx自助购物超市'.center(50,'='))
# 购物车
shop_car = []
while True:
  print('商品信息如下：')
  for i,pro in enumerate(products):
      print(f'    编号{i}:名称：{pro[0]},价格:{pro[1]}')
  # 询问用户想买什么，用户选择一个商品编号
  choice = input('请输入需要购买的商品的编号【输入q退出】：')
  # 扩展：
  '''
  xxx.lower():将xxx字符串转化为小写
  xxx.upper():将xxx字符串转化为大写
  print('ffaa'.lower())  # 'ffaa'
  print('HFRDggq'.lower())  # hfrdggg
  '''
  # if choice == 'q' or choice == 'Q':
  if choice.lower() == 'q':
      print('购买完毕，退出系统')
      break
  if choice.isdigit():
      choice = int(choice)
      if choice in range(len(products)):
          # 添加到购物车
          shop_car.append(products[choice])
          print('添加成功!')
      else:
          print('暂无此商品')
  else:
      print('输入有误')
if shop_car:
  print(f'购物车列表为：{shop_car}')
else:
  print('没有购买任何商品')
```

