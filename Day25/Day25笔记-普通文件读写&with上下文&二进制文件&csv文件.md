### 一、文件读写【重点掌握】

> 常见文件的读写分类：
>
> ​	1.普通文件文件,如txt，py，html等
>
> ​	2.二进制文件，如图片，音频，视频，压缩包等
>
> ​	3.csv文件，如csv,需要借助于系统模块csv
>
> ​	4.对象的序列化和反序列化，如：pickle和json
>
> ​	5.常用的办公文件，如excel，word，pdf等，需要借助于第三方模块

#### 1.普通文件读写

##### 1.1文件路径说明

> ```Python
> '''
> open(file)
>     file：需要打开的文件路径
> 
> 文件路径：可以使用相对路径或绝对路径，但是推荐相对路径
>     绝对路径：从盘符开始的路径， 如：d:\Desktop\coding\Code\Day25Code\aaa\f1.txt
>     相对路径：相对于当前工程和当前py文件，如：aaa/f1.txt
> '''
> # 1.绝对路径
> # 注意1：因为路径中有特殊字符，为了保留字符原本的含义，建议使用r'xxx'表示路径的字符串
> # 错误写法
> # path1 = 'd:\Desktop\coding\Code\Day25Code\aaa\f1.txt'
> # print(path1)   # d:\Desktop\coding\Code\Day25Code1.txt
> # 正确写法
> path1 = r'd:\Desktop\coding\Code\Day25Code\a\f1.txt'
> print(path1)
> 
> # 2.相对路径
> # 情况一：如果当前py文件和txt文件平级，则可以直接书写txt文件名称
> # f1 = open(r't2.txt')  # FileNotFoundError: [Errno 2] No such file or directory: 't2.txt'
> f1 = open(r't1.txt')
> 
> # 情况二：如果当前py文件和txt文件的上级目录平级，则需要从上级目录开始书写
> f2 = open(r'aaa/f1.txt')
> 
> # 情况三：如果py文件的上级目录和txt文件平级，则需要回退路径
> '''
> # ..表示回退一级目录，..\..表示回退两级目录
> # f1 = open(r'..\f1.txt')
> f2 = open(r'..\..\t1.txt')
> '''
> ```

##### 1.2读取

> ```
> open(file,mode,encoding)
> ```

> ```Python
> '''
> open(file,mode,encoding)
> mode:打开文件的模式
>     'r' open for reading (default)，打开文件默认表示读取
>     'w' open for writing, truncating the file first，打开用于写入【工作原理：删除已经存在的文件，然后生成一个和原文件同名的新的空白文件】
>     'x' create a new file and open it for writing，用于创建一个新文件并打开用于写入，少用
>     'a' open for writing, appending to the end of the file if it exists，打开用于写入【工作原理：如果文件存在的情况下，则将新的内容追加到旧内容的后面】
>     'b' binary mode，打开一个二进制文件
>     't' text mode (default),默认识别文本，经常会省略
> encoding
>     encoding is the name of the encoding used to decode or encode the
>     file. This should only be used in text mode. The default encoding is
>     platform dependent, but any encoding supported by Python can be
>     passed  ，编码格式以字符串的方式表示，只要是Python支持的编码格式，都可以使用，默认编码格式由当前使用的平台决定
>     常用的编码格式：utf-8
>                  gbk
> '''
> # 第一步：打开文件
> # 注意1：在读取文件的时候，encoding的值一定要和被读取的文件的编码格式保持一致,否则因为无法解码而导致报错
> # 注意2：encoding一定要用关键字参数表示
> # 注意3：当open函数执行完毕，会得到一个被打开的文件对象，也被称为文件描述符，后续的操作都由文件描述符执行
> f1 = open(r'aaa/致橡树.txt','r',encoding='gbk')
> 
> # 第二步：读取内容
> # a.read():一次性读取全部内容
> # r1 = f1.read()
> # print(r1)
> # read(n):一次读取n个字符
> # r11 = f1.read(3)
> # print(r11)
> # r11 = f1.read(3)
> # print(r11)
> 
> # b.readline():一次读取一行内容，以换行符作为分割的依据
> # r2 = f1.readline()
> # print(r2)
> # r2 = f1.readline()
> # print(r2)
> 
> # c.readlines():一次全部读取完毕，但是返回一个列表，列表中的元素是每行内容
> r3 = f1.readlines()
> print(r3)
> # 注意4：如果读取到的数据没有达到预期的效果，需要手动处理
> for line in r3:
>     new_line = line.rstrip('\n').lstrip('\u3000').lstrip()
>     print(new_line)
> 
> # 第三步：关闭文件
> # 注意5：为了节约内存空间，当文件读写完毕之后，手动将文件关闭，释放占用的资源
> f1.close()
> 
> # 注意6：打开文件用于读取，则文件路径一定要存在，否则会报错FileNotFoundError
> # 注意7：在pycharm中手动创建一个文件，默认的编码格式是utf-8
> ```

##### 1.3循环读取

> ```Python
> # 1.read(n)：通过结合循环的方式，一般用于读取文件内容量较多的情况
> '''
> import  os
> path = r'aaa/致橡树.txt'
> f = open(path,'r',encoding='gbk')
> # 获取文件中的总字符数
> total_size = os.path.getsize(path)
> # print(total_size)
> # 设定一次需要读取的字符串
> sub_size = 8   # 一般设置为2的次方
> while total_size > 0:
>     r = f.read(sub_size)
>     print(r)
>     total_size -= sub_size
> # 关闭文件
> f.close()
> '''
> 
> 
> # 2.readline():结合循环读取所有的行
> path = r'aaa/致橡树.txt'
> f = open(path,'r',encoding='gbk')
> while True:
>     r = f.readline()
>     print(r)
>     if not r:
>         break
> f.close()
> ```

##### 1.4写入

> ```Python
> # 第一步：打开文件
> # 注意1：如果打开模式采用的是w或a，则表示打开文件用于写入，此时文件可以不存在，会自动生成
> # 注意2：如果打开模式使用的是w，则可以达到覆盖的目的
> # 注意3：如果打开模式使用的是a,则在原内容的基础上进行追加
> # f1 = open(r'aaa/a1.txt','w',encoding='utf-8')
> f2 = open(r'aaa/a1.txt','a',encoding='utf-8')
> 
> # 第二步：写入内容
> # f.write(字符串)
> f2.write('轻轻的我走了~~~')
> # 刷新，提高写入的效率
> f2.flush()
> 
> # 第三步：关闭文件
> f2.close()
> ```

#### 2.with上下文

> ```python
> """
> 语法：
> with  对象   as  变量:
>     pass
> 
> 在文件读写中：
> with  open()  as   f:
>     读/写
> 
> 说明：
>     a.with上下文管理器一般用于简化代码，如：文件读写，数据库操作等
>     b.使用with上下文管理器进行文件的读写之后，无需手动关闭文件，当with代码块执行完毕，对应的文件会自动关闭
>     c.变量表示文件描述符，也就是打开的文件对象
>     d.当通过with的方式打开文件，则文件读取和写入的操作一定要在with代码块中完成，否则文件会被关闭导致无法操作[ValueError: I/O operation on closed file.]
> """
> ```

> ```Python
> with open(r'aaa/致橡树.txt','r',encoding='gbk') as f1:
>     r = f1.read()
>     print(r)
> 
> with open(r'aaa/a1.txt','a',encoding='gbk') as f2:
>     f2.write('32345674123456789')
>     f2.flush()
> ```

#### 3.二进制文件读写

> 二进制文件：图片，音视频，压缩包等
>
> b:bin,binary

> 注意：
>
> ​	a.读取和写入二进制文件需要使用rb和wb
>  		 'rb'      打开二进制文件用于读取
>  		 'wb'      打开二进制文件用于写入
> 	b.因为二进制文件是由二进制【字节】组成，没有编码一说，所以需要省略encoding参数，如果设置encoding，报错ValueError: binary mode doesn't take an encoding argument
>
> ```Python
> with open(r'aaa/3.png','rb') as f1:
>     r = f1.read()
>     print(r)
> 
> with open(r'aaa/img.png','wb') as f2:
>     f2.write(r)   # f2.write(字节)
>     f2.flush()
> ```

#### 4.CSV文件读写

> CSV（Comma Separated Values逗号分隔值）
>
> .csv是一种文件格式（如.txt、.doc等），也可理解.csv文件就是一种特殊格式的纯文本文件。即是一组字符序列，字符之间用英文字符的逗号或制表符（Tab）分隔
>
> 所以，CSV文件本身就是是个纯文本文件，这种文件格式经常用来作为不同程序之间的数据交互的格式
>
> .csv文件打开方式有多种，如记事本、excel、Notepad++,sublime等，只要是文本编辑器都能正确打开
>
> ```Python
> import  csv
> 
> # 一、读取csv文件
> with open(r'aaa/b1.csv','r',encoding='utf-8') as f1:
>     # reader(iterable)----->iterator
>     reader = csv.reader(f1)
>     # for row in reader:
>     #     print(row)
>     datalist = list(reader)
>     print(datalist)
> 
> # 二、写入csv文件
> datalist = [['name', 'age', 'address'], ['zhangsan', '10', '上海'], ['lisi', '20', '北京'], ['wangwu', '19', '深圳'], ['xiaoming', '18', '成都']]
> # 如果在写入内容之后，发现每行内容的后面莫名其妙的出现了一个空行，则可以通过newline解决
> with open(r'aaa/b2.csv','w',encoding='utf-8',newline='') as f2:
>     writer = csv.writer(f2)
> 
>     # 方式一：通过遍历的方式，逐行写入
>     # for data in datalist:
>     #     writer.writerow(data)
> 
>     # 方式二：一次性写入多行
>     writer.writerows(datalist)
> ```
