### Day12作业讲解

> ```Python
> '''
> 1.定义一个电话簿，里头设置以下联系人：
> 'mayun':'13309283335',
> 'zhaolong':'18989227822',
> 'zhangmin':'13382398921',
> 'Gorge':'19833824743',
> 'Jordan':'18807317878',
> 'Curry':'15093488129',
> 'Wade':'19282937665'
> 现在输入人名，查询他的号码，如果人名存在，则输出电话号码，如果该人不存在，返回"not found"
> '''
> '''
> # 方式一
> info_dict = {
> 'mayun':'13309283335',
> 'zhaolong':'18989227822',
> 'zhangmin':'13382398921',
> 'Gorge':'19833824743',
> 'Jordan':'18807317878',
> 'Curry':'15093488129',
> 'Wade':'19282937665'
> }
> name = input('请输入需要查询的人名：')
> # if name in info_dict.keys():  # 正确，但是没必要
> if name in info_dict:  # 简化写法
>     print(info_dict[name])
> else:
>     print('not found')
> 
> # 方式二
> info_list = [
>     {'mayun':'13309283335'},
>     {'zhaolong':'18989227822'},
>     {'zhangmin':'13382398921'},
>     {'Gorge':'19833824743'},
>     {'Jordan':'18807317878'},
>     {'Curry':'15093488129'},
>     {'Wade':'19282937665'}
> ]
> name = input('请输入需要查询的人名：')
> for dic in info_list:
>     if name in dic:
>         print(dic[name])
>         break
> else:
>     print('not found')
> '''
> 
> # 2.已知列表numlist = [23,5,56,7,78,89,12,45,6,8,89,100,99],
> # 生成一个字典，将大于66的数字保存在字典的第一个key中，将小于等于66的数字保存在字典的第二个key中
> numlist = [23,5,56,7,78,89,12,45,6,8,89,100,99]
> # 方式一
> key1 = []
> key2 = []
> for num in numlist:
>     if num > 66:
>         key1.append(num)
>     else:
>         key2.append(num)
> dict1 = {'key1':key1,'key2':key2}
> print(dict1)
> 
> # 方式二
> dict1 = {'key1':[],'key2':[]}
> for num in numlist:
>     if num > 66:
>         dict1['key1'].append(num)
>     else:
>         dict1['key2'].append(num)
> print(dict1)
> 
> # 方式二
> dict1 = {'key1':[num for num in numlist if num > 66],'key2':[num for num in numlist if num <= 66]}
> print(dict1)
> ```

### 一、字符串

> 由若干个字符组成的一个序列被称为字符串，其中的字符可以是字母，数字，符号，中文等
>
> 注意1：字符串属于不可变的数据类型，可以作为字典的key
>
> 注意2：字符串也是有序的，所以和列表，元组类似，都是通过索引访问的
>
> 注意3：字符串的切片，遍历方式和列表的使用完全相同

#### 1.定义

> ```Python
> # 1.基本定义
> # 注意：在单个引号中，按照回车进行换行，只是视觉上的折行，而数据原本还是一行
> # 字符串的组成：数字，字母，符号，中文都可以出现在字符串中，但凡是要表示成文本的数据，都用字符串表示
> # a.单引号
> str1 = '23fahj' \
>        '计算机' \
>        '&……%'
> print(str1)
> 
> # b.双引号
> str2 = "23fahj计算机&……%"
> print(str2)
> 
> # c.三引号
> str3 = '''6463
> hrwthw
> &^^%
> 中科院'''
> print(str3)
> 
> str3 = """6463
> hrwthw
> &^^%
> 中科院"""
> print(str3)
> 
> # 2.将字符串存储在容器中
> list1 = ['abc', 'gwg', '4545']
> print(list1)
> 
> list2 = ["abc", "gwg", "4545"]
> print(list2)
> 
> # 3.转义字符
> '''
> /:斜杠
> \:反斜杠
> '''
> # \xx:如果xx是一个普通字符，\xx可能具有特殊含义
> # \xx:如果xx是一个特殊字符，\xx会将特殊字符转义为普通字符
> # 上述操作并不是对所有字符都起作用
> # a.\n        *****
> # n是一个普通字符，但是\n具有特殊含义，表示换行
> s1 = 'abc345n5351'
> print(s1)
> s1 = 'abc345\n5351'
> print(s1)
> 
> # b.\t        ******
> # t是一个普通字符，但是\t具有特殊含义，表示制表符tab键
> s1 = 'abc345t5351'
> print(s1)
> s1 = 'abc345\t5351'
> print(s1)
> s1 = 'abc345  5351'
> print(s1)
> 
> # c.\r表示回车,\f表示换页
> 
> # d.特殊字符---》普通字符
> s1 = '\'hello\''
> print(s1)
> s1 = '"hello"'
> print(s1)
> 
> s1 = 'abc345\\n5351'
> print(s1)
> 
> # e。文件或文件夹路径的表示
> # 错误写法
> path = 'd:\Desktop\coding\Day13\notes'
> print(path)
> 
> # 正确写法
> path = 'd:\\Desktop\\coding\\Day13\\notes'
> print(path)
> 
> # r'xxxxxx':表示字符串中的符号使用的都是原本的含义，无需依次转义，常用于路径中或者正则表达式中   ******
> path = r'd:\Desktop\coding\Day13\notes'
> print(path)
> ```

#### 2.操作

> ```Python
> # 1.字符串是有序的,所以可以通过索引访问其中的字符
> str1 = 'abcdef'
> print(str1[0])
> print(str1[-1])
> # print(str1[7])  # IndexError: string index out of range
> 
> print(str1[1:3])
> print(str1[::-1])  # 将字符串进行反转/逆序
> 
> # 2.字符串的遍历
> # 标识符：见名知意，使用简单英文单词或者缩写表示
> # ch--->character:字符
> for ch in str1:
>     print(ch)
> 
> for i in range(len(str1)):
>     print(str1[i])
> 
> for i,ch in enumerate(str1):
>     print(i,ch)
> 
> # 3.转化
> print(list(str1))
> print(tuple(str1))
> 
> list1 = [34,6,7,8]
> print(str(list1))  # 等价于'[34, 6, 7, 8]',但是没有意义
> 
> # 4.+   *
> print(str1 + 'fagnaqg')   # 拼接
> print(str1 * 3)
> print('*' * 50)
> 
> # print(str1 + 3)  # TypeError: can only concatenate str (not "int") to str
> # print(3 + str1)   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
> 
> # 5.in 和 not in:用在字符串中，表示模糊查询，==表示精确查询
> print('a' in str1)
> print('b' not in str1)
> 
> # 6.特点：字符串是不可变的数据类型，和元组类似
> ```

#### 3.系统功能

##### 3.1转换

> eval()：将str转换为有效的表达式
>
> upper():小——》大
>
> lower():大---》小
>
> swapcase():大---》小  小----》大
>
> capitalize():首单词的首字母大写，其他全部小写，英文句子
>
> title():每个单词的首字母大写，其他全部小写
>
> ord(),chr()
>
> ```Python
> # 一、转换
> '''
> eval()：将一个字符串中的Python有效的语法识别并执行
> upper():小——》大
> lower():大---》小
> swapcase():大---》小  小----》大
> capitalize():首单词的首字母大写，其他全部小写，英文句子
> title():每个单词的首字母大写，其他全部小写
> ord():获取一个字符在ASCII表中的十进制数字
> chr()：获取一个十进制数字在ASCII表中对应的字符
> '''
> # 1.eval()              ********
> r11 = eval('34')
> print(r11,type(r11))
> r11 = eval('34,19')
> print(r11,type(r11))
> r11 = eval('[4,67,8,9]')  # r11 = [4,67,8,9]
> print(r11,type(r11))
> 
> list1 = [2,3]
> r11 = eval('list1.append(100)')  # r11 = list1.append(100)
> print(r11,type(r11))  # None,NoneType
> print(list1)  # [2, 3, 100]
> 
> # 练习：从控制台输入一个列表
> # r11 = input("请输入一个列表:")  # 从控制台输入列表的时候，一定要按照从左往右的顺序依次输入
> # print(r11,type(r11))
> # r11 = eval(r11)
> # print(r11)
> 
> # 2.                *********
> '''
> upper():小——》大
> lower():大---》小
> swapcase():大---》小  小----》大
> capitalize():首单词的首字母大写，其他全部小写，符合英文句子的特征
> title():每个单词的首字母大写，其他全部小写
> '''
> # 【面试题】注意：字符串是不可变的，但凡涉及到字符串更改的操作，都是生成了新的字符串   ******
> # a
> str2 = 'this is A TEXT'
> str2.upper()
> print(str2)   # this is A TEXT
> 
> str2 = 'this is A TEXT'
> str2 = str2.upper()   # 将转换为大写之后生成的新的字符串重新赋值给了str2
> print(str2)   # THIS IS A TEXT
> 
> str2 = 'this is A TEXT'
> print(str2.upper())
> print(str2.lower())
> print(str2.swapcase())
> print(str2.capitalize())   # This is a text
> print(str2.title())  # This Is A Text
> 
> # 3.ord()和chr()
> print(ord('A'))
> print(chr(98))
> 
> # 练习：输入一段文本，将其中的大写字母转化为小写，小写字母转化为大写，输出新的字符串
> # data = input('请输入一段文本：')
> # new_data = ""
> # for ch in data:
> #     if 'A' <= ch <= 'Z':   # 大写字母，等价于ch >= 'A' and ch <= 'Z'
> #         new_data += chr(ord(ch) + 32)
> #     elif 'a' <= ch <= 'z':  # 小写字母
> #         new_data += chr(ord(ch) - 32)
> #     else:
> #         new_data += ch
> # print(new_data)
> ```

##### 3.2查找

> find():从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，如果查找不到返回-1				******
>
> rfind():从右往左进行检索
>
> index()：从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，如果查找不到则直接报错		****
>
> rindex():从右往左进行检索
>
> ```Python
> # 二、查找
> '''
> find():从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，如果查找不到返回-1				*******
> rfind():从右往左进行检索
> index()：从左往右进行检索，返回被查找的子字符串在原字符串中第一次出现的位置，如果查找不到则直接报错		
> rindex():从右往左进行检索
> '''
> str1 = 'abcadfeafrjgjgajha'
> # a.从左往右进行检索,默认全局检索
> # 1>子字符串在原字符串中存在，用法完全相同
> i1 = str1.index('a')
> print(i1)
> i1 = str1.find('a')
> print(i1)
> # 2>子字符串在原字符串中不存在，find返回-1，index会直接报错
> # i1 = str1.index('7')    # ValueError: substring not found
> # print(i1)
> i1 = str1.find('7')       # -1
> print(i1)
> 
> # b.从左往右进行检索,通过设置start和end进行局部检索,返回的索引仍然是在原字符串中的索引，
> # 注意：进行局部查找的过程中，要注意仍然遵循前闭后开区间
> i1 = str1.index('a',3,6)  # 3~6----》adfe
> print(i1)   # 3
> # i1 = str1.index('a',4,7)  # 书写4~7----》dfea   实际4~6----》dfe
> # print(i1)   # ValueError: substring not found
> 
> # c.从右往左进行检索,用法和find及index相同，也可以进行局部查找
> i1 = str1.rindex('a')
> print(i1)  # 17
> i1 = str1.rfind('a')
> print(i1)  # 17
> 
> # d.底层工作原理：
> str1 = 'abcadfeafrjgjgajha'
> 
> # 全局查找,只查找'a'在str1中第一次出现的索引
> for i in range(len(str1)):
>     if str1[i] == 'a':
>         print(i)
>         break
> else:
>     print(-1)
> 
> # 局部查找
> for i in range(3,6):
>     if str1[i] == 'a':
>         print(i)
>         break
> for i in range(4,7):
>     if str1[i] == 'a':
>         print(i)
>         break
> else:
>     print(-1)
> 
> # 全局查找,查找'a'在str1中所有出现的索引
> for i in range(len(str1)):
>     if str1[i] == 'a':
>         print(i)
> ```

##### 3.3填充

> center(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居中显示			****       
>
> ljust(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居左显示，
>
> rjust(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居右显示，
>
> zfill(width)：原字符串居右显示，剩余的字符默认用0填充
>
> ```Python
> # 三、填充
> '''
> center(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居中显示			       
> ljust(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居左显示，
> rjust(width[,fillchar]):用fillchar填充指定的字符串，填充之后的长度为width,原字符串居右显示，
> zfill(width)：原字符串居右显示，剩余的字符默认用0填充
> '''
> # 1.            ********
> # a.fillchar省略，默认使用空格填充
> str3 = 'hello'
> print(str3.center(50))
> print(str3.ljust(50))
> print(str3.rjust(50))
> 
> # b.fillchar使用指定字符填充,注意：此时的fillchar长度只能是1
> # print(str3.center(50,'***'))   # TypeError: The fill character must be exactly one character long
> print(str3.center(50,'*'))
> print(str3.ljust(50,'a'))
> print(str3.rjust(50,'='))
> 
> # 2.
> print(str3.zfill(50))  # 000000000000000000000000000000000000000000000hello
> ```

##### 3.4提取

> strip():去除一个指定字符串中两端指定的子字符       ****
>
> lstrip():去除一个指定字符串中左边指定的子字符
>
> rstrip():去除一个指定字符串中右边指定的子字符
>
> ```Python
> # 四、提取
> '''
> strip(char):去除一个指定字符串中两端指定的子字符       
> lstrip(char):去除一个指定字符串中左边指定的子字符
> rstrip(char):去除一个指定字符串中右边指定的子字符
> '''
> # 1.char被省略，默认去除字符串两端的空白字符  *****
> str4 = '    fh2387fsn,ma      '
> print(str4.strip())
> print(str4.lstrip())
> print(str4.rstrip())
> 
> # 2.char被指定，去除字符串两端的指定字符   *****
> str4 = '******fh2387fsn,ma****'
> print(str4.strip("*"))
> print(str4.lstrip("*"))
> print(str4.rstrip("*"))
> 
> # 3.char可以是多个字符，只要在字符串两端字符中包含，都可以去除,但是必须指定字符是连续的
> str4 = '**aaa*a***fh2387fsn,myte**aaa*a*'
> print(str4.strip("*a"))
> print(str4.lstrip("*a"))
> print(str4.rstrip("*a"))
> 
> str4 = '**aaab*a***fh2387fsn,myte**aaba*a*'
> print(str4.strip("*a"))   # b*a***fh2387fsn,myte**aab
> print(str4.lstrip("*a"))  # b*a***fh2387fsn,myte**aaba*a*
> print(str4.rstrip("*a"))  # **aaab*a***fh2387fsn,myte**aab
> 
> # 练习：           *******
> # username = input('请输入用户名：').strip()
> # pwd = input('请输入密码：').strip()
> 
> ```

##### 3.5合并和分割

> join()：使用指定的子字符串将列表中的元素连接【列表-----》字符串】		****
>
> split():使用指定的子字符串将原字符串进行分割，得到一个列表  【字符串-----》列表】****
>
> ```Python
> # 五、合并和分割           ********
> '''
> join()：使用指定的子字符串将列表中的元素连接【列表-----》字符串】
> split():使用指定的子字符串将原字符串进行分割，得到一个列表  【字符串-----》列表】
> '''
> # 1.join()
> # 语法：'连接符'.join(iterable)
> list1 = ['abc','hello','python']
> print('-'.join(list1))   # abc-hello-python
> print('/'.join(list1))
> 
> # 注意：列表中的元素必须为字符串
> # list1 = ['abc',34,'hello',True,'python']
> # print('-'.join(list1))   # TypeError: sequence序列 item 1: expected str instance, int found
> 
> # 2.连接符可以为空
> print(''.join(list1))              #  ******
> 
> # 3.split(),此处的split只能处理具有某种规律的字符串，如果数据没有规律，则需要借助于正则表达式中的re.split()
> # 语法：'xxxx'.split('分割符')
> str5 = 'tom-bob-jerry-lisa'
> print(str5.split('-'))
> 
> # 默认全部分割，也可以指定分割次数
> print(str5.split('-',2))
> ```

##### 3.6替换

> replace(old,new):将原字符串中的old替换为new			****
>
> 映射替换：
>
> ​	maketrans():生成映射表
>
> ​	translate():根据映射表将指定字符串中的指定字符替换为映射表中对应的字符
>
> ```Python
> # 六、替换
> '''
> replace(old,new):将原字符串中的old替换为new			
> 映射替换：
> 	maketrans():生成映射表
> 	translate():根据映射表将指定字符串中的指定字符替换为映射表中对应的字符
> '''
> # 1.replace()
> str6 = 'tom-bob-jerry-lisa-jack-herry'
> # a.全部替换
> print(str6.replace('-','*'))
> 
> # b.控制替换的次数
> print(str6.replace('-','*',3))
> 
> # 2.映射替换
> # 用途：可以实现替换，也可以实现字符串的简单加密，加密规则就是table
> # 第一步：生成映射表
> str61 = '2385620q8239fsjkghk'
> table = str.maketrans('0123456789','#$%=@!~*&-')  # 此处的str是一个模块，但是该模块的无需导入
> print(table) # {48: 35, 49: 36, 50: 37, 51: 61, 52: 64, 53: 33, 54: 126, 55: 42, 56: 38, 57: 45}
> # 第二步：根据映射表翻译指定字符
> print(str61.translate(table))
> 
> # 注意：maketrans在产生映射表的时候，给定的两个字符串必须长度相同，否则报错ValueError: the first two maketrans arguments must have equal length
> 
> # 练习
> str6 = 'tom-bob-jerry-lisa-jack-herry'
> table = str.maketrans('-','*')
> print(str6.translate(table))
> ```

##### 3.7判断

> isalpha():一个字符串非空并字符全部是字母才返回True    ，不推荐使用
>
> isalnum():一个字符串非空并字符是字母或者数字才返回True   ，不推荐使用
>
> isupper()/islower()/istitle():和upper，lower,title有关
>
> isdigit()/isdecimal():一个字符串非空并字符全部是数字才返回True   ***
>
> startswith()；判断一个字符串是否是以指定自字符串开头【前缀】  ***
>
> endswith():判断一个字符串是否是以指定自字符串结尾【后缀】  ****
>
> ```Python
> # 七、判断
> '''
> isalpha():一个字符串非空并字符全部是字母才返回True    ，不推荐使用
> isalnum():一个字符串非空并字符是字母或者数字才返回True   ，不推荐使用
> isupper()/islower():判断是否是大写或小写
> istitle():title有关
> isdigit()/isdecimal():一个字符串非空并字符全部是数字才返回True   ********
> startswith()；判断一个字符串是否是以指定自字符串开头【前缀】  *******
> endswith():判断一个字符串是否是以指定自字符串结尾【后缀】    *****
> '''
> # 1.isdigit()
> str71 = '4612741'
> print(str71.isdigit(),str71.isdecimal())
> str71 = '461.2741'
> print(str71.isdigit())  # False
> str71 = '-4612741'
> print(str71.isdigit())  # # False
> 
> # 2.startswith()和endswith(),经常结合if语句进行判断
> str72 = 'today is a nice day'
> print(str72.startswith('today'))
> print(str72.endswith('day'))
> 
> # 3.isupper()/islower():判断字符串中的字母是否为大写或小写,其他字符无所谓
> str73 = '3ABCD546346'
> print(str73.isupper())  # True
> str73 = '3ABCD546rty346'
> print(str73.isupper())  # False
> str73 = '3fafa546346'
> print(str73.islower())  # True
> str73 = '3fafa54O6346'
> print(str73.islower())  # False
> 
> # 4.isalpha()和isalnum():不推荐使用，底层是按照ACSCII表进行识别的，ASCII中没有中文的规则，但是，这两个功能会将中文也识别为字母
> str74 = 'fhdLAMF星期六'
> print(str74.isalpha())  # True
> str74 = 'fhdLAMF34'
> print(str74.isalpha())  # False
> str74 = 'fhdLAMF34星期六'
> print(str74.isalnum())  # True
> 
> # 推荐：模块string
> import  string
> print(string.digits)  # 等价于'0123456789'
> print(string.ascii_uppercase)  # 等价于'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
> print(string.ascii_lowercase) # 等价于'abcdefghijklmnopqrstuvwxyz'
> print(string.ascii_letters)  # 等价于'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
> # 判断一个字符是否是字母
> ch = 'r'
> if ch in string.ascii_uppercase:
>     print('大写字母')
> if ch in string.ascii_lowercase:
>     print('小写字母')
> if ch in string.ascii_letters:
>     print('字母')
> ```

##### 3.8编码和解码

> encode():编码
>
> decode()；解码
>
> ```Python
> # 八、编解码
> '''
> 【面试题】简述字符串的编码和解码
> 编码：将字符串类型转换为字节类型，实现方式：bytes()或encode()
> 解码：将字节类型转换为字符串类型，实现方式：str()或decode()
> 
> 字符串:''  ""  三引号
> 字节:b''  b""   b三引号
> 
> 常用编码格式：
>     utf-8
>     gbk
> '''
> # 1.encode():编码
> str8 = '347fjkha计算机编码&……%'
> # a.
> r1 = bytes(str8,encoding='utf-8')
> print(r1)
> 
> # 2.decode()；解码
> r2 = str8.encode(encoding='gbk')
> print(r2)
> 
> # 2.decode():解码
> # a.str()
> # 注意：字符串中的编码和解码的格式一定要保持一致，否则无法操作
> r3 = str(r1,encoding='utf-8')
> print(r3)
> 
> # b.decode()
> r4 = r2.decode(encoding='gbk')
> print(r4)
> ```

### 二、练习

> ```Python
> 1.写代码，有如下变量，请按照要求实现每个功能
> name = "gouguoQ "
> 
> a.移除name变量对应值的两边的空格，并输出移除后的内容
> b.判断name变量对应的值是否以"go"开头，并输出结果
> c.判断name变量对应的值是否以"Q"结尾，并输出结果
> d.将name变量对应的值中的"o"，替换为"p"，并输出结果
> e.将name变量对应的值根据"o"分割，并输出结果
> g.将name变量对应的值变大写，并输出结果
> h.将name变量对应的值变成小写，并输出结果
> i.请输出name变量对应的值的第二个字符
> j.请输出name变量对应的值的前三个字符
> k.请输出name变量对应值的后2个字符
> l.请输出name变量中的值"Q的索引的位置
> m.获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
> n.利用下划线将列表li = ['gou', 'guo', 'qi']的每一个元素拼接成字符串gou_guo_qi
> 
> 
> 2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
> a.请将a字符串的大写改为小写，小写改为大写
> b.请将a字符串的数字取出，并输出成一个新的字符串
> c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
> d.输出a字符串出现频率最高的字母
> e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False
> 
> 3.统计用户输入的内容中有几个数字，几个字母？
> 
> 4.编写敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符，如山寨 水货，则将内容替换为*****
> 
> 5.生成指定长度的验证码，该验证码可以由数字或字母组成
> ```

> ```Python
> # 1.写代码，有如下变量，请按照要求实现每个功能
> name = "gouguoQ "
> 
> # a.移除name变量对应值的两边的空格，并输出移除后的内容
> a1 = name.strip()
> print(a1)
> a2 = name.rstrip()
> print(a2)
> 
> # b.判断name变量对应的值是否以"go"开头，并输出结果
> print(name.startswith('go'))
> 
> # c.判断name变量对应的值是否以"Q"结尾，并输出结果
> print(name.endswith('Q'))
> 
> # d.将name变量对应的值中的"o"，替换为"p"，并输出结果
> d1 = name.replace('o','p')
> print(d1)
> 
> t = str.maketrans('o','p')
> d2 = name.translate(t)
> print(d2)
> 
> # e.将name变量对应的值根据"o"分割，并输出结果
> e1 = name.split('o')
> print(e1)
> 
> # g.将name变量对应的值变大写，并输出结果
> print(name.upper())
> 
> # h.将name变量对应的值变成小写，并输出结果
> print(name.lower())
> 
> # i.请输出name变量对应的值的第二个字符
> print(name[1])
> 
> # j.请输出name变量对应的值的前三个字符
> print(name[:3])
> 
> # k.请输出name变量对应值的后2个字符
> print(name[len(name) - 2:])
> # print(name[-1:-3:-1])
> print(name[-2::1])
> 
> # l.请输出name变量中的值"Q的索引的位置
> print(name.index('Q'))
> print(name.find('Q'))
> 
> # m.获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
> print(name[:-1])
> s = 'woaini'
> print(s[:-1])
> 
> # n.利用下划线将列表li = ['gou', 'guo', 'qi']的每一个元素拼接成字符串gou_guo_qi
> li = ['gou', 'guo', 'qi']
> print('_'.join(li))
> 
> # 2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
> a = "aAsmr3idd4bgs7Dlsf9eAF"
> # a.请将a字符串的大写改为小写，小写改为大写
> print(a.swapcase())
> # b.请将a字符串的数字取出，并输出成一个新的字符串
> # 方式一
> new_a = ''
> for ch in a:
>     if ch.isdigit():
>         new_a += ch
> print(new_a)
> 
> # 方式二
> new_list = []
> for ch in a:
>     if ch.isdigit():
>         new_list.append(ch)
> new_a = ''.join(new_list)
> print(new_a)
> 
> # 简化
> new_a = ''.join([ch for ch in a if ch.isdigit()])
> print(new_a)
> 
> # c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
> c = a.lower()
> ch_dict = {}
> for ch in c:
>     ch_dict[ch] = c.count(ch)    # 注意：如果要统计一个字符在字符串中出现的次数，和列表的用法完全相同
> print(ch_dict)
> 
> # d.输出a字符串出现频率最高的字母
> ch_dict = {}
> for ch in a:
>     ch_dict[ch] = a.count(ch)
> print(ch_dict)
> count_max = max(ch_dict.values())
> ch_list = []
> for ch,count in ch_dict.items():
>     if count == count_max:
>         ch_list.append(ch)
> print(f'a字符串出现频率最高的字母:{ch_list},次数为:{count_max}')
> 
> # e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False
> a = "aAsmro3iydd4gbs7Dlsf9eAF"
> substr = 'boy'
> # 方式一
> count = 0
> for ch in substr:
>     if ch in a:
>         count += 1
> if count == len(substr):
>     print(True)
> else:
>     print(False)
> 
> # 方式二
> for ch in substr:
>     if ch not in a:
>         print(False)
>         break
> else:
>     print(True)
> 
> # 方式三：set()
> set1 = set(a)  # 将字符串转化为集合
> set1.update(substr)  # 将子字符串中的字符更新到集合中
> if len(set1) == len(set(a)):
>     print(True)
> else:
>     print(False)
> 
> # 3.统计用户输入的内容中有几个数字，几个字母,几个其他字符？
> # import string
> # data = input('请输入一段文本：')
> # letters_count = 0
> # digits_count = 0
> # other_count = 0
> # for ch in data:
> #     if ch.isdigit():
> #         digits_count += 1
> #     elif ch in string.ascii_letters:
> #         letters_count += 1
> #     else:
> #         other_count += 1
> # print(f'输入的内容中有{digits_count}个数字，{letters_count}个字母,{other_count}个其他字符')
> 
> # 4.编写敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符，如山寨 水货，则将内容替换为*****
> # words_list = ['山寨','水货','钱','法轮功','枪']
> # data = input('请输入一段文本：')
> # for word in words_list:
> #     if data.find(word) != -1:        # word in words_list
> #         data = data.replace(word,'*' * len(word))
> # print(data)
> 
> # 5.生成指定长度的验证码，该验证码可以由数字或字母组成
> import  random
> import  string
> n = int(input('请输入验证码的长度：'))
> 
> # 方式一
> code = ""
> for _ in range(n):
>     code += random.choice(string.ascii_letters + string.digits)
> print(code)
> 
> # 方式二
> code = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])
> print(code)
> 
> # 方式三：不会重复。不符合实际情况
> code = ''.join(random.sample(string.ascii_letters + string.digits,n))
> print(code)
> ```
>
> 
>

