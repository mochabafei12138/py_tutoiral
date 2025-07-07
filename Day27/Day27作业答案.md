将多个内容一致的Excel文件合并到一个Excel文件中

小宝剑大药房（高新店）2018年销售数据.xlsx
小宝剑大药房（犀浦店）2018年销售数据.xlsx
小宝剑大药房（新津店）2018年销售数据.xlsx

```Python
# 方式一
import  openpyxl,os
# 获取数据，然后整合数据
result_list = []
header_list = []
def read_data(xlpath):
 # old_wb = openpyxl.load_workbook(fr'data/小宝剑大药房（{xlname}）2018年销售数据.xlsx')
 old_wb = openpyxl.load_workbook(xlpath)  # xlpath表示文件路径
 old_sheet = old_wb.active
 global  header_list
 header_list = [cell.value for cell in old_sheet[2]]
 for row in range(3,old_sheet.max_row + 1):
     sublist = [cell.value for cell in old_sheet[row] if cell.value != None]
     if sublist:
         result_list.append(sublist)

# 写入数据
def write_data():
 new_wb = openpyxl.Workbook()
 new_sheet = new_wb.active
 new_sheet.title = '药店汇总数据'
 # 写入表头
 new_sheet.append(header_list)
 # 写入正文
 for row in result_list:
     new_sheet.append(row)

 # 保存
 new_wb.save(r'data/药店汇总数据.xlsx')

if __name__ == '__main__':
 # 文件较少的情况，可以手动书写
 # xlnames_list = ['高新店','犀浦店','新津店']
 # 文件较多，则借助于os/glob模块
 '''
 import glob
 xlnames_list = glob.glob('data/*.xlsx')
 for xlname in xlnames_list:
     read_data(xlname)
 '''
 path = r'data'
 xlnames_list = os.listdir(path)
 for xlname in xlnames_list:
     filepath = os.path.join(path,xlname)
     read_data(filepath)
 write_data()
```

