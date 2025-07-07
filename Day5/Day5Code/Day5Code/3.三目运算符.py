# 语法：r = a if 条件  else  b
# 工作原理：如果条件成立，则r的结果是a,如果条件不成立，则r的结果是b

# 1.
num = int(input('请输入一个数：'))
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')

r = ''
if num % 2 == 0:
    r = '偶数'
else:
    r = '奇数'
print(r)

r = '偶数' if num % 2 == 0 else '奇数'
print(r)
r = True if num % 2 == 0 else False
print(r)

# 2.
year = int(input('请输入一个年份：'))
if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f'{year}是平年')

r1 = '闰年' if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0) else '平年'
print(r1)
r1 = True if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0) else False
print(r1)