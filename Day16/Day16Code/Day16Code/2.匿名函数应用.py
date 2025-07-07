# 1.思考题【面试题】请写出下面代码执行的结果，并说明原因
def func():
    lst = []
    for x in range(5):
        print(x)   # 0 ~4
        lst.append(lambda n:x * n)  # 搞清楚列表中的元素是什么?------->其中的元素是匿名函数【本质上是函数的定义】
    print(lst)  # [<function func.<locals>.<lambda> at 0x0000024CF441C430>.....]
    # 此时列表中添加的是函数的定义，这些函数还未被调用，所以x * n还未被执行
    return lst
r = func()  # [<function func.<locals>.<lambda> at 0x0000024CF441C430>.....]
# print(r)
# print(r[0])  # 获取列表中的第0个元素，是一个函数
# print(r[0](2))  # 调用第0个函数，2表示给该函数传参
# 下面代码输出的结果，并说明原因
# 开始调用函数，此时x * n才会被执行，这种情况下，for循环已经执行完毕，x最后只能取到4
print(r[0](2))
print(r[1](2))
print(r[2](2))
print(r[3](2))
print(r[4](2))

'''
正常思维/错误结果：0  2 4 6 8
正确结果：8 8 8 8 8
为什么是上述结果：
'''

# 2.匿名函数作为其他函数的参数使用
# a.lst.sort(reverse=False,key=None)
# 1>lst.sort()默认情况下，如果lst中的元素支持大小比较，则可以直接排序
lst1 = [45,67,8,9,0]
lst1.sort()
print(lst1)

lst1 = [45,67,8,9,0]
lst1.sort(reverse=True)
print(lst1)

lst1 = ['45','fa','DG','vw','237']
lst1.sort()
print(lst1)

# 2>在lst.sort()中设置key参数，用途一：用于给列表中的元素自定义排序规则，用途二：如果列表中的元素不支持大小比较，自己设置比较规则
# students = [
# {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
# '15300022839'},
# {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
# '15300022838'},
# {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
# '15300022839'},
# {'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
# '15300022428'},
# {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
# '15300022839'},
# {'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
# '15300022839'}
# ]
# 错误写法：
# students.sort()   # TypeError: '<' not supported between instances of 'dict' and 'dict'
'''
sort的工作原理
列表中的元素支持大小比较：
    将列表中的元素俩俩之间进行大小的比较，如果符合条件，则交换元素的位置
列表中的元素不支持大小比较：
    If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
    a.key的值必须是一个函数，key=func
    b.会依次将列表中的元素传递给func,会自动调用func，给func设置返回值，该返回值表示排序的规则,而注意：该函数一定要支持大小比较
    c.如果函数存在，则直接使用，但是只能使用函数名，格式：key=函数名
      如果函数不存在，则需要先定义函数【def或lambda】，然后再使用
'''
# 需求1：将列表中的字符串按照长度排序
lst1 = ['45454','fa','DG525542','vw55','237']
lst1.sort(key=len)
print(lst1)  # ['fa', '237', 'vw55', '45454', 'DG525542']

lst1 = ['45454','fa','DG525542','vw55','237']
lst1.sort(key=len,reverse=True)
print(lst1)  # ['DG525542', '45454', 'vw55', '237', 'fa']

# 需求2：将下面列表中的元素按照成绩进行降序排序
students = [
{'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
'15300022838'},
{'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
'15300022839'},
{'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
'15300022428'},
{'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
'15300022839'},
{'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
'15300022839'}
]
# 不推荐
# def rule(x):
#     return x['score']
# students.sort(key=rule,reverse=True)
# print(students)

# 推荐                *********
students.sort(key=lambda x:x['score'],reverse=True)
print(students)

# b.max/min(value....key=None),通过给key赋值一个函数func，可以自定义查找最大值的规则，func的返回值就是规则
# 需求：获取年龄最大的人的姓名
dic = {'herry':20,'tom':18,'bob':22,'jack':25,'jerry':23}
# 默认表示对字典中的所有的key求最大值
print(max(dic))   # tom，等价于max(['herry','tom'....'jerry'])

def rule(x):
    return dic[x]
print(max(dic,key=rule))  # jack

print(max(dic,key=lambda ele:dic[ele]))  # jack


