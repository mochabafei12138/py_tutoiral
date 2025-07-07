1.邮编查询，读取 youbian.txt 文件中的数据， 完成邮编查询的操作，从控制台输入邮编号，如果有此邮编，请输出对应的城市，否则提示无此邮编

```Python
"""
2.邮编查询，读取 youbian.txt 文件中的数据， 完成邮编查询的操作，
从控制台输入邮编号，如果有此邮编，请输出对应的城市，否则提示无此邮编
"""

path = r"youbian.txt"

# 方式一：切片
def get_city1(code):
    with open(path,"r",encoding="utf-8") as f:
        data_list = f.readlines()
        # print(data_list)
    # 遍历列表，查询
    for data in data_list:
        # ==：精确匹配   in：模糊匹配
        if data[1:7] == code:
            print(f"{code}存在，对应的城市为:{data[9:-4]}")
            break
    else:
        print(f"{code}不存在")

# 方式二:eval()
def get_city2(code):
    with open(path,"r",encoding="utf-8") as f:
        data_list = f.readlines()
        print(data_list)
    for data in data_list:
        info_list = eval(data.rstrip(",\n"))
        if str(info_list[0]) == code:
            print(f"{code}存在，对应的城市为:{info_list[1]}")
            break
    else:
        print(f"{code}不存在")

if __name__ == '__main__':
    code = input("请输入邮编：")
    get_city2(code)
```

2.将一个英文语句以单词为单位逆序排放到指定的文件中

```
例如：“I am a boy” 逆序排放后 "boy a am I" 将其写入到指定的文件中
```

```Python
"""
将一个英文语句以单词为单位逆序排放到指定的文件中
思路：1. 单词之间是以空格为分割的 所以按照空格分割 获取所有的单词
        2.分割之后是将数据存放于列表中的 将列表中的数据反转
        3.将反转的列表 使用 空格拼接在一起 然后写入到文件中
"""
sentence = input("请输入一段英文语句：")
# 对其进行切割
word_list = sentence.split() # 不传参默认以空字符序列为分割
print(word_list)
# 对列表进行反转
word_list.reverse()
# 将其拼接成 新的语句
new_sentence = " ".join(word_list)
# 打开文件 向里面写内容
file_handle = open("word.txt", "w", encoding="utf-8")
file_handle.write(new_sentence)
file_handle.flush() # 刷新
file_handle.close()
```

3.开房查询，从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中

```Python
"""
3.开房查询，
从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，
如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中
"""

# 一、封装函数
def read_data():
    # 拼接路径
    file_path = r'data/kaifanglist.txt'
    # 读取原文件中的数据
    src_file = open(file_path,'r',encoding='utf-8')
    alllist = src_file.readlines()
    src_file.close()
    return  alllist

# 查询指定人员的数据
def search_data(name):
    alllist = read_data()
    singlelist = []
    for line in alllist:
        infolist = line.split(',')
        if infolist[0] == name:
            singlelist.append(line)
    write_data(singlelist,name)

def write_data(singlelist,name):
    if singlelist:
        print(f"{name}果然去开房了~~~")
        # 查询到了数据
        des_path = f"data/{name}.txt"
        des_file = open(des_path,'w',encoding='utf-8')
        for line in singlelist:
            des_file.write(line)
            des_file.flush()
        des_file.close()
        print(f'{name}的数据提取成功')
    else:
        # 未查询到数据
        print(f"未查询到{name}相关的数据，{name}是一个好哥们")

# 二、调用函数
if __name__ == '__main__':
    name = input("请输入需要查询的人员的姓名：")
    search_data(name)
```







