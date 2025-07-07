'''
x?       匹配0个或者1个x
x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
x+       匹配1个 或者 多个
x{n}     匹配确定的n个x（n是一个非负整数）
x{n,}    匹配至少n个x
x{n,m}   匹配至少n个最多m个x。注意：n <= m
'''
import re

'''
x{n}     匹配确定的n个x（n是一个非负整数）
x{n,}    匹配至少n个x
x{n,m}   匹配至少n个最多m个x。注意：n <= m
'''
# a
r = re.match(r'\d{3}','12345678650493827')
print(r)
r = re.match(r'\d{3,}','12345678650493827')
print(r)
r = re.match(r'\d{3,6}','12345678650493827')
print(r)

# 练习：匹配一个由4位的验证码，每一位可以由数字或字母组成
r = re.match(r'[0-9a-zA-Z]{4}','45f7')
print(r)

# 注意：如果match或search能匹配上，返回Match object，则可以访问group()获取匹配到的子字符串,如果返回None，则无法访问group()
print(r.group())

# b.
r = re.search(r'\d{3}','a12345678650493827')
print(r)
r = re.search(r'\d{3,}','a12345678650493827')
print(r)
r = re.search(r'\d{3,6}','a12345678650493827')
print(r)

# c.
r = re.findall(r'\d{3}','a12345678650493827')
print(r)
r = re.findall(r'\d{3,}','a12345678650493827')
print(r)
r = re.findall(r'\d{3,6}','a123456786504938')
print(r)

# d.
r = re.findall(r'\d?','a123456786c50493827')
print(r)
r = re.findall(r'\d+','a123456786c50493827')
print(r)
r = re.findall(r'\d*','a123456786c504938')
print(r)
