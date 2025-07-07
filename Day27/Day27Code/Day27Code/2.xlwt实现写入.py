import xlwt,random,xlrd

# 1.创建工作簿对象
workbook = xlwt.Workbook()

# 2.向工作簿中添加工作表对象
sheet = workbook.add_sheet('千锋学员成绩表')

# 3.准备数据
stu_names = ['张三','李四','王五','小明','小花']  # 作为第0列的数据
subjects = ['姓名','语文','数学','英语','Python']    # 作为第0行的数据
scores = [[random.randint(40,100) for i in range(len(subjects) - 1)] for j in range(len(stu_names))]
print(scores)
# [[70, 58, 64, 60], [81, 75, 61, 77], [47, 67, 48, 43], [74, 48, 88, 68], [43, 59, 59, 85]]

# 4.写入数据
# 注意：写入数据的时候，文件一定要处于关闭状态，如果打开，执行写入操作，则PermissionError: [Errno 13] Permission denied: 'data/2024千锋成绩表.xls'
# sheet.write(row,col,value)
# a.写入第0行
for index,value in enumerate(subjects):
    sheet.write(0,index,value)
# b.写入第0列
for index,value in enumerate(stu_names):
    sheet.write(index + 1,0,value)
# c.写入成绩
for row in range(len(scores)):
    for col in range(len(scores[row])):
        # 从第1行第1列开始操作起
        sheet.write(row + 1,col + 1,scores[row][col])

# 5.保存工作簿
workbook.save(r'data/2024千锋成绩表.xls')


# 练习：读取阿里巴巴的数据，将其中的日期数据格式化为年月日，将小数保留小数点后3位，并将新的数据存储到一个新的工作簿中
# 获取已知的工作簿和工作表
workbook = xlrd.open_workbook(r'data/阿里巴巴2020年股票数据.xls')
sheet = workbook.sheet_by_name('股票数据')

# 创建新的工作簿和工作表
new_workbook = xlwt.Workbook()
new_sheet = new_workbook.add_sheet('新股票数据')

# 获取工作表中的总行数和总列数
print(sheet.nrows,sheet.ncols)  # 255 7
# 遍历工作表
for row in range(sheet.nrows):   # 遍历行
    for col in range(sheet.ncols):  # 遍历列
        # 获取每个单元格对象
        cell = sheet.cell(row,col)
        # 获取单元格的值
        value = cell.value

        if row == 0:  # row为0的时候为表头，不作任何处理
            new_value = value
        else:
            sub_value = ''
            if col == 0:
                # 对日期进行格式化
                # xldate_as_tuple(日期数据，0/1)将日期数据转化为元组形式
                # 0：以1900-1-1为基准的日期  1：1904-1-1为基准的日期
                date_tuple = xlrd.xldate_as_tuple(value,0)
                sub_value = '%d年-%.2d月-%.2d日' % (date_tuple[0],date_tuple[1],date_tuple[2])
            else:
                # 对数字进行格式化
                sub_value = '%.3f' % (value)
            new_value = sub_value

        # 将处理之后的新数据写入到新的工作表中
        new_sheet.write(row,col,new_value)

# 保存新的工作簿
new_workbook.save(r'data/处理结果-阿里巴巴.xls')