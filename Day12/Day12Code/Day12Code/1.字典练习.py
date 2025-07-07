'''
写一个学生作业情况录入并查询的小程序
a.录入学生作业情况：字典添加
b.查看学生作业情况：字典查询
c.录入时允许输入3次，3次输入不正确提示失败次数过多，禁止继续录入
'''
# 格式
homeworks = {
    'tom':{'2020.1.1':'未交','2021.1.8':'已交'},
    'bob':{'2020.1.1':'未交','2021.1.8':'未交'}
}
choice = {'1':'查询','2':'录入'}
while True:
    user_choice = input('请输入你的选择，1为查询学生作业，2为录入学生作业,输入q退出：')
    if user_choice.lower() == 'q':
        print('欢迎再次使用')
        # 结束的是while死循环
        break
    if choice.get(user_choice) == '查询':
        name = input('请输入学生的姓名:')
        if name in homeworks:
            print(f'{name}的作业情况为:{homeworks[name]}')
        else:
            print('查询学生不存在')
    elif choice.get(user_choice) == '录入':
        state = {'0': '未交', '1': '已交'}
        for i in range(3):
            name = input('请输入学生的姓名：')
            date = input('请输入提交作业的时间：')
            input_state = input('请输入学生作业的状态，0为未交，1为已交：')
            if state.get(input_state):  # 如果key不存在，get会返回None
                if name == '' or date == '':
                    print('学生姓名或日期不能为空')
                else:
                    # 判断学生信息在homeworks中在不在，在则修改，不在则添加
                    if name in homeworks:
                        # 方式一：用子字典中的键值对更新原字典
                        homeworks[name].update({date: state[input_state]})  # 学生存在，更新子字典
                        # 方式二：向指定字典中添加指定键值对
                        # homeworks[name][date] = state[input_state]
                    else:
                        homeworks[name] = {date: state[input_state]}  # 学生不存在，则添加新的key-value

                    print(f'{name}的作业情况为：{homeworks[name]}')
                    print(f'所有学生的作业情况为：{homeworks}')
                    # 一切输入正确的情况下，则提前结束for循环
                    break
            else:
                print('学生作业状态有误')
    else:
        print('选择输入有误')