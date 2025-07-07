# 2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
a = "aAsmr3idd4bgs7Dlsf9eAF"
# a.请将a字符串的大写改为小写，小写改为大写
print(a.swapcase())
# b.请将a字符串的数字取出，并输出成一个新的字符串
# 方式一
new_a = ''
for ch in a:
    if ch.isdigit():
        new_a += ch
print(new_a)

# 方式二
new_list = []
for ch in a:
    if ch.isdigit():
        new_list.append(ch)
new_a = ''.join(new_list)
print(new_a)

# 简化
new_a = ''.join([ch for ch in a if ch.isdigit()])
print(new_a)

# c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
c = a.lower()
ch_dict = {}
for ch in c:
    ch_dict[ch] = c.count(ch)    # 注意：如果要统计一个字符在字符串中出现的次数，和列表的用法完全相同
print(ch_dict)

# d.输出a字符串出现频率最高的字母
ch_dict = {}
for ch in a:
    ch_dict[ch] = a.count(ch)
print(ch_dict)
count_max = max(ch_dict.values())
ch_list = []
for ch,count in ch_dict.items():
    if count == count_max:
        ch_list.append(ch)
print(f'a字符串出现频率最高的字母:{ch_list},次数为:{count_max}')

# e.请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输出False
a = "aAsmro3iydd4gbs7Dlsf9eAF"
substr = 'boy'
# 方式一
count = 0
for ch in substr:
    if ch in a:
        count += 1
if count == len(substr):
    print(True)
else:
    print(False)

# 方式二
for ch in substr:
    if ch not in a:
        print(False)
        break
else:
    print(True)

# 方式三：set()
set1 = set(a)  # 将字符串转化为集合
set1.update(substr)  # 将子字符串中的字符更新到集合中
if len(set1) == len(set(a)):
    print(True)
else:
    print(False)

# 3.统计用户输入的内容中有几个数字，几个字母,几个其他字符？
# import string
# data = input('请输入一段文本：')
# letters_count = 0
# digits_count = 0
# other_count = 0
# for ch in data:
#     if ch.isdigit():
#         digits_count += 1
#     elif ch in string.ascii_letters:
#         letters_count += 1
#     else:
#         other_count += 1
# print(f'输入的内容中有{digits_count}个数字，{letters_count}个字母,{other_count}个其他字符')

# 4.编写敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符，如山寨 水货，则将内容替换为*****
# words_list = ['山寨','水货','钱','法轮功','枪']
# data = input('请输入一段文本：')
# for word in words_list:
#     if data.find(word) != -1:        # word in words_list
#         data = data.replace(word,'*' * len(word))
# print(data)

# 5.生成指定长度的验证码，该验证码可以由数字或字母组成
import  random
import  string
n = int(input('请输入验证码的长度：'))

# 方式一
code = ""
for _ in range(n):
    code += random.choice(string.ascii_letters + string.digits)
print(code)

# 方式二
code = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])
print(code)

# 方式三：不会重复。不符合实际情况
code = ''.join(random.sample(string.ascii_letters + string.digits,n))
print(code)

