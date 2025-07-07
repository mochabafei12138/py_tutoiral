1.要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资

```python
# emp_num = 0
# salary_sum = 0
# while True:
#     salary = input(f"请输入第{emp_num}位员工的薪资【输入q或Q退出】:")
#     if salary == 'q' or salary == 'Q':
#         print("录入完成，退出操作")
#         break
#     if float(salary) < 0:
#         print("薪资不能为负数，请重新输入")
#         continue
#     # 统计员工的数量
#     emp_num += 1
#     # 求所有员工的薪资和
#     salary_sum += float(salary)
# print(f"总共录入员工{emp_num}位，平均薪资：{salary_sum / emp_num}")
```

2.有一个棋盘，有64个方格，在第一个方格里面放1粒芝麻重量是0.00001kg，第二个里面放2粒，第三个里面放4，求棋盘上放的所有芝麻的重量

```python
# 方式一
total = 0
for n in range(0,64):
    total += 2 ** n
print(f"棋盘所以芝麻重量总和为{total * 0.00001}kg")

# 方式二
num = 1
total = 0
for n in range(63):
    # 记录下一个方格的芝麻数量
    num = 2 * num
    # 记录芝麻数量总和
    total += num
print(f"棋盘上芝麻重量总和为：{total * 0.00001}kg")
```

3.假设某人有100,000现金.每经过一次路口需要进行一次交费. 交费规则为当他现金大于50,000时每次需要交5%如果现金小于等于50,000时每次交5,000.请写一程序计算此人可以经过多少次这个路口

```python
money = 100000
count = 0
while money >= 5000:
    if money > 50000:
        money -= 0.05 * money
    else:
        money -= 5000
    count += 1
print(f"总共会经过{count}次路口")
```

4.有四个数字，1，2，3，4能组成多少个互不相同且无重复的三位数？各是多少？

```python
count = 0

for i in (1,2,3,4):
    for j in (1,2,3,4):
        for k in (1,2,3,4):
            # 去重
            if i != j and i != k and j!= k:
                print(i,j,k)
                count += 1
print(count)
```

