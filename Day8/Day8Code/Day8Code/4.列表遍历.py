numlist = [11,22,33,44,55,66,77,88,99]

# 遍历：将列表中的元素依次获取出来
# print(numlist[0])
# print(numlist[1])
# print(numlist[2])
# print(numlist[3])

# 方式一：只能获取到元素，适用于只操作元素的前提下   ******
for num in numlist:
    print(num)

# 方式二：获取到索引
i = 0
while i < len(numlist):
    print(i,numlist[i])
    i += 1

# 推荐for
for i in range(len(numlist)):
    print(i,numlist[i])

# 方式三：同时获取索引和元素
# 思路：将列表转化为enumerate,本质上也是一个容器，但是该容器中同时存储了索引和元素
# print(enumerate(numlist))   # <enumerate object at 0x00000283B9BBEFC0>
# print(list(enumerate(numlist))) # [(0, 11), (1, 22), (2, 33), (3, 44), (4, 55), (5, 66), (6, 77), (7, 88), (8, 99)]
for i,num in enumerate(numlist):   # 拆包
    print(i,num)

