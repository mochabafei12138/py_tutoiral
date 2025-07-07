# 1.
lst = []
#  在lst列表中依次追加10个数值[8, 93, 66, 83, 100, 95, 77, 93, 85, 98]
sublist = [8, 93, 66, 83, 100, 95, 77, 93, 85, 98]
# lst.append(sublist)
# print(lst)  # [[8, 93, 66, 83, 100, 95, 77, 93, 85, 98]]

# for num in sublist:
#     lst.append(num)
# print(lst)

lst.extend(sublist)   # 打碎加入
print(lst)  # [8, 93, 66, 83, 100, 95, 77, 93, 85, 98]

# 2.
# a. 生成一个存放1-100之间个位数为3的数据列表
list_a = [n for n in range(1,101) if n % 10 == 3]
print(list_a)

# b. 利用列表推导式将已知列表中的整数提取出来
list_b = [True, 17, "hello", "bye", 98, 34, 21]
new_list_b = [ele for ele in list_b if type(ele) == int]
print(new_list_b)

# c.利用列表推导式存放指定列表中字符串的长度
list_c =  ["good", "nice", "see you", "bye"]
# len()
new_list_c = [len(s) for s in list_c]
print(new_list_c)

# d.生成一个列表，其中的元素为'0-1'，'1-2'，'2-3'，'3-4'，'4-5'
list_d1 = [str(n) + '-' + str(n + 1) for n in range(5)]
print(list_d1)
list_d2 = [f'{n}-{n + 1}' for n in range(5)]
print(list_d2)

# 3.根据products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号,
# 就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。注意：本题可以自由发挥
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
# print('============','欢迎进入xxx自助购物超市','============')
# 扩展：xxx.center(width,ch):将xxx字符串居中显示，两端用ch填充，最终字符串的长度为width
print('欢迎进入xxx自助购物超市'.center(50,'='))
# 购物车
shop_car = []
while True:
    print('商品信息如下：')
    for i,pro in enumerate(products):
        print(f'    编号{i}:名称：{pro[0]},价格:{pro[1]}')
    # 询问用户想买什么，用户选择一个商品编号
    choice = input('请输入需要购买的商品的编号【输入q退出】：')
    # 扩展：
    '''
    xxx.lower():将xxx字符串转化为小写
    xxx.upper():将xxx字符串转化为大写
    print('ffaa'.lower())  # 'ffaa'
    print('HFRDggq'.lower())  # hfrdggg
    '''
    # if choice == 'q' or choice == 'Q':
    if choice.lower() == 'q':
        print('购买完毕，退出系统')
        break
    if choice.isdigit():
        choice = int(choice)
        if choice in range(len(products)):
            # 添加到购物车
            shop_car.append(products[choice])
            print('添加成功!')
        else:
            print('暂无此商品')
    else:
        print('输入有误')
if shop_car:
    print(f'购物车列表为：{shop_car}')
else:
    print('没有购买任何商品')

