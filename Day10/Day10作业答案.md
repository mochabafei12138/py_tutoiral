1.已知列表list1 = ['mon','sun','sat','fri','thu','wed'],list2 = ['sun','wed','thu']，将属于list2的元素从list1中删除

```Python
list1 = ['mon','sun','sat','fri','thu','wed']
list2 = ['sun','wed','thu']
# 方式一
for ele in list2:
	if ele in list1:
		list1.remove(ele)
print(list1)

# 方式二
for ele in list1[:]:
    if ele in list2:
        list1.remove(ele)
print(list1)

# 方式三
for ele in list1.copy():
    if ele in list2:
        list1.remove(ele)
print(list1)
```

2.输入一个包含若干整数的列表，输出新列表，要求新列表中的所有元素来自于输入的列表，并且降序排列

```Python
a = input("输入列表元素：")
item = a.split(" ")
new_list = [eval(x) for x in item]
new_list.sort(reverse=True)
print(new_list)
```

3.高考录取率

根据十年高考录取率表创建列表，并完成如下操作：
① 计算十年平均录取率。
② 找出录取率最高的年份。

```Python
year = [(2006,57),(2007,56),(2008,57),(2009,62),(2010,67),(2011,72),(2012,75),(2013,76),(2014,74.3),(2015,74)]
```

```Python
year=[(2006,57),(2007,56),(2008,57),(2009,62),(2010,67),(2011,72),(2012,75),(2013,76),(2014,74.3),(2015,74)]

rate = [x[1] for x in year]
avg = sum(rate) / len(rate)
print("平均录取率{}".format(avg))
max_avg = max(rate)
max_year = year[rate.index(max_avg)]
print("录取最高年份{}".format(max_year[0]))
```

3.编写程序，实现分段函数的计算，分段函数的取值如下表所示。要求：可连续输入5次，每次的结果都将添加到列表中

| 自变量x  | 因变量y |
| -------- | ------- |
| x＜0     | 0       |
| 0≤x＜5   | x       |
| 5≤x＜10  | 3x-5    |
| 10≤x＜20 | 0.5x-2  |
| x≥20     | 0       |

```Python
list1 = []
for i in range(5):
    x = eval(input('请输入 x 的值：'))
    if x < 0:
        y = 0
    elif 0 <= x < 5:
        y = x
    elif 5 <= x < 10:
        y = 3*x - 5
    elif 10 <= x < 20:
        y = 0.5*x - 2
    elif x >= 20:
        y = 0
    list1.append(y)
print(list1)
```

4.如果两个素数之差为2,这样的两个素数就叫作"孪生数",找出100以内的所有的素数保存到列表中，并找出其中的"孪生数"

```Python
ls = []
for num in range(2,101):
	flag = True
	for i in range(2,num):
		if num%i == 0:
			flag = False
			break
	if flag:
		ls.append(num)
print("1~100以内的素数有：")
print(ls)
i = 1
while i < len(ls):
	if ls[i] - ls[i - 1] == 2:
		print("{}和{}是孪生数".format(ls[i], ls[i - 1]),end="\n\n")
		if i == 6 or i == 10:
			print(" ")
	i += 1
```

