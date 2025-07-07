### 选择题

1. 下面关于input的用法结果正确的是（C ）

  ```
  a = input("请输入一个数字：")
  print(type(a))
  ```

  A.报错                

  B.<class  'int'>

  C.<class 'str'>

  D.<class 'list'>

2. Python不支持的数据类型有（C  ）

   A.int      B.str     C.char     D.list

### 填空题

1. 语句a, b=10,20执⾏后，a的值是(  10 )；语句a, a = 10, 20 执⾏后，a的值是( 20 )。
2. 布尔类型中的True和False分别表示数字(    1  )和（   0  ）
3. 如果想要查看⼀个数据或者变量的数据类型，可以用（   type() ）函数。
4. 如果要查看一个数据或变量在内存中的地址，可以用（  id()  ）功能

### 编程题

**提示：Python中的加减乘除分别表示为  +     -      *    /**

1. 提示⽤户输入⽤户名和密码，将数据以指定格式打印出来，要求分别用占位符和f""实现，

   格式：用户名：xxx,密码：xxx

   ```Python
   name = input("请输入用户名:")
   pwd = input("请输入密码：")
   print(f"用户名：{name},密码：{pwd}")
   print("用户名：%s,密码：%s" % (name,pwd))
   ```

2. 已知数据’aaa‘,'bbb','ccc',用一个print输出，最终结果为aaa=bbb=ccc

   ```Python
   print('aaa','bbb','ccc',sep='=')
   print(f"{'aaa'}={'bbb'}={'ccc'}")
   ```

3. 从控制台输入两个数据，分别定义给两个变量，然后实现变量值的交换

   ```Python
   # 方式一:
   a = 10
   b = 20
   temp = a
   a = b
   b = temp
   print(a,b)    
   
   # 方式二：    
   a = 10
   b = 20
   a,b = b,a    
   print(a,b)
   ```

4. 从控制台输入圆的半径，计算该圆的周长和面积，圆周率可以定义为3.14

   ```Python
   r = input("请输入一个圆的半径：")
   r = float(r)
   PI = 3.14
   length = 2 * PI * r
   area = PI * r * r
   print(f"周长：{length},面积:{area}")
   print("周长：%.2f,面积：%.2f" % (length,area))
   ```

5. 一辆汽车以40km/h的速度行驶,行驶了45678.9km,求所用的时间

   ```Python
   speed = 40
   distance = 45678.9
   time = distance / speed
   print(f"所用的时间:{time}")
   ```

   ​
