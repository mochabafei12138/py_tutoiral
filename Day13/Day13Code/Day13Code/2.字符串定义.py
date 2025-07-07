# 1.基本定义
# 注意：在单个引号中，按照回车进行换行，只是视觉上的折行，而数据原本还是一行
# 字符串的组成：数字，字母，符号，中文都可以出现在字符串中，但凡是要表示成文本的数据，都用字符串表示
# a.单引号
str1 = '23fahj' \
       '计算机' \
       '&……%'
print(str1)

# b.双引号
str2 = "23fahj计算机&……%"
print(str2)

# c.三引号
str3 = '''6463
hrwthw
&^^%
中科院'''
print(str3)

str3 = """6463
hrwthw
&^^%
中科院"""
print(str3)

# 2.将字符串存储在容器中
list1 = ['abc', 'gwg', '4545']
print(list1)

list2 = ["abc", "gwg", "4545"]
print(list2)

# 3.转义字符
'''
/:斜杠
\:反斜杠
'''
# \xx:如果xx是一个普通字符，\xx可能具有特殊含义
# \xx:如果xx是一个特殊字符，\xx会将特殊字符转义为普通字符
# 上述操作并不是对所有字符都起作用
# a.\n        *****
# n是一个普通字符，但是\n具有特殊含义，表示换行
s1 = 'abc345n5351'
print(s1)
s1 = 'abc345\n5351'
print(s1)

# b.\t        ******
# t是一个普通字符，但是\t具有特殊含义，表示制表符tab键
s1 = 'abc345t5351'
print(s1)
s1 = 'abc345\t5351'
print(s1)
s1 = 'abc345  5351'
print(s1)

# c.\r表示回车,\f表示换页

# d.特殊字符---》普通字符
s1 = '\'hello\''
print(s1)
s1 = '"hello"'
print(s1)

s1 = 'abc345\\n5351'
print(s1)

# e。文件或文件夹路径的表示
# 错误写法
path = 'd:\Desktop\coding\Day13\notes'
print(path)

# 正确写法
path = 'd:\\Desktop\\coding\\Day13\\notes'
print(path)

# r'xxxxxx':表示字符串中的符号使用的都是原本的含义，无需依次转义，常用于路径中或者正则表达式中   ******
path = r'd:\Desktop\coding\Day13\notes'
print(path)