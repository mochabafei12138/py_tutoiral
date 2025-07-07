# 1.+:添加元素/组合
print(34 + 45)  # 数学元素
print('12r' + 'abc')  # 字符串拼接
l1 = [1,2,3]
l2 = [4,67,8]
l3 = l1 + l2
print(l3)   # 生成了一个新的列表
print(l1)
print(l2)

# 在原列表的基础上新增元素     *****
l4 = [45,7,9]
num = 10
l4 += [num]   # 错误写法：l4 += num
print(l4)

# 2.*
print('abc' * 3)
print([23,5,6] * 3)  # 注意：生成了一个新的列表

# 3.in和not  in,一般结合if语句使用   ********
# 注意：在删除元素之前，最好判断该元素在列表中是否存在，如果存在，再执行删除操作
print(10 in [34,2,10])
print(10 not in [34,23,4])

# 练习
emp_num = 0
salary_list = []  # 薪资明细
while True:
    salary = input(f'请输入第{emp_num}位员工的薪资,输入q结束退出：')
    # 程序结束的出口
    if salary == 'q' or salary == 'Q':
        print('退出操作')
        break
    salary = float(salary)
    if salary < 0:   # 目前考虑理想化的状态，如果要校验浮点数，则需要借助于正则表达式
        print('薪资小于0，请重新输入')
        continue
    # 计数
    emp_num += 1
    # 薪资明细
    salary_list += [salary]

if salary_list:
    print(f'录入员工的数量：{emp_num}，平均薪资:{sum(salary_list) / len(salary_list)}，薪资明细:{salary_list}')
else:
    print('未录入员工薪资')