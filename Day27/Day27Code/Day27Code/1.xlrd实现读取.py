import xlrd

# 处理流程：工作簿----》工作表----》单元格【坐标：行 列】

# 1.打开xls文件，得到一个工作簿对象workbook
workbook = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')

# 2.获取工作簿中的工作表名称
sheetnames = workbook.sheet_names()
print(sheetnames)

# 3.获取工作表对象sheet
# 方式一：根据名称获取
sheet1 = workbook.sheet_by_name('股票数据')
print(sheet1)
# 方式二：根据索引获取
sheet2 = workbook.sheet_by_index(2)
print(sheet2)

# 4.获取单元格对象cell
'''
xlrd和xlwt中
row:
    Excel: 1 2 3 4 5 6.....
    Python:0 1 2 3 4 5....
col:
    Excel: A B C D....
    Python:0 1 2 3....
'''
# sheet.cell(row,col):获取某行某列处的单元格对象
# 需求1：获取A1
cell1 = sheet1.cell(0,0)
print(cell1)
# 需求2：获取D3
cell2 = sheet1.cell(2,3)
print(cell2)

print(type(cell1))

# 5.获取某行的某几列数据
# a.sheet.row_values(row,col1,col2):前闭后开区间，返回一个列表，其中的元素是数据字符串，col1和col2可以省略
# 需求1：获取第0行的数据
print(sheet1.row_values(0))

# 需求2：获取第0行的第0~3列
print(sheet1.row_values(0,0,4))

# slice:切片
# b.sheet.row_slice(row,col1,col2)：前闭后开区间，返回一个列表，其中的元素是单元格对象
print(sheet1.row_slice(0))
print(sheet1.row_slice(0,0,4))

# 练习：读取阿里巴巴的数据，将其中的日期数据格式化为年月日，将小数保留小数点后3位
workbook = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')
sheet = workbook.sheet_by_name('股票数据')
# 获取工作表中的总行数和总列数
print(sheet.nrows,sheet.ncols)  # 255 7
# 遍历工作表
for row in range(sheet.nrows):   # 遍历行
    for col in range(sheet.ncols):  # 遍历列
        # 获取每个单元格对象
        cell = sheet.cell(row,col)
        # 获取单元格的值
        value = cell.value
        # print(value)
        if row > 0:  # row为0的时候为表头，不作任何处理
            if col == 0:
                # 对日期进行格式化
                # xldate_as_tuple(日期数据，0/1)将日期数据转化为元组形式
                # 0：以1900-1-1为基准的日期  1：1904-1-1为基准的日期
                date_tuple = xlrd.xldate_as_tuple(value,0)
                new_value = '%d年-%.2d月-%.2d日' % (date_tuple[0],date_tuple[1],date_tuple[2])
                print(new_value)
            else:
                # 对数字进行格式化
                new_value = '%.3f' % (value)
                print(new_value)

