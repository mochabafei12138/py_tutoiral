### 一、Python基础及应用回顾总结

> 推荐画思维导图：xmind

> 1.常识语法
>
> ```
> 注释   标识符和关键字  输入输出  
> 格式化输出：输出的内容需要是指定的格式，如：占位符  f-string   format()
> ```
>
> 2.变量
>
> ```
> 定义变量   变量的重新赋值    变量的类型转换
> 全局变量和局部变量
> ```
>
> 3.语句
>
> ```
> if语句【重要：判断】     while语句【常用：结合死循环】   for语句【重要】
> 注意：
> 	a.避免漏掉冒号
> 	b.缩进问题
> ```
>
> 4.常用的数据类型
>
> ```
> 数字
> 列表：x[index] 列表的遍历    系统功能：append()  切片   元素的删除
> 字典：x[key]  字典的遍历    添加键值对    
> 字符串
> 
> 注意：
> 	a.及时复习
> 	b.多做练习【重复做作业】
> 	c.刷题网站：牛客网，力扣
> ```
>
> 5.函数
>
> ```
> 重点掌握：
> 	函数的定义和调用		参数【传参】和返回值     匿名函数   高阶函数【匿名函数作为参数】
> 	变量的作用域
> 了解：
> 	闭包    装饰器    递归
> 	
> 注意：
> 	a.要有封装函数的意识
> 	b.函数之间的相互调用
> 	c.注意函数的参数和返回值
> ```
>
> 6.面向对象
>
> ```
> 重点掌握：
> 	创建对象 		调用类中的函数
> 了解：
> 	封装  继承  多态
> 	函数的重写	运算符的重载    单例类
> ```
>
> 7.文件读写【自动化办公】
>
> ```
> 重点掌握
> 	常用的文本文件/二进制文件：read()     write()
> 	csv文件：import csv   reader()   writer()
> 	对象的序列化和反序列化：pickle【一切对象】   json【针对字典和列表】
> 	excel的读写：openpyxl   pandas
> 了解：
> 	word的读写
> 	pdf的读取
> 	发送邮件
> ```

### 二、综合项目：购物车

#### 1.项目分析

> 应用到的知识点
>
> ```
> 包和模块：创建一个包，其中定义不同的模块，一个模块中管理一个类
> 类和对象：定义类   创建对象    调用类中的函数
> 函数
> 对象的序列化和反序列化：pickle
> ```

> 项目需求:
>
> ```
> 系统类
> 	因为一个程序可能有很多用户，则需要将用户保存在本地
> 			将注册的用户添加在字典中
> 				key：用户id 【用户id随机产生即可，从10000~99999中随机产生一个】
> 				value：对应的用户对象
> 
> 	行为：
> 	用户注册——》根据下面信息生成一个用户，并将用户保存在本地
> 		随机产生 id
> 		输入姓名和密码
> 		创建一个购物车对象
> 
> 
> 	登录 ——》 登录成功返回为 True  否则返回为 False
> 		输入用户id 检测是否有该用户  没有的话提示注册
> 		有的话检测用户登录状态 若为 True  提示已登录
> 		否则 再输入密码进行登录
> 			不要忘记修改用户的登录状态
> 
> 	向购物车中添加商品 ——》验证用户是否登录，没有登录提示登录
> 		否则
> 			列出仓库中商品名单
> 				1. Mac电脑
> 				2.PthonBook
> 				3.草莓键盘
> 				4.iPhone
> 			用户输入对应的编号 在仓库中获得对应的商品
> 			用户输入数量 — 与该商品的的剩余量对比
> 				> 剩余量
> 					让用户重新输入并提示该商品的剩余量
> 				<=剩余量
> 					将该商品添加在该用户的购物车中
> 					并将仓库中的数据量做出相应的减少
> 				注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> 
> 	删除购物车的商品——》验证用户是否登录，没有登录提示登录
> 		否则
> 			请用户输入商品名字 查看该用户的购物车中是否有该商品
> 			如果没有，提示购物车中没有该商品
> 			否则：
> 				先选择要删除的商品
> 				请用户设置删除的数量
> 					数量  >=   购物车中商品数量
> 						购物车清单中删除该商品
> 					否则：
> 						购物车清单中做出相应的减少
> 			注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> 
> 
> 	结算——》验证用户是否登录 没有登录提示登录
> 		否则
> 			获取该用户的购物车中商品清单，计算总额
> 		注意： 结算完成 购物车清空
> 			  将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> 
> 
> 	退出登录———》验证用户是否登录 没有登录提示登录
> 		否则
> 			修改用户登录状态
> 		注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> ```
>
> 分析：
>
> ```
> 用户类：
> 	姓名   用户id【唯一的】  密码    购物车   用户登录状态【默认为未登录状态，表示为False,如果登录成功，则需要修改登录状态为True】
> 	
> 购物车类：
> 	商品字典：程序初始状态时，购物车肯定为空
> 		     向购物车中添加商品的时候，商品对象作为key,数量作为value
> 		     
> 仓库类：
> 	商品列表
> 	注意：信息保存到本地磁盘：程序刚启动时把商品列表存储到文本，之后使用再读取出来
> 	
> 商品类：
> 	商品名称   商品价格 	商品剩余量【仓库中的剩余量和购物车中的数量】
> 
> 系统管理类：
> 	让上述类产生联系，实现核心需求
> ```

#### 2.项目实现

> user.py
>
> ```Python
> '''
> 用户类：
> 	姓名   用户id【唯一的】  密码    购物车
> 	用户登录状态【默认为未登录状态，表示为False,如果登录成功，则需要修改登录状态为True】
> '''
> class User():
>     __slots__ = ('uid','uname','pwd','shopcar','islogin')
>     # 设置在参数部分的变量，意味着需要从外界传参，但是，登录状态不是由外界决定，无需从外界传参
>     def __init__(self,uid,uname,pwd,shopcar):
>         self.uid = uid
>         self.uname = uname
>         self.pwd = pwd
>         self.shopcar = shopcar
>         self.islogin = False
>     def __str__(self):
>         return f'【User】:{self.uid},{self.uname},{self.islogin}'
>     __repr__ = __str__
> ```
>
> goods.py
>
> ```Python
> '''
> 商品类：
> 	商品名称   商品价格 	商品剩余量【仓库中的剩余量和购物车中的数量】
> '''
> class Goods():
>     __slots__ = ('gname','gprice','balance')
>     def __init__(self,gname,gprice,balance):
>         self.gname = gname
>         self.gprice = gprice
>         self.balance  = balance
>     def __str__(self):
>         return f'【Goods】:{self.gname},{self.gprice},{self.balance}'
>     __repr__ = __str__
> ```
>
> shoppingcar.py
>
> ```Python
> '''
> 购物车类：
> 	商品字典：程序初始状态时，购物车肯定为空
> 		    后期操作过程中，向购物车中添加商品的时候，商品对象作为key,数量作为value
> '''
> class ShoppingCar():
>     __slots__ = ('goods_dict',)
>     def __init__(self):
>         self.goods_dict = {}
>     def __str__(self):
>         return f'【ShoppingCar】：{self.goods_dict}'
>     __repr__ = __str__
> ```
>
> storage.py
>
> ```Python
> '''
> 仓库类：
> 	商品列表:其中的对象是商品对象
> 	注意：信息保存到本地磁盘：程序刚启动时把商品列表存储到文本，之后使用再读取出来
> '''
> from goods import Goods  # 因为当前py文件和被导入的模块处于同一级目录下
> # from shopcar.goods import Goods  # 从工程的根目录开始导入，也可以
> import os,pickle
> 
> # 当前管理系统中会有很多不同的用户，不同的用户访问的仓库应该是同一个，简单来说，仓库对象有且只有一个
> # 在当前项目中，无论在哪里访问，访问到的都是同一个仓库对象，所以将仓库类设置为单例类
> 
> # 文件路径
> path = r'data/goodslist.txt'
> 
> # 书写单例装饰器
> def singleton(cls):
>     instance = None
>     def get_instance(*args,**kwargs):
>         nonlocal instance
>         if not instance:
>             instance = cls(*args,**kwargs)
>         return instance
>     return get_instance
> 
> # 单例类
> @singleton
> class Storage():
>     __slots__ = ('goods_list',)
>     def __init__(self):
>         # 一般情况下，构造函数中的代码尽量简化，如果逻辑较为复杂，建议封装新的函数，在构造函数中只需要调用即可
>         self.__load_goods()
> 
>     def __load_goods(self):
>         # 如果文件不存在，则定义商品列表，然后将列表序列化到本地文件；如果文件存在，把文件中的内容反序列化到程序中
>         # 假设仓库中的商品列表保存的文件为goodslist.txt
>         if os.path.exists(path):
>             # 文件存在，则反序列化
>             self.get_goods()
> 
>         else:
>             # 文件不存在【第一个运行程序，文件肯定不存在】
>             self.goods_list  = []  # 其中的元素是Goods对象
>             # 商品数据
>             goods_info = [['food',19,100],['Mac电脑',20000,100],['kindle',500,100],['water',2,100],['shoes',800,100]]
>             # 遍历给定的商品数据，创建对象，然后添加到商品列表中
>             for sublist in goods_info:
>                 # 创建Goods对象
>                 goods = Goods(gname=sublist[0],gprice=sublist[1],balance=sublist[2])
>                 self.goods_list.append(goods)
> 
>             # 将仓库中的商品列表序列化到本地文件
>             self.save_goods()
> 
>     # 序列化
>     def save_goods(self):
>         with open(path, 'wb') as f:
>             # 将程序中的goods_list序列化到本地文件
>             pickle.dump(self.goods_list, f)
> 
>     # 反序列化
>     def get_goods(self):
>         with open(path, 'rb') as f:
>             # 将本地文件中的数据反序列化出来，赋值给goods_list，保证了数据的同步性
>             self.goods_list = pickle.load(f)
> ```
>
> operation.py
>
> ```Python
> '''
> 系统类
> 	因为一个程序可能有很多用户，则需要将用户保存在本地
> 			将注册的用户添加在字典中
> 				key：用户id 【用户id随机产生即可，从10000~99999中随机产生一个】
> 				value：对应的用户对象
> 
> 	行为：
> 	用户注册——》根据下面信息生成一个用户，并将用户保存在本地
> 		随机产生 id
> 		输入姓名和密码
> 		创建一个购物车对象
> 
> 	登录 ——》 登录成功返回为 True  否则返回为 False
> 		输入用户id 检测是否有该用户  没有的话提示注册
> 		有的话检测用户登录状态 若为 True  提示已登录
> 		否则 再输入密码进行登录
> 			不要忘记修改用户的登录状态
> 
> 	向购物车中添加商品 ——》验证用户是否登录，没有登录提示登录
> 		否则
> 			列出仓库中商品名单
> 				1. Mac电脑
> 				2.PthonBook
> 				3.草莓键盘
> 				4.iPhone
> 			用户输入对应的编号 在仓库中获得对应的商品
> 			用户输入数量 — 与该商品的的剩余量对比
> 				> 剩余量
> 					让用户重新输入并提示该商品的剩余量
> 				<=剩余量
> 					将该商品添加在该用户的购物车中
> 					并将仓库中的数据量做出相应的减少
> 				注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> 
> 	删除购物车的商品——》验证用户是否登录，没有登录提示登录
> 		否则
> 			请用户输入商品名字 查看该用户的购物车中是否有该商品
> 			如果没有，提示购物车中没有该商品
> 			否则：
> 				先选择要删除的商品
> 				请用户设置删除的数量
> 					数量  >=   购物车中商品数量
> 						购物车清单中删除该商品
> 					否则：
> 						购物车清单中做出相应的减少
> 			注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> 
> 	结算——》验证用户是否登录 没有登录提示登录
> 		否则
> 			获取该用户的购物车中商品清单，计算总额
> 		注意： 结算完成 购物车清空
> 			  将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> 
> 	退出登录———》验证用户是否登录 没有登录提示登录
> 		否则
> 			修改用户登录状态
> 		注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性
> '''
> 
> from goods import Goods
> from shoppingcar import ShoppingCar
> from user import User
> from  storage import Storage
> import os,pickle,random
> 
> user_path = r'data/userslist.txt'
> 
> class Operation():
>     __slots__ = ('user_dict',)
>     def __init__(self):
>         # 当程序启动的时候，判断存储用户信息的文件是否存在，如果不存在，则闯将；如果存在，则直接加载
>         self.__load_user()
> 
>     # 如果类中定义的函数，不希望在类的外面被访问，只是在类中被调用，则可以私有化
>     def __load_user(self):
>         if os.path.exists(user_path):
>             # 存在:则反序列化文件内容，然后给user_dict赋值
>             with open(user_path,'rb') as f:
>                 self.user_dict = pickle.load(f)
>         else:
>             # 不存在【第一次运行，肯定不存在】
>             self.user_dict = {}
> 
>     # 序列化用户字典
>     def __save_user(self):
>         with open(user_path,'wb') as f:
>             pickle.dump(self.user_dict,f)
> 
>     # 用户id随机产生即可，从10000~99999中随机产生一个
>     def __get_uid(self):
>         while True:
>             uid = str(random.randint(10000,99999))
>             # key：用户id 【用户id随机产生即可，从10000~99999中随机产生一个】
>             # value：对应的用户对象
>             if uid not in self.user_dict:
>                 return uid
> 
>     # 用户注册
>     def user_register(self):
>         # 获取用户id
>         uid = self.__get_uid()
>         print(f'你的用户id为：{uid}')
>         # 创建购物车对象
>         sp = ShoppingCar()
>         # 引导用户从控制台输入用户名和密码，此处可以扩展：添加对用户名和密码的校验，比如要求用户名由字母和数字组成，至少4位，密码全部是数字，只能4位
>         uname = input('请输入你的用户名：')
>         pwd = input('请输入你的密码：')
>         # 根据以上信息创建一个用户对象
>         user = User(uid=uid,shopcar=sp,uname=uname,pwd=pwd)
>         # 将用户对象添加到用户字典中
>         self.user_dict[uid] = user
> 
>         # 将用户字典序列化到本地
>         self.__save_user()
> 
>         print('用户注册完成！')
> 
> 
>     # 用户登录
>     def user_login(self):
>         # 判断用户id是否存在，如果不存在，则表示未注册
>         uid = input('请输入你的用户id:')
>         if uid not in self.user_dict:
>             print('请先注册')
>             self.user_register()
> 
>         # 获取用户对象
>         user = self.user_dict[uid]
>         if user.islogin:
>             print('已经处于登录状态，无需再次登录')
>             return user
> 
>         # 表示未登录状态，则实现登录
>         while True:   # 如果登录不成功，则一直登录，直到成功，也可以限制错误的次数
>             uname = input('请输入用户名：')
>             pwd = input('请输入密码：')
>             if uname == user.uname and pwd == user.pwd:
>                 print('登录成功！')
>                 # 修改用户的登录状态
>                 user.islogin = True
>                 return user
>             else:
>                 print('用户名或密码有误，请重新登录')
> 
>     # 向购物车中添加商品
>     def add_goods(self):
>         user = self.user_login()
>         if not user:
>             print('请先登录')
>             return
> 
>         print('仓库中的商品信息如下：')
>         storage = Storage()
>         for i,goods in enumerate(storage.goods_list):
>             print(f'{i}:{goods.gname}')
> 
>         # 引导用户选择商品
>         index = input('请输入需要选择的商品的编号：')
>         if index.isdigit():
>             index = int(index)
>             if index in range(len(storage.goods_list)):
>                 # 根据索引从仓库的列表中获取商品对象
>                 storage_goods = storage.goods_list[index]
>                 # 引导用户输入需要添加到购物车的商品数量
>                 num = int(input('请输入需要添加的商品的数量：'))
>                 if num < 0:
>                     print('数量输入有误')
>                 else:
>                     # 将输入的数量和仓库中的库存量做比较
>                     while num > storage_goods.balance:
>                         num = int(input(f'商品库存量为:{storage_goods.balance},请重新输入需要添加的商品的数量：'))
>                     else:
>                         # num <= storage_goods.balance
>                         # 重新创建一个新的商品对象，用于添加到购物车中的对象
>                         shopcar_goods = Goods(gname=storage_goods.gname,gprice=storage_goods.gprice,balance=num)
>                         # 将该商品对象添加到当前用户的购物车中
>                         user.shopcar.goods_dict[shopcar_goods] = num
> 
>                         # 将仓库中的商品的库存量修改
>                         storage_goods.balance -= num
> 
>                         # 同步数据到本地
>                         self.__save_user()
>                         storage.save_goods()
> 
>                         print('商品添加成功！')
> 
>             else:
>                 print('暂无此商品')
>         else:
>             print('输入有误')
> 
>     # 从购物车中删除商品
>     def del_goods(self):
>         user = self.user_login()
>         if not user:
>             print('请先登录')
>             return
> 
>         gname = input('请输入需要删除的商品的名称：')
> 
>         # 购物车中的商品对象
>         shopcar_goods = None
>         # 仓库中的商品对象
>         storage_goods = None
>         # 用于标记商品在购物车中是否存在，默认不存在
>         flag = False
> 
>         # 寻找购物车中的商品对象
>         for goods in user.shopcar.goods_dict:
>             if goods.gname == gname:
>                 shopcar_goods = goods
>                 flag = True
> 
>         if not flag:
>             print(f'商品{gname}不存在')
>             return
> 
>         # 寻找仓库中对应的商品对象
>         storage = Storage()
>         for goods in storage.goods_list:
>             if goods.gname == gname:
>                 storage_goods = goods
> 
>         # 输入需要删除的商品的数量
>         num = int(input(f'请输入需要删除的商品{gname}的数量：'))
> 
>         if num >= user.shopcar.goods_dict[shopcar_goods]:
>             # 全部删除：删除购物车中对应的键值对
>             user.shopcar.goods_dict.pop(shopcar_goods)
>             # 添加到仓库中
>             storage_goods.balance += shopcar_goods.balance
>         else:
>             # 删除部分：给value做减法
>             shopcar_goods.balance -= num
>             # 更新购物车中的商品键值对
>             user.shopcar.goods_dict[shopcar_goods] = shopcar_goods.balance
>             # 加回到仓库中
>             storage_goods.balance += num
> 
>         # 同步数据到本地
>         self.__save_user()
>         storage.save_goods()
> 
>         print('商品删除成功！')
> 
> 
>     # 结算购物车
>     def get_total(self):
>         user = self.user_login()
>         if not user:
>             print('请先登录')
>             return
>         # 计算总价格
>         total = 0
>         for goods,num in user.shopcar.goods_dict.items():
>             total += goods.gprice * num
>         print(f'结算成功，所有商品总计为:{total}')
> 
>         # 清空购物车
>         user.shopcar.goods_dict.clear()
> 
>         # 同步数据到本地文件
>         self.__save_user()
> 
>     # 退出登录
>     def user_quit(self):
>         user = self.user_login()
>         if user:
>             user.islogin = False
>             # 同步数据到本地文件
>             self.__save_user()
> 
>             print('用户注销成功')
> ```
>
> test.py
>
> ```python
> 
> from operation import Operation
> 
> def main():
>     op = Operation()
>     print('欢迎进入xxx自助购物系统'.center(40,'*'))
>     while True:
>         print('''本系统提供了如下功能：
>         0.用户注册
>         1.用户登录
>         2.添加商品
>         3.删除商品
>         4.结算购物车
>         5.注销登录
>         6.退出系统''')
> 
>         select = input('请输入需要进行的操作：')
>         if select == '0':
>             op.user_register()
>         elif select == '1':
>             op.user_login()
>         elif select == '2':
>             op.add_goods()
>         elif select == '3':
>             op.del_goods()
>         elif select == '4':
>             op.get_total()
>         elif select == '5':
>             op.user_quit()
>         elif select == '6':
>             print('欢迎再次使用')
>             break
>         
> if __name__ == '__main__':
>     main()
> ```