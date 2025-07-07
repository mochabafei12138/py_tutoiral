'''
分配办公室
3个办公室，8位老师，随机分配办公室
'''
import  random

# 定义列表，表示一个学校中的三个办公室
schools = [[],[],[]]  # 三个小列表就是三个办公室，对应的索引为0 1 2
# 定义列表，表示八位老师
techers = ['李','张','姚','杨','赵','王','孙','周']

# 让老师抓阄
# 遍历老师的列表
for tea in techers:
    # 产生办公室的随机数
    room = random.randint(0,2)
    # 让当前老师进入抓到的办公室
    schools[room].append(tea)

for room in schools:
    print(f'该办公室中老师的数量为{len(room)},分别是:')
    for tea in room:
        print(tea,end=',')
    print()

# 扩展：'xxx'.join(iterable):当iterable中的元素为字符串时，用xx将这些元素进行拼接
# 举例：l = ['a','b','c']----->'-'.join(l)---->'a-b-c'
for room in schools:
    result = ','.join(room)
    print(f'该办公室中老师的数量为{len(room)},分别是:{result}')




