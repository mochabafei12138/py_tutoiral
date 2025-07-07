import  csv

# 一、读取csv文件
with open(r'aaa/b1.csv','r',encoding='utf-8') as f1:
    # reader(iterable)----->iterator
    reader = csv.reader(f1)
    # for row in reader:
    #     print(row)
    datalist = list(reader)
    print(datalist)

# 二、写入csv文件
datalist = [['name', 'age', 'address'], ['zhangsan', '10', '上海'], ['lisi', '20', '北京'], ['wangwu', '19', '深圳'], ['xiaoming', '18', '成都']]
# 如果在写入内容之后，发现每行内容的后面莫名其妙的出现了一个空行，则可以通过newline解决
with open(r'aaa/b2.csv','w',encoding='utf-8',newline='') as f2:
    writer = csv.writer(f2)

    # 方式一：通过遍历的方式，逐行写入
    # for data in datalist:
    #     writer.writerow(data)

    # 方式二：一次性写入多行
    writer.writerows(datalist)

