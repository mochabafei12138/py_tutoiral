### 一、Excel简介

> ​	Excel是Microsoft（微软）为使用Windows和macOS操作系统开发的一款电子表格软件。Excel凭借其直观的界面、出色的计算功能和图表工具，再加上成功的市场营销，一直以来都是最为流行的个人计算机数据处理软件。当然，Excel也有很多竞品，例如Google Sheets、LibreOffice Calc、Numbers等，这些竞品基本上也能够兼容Excel，至少能够读写较新版本的Excel文件，当然这些不是我们讨论的重点。掌握用Python程序操作Excel文件，可以让日常办公自动化的工作更加轻松愉快，而且在很多商业项目中，导入导出Excel文件都是特别常见的功能。
>
> ​	Python操作Excel需要三方库的支持，如果要兼容Excel 2007以前的版本，也就是`xls`格式的Excel文件，可以使用三方库`xlrd`和`xlwt`，前者用于读Excel文件，后者用于写Excel文件。如果使用较新版本的Excel，即操作`xlsx`格式的Excel文件，可以使用`openpyxl`库，当然这个库不仅仅可以操作Excel，还可以操作其他基于Office Open XML的电子表格文件。`openpyxl`并不支持操作Office 2007以前版本的Excel文件。
>

> xls和xlsx和csv有什么区别

> ```python
> 1、文件格式不同。xls 是一个特有的二进制格式，其核心结构是复合文档类型的结构，而 xlsx 的核心结构是 XML 类型的结构，采用的是基于 XML 的压缩方式，使其占用的空间更小。xlsx 中最后一个 x 的意义就在于此。
>
> 2、版本不同。xls是excel2007及以前版本生成的文件格式，而xlsx是excel2007及以后版本生成的文件格式。
>
> 3、兼容性不同。xlsx格式是向下兼容的，可兼容xls格式。
>
> 4.csv是文本文件,用记事本就能打开.
> ```
>

### 二、xlrd和xlwt操作Excel文件【了解】

> 如果没有则安装：
>
> ```Python
> pip install xlwt
> pip install xlrd
> ```

#### 1.xlrd实现读取

> 例如在当前工程的data文件夹下有一个名为“阿里巴巴2020年股票数据.xls”的Excel文件
>
> ```Python
> import xlrd
> 
> # 处理流程：工作簿----》工作表----》单元格【坐标：行 列】
> 
> # 1.打开xls文件，得到一个工作簿对象workbook
> workbook = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')
> 
> # 2.获取工作簿中的工作表名称
> sheetnames = workbook.sheet_names()
> print(sheetnames)
> 
> # 3.获取工作表对象sheet
> # 方式一：根据名称获取
> sheet1 = workbook.sheet_by_name('股票数据')
> print(sheet1)
> # 方式二：根据索引获取
> sheet2 = workbook.sheet_by_index(2)
> print(sheet2)
> 
> # 4.获取单元格对象cell
> '''
> xlrd和xlwt中
> row:
>     Excel: 1 2 3 4 5 6.....
>     Python:0 1 2 3 4 5....
> col:
>     Excel: A B C D....
>     Python:0 1 2 3....
> '''
> # sheet.cell(row,col):获取某行某列处的单元格对象
> # 需求1：获取A1
> cell1 = sheet1.cell(0,0)
> print(cell1)
> # 需求2：获取D3
> cell2 = sheet1.cell(2,3)
> print(cell2)
> 
> print(type(cell1))
> 
> # 5.获取某行的某几列数据
> # a.sheet.row_values(row,col1,col2):前闭后开区间，返回一个列表，其中的元素是数据字符串，col1和col2可以省略
> # 需求1：获取第0行的数据
> print(sheet1.row_values(0))
> 
> # 需求2：获取第0行的第0~3列
> print(sheet1.row_values(0,0,4))
> 
> # slice:切片
> # b.sheet.row_slice(row,col1,col2)：前闭后开区间，返回一个列表，其中的元素是单元格对象
> print(sheet1.row_slice(0))
> print(sheet1.row_slice(0,0,4))
> 
> # 练习：读取阿里巴巴的数据，将其中的日期数据格式化为年月日，将小数保留小数点后3位
> workbook = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')
> sheet = workbook.sheet_by_name('股票数据')
> # 获取工作表中的总行数和总列数
> print(sheet.nrows,sheet.ncols)  # 255 7
> # 遍历工作表
> for row in range(sheet.nrows):   # 遍历行
>     for col in range(sheet.ncols):  # 遍历列
>         # 获取每个单元格对象
>         cell = sheet.cell(row,col)
>         # 获取单元格的值
>         value = cell.value
>         # print(value)
>         if row > 0:  # row为0的时候为表头，不作任何处理
>             if col == 0:
>                 # 对日期进行格式化
>                 # xldate_as_tuple(日期数据，0/1)将日期数据转化为元组形式
>                 # 0：以1900-1-1为基准的日期  1：1904-1-1为基准的日期
>                 date_tuple = xlrd.xldate_as_tuple(value,0)
>                 new_value = '%d年-%.2d月-%.2d日' % (date_tuple[0],date_tuple[1],date_tuple[2])
>                 print(new_value)
>             else:
>                 # 对数字进行格式化
>                 new_value = '%.3f' % (value)
>                 print(new_value)
> ```

#### 2.xlwt实现写入

> 写入Excel文件可以通过`xlwt` 模块的`Workbook`类创建工作簿对象，通过工作簿对象的`add_sheet`方法可以添加工作表，通过工作表对象的`write`方法可以向指定单元格中写入数据，最后通过工作簿对象的`save`方法将工作簿写入到指定的文件或内存中
>
> ```Python
> import xlwt,random,xlrd
> 
> # 1.创建工作簿对象
> workbook = xlwt.Workbook()
> 
> # 2.向工作簿中添加工作表对象
> sheet = workbook.add_sheet('千锋学员成绩表')
> 
> # 3.准备数据
> stu_names = ['张三','李四','王五','小明','小花']  # 作为第0列的数据
> subjects = ['姓名','语文','数学','英语','Python']    # 作为第0行的数据
> scores = [[random.randint(40,100) for i in range(len(subjects) - 1)] for j in range(len(stu_names))]
> print(scores)
> # [[70, 58, 64, 60], [81, 75, 61, 77], [47, 67, 48, 43], [74, 48, 88, 68], [43, 59, 59, 85]]
> 
> # 4.写入数据
> # 注意：写入数据的时候，文件一定要处于关闭状态，如果打开，执行写入操作，则PermissionError: [Errno 13] Permission denied: 'data/2024千锋成绩表.xls'
> # sheet.write(row,col,value)
> # a.写入第0行
> for index,value in enumerate(subjects):
>     sheet.write(0,index,value)
> # b.写入第0列
> for index,value in enumerate(stu_names):
>     sheet.write(index + 1,0,value)
> # c.写入成绩
> for row in range(len(scores)):
>     for col in range(len(scores[row])):
>         # 从第1行第1列开始操作起
>         sheet.write(row + 1,col + 1,scores[row][col])
> 
> # 5.保存工作簿
> workbook.save(r'data/2024千锋成绩表.xls')
> 
> 
> # 练习：读取阿里巴巴的数据，将其中的日期数据格式化为年月日，将小数保留小数点后3位，并将新的数据存储到一个新的工作簿中
> # 获取已知的工作簿和工作表
> workbook = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')
> sheet = workbook.sheet_by_name('股票数据')
> 
> # 创建新的工作簿和工作表
> new_workbook = xlwt.Workbook()
> new_sheet = new_workbook.add_sheet('新股票数据')
> 
> # 获取工作表中的总行数和总列数
> print(sheet.nrows,sheet.ncols)  # 255 7
> # 遍历工作表
> for row in range(sheet.nrows):   # 遍历行
>     for col in range(sheet.ncols):  # 遍历列
>         # 获取每个单元格对象
>         cell = sheet.cell(row,col)
>         # 获取单元格的值
>         value = cell.value
> 
>         if row == 0:  # row为0的时候为表头，不作任何处理
>             new_value = value
>         else:
>             sub_value = ''
>             if col == 0:
>                 # 对日期进行格式化
>                 # xldate_as_tuple(日期数据，0/1)将日期数据转化为元组形式
>                 # 0：以1900-1-1为基准的日期  1：1904-1-1为基准的日期
>                 date_tuple = xlrd.xldate_as_tuple(value,0)
>                 sub_value = '%d年-%.2d月-%.2d日' % (date_tuple[0],date_tuple[1],date_tuple[2])
>             else:
>                 # 对数字进行格式化
>                 sub_value = '%.3f' % (value)
>             new_value = sub_value
> 
>         # 将处理之后的新数据写入到新的工作表中
>         new_sheet.write(row,col,new_value)
> 
> # 保存新的工作簿
> new_workbook.save(r'data/处理结果-阿里巴巴.xls')
> ```

### 三、openpyxl操作Excel文件【重点掌握】

> openpyxl库用于操作2007年之后的office软件.主要指用于操作.xlsx文件.
>
> 安装：
>
> ```
> pip install openpyxl
> ```
>
> ​	`openpyxl`的优点在于，当我们打开一个Excel文件后，既可以对它进行读操作，又可以对它进行写操作，而且在操作的便捷性上是优于`xlwt`和`xlrd`的。此外，如果要进行样式编辑和公式计算，使用`openpyxl`也远比上一个章节我们讲解的方式更为简单，而且`openpyxl`还支持数据透视和插入图表等操作，功能非常强大。
>
> 注意：有一点需要再次强调，`openpyxl`并不支持操作Office 2007以前版本的Excel文件。

#### 1.概念简介

> 对象：
>
> ```
> Workbook:代表一个Excel 工作薄
> Worksheet:代表一个Excel 工作表中的一页（sheet）
> Cell:代表最简单的一个单元格
> ```
>
> Workbook 对象涉及属性和方法：
>
> ```
> Workbook 对象涉及属性如下:
> active: 获取当前活跃的Worksheet    ******
> worksheets: 以列表的形式返回所有Worksheet   *****
> read_only: 判断是否以read_only 模式打开excel 文档
> encoding：获取文档的字符集编码
> properties: 获取文档的元数据，如标题、创建者、创建日期等
> ```
>
> Workbook 对象涉及方法如下:
>
> ```
> get_sheet_names:获取所有表格的名称(该方法已经被废弃，推荐使用:通过Workbook 的sheetnames 属性即可获取)
> get_sheet_by_name:通过表格名称获取WorkSheet对象(该方法已经被废弃，推荐使用:通过Worksheet['表名']获取)
> get_active_sheet: 获取活跃的表格
> remove_sheet:删除一个表格
> create_sheet：创建一个表格
> copy_worksheet：在Workbook 内复制表格
> ```
>
> Worksheet 对象涉及属性和方法：
>
> ```
> title：表格的标题
> dimensions:表示表格的大小，这里的大小是指数据的表格大小，即，左上角的坐标和右下角的坐标
> max_row:表格最大行数
> min_row:表格最小行数
> max_column：表格最大列数
> min_column：表格最小列数
> rows:按行获取单元格
> columns:按列获取单元格
> freeze_panes:冻结窗口
> values:按行获取表格内容
> ```
>
> Worksheet 对象涉及相关方法
>
> ```
> iter_rows:按行获取所有单元格，内置属性有:min_row、max_row、min_col和max_col
> iter_columns：按列获取所有单元格
> append：在表格末尾添加数据    ******
> merged_cells：合并多个单元格   ******
> unmerged_cells：移除合并的单元格
> ```
>
> Cell 对象涉及属性和方法:
>
> ```
> Cell 对象涉及相关属性
> row: 单元格所在的行
> column： 单元格所在的列
> value: 单元格的值
> coordinate:单元格的坐标
> ```

#### 2.openpyxl实现读取

> ​	需要提醒大家一点，`openpyxl`获取指定的单元格有两种方式，一种是通过`cell`方法，需要注意，该方法的行索引和列索引都是从`1`开始的，这是为了照顾用惯了Excel的人的习惯；另一种是通过索引运算，通过指定单元格的坐标，例如`C3`、`G255`，也可以取得对应的单元格，再通过单元格对象的`value`属性，就可以获取到单元格的值。通过上面的代码，相信大家还注意到了，可以通过类似`sheet['A2:C5']`或`sheet['A2':'C5']`这样的切片操作获取多个单元格，该操作将返回嵌套的元组，相当于获取到了多行多列。
>
> 注意：openpyxl中cell方法的行索引和列索引都是从1开始的，区别于xlrd和xlwt中是从0开始的
>
> ```Python
> import openpyxl
> 
> # 1.获取工作簿对象
> workbook = openpyxl.load_workbook(r'data/阿里巴巴2020年股票数据.xlsx')
> print(workbook)
> 
> # 2.获取工作表对象
> # a.获取所有工作表名称
> print(workbook.sheetnames)
> # b.获取当前处于活跃状态的工作表对象
> # 注意：读取excel文件的时候，可以不关闭文件，但是获取的结果可能不准确
> sheet1 = workbook.active  # 最近一次关闭工作簿之后，选中的工作表
> print(sheet1)
> 
> # c.通过工作表名称获取工作表对象，语法：wb['工作表名称']
> sheet2 = workbook['Sheet1']
> print(sheet2)
> 
> # d.通过索引获取工作表对象，语法：wb.worksheets[index]
> # 获取所有的工作表对象，返回一个列表
> print(workbook.worksheets)
> sheet3 = workbook.worksheets[2]
> print(sheet3)
> 
> # 3.获取工作表的行数和列数【范围】
> print(sheet1.dimensions)   # A1:G255
> print(sheet1.max_row,sheet1.max_column)   # 255 7
> 
> # 4.获取单元格对象
> # a.sheet['B5']
> cell1 = sheet1['A1']
> print(cell1)
> 
> # b.sheet.cell(row,col)
> '''
> openpyxl
> row:
>     Excel: 1 2 3 4 5 6....
>     Python:1 2 3 4 5 6....
> col:
>     Excel: A B C D....
>     Python:1 2 3 4.....   
> '''
> cell2 = sheet1.cell(1,2)
> print(cell2)
> 
> # 练习：C5
> print(sheet1['C5'])
> print(sheet1.cell(5,3))
> 
> # 5.获取单元格的值
> print(cell1.value)
> print(cell2.value)
> 
> # 6.获取指定行或指定列，返回一个元组，其中的元素是cell对象
> # a.获取行
> # sheet[row]:row和Excel中是对应的
> row = sheet1[1]
> print(row)
> # for cell in row:
> #     print(cell.value)
> row_data = [cell.value for cell in row]
> print(row_data)
> 
> # b.获取列
> # sheet[col]:col和Excel中是对应的
> col = sheet1['C']
> print(col)
> col_data = [cell.value for cell in col]
> print(col_data)
> 
> # c.获取多行或多列，返回一个二维元组，其中的元素是一行的单元格对象的元组
> rows = sheet1['A2:D10']     # 闭区间
> print(rows)
> for row in rows:
>     for cell in row:
>         print(cell.value)
> ```

#### 3.openpyxl实现写入

> ```Python
> import openpyxl
> 
> # 1.创建工作簿
> workbook = openpyxl.Workbook()
> # 注意：区别于xlwt,当创建完工作簿之后，会自动创建一个默认的工作表，默认名为Sheet
> print(workbook.sheetnames)   # ['Sheet']
> 
> # 给工作表重命名
> sheet = workbook['Sheet']
> sheet.title = '用户表'
> print(workbook.sheetnames)   # ['用户表']
> 
> # 2.创建表
> # 注意：创建表的时候，如果没有指明名称，则默认为Sheet,Sheet1......
> workbook.create_sheet()
> print(workbook.sheetnames)
> workbook.create_sheet()
> print(workbook.sheetnames)
> workbook.create_sheet()
> print(workbook.sheetnames)
> workbook.create_sheet('成绩表')
> print(workbook.sheetnames)
> 
> # 3.删除表
> sheet1 = workbook['Sheet1']
> workbook.remove(sheet1)
> print(workbook.sheetnames)
> 
> # 4.复制表
> sheet2 = workbook['用户表']
> workbook.copy_worksheet(sheet2)
> print(workbook.sheetnames)
> # 给复制之后的表重命名
> sheet3 = workbook['用户表 Copy']
> sheet3.title = '会员表'
> print(workbook.sheetnames)
> 
> # 5.修改单元格数据
> user_sheet = workbook['用户表']
> # 方式一
> # sheet['A1'] = 值
> user_sheet['A1'] = '姓名'
> user_sheet['B1'] = '年龄'
> user_sheet['C1'] = '用户编号'
> 
> # 方式二
> # sheet.cell(row,col,value)
> user_sheet.cell(2,1,'小明')
> user_sheet.cell(2,2,10)
> user_sheet.cell(2,3,'1001')
> 
> # 6.追加数据
> # 注意：sheet.append()可以向excel中追加一行内容，所以append的参数一般是是可迭代对象【常用列表或元组】
> # user_sheet.append(['小花',11,'1002'])
> 
> # 注意：后期只要将数据整理成下面二维列表的格式，就可以一次性追加多行
> info_list = [
> ['Tom',13,'1008'],
> ['Bob',10,'1005'],
> ['小花',11,'1003'],
> ['Jack',12,'1007'],
> ['小花2',15,'1009'],
> ['小花1',17,'1006'],
> ['小花3',12,'1004']
> ]
> for info in info_list:
>     user_sheet.append(info)
> 
> # 7.保存工作簿
> workbook.save(r'data/演示写入操作.xlsx')
> ```

#### 4.练习

> ```Python
> import  openpyxl
> 
> # 练习一：获取student-score.xlsx中的'成绩表'中涉及哪几个学校，总共有多少个学校
> wb = openpyxl.load_workbook(r'data/student-score.xlsx')
> # print(wb.sheetnames)
> sheet = wb['成绩表']
> # 获取c列
> c_col = sheet['C'][2:]
> # print(c_col)
> school_names = set([cell.value for cell in c_col])
> print(f'总共涉及到{len(school_names)}个学校，分别是{school_names}')
> 
> # 练习二：处理 练习数据.xlsx 文件中的数据，将日期和成交量拆分，保存到一个新的工作簿中，日期和成交量显示两列
> wb1 = openpyxl.load_workbook(r'data/练习数据.xlsx')
> sheet1 = wb1.active
> a_col = sheet1['A']
> print(a_col)
> # 整理数据
> data_list = []
> for cell in a_col:
>     value = cell.value
>     date_num_list = value.split(';')
>     print(date_num_list)
>     for date_num in date_num_list:
>         sublist = date_num.strip().split(":")
>         if len(sublist) == 2:
>             sublist[1] = sublist[1].strip()
>         data_list.append(sublist)
> print(data_list)
> 
> # 写入
> wb2 = openpyxl.Workbook()
> sheet2 = wb2.active
> sheet2.title = '处理结果'
> sheet2.append(['日期','成交量'])
> for data in data_list:
>     sheet2.append(data)
> 
> wb2.save(r'data/练习数据-处理结果.xlsx')
> ```

#### 5.其他扩展【了解】

> ```Python
> from openpyxl import  load_workbook
> from openpyxl.styles import Font   # 设置字体样式
> from openpyxl.styles import  Side,Border  # 设置边框样式
> from openpyxl.styles import  PatternFill,GradientFill  # 设置背景颜色
> from openpyxl.styles import  Alignment  # 设置对齐方式
> 
> # 1.将公式写入到单元格保存
> wb = load_workbook(r'data/student-score1.xlsx')
> sheet = wb['成绩表']
> 
> # 计算成绩和
> sheet['I2'] = '总分'
> # 注意：和excel中公式的写法一模一样，只需要给定字符串即可
> # sheet['I3'] = '=sum(D3:H3)'
> # print(sheet.max_row)
> 
> # 求所有学生的总分
> for row in range(3,sheet.max_row):
>     sheet[f'I{row}'] = f'=sum(D{row}:H{row})'
> # 保存
> wb.save(r'data/student-score1.xlsx')
> 
> # 2.设置单个单元格的字体样式
> wb = load_workbook(r'data/student-score1.xlsx')
> sheet = wb['成绩表']
> 
> cell = sheet['C5']
> print(cell.font)
> # name='Arial', charset=134, family=None, b=False, i=False, strike=None, outline=None, shadow=None, condense=None, color=None, extend=None, sz=10.0, u=None, vertAlign=None, scheme=None
> 
> # 创建字体对象
> # font = Font(name='黑体',size=20,bold=True,italic=True,color='66CCFF')  # 颜色只能使用rgb的十六进制表示
> # 对一个单元格设置字体样式
> # cell.font = font
> 
> # 对多个单元格设置字体样式
> font = Font(name='黑体',size=15,bold=True,italic=True,color='FF66FF')
> cells = sheet[2]
> for cell in cells:
>     cell.font = font
> 
> # 保存
> wb.save(r'data/student-score1.xlsx')
> 
> # 3.设置边框样式
> wb = load_workbook(r'data/student-score1.xlsx')
> sheet = wb['成绩表']
> 
> # 创建线条对象
> side = Side(border_style='double',color='FFCC00')
> # 创建边框对象
> border = Border(left=side,right=side,top=side,bottom=side)
> cells = sheet[2]
> for cell in cells:
>     cell.border = border
> # 保存
> wb.save(r'data/student-score1.xlsx')
> 
> # 4.设置其他样式
> wb = load_workbook(r'data/student-score1.xlsx')
> sheet = wb['成绩表']
> # a.设置单元格背景色
> pattern_fill = PatternFill(fill_type='solid',fgColor='FF6666')
> gradient_fill = GradientFill(stop=('FFFFFF','FF3333','000000'))    # 渐变色
> 
> # 设置第3行的背景色
> cells = sheet[3]
> for cell in cells:
>     cell.fill = pattern_fill
> 
> # 设置第4行的背景色
> cells = sheet[5]
> for cell in cells:
>     cell.fill = gradient_fill
> 
> # b.设置文本居中
> # horizontal表示水平方向，常用的left center right
> # vertical表示垂直方向，常用的top  center  bottom
> alignment = Alignment(horizontal='center',vertical='center')
> cells = sheet[6]
> for cell in cells:
>     cell.alignment = alignment
> 
> # c.设置行高和列高
> print(sheet.row_dimensions)  # 字典
> # for r in sheet.row_dimensions:
> #     print(r)
> 
> # 将第1行的行高设置为30
> sheet.row_dimensions[8].height = 30
> 
> # 设置第C列的列宽为30
> sheet.column_dimensions['C'].width = 30
> 
> # 保存
> wb.save(r'data/student-score1.xlsx')
> ```

### 四、pandas操作Excel文件

> ```Python
> # pandas可以从各种文件格式比如：csv,json,sql,excel导入数据
> import pandas as pd
> from pandas import  DataFrame
> 
> # 1.创建按DataFrame的对象
> data = {
>     'address':['SZ','SH','BJ'],
>     'number':[1,2,3]
> }
> 
> df = DataFrame(data)
> print(df)
> 
> # 2.读取excel文件
> # 注意：pd.read_excel()底层会依赖于openpyxl，如果版本低，则需要进行更新
> '''
> 更新库的两种方式
> 方式一：
>     pip uninstall openpyxl
>     pip install openpyxl
> 方式二：
>     pip install openpyxl --upgrade --user
>     
> pip install xxx默认安装的就是最新版本
> pip install xxx=2.1.0安装指定的版本
> '''
> df = pd.read_excel(r'data/student-score.xlsx',sheet_name='第3小学')
> print(df)
> 
> # df.head(n),如果n省略，查看前5行数据，如果n指定，则查看前n行数据
> print(df.head())
> # df.tail(n),如果n省略，查看后5行数据，如果n指定，则查看后n行数据
> print(df.tail())
> 
> print(df.columns)
> print(df.index)
> 
> # 获取指定列
> print(df['语文'])
> 
> # 描述数据
> print(df.describe())
> 
> # 3.写入
> # df.to_excel()
> # data = {
> #     'name':['aa','bb','cc'],
> #     'age':[32,5,7],
> #     'gender':['male','female','male']
> # }
> # df = DataFrame(data)
> # df.to_excel(r'data/new.xlsx')
> 
> 
> # 4.获取行或列的数据
> # a.获取指定的某一行数据
> row = df.loc[0].values
> print(row)
> # b.获取指定的多行数据
> rows = df.loc[[0,1]].values
> print(rows)
> ```

