# 4.写出下面代码的输出结果并说明原因
list1 = ['a', 'b', 'c', 'd', 'e']
# 注意：只要符合切片的语法，不会报错，比如列表。返回的结果无非就是空和非空的区别
print(list1[10:])   # []

# 5.写出下面代码的输出结果并说明原因
str1 = 'hello python'
str1.title()
# 注意：字符串是不可变的数据类型，所以但凡调用了字符串更改的函数，返回一个新的字符串，对原字符串没有任何影响
print(str1)  # hello python

str1 = 'hello python'
str1 = str1.title()
# 如果调用了字符串的函数，并对原变量进行了重新赋值，结果就是函数的返回值
print(str1)  # Hello Python

# 8.在控制台中录入，所有学生名字，如果姓名重复，则提示"姓名已经存在"，不添加到列表中，如果录入空字符串，则倒序打印所有学生
stus_list = []
def func():
    while True:
        name = input('请输入学生的名字【无任何输入则退出】：')   # '':空字符串  ' '：非空字符串
        if not name:
            stus_list.reverse()
            print(stus_list)
            break

        if name in stus_list:
            print('姓名已经存在')
        else:
            stus_list.append(name)
func()


# 10.有如下商品价格：568，239，368，425，121，219，834，1263，26，请输入随意一个价格区间进行商品的筛选，
# 并能够对筛选出的商品进行从大到小和从小到大进行排序，并求出这个区间的商品的平均价格
price_list = [568,239,368,425,121,219,834,1263,26]
min_price,max_price = eval(input('请输入两个数字表示价格区间：'))
result_list = []
for price in price_list:
    if price in range(min_price,max_price):
        result_list.append(price)

if result_list:
    new_list = result_list.copy()
    # 升序
    new_list.sort()
    print(new_list)

    # 降序
    new_list.reverse()  # new_list.sort(reverse=True)
    print(new_list)

    # 平均价格
    avg_price = sum(result_list) / len(result_list)
else:
    print('没有符合给定区间的价格数据')
