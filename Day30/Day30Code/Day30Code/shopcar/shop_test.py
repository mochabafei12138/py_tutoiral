
from operation import Operation

def main():
    op = Operation()
    print('欢迎进入xxx自助购物系统'.center(40,'*'))
    while True:
        print('''本系统提供了如下功能：
        0.用户注册
        1.用户登录
        2.添加商品
        3.删除商品
        4.结算购物车
        5.注销登录
        6.退出系统''')

        select = input('请输入需要进行的操作：')
        if select == '0':
            op.user_register()
        elif select == '1':
            op.user_login()
        elif select == '2':
            op.add_goods()
        elif select == '3':
            op.del_goods()
        elif select == '4':
            op.get_total()
        elif select == '5':
            op.user_quit()
        elif select == '6':
            print('欢迎再次使用')
            break
        
if __name__ == '__main__':
    main()