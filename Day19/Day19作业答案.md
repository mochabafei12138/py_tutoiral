1.封装函数，给定一个文件夹路径，获取该路径下所有的文件，注意：要输出所有文件夹及子文件夹下面的文件

```Python
# 1.封装函数，给定一个文件夹路径，获取该路径下所有的文件，注意：要输出所有文件夹及子文件夹下面的文件
import os
def get_file(folder_path):
    # 判断路径是否存在
    if not os.path.exists(folder_path):
        print('路径不存在')
        return

    # 判断路径表示的是文件还是文件夹
    if os.path.isfile(folder_path):
        print(f'是文件：{folder_path}')
        return

    # 说明folder_path是一个文件夹
    # 获取该文件夹下的所有的内容的名称
    names_list = os.listdir(folder_path)
    # print(names_list)
    # 遍历列表，获取其中的名称，然后拼接为路径
    for name in names_list:
        sub_path = os.path.join(folder_path,name)
        # print(sub_path)
        if os.path.isfile(sub_path):
            # 文件
            print(f'是文件：{sub_path}')
        else:
            # 文件夹,则就可以递归执行【因为子路径是文件夹的情况下，需要反复获取，遍历，拼接，判断】
            get_file(sub_path)

folder_path = r'd:\Desktop\coding'
# get_file(folder_path)


```

2.获取当前时间，判断是否是元旦，如果不是，计算和元旦差了多少天

```Python


# 2.获取当前时间，判断是否是元旦，如果不是，计算和元旦差了多少天
import  datetime

# 获取当前时间
now = datetime.datetime.now()
print(now)
# today = datetime.datetime.today()
# print(today)

# 获取元旦日期
new_year = datetime.datetime(now.year,1,1)

# 判断
if now.month == 1 and now.day == 1:
    print('今天是元旦！')
else:
    # 计算差值
    days_diff = (now - new_year).days
    print(f'今天不是元旦，距离元旦{days_diff}天')
```

