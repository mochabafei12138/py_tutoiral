### Day8作业讲解

> ```Python
> names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']
> # c.取出names列表中最后3个元素
> for i in range(-3,0):   # range(-1,-3,-1)
>     print(names[i])
> 
> # d.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
> # 错误写法：
> for i,num in enumerate(names):
>     if i % 2 == 0:
>         num = -1   # 只是将列表中的元素赋值给num，num只是一个普通的变量
>     print(i,num)
> print(names)  # ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
> 
> # 正确写法
> for i in range(len(names)):
>     if i % 2 == 0:
>         names[i] = -1   # 修改列表中的元素
>     print(i,names[i])
> print(names)   # [-1, 'rain', -1, 'shanshan', -1, 'black_girl']
> 
> # 自定义一个数字列表，获取该列表中元素的最小值，注意: 自己实现，不能使用min函数
> numlist = [34,6,67,8,90,31,5,78]
> # 假设法
> min_value = numlist[0]
> for num in numlist:
>     if num < min_value:
>         min_value = num
> print(min_value)
> 
> ```

### 一、列表进阶

#### 1.列表系统功能【重点掌握】

> |               函数                |                             说明                             |
> | :-------------------------------: | :----------------------------------------------------------: |
> |             len(list)             |                       获取列表元素个数                       |
> |             max(list)             |                      返回列表元素最大值                      |
> |             min(list)             |                      返回列表元素最小值                      |
> |             list(seq)             |                       将元组转换为列表                       |
> |         list.append(obj)          |                    在列表末尾添加新的对象                    |
> |          list.count(obj)          |                统计某个元素在列表中出现的次数                |
> |         list.extend(seq)          | 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
> |          list.index(seq)          |           从列表中找出某个值第一个匹配项的索引位置           |
> |      list.insert(index,obj)       |                        将对象插入列表                        |
> |          list.pop(index)          | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
> |         list.remove(obj)          |                移除列表中某个值的第一个匹配项                |
> |          list.reverse()           |                        反向列表中元素                        |
> | list.sort(key=None,reverse=False) |                       对原列表进行排序                       |
> |            list.copy()            |                           复制列表                           |
> |           list.clear()            |                           清空列表                           |

##### 1.1增

> ```Python
> # 1.list.append(obj)在列表末尾添加新的对象,特点：obj表示任意类型   *******
> # 2.list.extend(iterable)在列表末尾一次性追加另一个序列中的多个值（用新列表中的元素扩展原来的列表）
> # 3.list.insert(index,obj)将数据插入到列表的指定索引处，原元素向后顺延,
> ```

> ```Python
> # 1.list.append(obj)在列表末尾添加新的元素,特点：obj表示任意类型   *******
> list1 = [12,4,5]
> print(list1)
> list1.append(55)
> list1.append(False)
> list1.append('faf')
> list1.append([45,67,9,0])
> print(list1)  # [12, 4, 5, 55, False, 'faf', [45, 67, 9, 0]]
> 
> # 2.list.extend(iterable)在列表末尾一次性追加另一个序列中的多个值（用新列表中的元素扩展原来的列表）
> # iterable:list tuple  dict set str等
> list2 = [12,4,5]
> print(list2)
> list2.extend('abc')
> list2.extend([45,7])
> list2.extend((56,8))
> print(list2)   # [12, 4, 5, 'a', 'b', 'c', 45, 7, 56, 8]
> '''
> 注意：
>     a.extend只能添加iterable类型的数据
>     b.添加进去的数据不包含容器本身
> '''
> 
> # 3.list.insert(index,obj)将数据插入到列表的指定索引处，原元素向后顺延
> list3 = [34,8,10]
> print(list3)
> list3.insert(1,88)
> print(list3)   # [34, 88, 8, 10]
> 
> # 需求：将数据插入到末尾
> # 【面试题】注意：insert也可以实现追加元素的效果，当index >= len()
> # list3.insert(4,'abc')
> # print(list3)   # [34, 88, 8, 10, 'abc']
> 
> # 需求：将数据插入到开头
> list3.insert(0,'abc')
> print(list3)   # ['abc', 34, 88, 8, 10]
> ```

##### 1.2删

> ```Python
> # 1.list.remove(obj)移除列表中某个值的第一个匹配项   *******
> # 2.list.pop(index)移除列表中的一个元素（默认最后一个元素），并且返回该元素的值  ******
> # 3.list.clear()清空列表
> # 4.del list[index]
> ```

> ```Python
> 
> # 问题
> # 注意：列表是可变的数据类型，所以一般情况下，但凡涉及到列表元素的更改，都是在原列表内部进行操作的，要查看结果，直接输出列表本身即可
> list1 = [12,4,5]
> r1 = list1.append(55)
> print(r1)  # None
> print(list1)  # [12, 4, 5, 55]
> 
> # 1.list.remove(obj)移除列表中某个值的第一个匹配项   *******
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> print(list1)
> list1.remove(6)
> print(list1)
> 
> # 问题1：删除列表中所有的6,则需要用到循环处理
> # list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> # for _ in range(8):
> #     list1.remove(6)
> # print(list1)
> 
> # 问题2：元素不存在,ValueError: list.remove(x): x not in list
> # 注意：删除列表中元素之前，建议尽量先判断元素在列表中是否存在
> num = 10
> if num in list1:
>     list1.remove(num)
> 
> # 问题3：删除列表中所有的6
> # 错误代码
> '''
> 出现问题的原因：
>     [34,6,87,9,34,6,6,6,6,6,6,6,8,12]--->0~1
>     [34,87,9,34,6,6,6,6,6,6,6,8,12] ----> 2
>     在遍历列表的过程中，同时删除该列表中的元素，会导致列表变短，所以循环结束的时候，有些元素还未来得及删除
> '''
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> for num in list1:
>     print(num)
>     if num == 6:
>         list1.remove(num)
> print(list1)   # [34, 87, 9, 34, 6, 6, 6, 8, 12]
> 
> # 解决方案
> '''
> 解决方案：
>     a.将删除改为添加
>     b.对列表进行备份【拷贝】,为了保证循环的次数不变，还是原列表的长度
> '''
> # 方式一  *******
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> new_list1 = []
> for num in list1:
>     if num != 6:
>        new_list1.append(num)
> print(new_list1)  # [34, 87, 9, 34, 8, 12]
> 
> # 方式二    ******
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> for num in list1.copy():  # 遍历备份之后的列表
>     if num == 6:
>         list1.remove(num) # 删除原列表
> print(list1)   # [34, 87, 9, 34, 8, 12]
> 
> # 方式三：工作原理
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> i = 0
> while i < len(list1):
>     if list1[i] == 6:
>         list1.remove(6)
>         i -= 1   # 为了保证每个元素都可以被遍历到
>     i += 1
> print(list1)
> 
> # 2.list.pop(index)移除列表中的一个元素（默认最后一个元素），并且返回该元素的值  ******
> list2 = [34,6,87,9,34,6,8,12]
> print(list2)
> # a.默认删除列表中的最后一个元素
> # list2.pop()
> # print(list2)
> 
> # b.删除指定元素
> # list2.pop(2)
> # print(list2)
> 
> # c.pop:弹出，只是将指定索引处的元素从列表中弹出，并没有被销毁，而remove会直接销毁
> r = list2.pop()  # r可以将pop之后的结果接出来，该结果表示被弹出的元素
> print(r)  # 12
> print(list2)
> 
> # 3.list.clear()清空列表
> list3 = [34,6,87,9,34,6,8,12]
> print(list3)
> list3.clear()
> print(list3)
> 
> # 4.del list[index]
> list4 = [34,6,87,9,34,6,8,12]
> print(list4)
> del list4[0]
> print(list4)
> 
> # 注意：
> list4 = [34,6,87,9,34,6,8,12]
> del list4    # 删除列表
> # print(list4)  # NameError: name 'list4' is not defined
> 
> list4 = [34,6,87,9,34,6,8,12]
> list4.clear()  # 清空列表
> print(list4)  # []
> ```

##### 1.3改

> ```Python
> # 1.list.sort(key=None,reverse=False)对原列表进行排序       ******
> # 2.list.reverse()翻转列表中元素   ******
> ```

> ```Python
> # 1.list.reverse()翻转/反转/逆序列表中元素   ******
> list1 = [34,6,87,9,34,6,8,12]
> print(list1)
> list1.reverse()
> print(list1)
> 
> # 2.list.sort(key=None,reverse=False)对原列表进行排序       ******
> # 注意：如果要对列表中的元素进行排序，一定要先保证列表中的元素是可以比较大小的
> # a.升序
> list1 = [34,6,87,9,34,6,8,12]
> print(list1)
> list1.sort()
> print(list1)
> 
> # b.降序
> list1 = [34,6,87,9,34,6,8,12]
> print(list1)
> list1.sort(reverse=True)
> print(list1)
> 
> 
> 
> 
> ```

##### 1.4查

> ```Python
> # 1.len(list)获取列表元素个数       ********
> # 2.max(list)返回列表元素最大值
> # 3.min(list)返回列表元素最小值
> # 4.list.count(obj)统计某个元素在列表中出现的次数  ******
> # 5.list.index(obj)从列表中找出某个值第一个匹配项的索引位置
> ```

> ```Python
> 
> list1 = [34,6,87,9,34,6,8,12]
> 
> # 1.len(list)获取列表元素个数       ********
> print(len(list1))
> # 2.max(list)返回列表元素最大值
> print(max(list1))
> # 3.min(list)返回列表元素最小值
> print(min(list1))
> # 4.list.count(obj)统计某个元素在列表中出现的次数  ******
> r1 = list1.count(34)
> print(r1)
> 
> # 优化：删除列表中所有的6,则需要用到循环处理
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> c = list1.count(6)
> for _ in range(c):
>     list1.remove(6)
> print(list1)
> 
> # 5.list.index(obj)从列表中找出某个值第一个匹配项的索引位置
> list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
> i1 = list1.index(6)
> print(i1)
> 
> # i2 = list1.index(10)   # ValueError: 10 is not in list
> 
> ```

#### 2.列表推导式【重点掌握】

> 列表推导式，就是指的轻量级循环创建列表的方式
>
> 列表推导式/列表生成式:是Python特有的语法，通过循环和if语句专门用来创建列表
> 特点：根据一个已知的Iterable,使用一行代码实现简单的逻辑，生成一个新的列表
>
> 语法：[新列表中元素的规律       for循环     if判断]
>
> 工作原理：执行for循环，获取已知iterable中的元素，结合if进行判断，最终得到新的列表中元素的规律
> 作用：生成列表
>
> ```Python
> 
> # 语法：[新列表中元素的规律       for循环     if判断]
> 
> # 1.已知一个数字列表nums = [1, 2, 5, 9]，根据该列表生成一个新的列表，其中的元素是nums中每个元素的2倍，
> # 例如：[1, 2, 5, 9]   -> [2, 4, 10, 18]
> nums = [1, 2, 5, 9]
> # 方式一
> nums1 = []
> for num in nums:
>     nums1.append(num * 2)
> print(nums1)
> 
> # 方式二
> nums2 = [num * 2 for num in nums]
> print(nums2)
> 
> # 问题：xx.append()的返回值的为None，相当于将None作为新列表中的元素
> nums2 = [nums1.append(num * 2) for num in nums]
> print(nums2)   # [None, None, None, None]
> 
> # 2.将1~100之间3的倍数挑出来，生成一个新的列表
> # 方式一
> list21 = []
> for n in range(1,101):
>     if n % 3 == 0:
>         list21.append(n)
> print(list21)
> 
> # 方式二
> list22 = [n for n in range(1,101) if n % 3 == 0]
> print(list22)
> 
> # 扩展
> list22 = [n ** 2 for n in range(1,101) if n % 3 == 0]
> print(list22)
> 
> # 3.在列表推导式中，for语句和if语句可以根据具体的需求书写多个，从左往右表示依次嵌套的关系
> # a
> list31 = [m + n for m in 'abc' for n in '123']
> print(list31)
> 
> # 工作原理
> list31 = []
> for m in 'abc':
>     for n in '123':
>         list31.append(m + n)
> print(list31)
> 
> # b.
> list32 = [n for n in range(1,101) if n % 3 == 0 if n % 5 == 0]
> print(list32)
> 
> list32 = []
> for n in range(1,101):
>     if n % 3 == 0:
>         if n % 5 == 0:
>             list32.append(n)
> print(list32)
> ```

#### 3.二维列表

> ```python
> # 1.一维列表
> list1 = [34,67,8,9,'dada',False,34.1]
> 
> # 2.二维列表
> list2 = [[12,4,6],[56,8,9,67,8,9],[3,5]]
> 
> # 3.二维列表中元素的访问
> sublist1 = list2[0]
> print(sublist1)
> num1 = sublist1[1]
> print(num1)
> 
> num2 = list2[-1][0]
> print(num2)
> 
> # 3.遍历二维列表
> # a.直接遍历元素
> for sublist in list2:
>     print(sublist)
>     for num in sublist:
>         print(num)
> 
> # 问题：
> list3 = [[34,6,77],34,76,8,9,[34,6,8,9,90]]
> for sublist in list3:
>     print(sublist)
>     if type(sublist) == list:
>         for num in sublist:
>             print(num)
>     else:
>         print(sublist)
> 
> # b.遍历索引
> for i in range(len(list2)):  # 遍历外层列表
>     print(i,list2[i])
>     for j in range(len(list2[i])):     # 遍历内层列表
>         print(list2[i][j])
> ```