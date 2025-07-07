'''
Python异常处理的方式：捕获和抛出
'''

# 1.根据具体的问题创建异常对象
# try:
#     list1 = [4,6,7,89,9]
#     print(list1[20])
# except IndexError as e:
#     print(e)

# 2.可以通过异常的类创建异常的对象，控制代码的执行
# 语法：raise 异常类('描述信息')，注意：raise常用于自定义异常中
print('start~~~~')
try:
    raise IndexError('索引越界问题')
except Exception as e:
    print(e)
print('end~~~~~~')
