### 一、正则表达式

#### 1.案例-校验qq号

> 合法的qq号：
>
> ​	a.全部是数字
> 	b.位数5~11位
> 	c.开头不能为0
>
> ```Python
> '''
> 合法的qq号：
> 	a.全部是数字
> 	b.位数5~11位
> 	c.开头不能为0
> '''
> # 方式一
> def check_qq1(qq:str):
>     result = True
>     if qq.isdigit():
>         if len(qq) in range(5,12):
>             if qq[0] == '0':
>                 result = False
>         else:
>             result = False
>     else:
>         result  = False
>     return result
> 
> # 方式二
> def check_qq2(qq):
>     if (qq.isdigit()) and (len(qq) in range(5,12)) and (qq[0] != '0'):
>         return True
>     return False
> 
> # 方式三
> import re
> def check_qq3(qq):
>     # 如果匹配上了则返回Match object，如果匹配不上则返回None
>     # r = re.match(r'[1-9][0-9]{4,10}$',qq)
>     r = re.match(r'[1-9]\d{4,10}$', qq)
>     return True if r else False
> 
> if __name__ == '__main__':
>     qq = '2557746765226272727'
>     print(check_qq3(qq))
> ```

#### 2.概念

> 正则表达式（英语：Regular Expression，在代码中常简写为regex、regexp）使用单个字符串来描述、匹配一系列符合某个句法规则的字符串搜索模式。注意：Python中的正则的模块名为re,所以自定义文件的名字不能命名为re
>
> 【面试题】正则表达式的特点
>
> - 搜索模式可用于文本搜索。如：search(),findall(),finditer()    *******
> - 正则表达式是由一个字符序列形成的搜索模式。
> - 当你在文本中搜索数据时，你可以用搜索模式来描述你要查询的内容。
> - 正则表达式可以是一个简单的字符，或一个更复杂的模式。
> - 正则表达式可用于所有文本替换的操作,如：sub(),subn()
>
> 而在python中，通过内嵌集成re模块，可以直接调用来实现正则匹配。正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行
>
> 使用场景：
>
> - 用于验证用户名，密码，银行卡号，身份证号，手机号，邮箱，ip地址等
> - 爬虫时，使用正则解析网页中的内容
>
> Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
>
> re 模块使 Python 语言拥有全部的正则表达式功能
>

#### 3.单字符匹配

> ```Python
> """
> .                匹配除换行符以外的任意字符
> [0123456789]     []是字符集合，表示匹配方括号中所包含的任意一个字符
> [good]           匹配good中任意一个字符
> [a-z]            匹配任意小写字母
> [A-Z]            匹配任意大写字母
> [0-9]            匹配任意数字，类似[0123456789]
> [0-9a-zA-Z]      匹配任意的数字和字母
> [0-9a-zA-Z_]     匹配任意的数字、字母和下划线
> [^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
> [^0-9]           匹配所有的非数字字符
> \d               匹配数字，效果同[0-9]
> \D               匹配非数字字符，效果同[^0-9]
> \w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
> \W               匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
> \s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
> \S               匹配任意的非空白符，效果同[^ \f\n\r\t]
> """
> ```

> ```Python
> """
> .                匹配除换行符以外的任意字符
> [0123456789]     []是字符集合，表示匹配方括号中所包含的任意一个字符
> [good]           匹配good中任意一个字符
> [a-z]            匹配任意小写字母
> [A-Z]            匹配任意大写字母
> [0-9]            匹配任意数字，类似[0123456789]
> [0-9a-zA-Z]      匹配任意的数字和字母
> [0-9a-zA-Z_]     匹配任意的数字、字母和下划线
> [^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
> [^0-9]           匹配所有的非数字字符
> \d               匹配数字，效果同[0-9]
> \D               匹配非数字字符，效果同[^0-9]
> \w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
> \W               匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
> \s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
> \S               匹配任意的非空白符，效果同[^ \f\n\r\t]
> """
> '''
> 匹配：match()
> 查找/搜索：search()/findall()/finditer()
> 替换：sub()/subn()
> 分割：split()
> '''
> import re
> 
> # 1.re模块中函数的调用方式
> # a.方式一
> # 注意：因为正则表达式中有很多特殊符号，所以书写正则采用r'xxxx'
> pattern = re.compile(r'\d')
> r = pattern.match('6')
> print(r)
> 
> # b.方式二:推荐使用
> r = re.match(r'\d','6')
> print(r)
> 
> # 2.     .                匹配除换行符以外的任意字符   *****
> # 注意：默认情况下，可以匹配除了换行符\n以外的任意字符
> r = re.match(r'.','\n')
> print(r)  # None
> 
> # 注意：设置flags=re.DOTALL,可以匹配所有字符，常用于存在大量换行符的文本匹配中
> # 注意：flags一般以关键字参数的方式使用，避免在某些函数中无法使用
> r = re.match(r'.','\n',re.DOTALL)
> print(r)   # <re.Match object; span=(0, 1), match='\n'>
> 
> # 3.[xxxxx...]不管[]中书写了多少个字符，都只能匹配其中的一位
> '''
> [0123456789] ---->[0-9]    []是字符集合，表示匹配方括号中所包含的任意一个字符
> [good]           匹配good中任意一个字符
> [a-z]            匹配任意小写字母
> [A-Z]            匹配任意大写字母
> [0-9]            匹配任意数字，类似[0123456789]
> [0-9a-zA-Z]      匹配任意的数字和字母
> [0-9a-zA-Z_]     匹配任意的数字、字母和下划线
> '''
> r = re.match(r'[a-z]','y')
> print(r)
> 
> r = re.match(r'[0-9a-zA-Z_]','%')
> print(r)
> 
> r = re.match(r'[hywlxa]','%')
> print(r)
> 
> # 4.[^xxxxxxx]:表示否定
> '''
> [^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
> [^0-9]           匹配所有的非数字字符
> '''
> r = re.match(r'[^hywlxa]','h')
> print(r)   # None
> 
> r = re.match(r'[^0-9a-zA-Z_]','%')
> print(r)
> 
> # 5.
> '''
> \d               匹配数字，效果同[0-9]
> \D               匹配非数字字符，效果同[^0-9]
> \w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
> \W               匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
> \s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
> \S               匹配任意的非空白符，效果同[^ \f\n\r\t]
> '''
> r = re.match(r'\w','%')
> print(r)
> 
> # 练习：匹配一个由4位的验证码，每一位可以由数字或字母组成
> r = re.match(r'[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]','45f7')
> print(r)
> ```

#### 4.数量词匹配

> ```Python
> """
> x?       匹配0个或者1个x
> x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
> x+       匹配1个 或者 多个
> x{n}     匹配确定的n个x（n是一个非负整数）
> x{n,}    匹配至少n个x
> x{n,m}   匹配至少n个最多m个x。注意：n <= m
> """
> ```

> match():匹配，从左往右依次匹配，如果匹配上，返回Match对象，如果匹配不上，返回None
> search():搜索，底层和match的使用相同，如果搜索到，返回Match对象，如果搜索不上，返回None
>
> ​	注意：只要搜索到一个符合条件的子字符串，则停止搜索
>
> findall():查找所有，最终的结果返回一个列表
>
> ```Python
> '''
> x?       匹配0个或者1个x
> x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
> x+       匹配1个 或者 多个
> x{n}     匹配确定的n个x（n是一个非负整数）
> x{n,}    匹配至少n个x
> x{n,m}   匹配至少n个最多m个x。注意：n <= m
> '''
> import re
> 
> '''
> x{n}     匹配确定的n个x（n是一个非负整数）
> x{n,}    匹配至少n个x
> x{n,m}   匹配至少n个最多m个x。注意：n <= m
> '''
> # a
> r = re.match(r'\d{3}','12345678650493827')
> print(r)
> r = re.match(r'\d{3,}','12345678650493827')
> print(r)
> r = re.match(r'\d{3,6}','12345678650493827')
> print(r)
> 
> # 练习：匹配一个由4位的验证码，每一位可以由数字或字母组成
> r = re.match(r'[0-9a-zA-Z]{4}','45f7')
> print(r)
> 
> # 注意：如果match或search能匹配上，返回Match object，则可以访问group()获取匹配到的子字符串,如果返回None，则无法访问group()
> print(r.group())
> 
> # b.
> r = re.search(r'\d{3}','a12345678650493827')
> print(r)
> r = re.search(r'\d{3,}','a12345678650493827')
> print(r)
> r = re.search(r'\d{3,6}','a12345678650493827')
> print(r)
> 
> # c.
> r = re.findall(r'\d{3}','a12345678650493827')
> print(r)
> r = re.findall(r'\d{3,}','a12345678650493827')
> print(r)
> r = re.findall(r'\d{3,6}','a123456786504938')
> print(r)
> 
> # d.
> r = re.findall(r'\d?','a123456786c50493827')
> print(r)
> r = re.findall(r'\d+','a123456786c50493827')
> print(r)
> r = re.findall(r'\d*','a123456786c504938')
> print(r)
> 
> ```

#### 5.边界匹配

> ```Python
> """
> ^     行首匹配，和在[]里的^不是一个意思
> $     行尾匹配
>
> \A    匹配字符串开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
> \Z    匹配字符串结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾
> """
> ```

> ```Python
> """
> ^     行首匹配/边界匹配，和在[]里的^不是一个意思   *****
> $     行尾匹配 /边界匹配         *****
> 
> \A    匹配字符串开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
> \Z    匹配字符串结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾
> """
> import re
> 
> # 注意1：默写情况下，字符串使用的是单行模式，哪怕字符串中使用\n表示换行
> r1 = re.findall(r'^today','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day')
> print(r1)   # ['today']
> r2 = re.findall(r'day$','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day')
> print(r2)  # ['day']
> 
> # 注意2：如果要匹配到多行的行首或行尾，则需要设置flags=re.M或flags=re.MULTILINE，才表示多行模式
> r1 = re.findall(r'^today','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.MULTILINE)
> print(r1)   # ['today', 'today', 'today']
> r2 = re.findall(r'day$','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.M)
> print(r2)  # ['day', 'day', 'day']
> 
> # 注意3:$经常用来限制位数,^用来匹配字符串的开头  ****
> qq = '2557746765226272727'
> r = re.match(r'[1-9]\d{4,10}$', qq)
> print(r)
> 
> # 注意4：即使在re.M模式下也不会匹配它行的行首或行尾
> r1 = re.findall(r'\Atoday','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.MULTILINE)
> print(r1)   # ['today']
> r2 = re.findall(r'day\Z','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.M)
> print(r2)  # ['day']
> 
> ```

#### 6.分组匹配

> ```python
> """
> x|y      |表示或，匹配的是x或y
> (xyz)    匹配小括号内的xyz(作为一个整体去匹配)
> """
> ```

> ```Python
> """
> x|y      |表示或，匹配的是x或y
> (xyz)    匹配小括号内的xyz(作为一个整体去匹配)
> """
> 
> import re
> 
> # 1
> print(re.findall(r'\d+','d3464-kfghj23747abv485'))
> print(re.findall(r'[a-z]+','d3464-kfghj23747abv485'))
> '''
> ['3464', '23747', '485']
> ['d', 'kfghj', 'abv']
> '''
> 
> # 2.
> print(re.findall(r'\d+|[a-z]+','d3464-kfghj23747abv485'))
> # ['d', '3464', 'kfghj', '23747', 'abv', '485']
> 
> # 3.
> print(re.findall(r'(\d+)|[a-z]+','d3464-kfghj23747abv485'))
> print(re.findall(r'\d+|([a-z]+)','d3464-kfghj23747abv485'))
> '''
> ['', '3464', '', '23747', '', '485']
> ['d', '', 'kfghj', '', 'abv', '']
> '''
> 
> r1 = re.finditer(r'(\d+)|[a-z]+','d3464-kfghj23747abv485')
> print([obj.group() for obj in r1])   # ['d', '3464', 'kfghj', '23747', 'abv', '485']
> 
> r2 = re.finditer(r'\d+|([a-z]+)','d3464-kfghj23747abv485')
> print([obj.group() for obj in r2])  # ['d', '3464', 'kfghj', '23747', 'abv', '485']
> 
> # 4.
> # a.捕获型分组：正则表达式中有(),findall查找完毕之后只显示()中匹配的内容    *******
> print(re.findall(r'(\d+)|[a-z]+','d3464-kfghj23747abv485'))
> print(re.findall(r'\d+|([a-z]+)','d3464-kfghj23747abv485'))
> '''
> ['', '3464', '', '23747', '', '485']
> ['d', '', 'kfghj', '', 'abv', '']
> '''
> 
> # b.非捕获分组：格式：(?:xxx)
> print(re.findall(r'(?:\d+)|[a-z]+','d3464-kfghj23747abv485'))
> print(re.findall(r'\d+|(?:[a-z]+)','d3464-kfghj23747abv485'))
> '''
> ['d', '3464', 'kfghj', '23747', 'abv', '485']
> ['d', '3464', 'kfghj', '23747', 'abv', '485']
> '''
> ```

#### 7.贪婪匹配和非贪婪匹配

> ```Python
> """
> 注意：
>     a.+和*都是贪婪匹配，会尽可能多的匹配
>     b.在+或*的后面添加？，可以将贪婪匹配转换为非贪婪匹配
>     c.在爬虫中，re.findall(r".+?img.+?src=(.+?)","xxxxxxxx",flags=re.DOTALL)
> """
> 
> """
> 非贪婪匹配
> x?       匹配0个或者1个x
> 
> 贪婪匹配
> x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
> x+       匹配1个 或者 多个
> """
> ```

> ```Python
> import re
> 
> '''
> *和+：贪婪匹配
> ?:非贪婪匹配
> 
> *?和+?：将贪婪匹配转换为非贪婪匹配，只要遇到限制的条件则会停止贪婪匹配
> '''
> 
> # 1.
> print(re.findall(r'd\w+','d3464_kfghj23747abdv485k'))
> print(re.findall(r'\w+k','d3464_kfghjk23747abdv485k'))
> print(re.findall(r'd\w+k','d3464_kfghjk23747abdv485k'))
> '''
> ['d3464_kfghj23747abdv485k']
> ['d3464_kfghjk23747abdv485k']
> ['d3464_kfghjk23747abdv485k']
> '''
> 
> # 2.
> print(re.findall(r'd\w+?','d3464_kfghj23747abdv485k'))
> print(re.findall(r'\w+?k','d3464_kfghjk23747abdv485k'))
> print(re.findall(r'd\w+?k','d3464_kfghjk23747abdv485k'))
> '''
> ['d3', 'dv']
> ['d3464_k', 'fghjk', '23747abdv485k']
> ['d3464_k', 'dv485k']
> '''
> 
> # 3.
> print(re.findall(r'd\w*','d3464_kfghj23747abdv485k'))
> print(re.findall(r'\w*k','d3464_kfghjk23747abdv485k'))
> print(re.findall(r'd\w*k','d3464_kfghjk23747abdv485k'))
> '''
> ['d3464_kfghj23747abdv485k']
> ['d3464_kfghjk23747abdv485k']
> ['d3464_kfghjk23747abdv485k']
> '''
> 
> # 4.
> print(re.findall(r'd\w*?','d3464_kfghj23747abdv485k'))
> print(re.findall(r'\w*?k','d3464_kfghjk23747abdv485k'))
> print(re.findall(r'd\w*?k','d3464_kfghjk23747abdv485k'))
> '''
> ['d', 'd']
> ['d3464_k', 'fghjk', '23747abdv485k']
> ['d3464_k', 'dv485k']
> '''
> ```

#### 8.常用函数【自学】

> ```Python
> import  re
> 
> # 1.compile():将正则字符串编译成正则对象，一般都是为了结合其他 函数使用
> 
> # 2.match():用正则匹配指定字符串中的内容，如果匹配上，返回Match对象，如果未匹配上，则返回None   *****
> # 应用：判断用户名或密码是否合法
> 
> # 3.search():用正则搜索指定字符串中的内容，如果匹配上，返回Match对象，如果未匹配上，则返回None
> # 注意：只会查找一次
> 
> # 4.findall():用正则搜索指定字符串中的内容，如果匹配上，返回非空列表，如果未匹配上，则返回[]  ******
> # 注意：查找所有
> # 应用：全局搜索数据，在爬虫中一般使用findall
> r = re.findall(r"a\d","6a8ghjaga3474a9")
> print(r)  # ['a8', 'a3', 'a9']
> 
> # 5.finditer():用正则搜索指定字符串中的内容，返回一个迭代器，如果匹配上，则迭代器中的元素为Match对象  *****
> # 注意：查找所有
> r = re.finditer(r"a\d","6a8ghjaga3474a9")
> print(r) # <callable_iterator object at 0x100f8dcc0>
> 
> # 方式一
> # for obj in r:
> #     print(obj)
> #     print(obj.group())   # 获取Match对象的文本内容
> 
> # 方式二
> # print(next(r))
> # print(next(r))
> # print(next(r))
> while True:
>     try:
>         obj = next(r)
>         print(obj,obj.group())
>     except StopIteration as e:
>         # 如果出现异常，则说明迭代器中的元素已经获取完毕
>         break
> 
> # 6.split():用正则指定的规则分割指定字符串，返回一个列表    *******
> str1 = 'one1two1three1four'
> l1 = str1.split("1")     # 字符串.split(分割符)，返回一个列表,适用于分割有规律的字符串
> print(l1)
> 
> str1 = 'one1two6three3four'
> l1 = re.split(r'\d',str1) # re.split(正则分割符,字符串)
> print(l1)
> 
> str1 = 'one1466two624492236three354four'
> l1 = re.split(r'\d+',str1)
> print(l1)
> 
> # 同字符串.split(),re.split()也可以指定分割次数
> str1 = 'one1466two624492236three354four'
> l1 = re.split(r'\d+',str1,2)
> print(l1)
> 
> # 7.sub():将正则匹配到的子字符串用指定字符串进行替换   ********
> # subn()
> str1 = 'one111two111three111four'
> l1 = str1.replace('111',"-")
> print(l1)
> 
> str1 = 'one34628two5558252three16266four'
> l1 = re.sub(r"\d+",'-',str1)
> print(l1)
> 
> # 可以指定替换的次数
> str1 = 'one34628two5558252three16266four'
> l1 = re.sub(r"\d+",'-',str1,2)
> print(l1)
> 
> # subn()返回一个元组，格式：(新字符串，替换的次数)
> str1 = 'one34628two5558252three16266four'
> l1 = re.subn(r"\d+",'-',str1)
> print(l1)  # ('one-two-three-four', 3)
> ```

#### 9.练习

> ```python
> """
> 1.用户名匹配
> 			要求:	1.用户名只能包含数字 字母 下划线
> 					2.不能以数字开头
> 					3.⻓度在 6 到 16 位范围内
> """
>
> """
> 2.密码匹配 
>
> 			要求:	1.不能包含!@#¥%^&*这些特殊符号
> 					2.必须以字母开头 
> 					3.⻓度在 6 到 12 位范围内
> """
>
> # 3.将给定字符串中的数字挑出，拼接成一个新的字符串
>
> # 4.将给定字符串中的数字挑出，求和
> ```

> ```Python
> import re
> """
> 1.用户名匹配
> 			要求:	1.用户名只能包含数字 字母 下划线
> 					2.不能以数字开头
> 					3.⻓度在 6 到 16 位范围内
> """
> def check_username(username):
>     r = re.match(r'[a-zA-Z_]\w{5,15}$',username)
>     return True if r else False
> 
> print(check_username('hf_faj'))
> 
> """
> 2.密码匹配 
> 
> 			要求:	1.不能包含!@#¥%^&*这些特殊符号
> 					2.必须以字母开头 
> 					3.⻓度在 6 到 12 位范围内
> """
> def check_pwd(pwd):
>     r = re.match(r'[a-zA-Z][^!@#¥%^&*]{5,11}$',pwd)
>     return True if r else False
> 
> print(check_pwd('545be4btj'))
> 
> # 3.将给定字符串中的数字挑出，拼接成一个新的字符串
> def get_num(data):
>     # 方式一
>     # r = re.findall(r'\d+',data)
>     # return  ''.join(r)
> 
>     # 方式二
>     r = re.split(r'\D+',data)
>     return ''.join(r)
> 
> print(get_num('46fah490%43gg'))
> 
> # 4.将给定字符串中的数字挑出，求和
> def get_sum(data):
>     # 方式一
>     # r = re.findall(r'\d+',data)
>     # total = sum([int(ele) for ele in r])
>     # return total
> 
>     # 方式二
>     r = re.split(r'\D+', data)
>     total = sum([int(ele) for ele in r if ele != ''])
>     return total
> 
> print(get_sum('46fah490%43gg'))
> ```

