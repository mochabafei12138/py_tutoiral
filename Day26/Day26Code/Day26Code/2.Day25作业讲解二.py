# 3.开房查询，从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，
# 如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中
# a.读取已知文件中的数据
def read_data():
    with open(r'data/kaifanglist.txt','r',encoding='utf-8') as f:
        all_list = f.readlines()
    return all_list

# b.查询
# 思路：根据指定的姓名查询数据，如果存在，则将数据单独保存到一个新的列表
def search_data(name):
    single_list = []
    all_list = read_data()
    for row in all_list:
        if name == row.split(',')[0]:
            single_list.append(row)
    write_data(single_list,name)

# c.将查询后的结果写入到指定文件中
def write_data(single_list,name):
    if single_list:
        print(f'{name}果然去了~~~~~')
        des_path = rf'data/{name}.txt'
        # 如果是多次open，为了不丢失原数据，建议使用a，但是如果文件只open一次，循环写入，w也是可以的
        with open(des_path,'w',encoding='utf-8') as f:
            for row in single_list:
                f.write(row)
                f.flush()
    else:
        print(f'未查到{name}的信息')

if __name__ == '__main__':
    name = input('请输入需要查询的人的姓名：')
    search_data(name)