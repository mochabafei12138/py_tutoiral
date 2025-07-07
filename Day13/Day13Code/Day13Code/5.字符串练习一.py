# 1.写代码，有如下变量，请按照要求实现每个功能
name = "gouguoQ "

# a.移除name变量对应值的两边的空格，并输出移除后的内容
a1 = name.strip()
print(a1)
a2 = name.rstrip()
print(a2)

# b.判断name变量对应的值是否以"go"开头，并输出结果
print(name.startswith('go'))

# c.判断name变量对应的值是否以"Q"结尾，并输出结果
print(name.endswith('Q'))

# d.将name变量对应的值中的"o"，替换为"p"，并输出结果
d1 = name.replace('o','p')
print(d1)

t = str.maketrans('o','p')
d2 = name.translate(t)
print(d2)

# e.将name变量对应的值根据"o"分割，并输出结果
e1 = name.split('o')
print(e1)

# g.将name变量对应的值变大写，并输出结果
print(name.upper())

# h.将name变量对应的值变成小写，并输出结果
print(name.lower())

# i.请输出name变量对应的值的第二个字符
print(name[1])

# j.请输出name变量对应的值的前三个字符
print(name[:3])

# k.请输出name变量对应值的后2个字符
print(name[len(name) - 2:])
# print(name[-1:-3:-1])
print(name[-2::1])

# l.请输出name变量中的值"Q的索引的位置
print(name.index('Q'))
print(name.find('Q'))

# m.获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
print(name[:-1])
s = 'woaini'
print(s[:-1])

# n.利用下划线将列表li = ['gou', 'guo', 'qi']的每一个元素拼接成字符串gou_guo_qi
li = ['gou', 'guo', 'qi']
print('_'.join(li))