# pandas可以从各种文件格式比如：csv,json,sql,excel导入数据
import pandas as pd
from pandas import  DataFrame

# 1.创建按DataFrame的对象
data = {
    'address':['SZ','SH','BJ'],
    'number':[1,2,3]
}

df = DataFrame(data)
print(df)

# 2.读取excel文件
# 注意：pd.read_excel()底层会依赖于openpyxl，如果版本低，则需要进行更新
'''
更新库的两种方式
方式一：
    pip uninstall openpyxl
    pip install openpyxl
方式二：
    pip install openpyxl --upgrade --user
    
pip install xxx默认安装的就是最新版本
pip install xxx=2.1.0安装指定的版本
'''
df = pd.read_excel(r'data/student-score.xlsx',sheet_name='第3小学')
print(df)

# df.head(n),如果n省略，查看前5行数据，如果n指定，则查看前n行数据
print(df.head())
# df.tail(n),如果n省略，查看后5行数据，如果n指定，则查看后n行数据
print(df.tail())

print(df.columns)
print(df.index)

# 获取指定列
print(df['语文'])

# 描述数据
print(df.describe())

# 3.写入
# df.to_excel()
# data = {
#     'name':['aa','bb','cc'],
#     'age':[32,5,7],
#     'gender':['male','female','male']
# }
# df = DataFrame(data)
# df.to_excel(r'data/new.xlsx')


# 4.获取行或列的数据
# a.获取指定的某一行数据
row = df.loc[0].values
print(row)
# b.获取指定的多行数据
rows = df.loc[[0,1]].values
print(rows)

