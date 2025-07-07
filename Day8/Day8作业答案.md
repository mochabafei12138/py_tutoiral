### 初级编程题

1.已知列表names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']

​	a.取出names列表中索引4-7的元素

​	b.取出names列表中索引2-10的元素，步长为2

​	c.取出names列表中最后3个元素

​	d.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1

```Python
# a.取出names列表中索引4-7的元素
for i in range(4,8):
    print(names[i])

# b.取出names列表中索引2-8的元素，步长为2
for i in range(2,9,2):
    print(names[i])

# c.取出names列表中最后3个元素
for i in range(-3,0):
    print(names[i])

# d.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
for i in range(len(names)):
    if i % 2 == 0:
        names[i] = -1
    print("索引：%d-元素%s" % (i, names[i]))
```

2.已知一个列表names = ['鲁班七号','后裔', '狄仁杰', '黄忠', '孙尚香']，编写程序用两种方法获取names中的元素黄忠

```Python
names = ['鲁班七号','后裔', '狄仁杰', '黄忠', '孙尚香']
# 方式一
name1 = names[-2]
# 方式二
for name in names:
  if name == "黄忠":
    print(name)
```

3.已知一个数字列表nums = [1, 2, 3,1, 4, 2, 1 ,3, 7, 3, 3]，输出索引为奇数的元素

```Python
nums = [1, 2, 3,1, 4, 2, 1 ,3, 7, 3, 3]
for i in range(len(list1)):
    if i % 2 == 1:
        print(list1[i])
```

### 中级编程题

1. 已知一个数字列表nums = [1, 2, 5, 9]，根据该列表生成一个新的列表，其中的元素是nums中每个元素的2倍，**例如：**nums = [1, 2, 5, 9]   ->  nums = [2, 4, 10, 18]

   ```Python
   nums = [1, 2, 5, 9]
   new_nums = []
   for num in nums:
     	new_nums.append(num * 2)
   ```

2. 自定义一个数字列表，获取该列表中元素的最小值，注意: 自己实现，不能使用min函数

   ```Python
   numlist = [34,76,2,100,6,15]
   min_value = numlist[0]
   for num in numlist:
     	if num < min_value:
       	min_value = num
   print(min_value)
   ```

4. 用户输入月份,判断这个月是哪个季节，提示：先用列表定义季节包含的月份，然后再判断

   ```
   分析：
   3，4，5月----春季  6，7，8----夏季   9，10，11---秋季  12，1，2----冬季 
   ```
   ```Python
   #分析：
   #3，4，5月----春季  6，7，8----夏季   9，10，11---秋季  12，1，2----冬季 
   
   # 接收用户输入的月份
   month = int(input('month:'))
   
   # 定义列表
   spring = [3,4,5]
   summer = [6,7,8]
   autom = [9,10,11]
   winter = [12,1,2]
   
   # 判断输入的月份属于哪个季节
   # 列表的特性：成员操作符
   if month in spring:
       print('%s月是春天' %(month))
   elif month in summer:
       print('%s月是夏天' %(month))
   elif month in autom:
       print('%s月是秋天' %(month))
   elif month in winter:
       print('%s月是冬天' % (month))
   else:
       print('请输入正确的月份')
   ```
