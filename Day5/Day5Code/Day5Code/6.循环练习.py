# 1.求1~100之间所有整数的和
n = 1
total = 0
while n <= 100:
    # print(n)
    total += n     # 求和
    n += 1
print(total)

total = 0
for n in range(1,101):
    total += n
print(total)

# 2.统计1~100之间3的倍数的个数
n = 1
count = 0
while n <= 100:
    if n % 3 == 0:
        count += 1    # 计数
    n += 1
print(count)

count = 0
for n in range(1,101):
    if n % 3 == 0:
        count += 1
print(count)

n = 3
count = 0
while n <= 100:
    count += 1
    n += 3
print(count)

count = 0
for n in range(3,101,3):
    count += 1
print(count)