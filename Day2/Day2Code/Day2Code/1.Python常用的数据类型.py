
# 前期掌握数字，字符串，布尔
# 1. 数字型：整型【int】,浮点型【float】,复数【complex】
# 数字:number
n1 = 88   # int
n2 = 89.23  # float
n3 = 3 + 10j   # 数学上：3 + 10i,了解
print(n1,n2,n3)

# 2. 布尔型：bool
# 注意1：常用于表示结果只有两种的情况，如：成立或不成立，是或不是
# 注意2：只有两个值，分别是True和False,如果和数字进行数学运算，被当成1和0使用
b1 = True
b2 = False
print(b1,b2)
print(b1 + 1)   # 2
print(b2 + 1)   # 1

# 3. 字符串型：str
# 只要是文本，都可以表示成字符串，如：姓名，密码，爱好，描述等
# 注意1：字符串中可以包含数字，字母，特殊符号，中文，简单来说，只要键盘上可以敲出来的内容，都可以在字符串中表示
# 注意2：可以用单引号，也可以用双引号，甚至可以用三引号
# 注意3：在一个引号中，敲回车，仅仅是为了折行，本质还是同一行
s1 = '454' \
     'fjhgk' \
     '&^%4' \
     '计算机'
s2 = "454fjhgk&^%4计算机"
print(s1)
print(s2)
s31 = '''454
fjhgk
&^%4
计算机'''
s32 = """454
fjhgk
&^%4
计算机"""
print(s31)
print(s32)

# 后期会陆续着重讲解
# 4.列表：list
l1 = [34,6,78,9,0]
print(l1)

# 5. 元组：tuple
t1 = (34, 6, 78, 9, 0)
print(t1)

# 6. 字典：dict
# xx:xx
d1 = {'a':10,'x':99}
print(d1)
d2 = {66:'qafaq',True:19}
print(d2)

# 7. 集合：set
set1 = {'a','x',45,7,8}
print(set1)

# 8. 字节：bytes
# 在Python中，图片，音视频等都会被表示成字节【二进制】
by1 = b'hfj3fhjahf'
print(by1)
by2 = b"4562hjghnvg"
print(by2)

# 9. 空值：NoneType
# 注意1：只有一个值，是None
# 注意2：区分None和''的区别，二者不等价
n = None
print(n)
