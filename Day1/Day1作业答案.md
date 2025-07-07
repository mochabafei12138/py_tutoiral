### 选择题

1. 下⾯哪个不是Python合法的标识符（B）
   A. int64
   B. 40XL
   C. self
   D. stu_name
2. 下列关于Python语⾔说法错误的是（C）
   A. Python是解释型语言
   B. Python是⾯向对象语⾔
   C. Python2.x和Python3.x是完全兼容的
   D. Python语言是跨平台的
3. 下列关于print函数用法错误的是（D）
   A. print(100)
   B. print(100, 200)
   C. print(100, 'hello world!')
   D. print(10 20)

### 填空题

1. Python中单行注释的符号是（  # ）, 多⾏注释的符号是（  ''''''或""""""  ）。
2. Python程序文件扩展名是(   .py)。
3. 在Python中，int表示的数据类型是（整型  ）。
4. 在Python中，给多行代码同时添加注释的快捷键是（ctrl +/  ）。

### 简答题

1. 简述标识符的规则和规范。

   ```
   合法标识符的命名规则：

   - 只能由数字，字母和下划线组成
   - 不可以是除了下划线之外的其他特殊字符
   - 开头不能是数字或者空格
   - 不能是Python的关键字
   - 严格区分大小写    age   Age

   标识符的命名规范：

   - 尽量做到见名知意【具有描述性】：尽量使用简单的英文单词表示
   - 遵守一定的命名规范
     - Python官方推荐的命名方式：变量名，函数名和文件名全小写，使用下划线连接，如：stu_name     check_qq
     - 驼峰命名法：不同的单词之间使用首字母大写的方式进行分隔，又分为大驼峰和小驼峰，比如：stuName就是小驼峰，StuName就是大驼峰，小驼峰常用于变量或者函数的命名，大驼峰常用于类的命名
   ```

2. 请写出Python语言有哪些特点。

   ```
   - Python是一种解释性语言【开发过程中没有了编译这个环节，类似于PHP或者Perl语言】
   - Python是交互式语言【可以在一个Python提示符，直接互动执行程序】
   - Python是面向对象语言【Python支持面向对象的风格或代码封装在对象的编程技术，面向对象语言的三大特征：封装，继承和多态】
   - Python是跨平台的【它可以运行在Windows、Mac os或者Linux系统上，也就是说，在Windows上书写的Python程序，在Linux上也是可以运行的，类似于Java】

   ```

3. 请写出Python常⻅的应用领域

   ```Python
   - Web开发【通过mod_wsgi模块，Apache可以运行用Python编写的Web程序。Python定义了WSGI标准应用接口来协调Http服务器与基于Python的Web程序之间的通信。一些Web框架，如Django,TurboGears,web2py,Zope等，可以让程序员轻松地开发和管理复杂的Web程序】
   - 操作系统管理、服务器运维的自动化脚本【在很多操作系统里，Python是标准的系统组件。 大多数Linux发行版以及NetBSD、OpenBSD和Mac OS X都集成了Python，可以在终端下直接运行Python。Python编写的系统管理脚本在可读性、性能、代码重用度、扩展性几方面都优于普通的shell脚本】
   - 网络爬虫【Python有大量的HTTP请求处理库和HTML解析库，并且有成熟高效的爬虫框架Scrapy和分布式解决方案scrapy-redis，在爬虫的应用方面非常广泛】
   - 科学计算（数据分析）【NumPy、SciPy、Pandas、Matplotlib可以让Python程序员编写科学计算程序】
   - 桌面软件【PyQt、PySide、wxPython、PyGTK是Python快速开发桌面应用程序的利器】
   - 服务器软件（网络软件）【Python对于各种网络协议的支持很完善，因此经常被用于编写服务器软件、网络爬虫。第三方库Twisted支持异步网络编程和多数标准的网络协议(包含客户端和服务器)，并且提供了多种工具，被广泛用于编写高性能的服务器软件】
   - 游戏【很多游戏使用C++编写图形显示等高性能模块，而使用Python或者Lua编写游戏的逻辑、服务器。相较于Python，Lua的功能更简单、体积更小；而Python则支持更多的特性和数据类型】
   - 自动化测试
   - 少儿编程讲师
   ```

### 编程题

1.从控制台分别输入姓名，年龄和爱好，并按照指定格式输出到控制台上

```
运行效果：
请输入姓名：张三
请输入年龄：18
请输入爱好：吹牛逼
我是张三，今年18，爱好吹牛逼
```

```Python
name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
hobby = input("请输入你的爱好：")
print('大家好，我是',name,'今年',age,'爱好：',hobby)
```

