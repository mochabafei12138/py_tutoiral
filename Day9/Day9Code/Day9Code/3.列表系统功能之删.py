
# 问题
# 注意：列表是可变的数据类型，所以一般情况下，但凡涉及到列表元素的更改，都是在原列表内部进行操作的，要查看结果，直接输出列表本身即可
list1 = [12,4,5]
r1 = list1.append(55)
print(r1)  # None
print(list1)  # [12, 4, 5, 55]

# 1.list.remove(obj)移除列表中某个值的第一个匹配项   *******
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
print(list1)
list1.remove(6)
print(list1)

# 问题1：删除列表中所有的6,则需要用到循环处理
# list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
# for _ in range(8):
#     list1.remove(6)
# print(list1)

# 问题2：元素不存在,ValueError: list.remove(x): x not in list
# 注意：删除列表中元素之前，建议尽量先判断元素在列表中是否存在
num = 10
if num in list1:
    list1.remove(num)

# 问题3：删除列表中所有的6
# 错误代码
'''
出现问题的原因：
    [34,6,87,9,34,6,6,6,6,6,6,6,8,12]--->0~1
    [34,87,9,34,6,6,6,6,6,6,6,8,12] ----> 2
    在遍历列表的过程中，同时删除该列表中的元素，会导致列表变短，所以循环结束的时候，有些元素还未来得及删除
'''
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
for num in list1:
    print(num)
    if num == 6:
        list1.remove(num)
print(list1)   # [34, 87, 9, 34, 6, 6, 6, 8, 12]

# 解决方案
'''
解决方案：
    a.将删除改为添加
    b.对列表进行备份【拷贝】,为了保证循环的次数不变，还是原列表的长度
'''
# 方式一  *******
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
new_list1 = []
for num in list1:
    if num != 6:
       new_list1.append(num)
print(new_list1)  # [34, 87, 9, 34, 8, 12]

# 方式二    ******
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
for num in list1.copy():  # 遍历备份之后的列表
    if num == 6:
        list1.remove(num) # 删除原列表
print(list1)   # [34, 87, 9, 34, 8, 12]

# 方式三：工作原理
list1 = [34,6,87,9,34,6,6,6,6,6,6,6,8,12]
i = 0
while i < len(list1):
    if list1[i] == 6:
        list1.remove(6)
        i -= 1   # 为了保证每个元素都可以被遍历到
    i += 1
print(list1)

# 2.list.pop(index)移除列表中的一个元素（默认最后一个元素），并且返回该元素的值  ******
list2 = [34,6,87,9,34,6,8,12]
print(list2)
# a.默认删除列表中的最后一个元素
# list2.pop()
# print(list2)

# b.删除指定元素
# list2.pop(2)
# print(list2)

# c.pop:弹出，只是将指定索引处的元素从列表中弹出，并没有被销毁，而remove会直接销毁
r = list2.pop()  # r可以将pop之后的结果接出来，该结果表示被弹出的元素
print(r)  # 12
print(list2)

# 3.list.clear()清空列表
list3 = [34,6,87,9,34,6,8,12]
print(list3)
list3.clear()
print(list3)

# 4.del list[index]
list4 = [34,6,87,9,34,6,8,12]
print(list4)
del list4[0]
print(list4)

# 注意：
list4 = [34,6,87,9,34,6,8,12]
del list4    # 删除列表
# print(list4)  # NameError: name 'list4' is not defined

list4 = [34,6,87,9,34,6,8,12]
list4.clear()  # 清空列表
print(list4)  # []