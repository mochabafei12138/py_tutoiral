'''
reduce:减少
functools.reduce(func,sequence),返回值是一个value
    func：函数
    sequence：序列，如：列表，元组，字符串
功能：首先将seq中的第0个和第1个元素传递给func，进行指定的运算，返回结果a
     接着，将 结果a 和第2个元素传递给func，进行指定的运算，返回结果b
     接着，将 结果b 和第3个元素传递给func，进行指定的运算，返回结果c
     .....
     直到seq中的所有元素全部参与运算，才会停止，最后得到一个结果n
For example：
    reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    计算过程：((((1+2)+3)+4)+5)
'''

'''
注意：
    a.func函数必须设置两个参数，设置1个返回值
    b.区别于map，reduce使用之前一定要导入functools
'''

from functools import  reduce

# 1.已知列表 [1, 2, 3, 4, 5],求其中所有元素的和
list1 = [1, 2, 3, 4, 5]
def f(x,y):
    # print(x,y)
    return x + y
r1 = reduce(f,list1)
print(r1)

r1 = reduce(lambda x,y:x + y,list1)
print(r1)

# 练习1：用reduce求1~100之间所有整数的和
print(reduce(lambda x,y:x + y,range(1,101)))

# 练习2：用reduce求15的阶乘
print(reduce(lambda x,y:x * y,range(1,16)))

# 练习3：已知[3,1,7,4],得到3174
'''
3 1--->31---->3 * 10 + 1
31 7--->317--->31 * 10 + 7
317 4---->3174---->317 * 10 + 4
'''
print(reduce(lambda x,y:x * 10 + y,[3,1,7,4]))
