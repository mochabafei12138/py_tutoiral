# 6.实现将字符串  "1,2,3"   变成列表 ["1","2","3"]
s = '1,2,3'
r = s.split(',')    # 分割字符串，返回一个列表
print(r)

# 2.输入用户名，判断用户名是否合法，用户名的要求：必须由数字和字母且只能有数字和字母，并且第一个字符是大写字母
# 例如：  'Abc'  — 不合法    '123'  — 不合法   'abc123'  — 不合法    'Abc123ahs' — 合法
# import  string
# username = input('请输入用户名：')
# letters_count = 0
# digits_count = 0
# if username[0] in string.ascii_uppercase:   # username[0].isupper()
#     for ch in username:
#         if ch in string.ascii_letters:
#             letters_count += 1
#         elif ch in string.digits:  # ch.isdigit()
#             digits_count += 1
#     if digits_count == 0 or letters_count + digits_count != len(username):
#         print(f'{username}不合法')
#     else:
#         print(f'{username}合法')
# else:
#     print(f'{username}不合法')

# 4.如下字符串:  "01#张三#60-02#李四#90-03#王五#70", 每一部分表示  学号#姓名#分数，提取学生信息存放于列表中，列表形式如下：
# 结果显示为:
# [{"学号":'02', '姓名':'李四', '分数':90}, {"学号":'03', '姓名':'王五', '分数':70}, {"学号":'01', '姓名':'张三', '分数':60}]
data = "01#张三#60-02#李四#90-03#王五#70"
# 方式一
data_list = []
stu_list = data.split('-')
for stu in stu_list:
    info_list = stu.split('#')
    data_list.append(dict(zip(['学号','姓名','成绩'],info_list)))
print(data_list)

# 方式二
data_list = []
stu_list = data.split('-')
for stu in stu_list:
    dic = {}   # 将dic定义在循环中，是为了每次循环进来，创建一个新的字典
    info_list = stu.split('#')
    dic['学号'] = info_list[0]
    dic['姓名'] = info_list[1]
    dic['成绩'] = info_list[2]
    data_list.append(dic)
print(data_list)