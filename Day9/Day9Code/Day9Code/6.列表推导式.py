
# 语法：[新列表中元素的规律       for循环     if判断]

# 1.已知一个数字列表nums = [1, 2, 5, 9]，根据该列表生成一个新的列表，其中的元素是nums中每个元素的2倍，
# 例如：[1, 2, 5, 9]   -> [2, 4, 10, 18]
nums = [1, 2, 5, 9]
# 方式一
nums1 = []
for num in nums:
    nums1.append(num * 2)
print(nums1)

# 方式二
nums2 = [num * 2 for num in nums]
print(nums2)

# 问题：xx.append()的返回值的为None，相当于将None作为新列表中的元素
nums2 = [nums1.append(num * 2) for num in nums]
print(nums2)   # [None, None, None, None]

# 2.将1~100之间3的倍数挑出来，生成一个新的列表
# 方式一
list21 = []
for n in range(1,101):
    if n % 3 == 0:
        list21.append(n)
print(list21)

# 方式二
list22 = [n for n in range(1,101) if n % 3 == 0]
print(list22)

# 扩展
list22 = [n ** 2 for n in range(1,101) if n % 3 == 0]
print(list22)

# 3.在列表推导式中，for语句和if语句可以根据具体的需求书写多个，从左往右表示依次嵌套的关系
# a
list31 = [m + n for m in 'abc' for n in '123']
print(list31)

# 工作原理
list31 = []
for m in 'abc':
    for n in '123':
        list31.append(m + n)
print(list31)

# b.
list32 = [n for n in range(1,101) if n % 3 == 0 if n % 5 == 0]
print(list32)

list32 = []
for n in range(1,101):
    if n % 3 == 0:
        if n % 5 == 0:
            list32.append(n)
print(list32)