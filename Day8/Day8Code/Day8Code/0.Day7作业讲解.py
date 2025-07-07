# 1.要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
'''
emp_num = 0
salary_sum = 0
salary_detail = ''  # 薪资明细
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
    # 求薪资总和
    salary_sum += salary
    # 薪资明细
    salary_detail += str(salary) + ';'    # +在字符串之间表示拼接

if emp_num:
    print(f'录入员工的数量：{emp_num}，平均薪资:{salary_sum / emp_num}，薪资明细:{salary_detail}')
else:
    print('未录入员工薪资')
'''

# 3.假设某人有100,000现金.每经过一次路口需要进行一次交费. 交
# 费规则为当他现金大于50,000时每次需要交5%,如果现金小于等于50,000时每次交5,000.请写一程序计算此人可以经过多少次这个路口
money = 100000
count = 0
while money >= 5000:
    count += 1
    if money >= 50000:
        money -= money * 0.05
    elif money <= 50000:
        money -= 5000
print(f'此人可以经过{count}次这个路口')