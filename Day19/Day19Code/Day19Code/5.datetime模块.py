import datetime
from datetime import *

# 1.now():获取当前时间   *****
d1 = datetime.now()    # datetime.datetime.now()
print(d1)  # 2024-02-29 21:11:38.595202

# 2.datetime之间可以进行减法运算   *****
d2 = datetime(2025,4,3,10,10,10,100)
d3 = datetime(2025,4,4,10,45,10,100)
d11 = d3 - d2
print(d11)
print(d11.days)
print(d11.seconds)

