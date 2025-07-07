
# 6.注意：布尔和数字进行数学运算时，被当成0和1使用，其他情况下，正常使用
a = 100
b = False
print(a * b > -1)
print(100 * False > -1)   # True

# 3.已知x = 3 == 3,执行结束后，变量x的值为（True）。
# 注意：先计算3 == 3，结果为True,将True赋值给x
x = 3 == 3
print(x)

# 表达式 9 ** 0.5的值为（3.0）。
# 注意：但凡右浮点数参与运算符，结果都是浮点数

# 从控制台输入一个三位数，分别拆分出个位数，十位数和百位数，将拆分结果输出，格式为：百位：xx,十位：xx，个位：xx
# 方式一：算术运算符
num = int(input('请输入一个三位数：'))  # 562
gw = num % 10
sw = num // 10 % 10   # num % 100 // 10
bw = num // 100
print(f'百位：{bw},十位：{sw}，个位：{gw}')   # int

# 方式二：字符串
num = input('请输入一个三位数：')
'''
x[n]:x可以是字符串，列表或元组，n是从0开始的数字【索引】
如：
s = 'abc'
s[0] ----->'a'
s[1]----->'b'
s[2]----->'c'
'''
bw = num[0]
sw = num[1]
gw = num[2]
print(f'百位：{bw},十位：{sw}，个位：{gw}')  # str


'''
下列表达式的值为True的是（B）。
A. 3>2>2                3>2 and 2>2 ----->True and False----->False
B. 1 and 2 != 1         1 and True----->True
C. not(11and 0!=1)      11 and True---->True   not True---->False
D. 10 < 20 and 10 < 5     True and False---->False
'''