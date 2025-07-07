# 注意：安装：pypdf2     导入:PyPDF2
import PyPDF2

# 1.读取pdf文件中的文本内容
# a.获取reader对象
reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
# b.获取指定页的字典
print(reader.pages)   # 列表，其中的元素是字典
page = reader.pages[0]
print(page)
# c.获取指定页的文本内容
# 废弃的函数
# text = page.extractText()
# print(text)
# 更新之后的函数
text = page.extract_text()    # *****
print(text)
'''
PyPDF2.errors.DeprecationError: extractText is deprecated废弃 and was removed in PyPDF2 3.0.0. Use extract_text instead.
'''

# 2.加密pdf文件
# a.创建writer对象
writer = PyPDF2.PdfWriter()
# b.获取已知文件中的每一页，添加到新的文件对象中去
for i in range(len(reader.pages)):
    page = reader.pages[i]
    writer.add_page(page)
# c.设置加密
writer.encrypt('abc123')    # *******

# d.保存文件
with open(r'data/XGBoost-加密.pdf','wb') as f:
    writer.write(f)   # 注意和f.write()区别，f.write()只能传参字符串

