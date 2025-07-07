'''
open(file)
    file：需要打开的文件路径

文件路径：可以使用相对路径或绝对路径，但是推荐相对路径
    绝对路径：从盘符开始的路径， 如：d:\Desktop\coding\Code\Day25Code\aaa\f1.txt
    相对路径：相对于当前工程和当前py文件，如：aaa/f1.txt
'''
# 1.绝对路径
# 注意1：因为路径中有特殊字符，为了保留字符原本的含义，建议使用r'xxx'表示路径的字符串
# 错误写法
# path1 = 'd:\Desktop\coding\Code\Day25Code\aaa\f1.txt'
# print(path1)   # d:\Desktop\coding\Code\Day25Code1.txt
# 正确写法
path1 = r'd:\Desktop\coding\Code\Day25Code\a\f1.txt'
print(path1)

# 2.相对路径
# 情况一：如果当前py文件和txt文件平级，则可以直接书写txt文件名称
# f1 = open(r't2.txt')  # FileNotFoundError: [Errno 2] No such file or directory: 't2.txt'
f1 = open(r't1.txt')

# 情况二：如果当前py文件和txt文件的上级目录平级，则需要从上级目录开始书写
f2 = open(r'aaa/f1.txt')

# 情况三：如果py文件的上级目录和txt文件平级，则需要回退路径
'''
# ..表示回退一级目录，..\..表示回退两级目录
# f1 = open(r'..\f1.txt')
f2 = open(r'..\..\t1.txt')
'''




