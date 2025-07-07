# 一、占位符
'''
%d:可以匹配数字，一般匹配整型【整数】
%f：可以匹配数字，一般匹配浮点型【小数】
%s：可以匹配Python中的一切数据类型
'''
# 语法：'按照指定格式定义占位符' % (实际的数据)
print('%d-%d-%d' % (34,6,8))
print('%f~~~~%d~~~~%s~~~~~%f' % (89.24,66,'abc',66))
print('姓名：%s,年龄：%d,成绩:%d' % ('张三',18,88))

# 问题1：占位符的数量和实际数据的数量一定要保持一致
# print('%f~~~~%d~~~~%s~~~~~%f' % (89.24,66,'abc'))  # TypeError: not enough arguments for format string
# print('%f~~~~%d~~~~%s' % (89.24,66,'abc',67,8))   # TypeError: not all arguments converted during string formatting

# 问题2：占位符和实际数据的类型要保持一致，特别是%d和%f
print('姓名：%s,年龄：%d,体重:%f' % ('张三',18,65.5))
# print('姓名：%s,年龄：%d,体重:%f' % ('张三','18',65.5))  # TypeError: %d format: a number is required, not str
# print('姓名：%s,年龄：%d,体重:%f' % ('张三',18,'65.5'))   # TypeError: must be real number, not str
print('姓名：%s,年龄：%s,体重:%s' % ('张三',18,'65.5'))

# 问题3：%.nd,n>=1,可以实现填充,填充的是0，如果省略.，则在左边填充空格
print('学号:%d' % (1))
print('学号:%.5d' % (1))   # 学号:00001
print('学号:%.5d' % (16))  # 学号:00016
print('学号:%5d' % (16))  # 学号:   16

# 问题4：%.nf，n >= 1,可以实现小数点后位数的保留，会涉及四舍五入    *******
print('身高:%f' % (45.67899))
print('身高:%.2f' % (45.67899))
print('身高:%.f' % (45.67899))  # 46   如果省略n,则表示取整，会涉及四舍五入

# 二、format()
# 语法：'通过{}设定格式'.format(value1,value2,value3.....)
# 1.用法：字符串中的占位符由成对的{}表示，在{}内部，使用格式说明符来控制被替换的数据的格式
print('{}-{}-{}'.format(34,6,8))

# 2.实际的数据有位置编号，如：34,6,8的位置编号分别为0,1,2
print('{0}-{1}-{2}'.format(34,6,8))
print('{2}-{0}-{1}'.format(34,6,8))
print('{0}-{0}-{0}'.format(34,6,8))

# 3.通过关键字替换占位符
print('我是{name}，今年{age}岁'.format(age=18,name='张三'))

# 4. {:.nf}表示保留小数点后n位
print('数字：{}'.format(354.45656))
print('数字：{:.2f}'.format(354.45656))
print('数字：{:.2%}'.format(354.45656))  # 带有2位小数的百分比

# 5.填充
print('{:>5}'.format(45))  # 将原数据右对齐，并在左侧填充空格，总长度达到5
print('{:<5}'.format(45))  # 将原数据左对齐，并在右侧填充空格，总长度达到5
print('{:^6}'.format(45))  # 将原数据居中，并在两侧填充空格，总长度达到6

# 三、f-string   常用
# 语法：f'xxx{value1},xxx{value2}'
print(f'{45}-{67}-{12}')

# 1.
num1 = 45
data = 'abc'
print(f'{23}~~~{num1}~~~{False}~~~~{data}')
# 注意：如果实际的数据是字符串，单双引号要岔开写
print(f'{23}~~~{num1}~~~{False}~~~~{"abc"}')
print(f"{23}~~~{num1}~~~{False}~~~~{'abc'}")

# 2.f'{xxx:.nf}'
print(f'体重：{56.456756:.2f}')

# 3.填充
data = 'Python'
print(f'{data}')
# 默认使用空格填充
print(f'{data:>10}')  # 将原数据右对齐，并在左侧填充空格，总长度达到10
print(f'{data:<10}')  # 将原数据左对齐，并在右侧填充空格，总长度达到10
print(f'{data:^10}')  # 将原数据居中，并在两侧填充空格，总长度达到10
# 使用指定的字符填充
print(f'{data:*^10}')
print(f'{data:%>10}')

# 四、练习
'''
11.从控制台分别输入姓名，年龄和爱好，并按照指定格式输出到控制台上
运行效果：
请输入姓名：张三
请输入年龄：18
请输入爱好：吹牛逼
我是张三，今年18，爱好吹牛逼
'''
name = input('请输入姓名：')
age = input('请输入年龄：')
hobby = input('请输入爱好：')
# 输出
print('我是',name,'今年',age,'爱好',hobby)  # 我是 张三 今年 18 爱好 吹牛逼
print('我是',name,'今年',age,'爱好',hobby,sep='')  # 我是张三今年18爱好吹牛逼
print('我是',name,',','今年',age,',','爱好',hobby,sep='')  # 我是张三,今年18,爱好吹牛逼

# 优化
print('我是%s,今年%s,爱好%s' % (name,age,hobby))
print('我是{},今年{},爱好{}'.format(name,age,hobby))
print(f'我是{name},今年{age},爱好{hobby}')