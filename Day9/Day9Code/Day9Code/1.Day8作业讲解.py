names = ['old_driver','rain','jack','shanshan','peiqi','black_girl']
# c.取出names列表中最后3个元素
for i in range(-3,0):   # range(-1,-3,-1)
    print(names[i])

# d.循环names列表，打印每个元素的索引值，和元素，当索引值 为偶数时，把对应的元素改成-1
# 错误写法：
for i,num in enumerate(names):
    if i % 2 == 0:
        num = -1   # 只是将列表中的元素赋值给num，num只是一个普通的变量
    print(i,num)
print(names)  # ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']

# 正确写法
for i in range(len(names)):
    if i % 2 == 0:
        names[i] = -1   # 修改列表中的元素
    print(i,names[i])
print(names)   # [-1, 'rain', -1, 'shanshan', -1, 'black_girl']

# 自定义一个数字列表，获取该列表中元素的最小值，注意: 自己实现，不能使用min函数
numlist = [34,6,67,8,90,31,5,78]
# 假设法
min_value = numlist[0]
for num in numlist:
    if num < min_value:
        min_value = num
print(min_value)
