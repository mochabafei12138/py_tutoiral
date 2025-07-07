# 1.基本语法
# 需求：从控制台输入一个数，判断一个数是否能同时被5和8整除
# num = int(input('请输入一个数：'))
# if num % 5 == 0 and num % 8 == 0:   # and实现的语句可以使用嵌套if语句等价转换
#     print(f'{num}能被5和8同时整除')
#
# if num % 5 == 0:
#     print(f'{num}能被5整除')
#     if num % 8 == 0:
#         print(f'{num}能被5和8同时整除')
#
# if num % 5 == 0:
#     print(f'{num}能被5整除')
#     if num % 8 == 0:
#         print(f'{num}能被5和8同时整除')
# else:
#     print(f'{num}不能被5整除')
#
# if num % 5 == 0:
#     print(f'{num}能被5整除')
#     if num % 8 == 0:
#         print(f'{num}能被5和8同时整除')
#     else:
#         print(f'{num}不能被5和8同时整除')
# else:
#     print(f'{num}不能被5整除')

'''
注意：
    a.单分支，双分支和多分支两两之间可以互相嵌套
    b.嵌套的过程中，一定不要注意缩进问题
    c.理论上来说，嵌套的层数没有限制，但是，为了代码的可读性和后期的可维护性，建议嵌套的层数最多三层
'''

# 2.扩展：实际应用
num = input('请输入一个三位数：')
'''
x.isdigit():判断字符串x是否非空且全部由数字组成，如果是，则结果为True,如果不是，结果为False
len(x):获取列表，元组或集合中元素的个数
       获取字符串的长度  或者  获取字符串中字符的个数
'''
if num.isdigit():
    if len(num) == 3:
        num = int(num)
        gw = num % 10
        sw = num // 10 % 10
        bw = num // 100
        if num == gw ** 3 + bw ** 3 + sw ** 3:
            print(f'{num}是水仙花数')
        else:
            print(f'{num}不是水仙花数')
    else:
        print(f'{num}不是一个三位数')
else:
    print('输入有误')