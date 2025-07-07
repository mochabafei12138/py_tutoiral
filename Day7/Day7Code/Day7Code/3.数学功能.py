# 1.
# - abs(x):返回数字的绝对值
print(abs(-34))
# - max(x1,x2,…):返回给定参数的最大值     *****
print(max(354,7,8,9,9,23,239))
# - min(x1,x2,…):返回给定参数的最小值     *****
print(min(354,7,8,9,9,23,239))
# - pow(x,y):求x的y次方的值
print(pow(5,3))  # 5 ** 3           ******
# - round(x,n):返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
print(round(35.6354))  # 36
print(round(35.4354))  # 35
print(round(35.6354))  # 36
print(round(35.4354,2))  # 35.44

# - sum(容器)：求容器中元素的和        ******
print(sum([45,67,78,8]))
print(sum(range(1,101)))

# 2.导入math模块
import  math     # 注意：自己创建py文件的时候，千万不要和系统的模块重名，如：math.py,random.py,会导致系统的模块失效
# - ceil(x):返回x的上入整数，不能直接访问，需要通过math访问，即math.ceil(18.1),向上取整        ******
print(math.ceil(19.98475))   # 20
print(math.ceil(19.18475))   # 20

# - floor(x):返回x的下入整数，同ceil的用法，向下取整     ******
print(math.floor(19.98475))   # 19
print(math.floor(19.18475))   # 19

# - modf(x):返回x的整数部分和小数部分，两部分的数值符号与x相同，整数部分以浮点型表示，同ceil的用法
print(math.modf(45.6778))

# - sqrt(x):返回数字x的平方根，数字可以为负数，返回类型为实数【浮点型】，同ceil的用法
print(math.sqrt(9))   # 3.0
print(9 ** 0.5)   # 3.0

