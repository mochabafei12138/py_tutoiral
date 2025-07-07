import  os

# 1.listdir():列出指定路径下所有的内容,返回一个列表，其中的元素是给定路径下所有文件及文件夹的名称
'''
绝对路径：带有盘符的路径
相对路径：当前工程下，相当于当前py文件，没有盘符的路径，建议使用
'''
path = r'd:\Desktop\coding'
r1 = os.listdir(path)
print(r1)

# 2.join(父路径，子路径):拼接路径
# d:\Desktop\coding\Day10
base_path = r'd:\Desktop\coding'
for name in r1:
    sub_path = os.path.join(base_path,name)  # 会自动识别当前的操作系统，从而确定路径中使用/还是\
    print(sub_path)

# 3.mkdir():创建文件夹
# os.mkdir(r'ddd')

# 4.exists()；判断路径是否存在
print(os.path.exists(r'd:\Desktop\coding\D34ay1'))
print(os.path.exists(r'aaa'))

# 5.isfile():判断路径是否是文件
# isdir():判断路径是否是文件夹
print(os.path.isfile(r'd:\Desktop\coding\Day1'))
print(os.path.isdir(r'd:\Desktop\coding\Day1'))