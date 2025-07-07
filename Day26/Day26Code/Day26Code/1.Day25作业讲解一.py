# 1.邮编查询，读取 youbian.txt 文件中的数据， 完成邮编查询的操作，从控制台输入邮编号，
# 如果有此邮编，请输出对应的城市，否则提示无此邮编

def read_data():
    # 读取已知文件
    with open(r'data/youbian.txt', 'r', encoding='utf-8') as f:
        data_list = f.readlines()
    return  data_list

# 方式一：切片
def get_city1(code):
    data_list = read_data()
    # 查询
    for data in data_list:
        if code == data[1:7]:
            print(f'邮编{code}对应的地区为：{data[9:-4]}')   # start和end不同的符号，以start为准
            break
    else:
        print('无此邮编')

# 方式二：eval()
def get_city2(code):
    data_list = read_data()
    # 查询
    for data in data_list:
        # data  [610202,"陕西省铜川市城区"],\n ----->[610202,"陕西省铜川市城区"]
        # a.切片实现
        # new_data = data[:-2]
        # b.rstrip()
        new_data = data.rstrip(',\n')

        # 通过eval将上述形似列表的字符串识别并转化
        info_list = eval(new_data)

        if str(info_list[0]) == code:
            print(f'邮编{code}对应的地区为：{info_list[1]}')
            break
    else:
        print('无此邮编')

# 2.将一个英文语句以单词为单位逆序排放到指定的文件中
def reverse_data(data):
    data_list = data.split(' ')
    data_list.reverse()
    new_data = ' '.join(data_list)
    with open(r'data/words.txt','w',encoding='utf-8') as f:
        f.write(new_data)
        f.flush()

if __name__ == '__main__':
    # code = input('请输入需要查询的邮编：')
    # get_city2(code)

    data = input('请输入一个英文句子：')
    reverse_data(data)

