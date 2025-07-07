# 一、转换
'''
eval()：将一个字符串中的Python有效的语法识别并执行
upper():小——》大
lower():大---》小
swapcase():大---》小  小----》大
capitalize():首单词的首字母大写，其他全部小写，英文句子
title():每个单词的首字母大写，其他全部小写
ord():获取一个字符在ASCII表中的十进制数字
chr()：获取一个十进制数字在ASCII表中对应的字符
'''
# 1.eval()              ********
r11 = eval('34')
print(r11,type(r11))
r11 = eval('34,19')
print(r11,type(r11))
r11 = eval('[4,67,8,9]')  # r11 = [4,67,8,9]
print(r11,type(r11))

list1 = [2,3]
r11 = eval('list1.append(100)')  # r11 = list1.append(100)
print(r11,type(r11))  # None,NoneType
print(list1)  # [2, 3, 100]

# 练习：从控制台输入一个列表
# r11 = input("请输入一个列表:")  # 从控制台输入列表的时候，一定要按照从左往右的顺序依次输入
# print(r11,type(r11))
# r11 = eval(r11)
# print(r11)

# 2.                *********
'''
upper():小——》大
lower():大---》小
swapcase():大---》小  小----》大
capitalize():首单词的首字母大写，其他全部小写，符合英文句子的特征
title():每个单词的首字母大写，其他全部小写
'''
# 【面试题】注意：字符串是不可变的，但凡涉及到字符串更改的操作，都是生成了新的字符串   ******
# a
str2 = 'this is A TEXT'
str2.upper()
print(str2)   # this is A TEXT

str2 = 'this is A TEXT'
str2 = str2.upper()   # 将转换为大写之后生成的新的字符串重新赋值给了str2
print(str2)   # THIS IS A TEXT

str2 = 'this is A TEXT'
print(str2.upper())
print(str2.lower())
print(str2.swapcase())
print(str2.capitalize())   # This is a text
print(str2.title())  # This Is A Text

# 3.ord()和chr()
print(ord('A'))
print(chr(98))

# 练习：输入一段文本，将其中的大写字母转化为小写，小写字母转化为大写，输出新的字符串
# data = input('请输入一段文本：')
# new_data = ""
# for ch in data:
#     if 'A' <= ch <= 'Z':   # 大写字母，等价于ch >= 'A' and ch <= 'Z'
#         new_data += chr(ord(ch) + 32)
#     elif 'a' <= ch <= 'z':  # 小写字母
#         new_data += chr(ord(ch) - 32)
#     else:
#         new_data += ch
# print(new_data)

# 二、查找
'''
find():从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，如果查找不到返回-1				*******
rfind():从右往左进行检索
index()：从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，如果查找不到则直接报错		
rindex():从右往左进行检索
'''
str1 = 'abcadfeafrjgjgajha'
# a.从左往右进行检索,默认全局检索
# 1>子字符串在原字符串中存在，用法完全相同
i1 = str1.index('a')
print(i1)
i1 = str1.find('a')
print(i1)
# 2>子字符串在原字符串中不存在，find返回-1，index会直接报错
# i1 = str1.index('7')    # ValueError: substring not found
# print(i1)
i1 = str1.find('7')       # -1
print(i1)

# b.从左往右进行检索,通过设置start和end进行局部检索,返回的索引仍然是在原字符串中的索引，
# 注意：进行局部查找的过程中，要注意仍然遵循前闭后开区间
i1 = str1.index('a',3,6)  # 3~6----》adfe
print(i1)   # 3
# i1 = str1.index('a',4,7)  # 书写4~7----》dfea   实际4~6----》dfe
# print(i1)   # ValueError: substring not found

# c.从右往左进行检索,用法和find及index相同，也可以进行局部查找
i1 = str1.rindex('a')
print(i1)  # 17
i1 = str1.rfind('a')
print(i1)  # 17

# d.底层工作原理：
str1 = 'abcadfeafrjgjgajha'

# 全局查找,只查找'a'在str1中第一次出现的索引
for i in range(len(str1)):
    if str1[i] == 'a':
        print(i)
        break
else:
    print(-1)

# 局部查找
for i in range(3,6):
    if str1[i] == 'a':
        print(i)
        break
for i in range(4,7):
    if str1[i] == 'a':
        print(i)
        break
else:
    print(-1)

# 全局查找,查找'a'在str1中所有出现的索引
for i in range(len(str1)):
    if str1[i] == 'a':
        print(i)

print('*' * 50)

# 三、填充
'''
center(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居中显示			       
ljust(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居左显示，
rjust(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居右显示，
zfill(width)：原字符串居右显示，剩余的字符默认用0填充
'''
# 1.            ********
# a.fillchar省略，默认使用空格填充
str3 = 'hello'
print(str3.center(50))
print(str3.ljust(50))
print(str3.rjust(50))

# b.fillchar使用指定字符填充,注意：此时的fillchar长度只能是1
# print(str3.center(50,'***'))   # TypeError: The fill character must be exactly one character long
print(str3.center(50,'*'))
print(str3.ljust(50,'a'))
print(str3.rjust(50,'='))

# 2.
print(str3.zfill(50))  # 000000000000000000000000000000000000000000000hello

# 四、提取
'''
strip(char):去除一个指定字符串中两端指定的子字符       
lstrip(char):去除一个指定字符串中左边指定的子字符
rstrip(char):去除一个指定字符串中右边指定的子字符
'''
# 1.char被省略，默认去除字符串两端的空白字符  *****
str4 = '    fh2387fsn,ma      '
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())

# 2.char被指定，去除字符串两端的指定字符   *****
str4 = '******fh2387fsn,ma****'
print(str4.strip("*"))
print(str4.lstrip("*"))
print(str4.rstrip("*"))

# 3.char可以是多个字符，只要在字符串两端字符中包含，都可以去除,但是必须指定字符是连续的
str4 = '**aaa*a***fh2387fsn,myte**aaa*a*'
print(str4.strip("*a"))
print(str4.lstrip("*a"))
print(str4.rstrip("*a"))

str4 = '**aaab*a***fh2387fsn,myte**aaba*a*'
print(str4.strip("*a"))   # b*a***fh2387fsn,myte**aab
print(str4.lstrip("*a"))  # b*a***fh2387fsn,myte**aaba*a*
print(str4.rstrip("*a"))  # **aaab*a***fh2387fsn,myte**aab

# 练习：           *******
# username = input('请输入用户名：').strip()
# pwd = input('请输入密码：').strip()


# 五、合并和分割           ********
'''
join()：使用指定的子字符串将列表中的元素连接【列表-----》字符串】
split():使用指定的子字符串将原字符串进行分割，得到一个列表  【字符串-----》列表】
'''
# 1.join()
# 语法：'连接符'.join(iterable)
list1 = ['abc','hello','python']
print('-'.join(list1))   # abc-hello-python
print('/'.join(list1))

# 注意：列表中的元素必须为字符串
# list1 = ['abc',34,'hello',True,'python']
# print('-'.join(list1))   # TypeError: sequence序列 item 1: expected str instance, int found

# 2.连接符可以为空
print(''.join(list1))              #  ******

# 3.split(),此处的split只能处理具有某种规律的字符串，如果数据没有规律，则需要借助于正则表达式中的re.split()
# 语法：'xxxx'.split('分割符')
str5 = 'tom-bob-jerry-lisa'
print(str5.split('-'))

# 默认全部分割，也可以指定分割次数
print(str5.split('-',2))

# 六、替换
'''
replace(old,new):将原字符串中的old替换为new			
映射替换：
	maketrans():生成映射表
	translate():根据映射表将指定字符串中的指定字符替换为映射表中对应的字符
'''
# 1.replace()
str6 = 'tom-bob-jerry-lisa-jack-herry'
# a.全部替换
print(str6.replace('-','*'))

# b.控制替换的次数
print(str6.replace('-','*',3))

# 2.映射替换
# 用途：可以实现替换，也可以实现字符串的简单加密，加密规则就是table
# 第一步：生成映射表
str61 = '2385620q8239fsjkghk'
table = str.maketrans('0123456789','#$%=@!~*&-')  # 此处的str是一个模块，但是该模块的无需导入
print(table) # {48: 35, 49: 36, 50: 37, 51: 61, 52: 64, 53: 33, 54: 126, 55: 42, 56: 38, 57: 45}
# 第二步：根据映射表翻译指定字符
print(str61.translate(table))

# 注意：maketrans在产生映射表的时候，给定的两个字符串必须长度相同，否则报错ValueError: the first two maketrans arguments must have equal length

# 练习
str6 = 'tom-bob-jerry-lisa-jack-herry'
table = str.maketrans('-','*')
print(str6.translate(table))

# 七、判断
'''
isalpha():一个字符串非空并字符全部是字母才返回True    ，不推荐使用
isalnum():一个字符串非空并字符是字母或者数字才返回True   ，不推荐使用
isupper()/islower():判断是否是大写或小写
istitle():title有关
isdigit()/isdecimal():一个字符串非空并字符全部是数字才返回True   ********
startswith()；判断一个字符串是否是以指定自字符串开头【前缀】  *******
endswith():判断一个字符串是否是以指定自字符串结尾【后缀】    *****
'''
# 1.isdigit()
str71 = '4612741'
print(str71.isdigit(),str71.isdecimal())
str71 = '461.2741'
print(str71.isdigit())  # False
str71 = '-4612741'
print(str71.isdigit())  # # False

# 2.startswith()和endswith(),经常结合if语句进行判断
str72 = 'today is a nice day'
print(str72.startswith('today'))
print(str72.endswith('day'))

# 3.isupper()/islower():判断字符串中的字母是否为大写或小写,其他字符无所谓
str73 = '3ABCD546346'
print(str73.isupper())  # True
str73 = '3ABCD546rty346'
print(str73.isupper())  # False
str73 = '3fafa546346'
print(str73.islower())  # True
str73 = '3fafa54O6346'
print(str73.islower())  # False

# 4.isalpha()和isalnum():不推荐使用，底层是按照ACSCII表进行识别的，ASCII中没有中文的规则，但是，这两个功能会将中文也识别为字母
str74 = 'fhdLAMF星期六'
print(str74.isalpha())  # True
str74 = 'fhdLAMF34'
print(str74.isalpha())  # False
str74 = 'fhdLAMF34星期六'
print(str74.isalnum())  # True

# 推荐：模块string
import  string
print(string.digits)  # 等价于'0123456789'
print(string.ascii_uppercase)  # 等价于'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase) # 等价于'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_letters)  # 等价于'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 判断一个字符是否是字母
ch = 'r'
if ch in string.ascii_uppercase:
    print('大写字母')
if ch in string.ascii_lowercase:
    print('小写字母')
if ch in string.ascii_letters:
    print('字母')

# 八、编解码
'''
【面试题】简述字符串的编码和解码
编码：将字符串类型转换为字节类型，实现方式：bytes()或encode()
解码：将字节类型转换为字符串类型，实现方式：str()或decode()

字符串:''  ""  三引号
字节:b''  b""   b三引号

常用编码格式：
    utf-8
    gbk
'''
# 1.encode():编码
str8 = '347fjkha计算机编码&……%'
# a.
r1 = bytes(str8,encoding='utf-8')
print(r1)

# 2.decode()；解码
r2 = str8.encode(encoding='gbk')
print(r2)

# 2.decode():解码
# a.str()
# 注意：字符串中的编码和解码的格式一定要保持一致，否则无法操作
r3 = str(r1,encoding='utf-8')
print(r3)

# b.decode()
r4 = r2.decode(encoding='gbk')
print(r4)
