import  PyPDF2

# 1.旋转
# a.创建reader和writer对象
reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
writer = PyPDF2.PdfWriter()

# b.旋转
# 需求1：将第0页顺时针旋转180
# page_0 = reader.pages[0]
# # page_0.rotate(angle),angle为正数：顺时针旋转   angle为负数：逆时针旋转
# page_0.rotate(-90)
# writer.add_page(page_0)

# 需求2：批量旋转
for i in range(len(reader.pages)):
    page = reader.pages[i]
    if i % 2 == 0:
        page.rotate(90)     # ******
    else:
        page.rotate(-90)
    writer.add_page(page)

# c.添加空白pdf
writer.add_blank_page()

# 注意：如果打开新生成的文件，报错文件损坏，则可能是writer是空的
with open(r'data/XGBoost-旋转.pdf','wb') as f:
    writer.write(f)
