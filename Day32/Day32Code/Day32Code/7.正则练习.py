import re
"""
1.用户名匹配
			要求:	1.用户名只能包含数字 字母 下划线
					2.不能以数字开头
					3.⻓度在 6 到 16 位范围内
"""
def check_username(username):
    r = re.match(r'[a-zA-Z_]\w{5,15}$',username)
    return True if r else False

print(check_username('hf_faj'))

"""
2.密码匹配 

			要求:	1.不能包含!@#¥%^&*这些特殊符号
					2.必须以字母开头 
					3.⻓度在 6 到 12 位范围内
"""
def check_pwd(pwd):
    r = re.match(r'[a-zA-Z][^!@#¥%^&*]{5,11}$',pwd)
    return True if r else False

print(check_pwd('545be4btj'))

# 3.将给定字符串中的数字挑出，拼接成一个新的字符串
def get_num(data):
    # 方式一
    # r = re.findall(r'\d+',data)
    # return  ''.join(r)

    # 方式二
    r = re.split(r'\D+',data)
    return ''.join(r)

print(get_num('46fah490%43gg'))

# 4.将给定字符串中的数字挑出，求和
def get_sum(data):
    # 方式一
    # r = re.findall(r'\d+',data)
    # total = sum([int(ele) for ele in r])
    # return total

    # 方式二
    r = re.split(r'\D+', data)
    total = sum([int(ele) for ele in r if ele != ''])
    return total

print(get_sum('46fah490%43gg'))