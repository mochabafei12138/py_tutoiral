import PyPDF2

# 1.创建reader和writer对象
src_reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
water_reader = PyPDF2.PdfReader(r'data/watermark.pdf')
writer = PyPDF2.PdfWriter()

# 2.遍历已知文件的每一页对象，和水印页进行合并，最终将合并之后的结果添加到writer中
water_page = water_reader.pages[0]  # 获取水印页对象
for i in range(len(src_reader.pages)):
    src_page = src_reader.pages[i]  # 获取原文件每一页的对象
    # 合并
    # a.merge_page(b):将b合并到a上
    src_page.merge_page(water_page)   # *****
    # 将合并之后的对象添加给writer
    writer.add_page(src_page)

with open(r'data/XGBoost-添加水印.pdf','wb') as f:
    writer.write(f)