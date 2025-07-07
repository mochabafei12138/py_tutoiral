'''
仓库类：
	商品列表:其中的对象是商品对象
	注意：信息保存到本地磁盘：程序刚启动时把商品列表存储到文本，之后使用再读取出来
'''
from goods import Goods  # 因为当前py文件和被导入的模块处于同一级目录下
# from shopcar.goods import Goods  # 从工程的根目录开始导入，也可以
import os,pickle

# 当前管理系统中会有很多不同的用户，不同的用户访问的仓库应该是同一个，简单来说，仓库对象有且只有一个
# 在当前项目中，无论在哪里访问，访问到的都是同一个仓库对象，所以将仓库类设置为单例类

# 文件路径
path = r'data/goodslist.txt'

# 书写单例装饰器
def singleton(cls):
    instance = None
    def get_instance(*args,**kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args,**kwargs)
        return instance
    return get_instance

# 单例类
@singleton
class Storage():
    __slots__ = ('goods_list',)
    def __init__(self):
        # 一般情况下，构造函数中的代码尽量简化，如果逻辑较为复杂，建议封装新的函数，在构造函数中只需要调用即可
        self.__load_goods()

    def __load_goods(self):
        # 如果文件不存在，则定义商品列表，然后将列表序列化到本地文件；如果文件存在，把文件中的内容反序列化到程序中
        # 假设仓库中的商品列表保存的文件为goodslist.txt
        if os.path.exists(path):
            # 文件存在，则反序列化
            self.get_goods()

        else:
            # 文件不存在【第一个运行程序，文件肯定不存在】
            self.goods_list  = []  # 其中的元素是Goods对象
            # 商品数据
            goods_info = [['food',19,100],['Mac电脑',20000,100],['kindle',500,100],['water',2,100],['shoes',800,100]]
            # 遍历给定的商品数据，创建对象，然后添加到商品列表中
            for sublist in goods_info:
                # 创建Goods对象
                goods = Goods(gname=sublist[0],gprice=sublist[1],balance=sublist[2])
                self.goods_list.append(goods)

            # 将仓库中的商品列表序列化到本地文件
            self.save_goods()

    # 序列化
    def save_goods(self):
        with open(path, 'wb') as f:
            # 将程序中的goods_list序列化到本地文件
            pickle.dump(self.goods_list, f)

    # 反序列化
    def get_goods(self):
        with open(path, 'rb') as f:
            # 将本地文件中的数据反序列化出来，赋值给goods_list，保证了数据的同步性
            self.goods_list = pickle.load(f)