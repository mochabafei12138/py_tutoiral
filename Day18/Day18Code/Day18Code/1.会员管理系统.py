import  random

# 定义列表，存储会员信息
users_list = []
# [{},{}......]

# 一、封装函数
def get_mid():
    while True:
        mid = str(random.randint(10000,99999))   # 后期查询的时候，从控制台输入会员号无需转化
        if mid not in [dic['mid'] for dic in users_list]:
            return mid
def add_user(name,sex,age):
    mid = get_mid()
    print(f'你的会员号是:{mid}')
    users_list.append(dict(zip(['mid','name','sex','age'],[mid,name,sex,age])))
    print('添加成功！')
def del_user(mid):
    # 注意：如果确定列表中的元素是唯一的，则删除可以不做拷贝处理，如果要删除的元素在2个及以上，则需要拷贝
    for user in users_list:
        if user['mid'] == mid:
            users_list.remove(user)
            print('删除成功')
            break
    else:
        print('会员信息不存在')
def show_user(mid):
    for user in users_list:
        if user['mid'] == mid:
            print(user)
            break
    else:
        print('会员信息不存在')
def sort_user():
    #  方式一
    # users_list.sort(key=lambda dic:dic['age'],reverse=True)
    # print(users_list)
    # 方式二
    new_list = sorted(users_list,key=lambda dic:dic['age'],reverse=True)
    print(new_list)

# 二、调用函数
def main():
    print('管理员登录界面'.center(50, '*'))
    for i in range(3):
        # 引导输入管理员的用户名和密码
        admin_name = input('请输入管理员的用户名:')
        admin_pwd = input('请输入管理员的密码：')
        if admin_name == 'admin' and admin_pwd == 'admin':
            print('管理员登录成功！')
            print('欢迎进入xxx会员管理系统')
            # 进入管理系统
            # 因为进入管理系统之后，具体要做哪些操作，进行几次操作不确定
            while True:
                print('''********操作目录**********
                        1.添加会员信息
                        2.删除会员信息
                        3.查看会员信息
                        4.对会员信息排序
                        5.退出''')
                # 引导管理员执行相应的操作
                choice = input('请输入需要执行的操作：')
                if choice == '1':
                    print('添加会员信息'.center(50, '*'))
                    name = input('请输入会员名：')
                    sex = input('请输入会员性别：')
                    age = int(input('请输入会员年龄：'))
                    add_user(name, sex, age)
                elif choice == '2':
                    print('删除会员信息'.center(50, '*'))
                    mid = input('请输入需要删除的会员号：')
                    del_user(mid)
                elif choice == '3':
                    print('查看会员信息'.center(50, '*'))
                    mid = input('请输入需要查找的会员号：')
                    show_user(mid)
                elif choice == '4':
                    print('对会员信息排序'.center(50, '*'))
                    sort_user()
                elif choice == '5':
                    print('欢迎再次使用')
                    # 此处的break结束的是while死循环
                    break  # 扩展：此处的break可以替换为exit()，表示退出程序
                    # exit()
                else:
                    print('输入有误，暂无此操作，请输入正确的操作编号')
            # 此处的break结束的是for循环
            break
        else:
            if i == 2:
                continue
            print('管理员登录失败,请重新输入')
    else:
        print('已经错误三次，禁止管理员登录')

main()