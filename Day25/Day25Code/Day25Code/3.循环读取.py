# 1.read(n)：通过结合循环的方式，一般用于读取文件内容量较多的情况
'''
import  os
path = r'aaa/致橡树.txt'
f = open(path,'r',encoding='gbk')
# 获取文件中的总字符数
total_size = os.path.getsize(path)
# print(total_size)
# 设定一次需要读取的字符串
sub_size = 8   # 一般设置为2的次方
while total_size > 0:
    r = f.read(sub_size)
    print(r)
    total_size -= sub_size
# 关闭文件
f.close()
'''


# 2.readline():结合循环读取所有的行
path = r'aaa/致橡树.txt'
f = open(path,'r',encoding='gbk')
while True:
    r = f.readline()
    print(r)
    if not r:
        break
f.close()
