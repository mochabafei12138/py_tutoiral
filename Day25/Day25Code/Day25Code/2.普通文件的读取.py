'''
open(file,mode,encoding)
mode:打开文件的模式
    'r' open for reading (default)，打开文件默认表示读取
    'w' open for writing, truncating the file first，打开用于写入【工作原理：删除已经存在的文件，然后生成一个和原文件同名的新的空白文件】
    'x' create a new file and open it for writing，用于创建一个新文件并打开用于写入，少用
    'a' open for writing, appending to the end of the file if it exists，打开用于写入【工作原理：如果文件存在的情况下，则将新的内容追加到旧内容的后面】
    'b' binary mode，打开一个二进制文件
    't' text mode (default),默认识别文本，经常会省略
encoding
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed  ，编码格式以字符串的方式表示，只要是Python支持的编码格式，都可以使用，默认编码格式由当前使用的平台决定
    常用的编码格式：utf-8
                 gbk
'''
# 第一步：打开文件
# 注意1：在读取文件的时候，encoding的值一定要和被读取的文件的编码格式保持一致,否则因为无法解码而导致报错
# 注意2：encoding一定要用关键字参数表示
# 注意3：当open函数执行完毕，会得到一个被打开的文件对象，也被称为文件描述符，后续的操作都由文件描述符执行
f1 = open(r'aaa/致橡树.txt','r',encoding='gbk')

# 第二步：读取内容
# a.read():一次性读取全部内容
# r1 = f1.read()
# print(r1)
# read(n):一次读取n个字符
# r11 = f1.read(3)
# print(r11)
# r11 = f1.read(3)
# print(r11)

# b.readline():一次读取一行内容，以换行符作为分割的依据
# r2 = f1.readline()
# print(r2)
# r2 = f1.readline()
# print(r2)

# c.readlines():一次全部读取完毕，但是返回一个列表，列表中的元素是每行内容
r3 = f1.readlines()
print(r3)
# 注意4：如果读取到的数据没有达到预期的效果，需要手动处理
for line in r3:
    new_line = line.rstrip('\n').lstrip('\u3000').lstrip()
    print(new_line)

# 第三步：关闭文件
# 注意5：为了节约内存空间，当文件读写完毕之后，手动将文件关闭，释放占用的资源
f1.close()

# 注意6：打开文件用于读取，则文件路径一定要存在，否则会报错FileNotFoundError
# 注意7：在pycharm中手动创建一个文件，默认的编码格式是utf-8