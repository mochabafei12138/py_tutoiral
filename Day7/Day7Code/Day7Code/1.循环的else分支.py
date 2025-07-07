# 注意：Python中的循环语句也是有else分支的，不光if语句中有else分支


# 1.for-else/while-else
# a.当if的条件按不成立时，才会执行else分支
n = 7
if n < 5:
    print('yes')
else:
    print('no')

# b.无论while或for循环的分支是否执行，一般情况下else分支都会执行
n = 0
while n > 10:
    print(n)
    n += 1
else:
    print('while~~~~else')

for n in range(10):
    print('~~~~~~',n)
else:
    print('for~~~else')

print('*' * 50)

# c.for/while【break】-----else
# 注意：如果在while或for中出现break且break会被执行，则循环的else分支不会被执行，反之，如果break不会被执行，则else分支会被执行
n = 0
while n < 10:
    print(n)
    if n == 2:
        break
    n += 1
else:
    print('while~~~~else')

for n in range(10):
    print('~~~~~~',n)
    if n > 20:
        break
else:
    print('for~~~else')