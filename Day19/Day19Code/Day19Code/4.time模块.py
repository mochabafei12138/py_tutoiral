# import time
from time import  *

# 1.time():获取当前时间的时间戳   ******
t1 = time()
print(t1)

# 2.gmtime():获取UTC时间的元组形式
t2 = gmtime()
print(t2)

# 获取北京时间的元组形式
t3 = localtime()
print(t3)

# 3.strftime():将时间的元组形式转化为格式化字符串，格式可以自定义   ******
t4 = strftime('%Y/%m/%d %H:%M:%S',t3)
print(t4)
t4 = strftime('%Y.%m.%d %H:%M:%S',t3)
print(t4)
t4 = strftime('%Y-%m-%d %H:%M:%S',t3)
print(t4)

# 4.strptime():将时间的格式化字符串转化为时间的元组形式   *****
# 注意：解析时间的字符串时，给定的format一定要和原字符串匹配，否则ValueError: time data '2024-02-29 21:02:54' does not match format '%Y.%m.%d %H:%M:%S'
time_str = '2024-02-29 21:02:54'
t5 = strptime(time_str,'%Y-%m-%d %H:%M:%S')
print(t5)