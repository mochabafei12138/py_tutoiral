'''
合法的qq号：
	a.全部是数字
	b.位数5~11位
	c.开头不能为0
'''
# 方式一
def check_qq1(qq:str):
    result = True
    if qq.isdigit():
        if len(qq) in range(5,12):
            if qq[0] == '0':
                result = False
        else:
            result = False
    else:
        result  = False
    return result

# 方式二
def check_qq2(qq):
    if (qq.isdigit()) and (len(qq) in range(5,12)) and (qq[0] != '0'):
        return True
    return False

# 方式三
import re
def check_qq3(qq):
    # 如果匹配上了则返回Match object，如果匹配不上则返回None
    # r = re.match(r'[1-9][0-9]{4,10}$',qq)
    r = re.match(r'[1-9]\d{4,10}$', qq)
    return True if r else False

if __name__ == '__main__':
    qq = '2557746765226272727'
    print(check_qq3(qq))