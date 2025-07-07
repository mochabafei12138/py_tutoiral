'''
后台管理员管理前台会员信息系统

1. 后台管理员只有一个用户: admin, 密码: admin
2. 当管理员登陆成功后， 可以管理前台会员信息.
3. 会员信息管理包含:
      添加会员信息
      删除会员信息
      查看会员信息
      退出
'''
# 定义列表，存储会员信息
users_list = []
# [[会员名称，会员密码]，]

print('管理员登录界面'.center(50,'*'))
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
                    4.退出''')
            # 引导管理员执行相应的操作
            choice = input('请输入需要执行的操作：')
            if choice == '1':
                print('添加会员信息'.center(50,'*'))
                user_name = input('请输入会员名：')
                user_pwd = input('请输入会员密码：')
                users_list.append([user_name,user_pwd])
                print('添加成功！')
            elif choice == '2':
                print('删除会员信息'.center(50,'*'))
                user_name = input('请输入需要删除的会员名：')
                # 设定：如果查找到会员信息，只删除一个【其他的同名的会员信息不做处理】
                for user in users_list:
                    if user[0] == user_name:
                        users_list.remove(user)
                        print('删除成功')
                        break
                else:
                    print('会员信息不存在')
            elif choice == '3':
                print('查看会员信息'.center(50, '*'))
                for user in users_list:
                    print(f'会员名：{user[0]},密码:{user[1]}')
            elif choice == '4':
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
