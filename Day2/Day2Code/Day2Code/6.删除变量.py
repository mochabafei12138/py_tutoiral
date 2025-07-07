# 1.定义变量
num = 20
print(num)

# 2.删除变量
del num
print(num)   # NameError: name 'num' is not defined

# 注意1：变量在使用之前，一定要先定义，然后才能使用
# 注意2：一个变量定义之后，在使用完毕或失去价值的情况下，可以将该变量删除，删除之后相当于该变量未被定义【空间会被释放】
