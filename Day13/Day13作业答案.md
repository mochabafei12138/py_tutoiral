### 必做题

1.输入一个字符串，判断字符串中有多少个字母？多少个数字？多少个其他符号

```
例如:'hello, nice to meet you. i am 18. my birthday is 1999-05-23'
		-- 结果: 字母的个数为33个，数字个数为10个， 其他字符为16个
```

```python
'''
isalpha():一个字符串非空并字符全部是字母才返回True
isalnum():一个字符串非空并字符是字母或者数字才返回True

一般情况下，不建议上述功能，
原因：底层只能针对ASCII码表进行判断，所以中文也会被统计为字母
'''
# 不严谨的写法
# data = input('请输入一段内容：')
# letters_count = 0
# digits_count = 0
# other_count = 0
# for ch in data:
#     if ch.isdigit():
#         digits_count += 1
#     elif ch.isalpha():
#         letters_count += 1
#     else:
#         other_count += 1
# print(f"字符串中有{letters_count}个字母,{digits_count}个数字,{other_count}个其他符号")

# 严谨书写
# import string
# data = input('请输入一段内容：')
# letters_count = 0
# digits_count = 0
# other_count = 0
# for ch in data:
#     if ch.isdigit():
#         digits_count += 1
#     # 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'
#     elif ch in string.ascii_letters:
#         letters_count += 1
#     else:
#         other_count += 1
# print(f"字符串中有{letters_count}个字母,{digits_count}个数字,{other_count}个其他符号")
```

2.以下是一段歌词，请从这段歌词中统计出朋友出现的次数。

```
“这些年一个人，风也过，雨也走，有过泪，有过错, 还记得坚持甚么，真爱过才会懂，会寂寞会回首，终有梦终有你在心中。朋友一生一起走，那些日子不再有，一句话，一辈子，一生情，一杯酒。朋友不曾孤单过，一声朋友你会懂，还有伤，还有痛，还要走，还有我。”
```

```python
str1 = "这些年一个人，风也过，雨也走，有过泪，有过错, 还记得坚持甚么，真爱过才会懂，会寂寞会回首，终有梦终有你在心中。朋友一生一起走，那些日子不再有，一句话，一辈子，一生情，一杯酒。朋友不曾孤单过，一声朋友你会懂，还有伤，还有痛，还要走，还有我。"
c = str1.count("朋友")
```

3.编写敏感词过滤程序
说明：在网络程序中，如聊天室、聊天软件等，经常需要对一些用户所提交的聊天内容中的敏感性词语进行过滤。如“性”、“色情”、“爆炸”、“恐怖”、“枪”、“军火”等，这些都不可以在网上进行传播，要求输入一段文本，如果包含以上的敏感词汇，需要*替换掉

```
例如：“军火走私” ---- 结果为 "**走私"
```

```python
data = input("请输入")
words = ['性'、'色情'、'爆炸'、'恐怖'、'枪'、'军火']

for word in words:
    print(data)
    if data.find(word) != -1:
        # 替换
        data = data.replace(word,"*" * len(word))
print(data)
```

4.输入一个用户名，判断用户名是否合法。用户名要求：由英文字母或数字组成，长度是6到12位

```
例如：‘abcd’ --- 不合法  "123456" -- 合法 ‘ABC23’ -- 不合法   ‘ABC123’ -- 合法
“abc 124” --- 不合法
```

```python
# username = input("请输入你的用户名：")  # hel=lo1234
# if 6 <= len(username) <= 12:
# if len(username) >= 6 and len(username) <= 12:
# if len(username) in range(6,13):
#     for ch in username:
#         if ch not in string.ascii_letters + string.digits:
#             print(f"{username}不合法")
#             break
#     else:
#         print(f"{username}合法")
# else:
#     print(f"{username}不合法")
```

5.随机生成长度为5的验证码， 验证码的组成是英文字母或者数字

```python
# 方式一
data =  string.ascii_letters + string.digits
code = ""
for _ in range(5):
    code += data[random.choice(range(len(data)))]
print(code)

# 方式二
data =  string.ascii_letters + string.digits
code_list = random.sample(data,5)
code = "".join(code_list)
print(code)

# 方式三
code = "".join([random.choice(data) for _ in range(5)])
print(code)
```

6.实现将字符串  "1,2,3"   变成列表 ["1","2","3"]

```python
str1 = "1,2,3" 
list1 = str1.split(",")
```

7.判断输入的字符串是否是 .py 结束

```python
data = input("请输入字符串：")
result = data.endswith(".py")
```

### 选做题

1.输入一个字符串，将字符串中所有的数字符取出来产生一个新的字符串 

```
例如： 输入: 'abc1shj23kls99+2kkk'   输出： '123992'
```

```python
new_str = input("请输入一段文本：")
new_str = ""
for ch in a:
    if ch.isdigit():
        new_str += ch
print(new_str)
```

2.输入用户名，判断用户名是否合法，用户名的要求：必须由数字**和**字母且只能有数字和字母，并且第一个字符是大写字母

```
例如：  'Abc'  — 不合法    '123'  — 不合法   'abc123'  — 不合法    'Abc123ahs' — 合法
```

```python
username = input("请输入你的用户名：")  # hel=lo1234
# 方式一
# if username[0] in string.ascii_uppercase:
# if username[0].isupper() and not username.isdigit() and not username.isalpha() and username.isalnum() :
#     print(f"{username}合法")
# else:
#     print(f"{username}不合法")

# 方式二
letters_count = 0
digits_count = 0
if username[0].isupper():
    for ch in username:
        if ch in string.ascii_letters:
            letters_count += 1
        elif ch in string.digits:
            digits_count += 1
    if digits_count == 0 or letters_count + digits_count != len(username):
        print(f"{username}不合法")
    else:
        print(f"{username}合法")
else:
    print(f"{username}不合法")
```

3.输入两个字符串，打印两个字符串中公共的字符，如果没有公共字符打印 **公共字符不存在**

```
例如： 字符串1为 abc123a , 字符串2为  huak33 , 打印 a3
```

```python
str1 = input("请输入第一段文本：")
str2 = input("请输入第二段文本：")
equal_list = [] 
for ch in str1:
    if ch in str2 and ch not in equal_list:
        equal_list.append(ch)
equal_str = "".join(equal_list)  
print(equal_str)
```

4.如下字符串:  "01#张三#60-02#李四#90-03#王五#70", 每一部分表示  学号#姓名#分数，提取学生信息存放于列表中

```
结果显示为:
[{"学号":'02', '姓名':'李四', '分数':90}, {"学号":'03', '姓名':'王五', '分数':70}, {"学号":'01', '姓名':'张三', '分数':60}]
```

```python
data = "01#张三#60-02#李四#90-03#王五#70"
stu_list = []  # [{},{}....]
for info in data.split("-"):     # 01#张三#60-02#李四#90-03#王五#70--->['01#张三#60','02#李四#90','03#王五#70']
    sublist = info.split("#")    # 01#张三#60 ---->['01','张三','60']
    stu_list.append(dict(zip(["学号","姓名","分数"],sublist)))
```

