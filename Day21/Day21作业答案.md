```Python
'''
1.有一个银行账户类 Account, 包括名字 , 余额等属性，方法有存钱、取钱、查询余额的操作。要求：
	a.在存钱时，注意存款数据的格式
	b.取钱时，要判断余额是否充足，余额不够的时候要提示余额不足
'''
class Account():
    __slots__ = ('name','__balance')
    def __init__(self,name,balance):
        self.name = name
        # 结合实际情况，银行卡余额不是随便可以访问的
        self.__balance = balance
    def save_money(self,money):
        if money < 0:
            money = -money
        self.__balance += money
        print(f'存了{money}元')
        self.show_balance()

    def get_money(self,money):
        if money > self.__balance:
            print('余额不足')
        else:
            self.__balance -= money
            print(f'取走{money}元')
            self.show_balance()

    def show_balance(self):
        print(f'当前余额为：{self.__balance}')

def main():
    a = Account('xxxx', 1000)
    print(f'欢迎进入{a.name}的账户操作界面'.center(40, '*'))
    while True:
        print('''可以进行如下功能：
            0.存钱
            1.取钱
            2.查询余额
            3.退出''')
        select = input('请输入需要进行的操作：')
        if select == '0':
            num = int(input('请输入需要存的钱数：'))
            a.save_money(num)
        elif select == '1':
            num = int(input('请输入需要取的钱数：'))
            a.get_money(num)
        elif select == '2':
            a.show_balance()
        elif select == '3':
            break

# if __name__ == '__main__':
#     main()


'''
2.家具类(HouseItem) 有 名字 和 占地面积属性，其中
    - 席梦思(bed) 占地 4 平米
    - 衣柜(chest) 占地 2 平米
    - 餐桌(table) 占地 1.5 平米

房子类(House) 有 户型、总面积 、剩余面积 和 家具名称列表 属性
    - 新房子没有任何的家具
    - 将 家具的名称 追加到 家具名称列表 中
    - 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具

a.将以上三件 家具对象 添加 到 房子对象 中
b.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
使用面向对象思想，编码完成上述功能。
'''
class HouseItem():
    __slots__ =  ('name','area')
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __repr__(self):
        return f'家具名称：{self.name}'
class House():
    __slots__ = ('kind','total_area','free_area','houseitem_list')
    def __init__(self,kind,total_area,free_area):
        self.kind = kind
        self.total_area = total_area
        self.free_area = free_area
        self.houseitem_list = []
    def add_item(self,item):
        if item.area > self.free_area:
            print('剩余面积不足，无法添加')
        else:
            # self.houseitem_list.append(item.name)  # 添加的是家具的名称
            self.houseitem_list.append(item)   # 添加的是家具的对象
            self.free_area -= item.area
    def __repr__(self):
        return f'{self.houseitem_list}'

if __name__ == '__main__':
    bed = HouseItem('席梦思',4)
    chest = HouseItem('沙发',3)
    table = HouseItem('餐桌',1.5)

    house = House('四室两厅两卫',160,120)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)


```

