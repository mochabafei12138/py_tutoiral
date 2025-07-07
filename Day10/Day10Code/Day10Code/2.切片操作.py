"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
"""
注意：
    a.切片之后会得到一个新的列表，对原列表没有任何影响,相当于是列表的拷贝
    b.在切片操作中，只要符合切片的语法，哪怕索引越界都不会报错，区别无非是列表是否为空
"""
numlist = [10,20,30,40,50,60,70,80,90]

# 一、基本使用【掌握】
# 1.注意1：明确end的情况下，end不包含在内
print(numlist[1:6])   # 前闭后开区间， [20, 30, 40, 50, 60]
print(numlist[1:6:1])  #  [20, 30, 40, 50, 60]
print(numlist[1:6:2]) # [20, 40, 60]
print(numlist)

# 2.注意2：end省略的情况下，从指定索引取到结尾，此时end包含在内
print(numlist[1:])  # [20, 30, 40, 50, 60, 70, 80, 90]

# 从左往右全部获取，拷贝列表，[10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numlist[::1])
print(numlist[::])
print(numlist[:])   # ********

# 从右往左全部获取，逆序拷贝列表,[90, 80, 70, 60, 50, 40, 30, 20, 10]
print(numlist[::-1])  # *******

# 3.【面试题】
# print(numlist[100])    # 不是切片，是访问列表中元素的语法，会索引越界，IndexError: list index out of range
print(numlist[100:])     # 是切片【至少出现一个冒号】，结果是[]

# 二、规律用法【了解】
# 1.
"""
规律1：如果start和end同正负
    第一步：计算start+step
    第二步：判断第一步计算的结果是否在给定的start和end区间内
    第三步：如果在区间内，则按照规律获取元素；如果不在区间内，则直接得结果[]
"""
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
# 注意：不管索引为正为负，只要end不省略，则end对应的元素都取不到
print(numlist[1:6:1])   # [20,30,...60]
print(numlist[1:6:-1])  # []

print(numlist[6:1:1])   # []
print(numlist[6:1:-1])  # [70,60...30]

print(numlist[-1:-6:1])   # []
print(numlist[-1:-6:-1])  # [90.80....50]

print(numlist[-6:-1:1])  # [40,50...80]
print(numlist[-6:-1:-1]) # []

# 2.
"""
规律2：如果start和end一个为正，一个为负
    第一步：查看start的正负，索引的使用和start的正负保持一致
    第二步：如果start为正，则使用正数索引【将end的索引等价转换为正数索引】
           如果start为负，则使用负数索引【将end的索引等价转换为负数索引】
    第三步：使用规律1
"""
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
print(numlist[-1:6:1])   # [-1:-3:1]---->[]
print(numlist[-1:6:-1])  # [-1:-3:-1]---->[90,80]

print(numlist[-6:1:1])   # [-6:-8:1]--->[]
print(numlist[-6:1:-1])  # [-6:-8:-1]--->[40,30]

print(numlist[1:-6:1])  # [1:3:1]--->[20,30]
print(numlist[1:-6:-1])  # [1:3:-1]--->[]

print(numlist[6:-1:1])   # [6:8:1]--->[70,80]
print(numlist[6:-1:-1])  # []

# 3.
"""
规律3：如果start和end都被省略，观察step的正负
    a.如果step为正数，则从左往右进行获取【顺序获取】
    b.如果step为负数，则从右往左进行获取【倒序获取】  
"""
print(numlist[:])
print(numlist[::-1])

# 4.
"""
规律4：列表[start::step]
    a.如果step为正数，则从左往右进行获取【顺序获取】
    b.如果step为负数，则从右往左进行获取【倒序获取】  
"""
"""
   0   1   2   3   4   5   6   7     8
  -9   -8  -7  -6  -5  -4  -3  -2   -1
  10   20  30  40  50  60  70  80   90
"""
print(numlist[6::-1])  # [60,50...10]
print(numlist[6::1])   # [70,80,90]

print(numlist[-6::-1])  # [40...10]
print(numlist[-6::1])   # [40,50,..90]

# 练习：
names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']
# a.取出names列表中索引4-7的元素
# for i in range(4,8):
#     print(names[i])

print(names[4:8])

# b.取出names列表中索引2-10的元素，步长为2
# for i in range(2,11,2):
#     print(names[i])

print(names[2:11:2])

# c.取出names列表中最后3个元素
for i in range(-3,0):   # range(-1,-3,-1)
    print(names[i])

print(names[-1:-4:-1])
print(names[len(names)-3:])