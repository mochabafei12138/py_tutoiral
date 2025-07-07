# 1.and：与
'''
真  and  真 ----》真
真  and  假----》假
假  and  真 ----》假
假  and  假 ----》假

规律：一假为假，全真为真
'''
print('abc' and 1)
print('abc' and 'xyz')
print('abc' and [4,6,7])
print('abc' and True)
print('abc' and 34.6)
print('abc' and 56)

print('abc' and 0)
print('abc' and '')
print('abc' and [])
print('abc' and False)
print('abc' and 0.0)
print('abc' and {})

print('+++++++++')

print(0 and 1)
print(0 and 'xyz')
print(0 and [4,6,7])
print(0 and True)
print(0 and 34.6)
print(0 and 56)

print(0 and 0)
print(0 and '')
print(0 and [])
print(0 and False)
print(0 and 0.0)
print(0 and {})

'''
结论：A  and  B
    a.如果A为真，则A and  B整个表达式的结果为B的值
    b.如果A为假，则A and B整个表达式的结果为A的值，此时的B会被短路
'''

# 2.or:或
'''
真  or  真 ----》真
真  or  假----》真
假  or  真 ----》真
假  or  假 ----》假

规律：一真为真，全假为假
'''

print('abc' or 1)
print('abc' or 'xyz')
print('abc' or [4,6,7])
print('abc' or True)
print('abc' or 34.6)
print('abc' or 56)

print('abc' or 0)
print('abc' or '')
print('abc' or [])
print('abc' or False)
print('abc' or 0.0)
print('abc' or {})

print('+++++++++')

print(0 or 1)
print(0 or 'xyz')
print(0 or [4,6,7])
print(0 or True)
print(0 or 34.6)
print(0 or 56)

print(0 or 0)
print(0 or '')
print(0 or [])
print(0 or False)
print(0 or 0.0)
print(0 or {})

'''
结论：A  or  B
    a.如果A为真，则A or  B整个表达式的结果为A的值，此时的B会被短路
    b.如果A为假，则A or B整个表达式的结果为B的值
'''

# 3.not:非
# 注意：not x的结果一定是布尔值
'''
not 真----》假
not  假----》真
'''
print(not 0)  # True
print(not 'abc')   # False

# 问题一：
print(not '0')   # False
print(not 'False')   # False

# 问题二:优先级：关系运算符 > 逻辑运算符
x = 45
y = 23
z = 100
print(x < y and y == z)  # 只有两个表达式都成立时结果才是True
print(x < y or y == z)   # 至少有一个表达式成立时结果就是True
