'''
商品类：
	商品名称   商品价格 	商品剩余量【仓库中的剩余量和购物车中的数量】
'''
class Goods():
    __slots__ = ('gname','gprice','balance')
    def __init__(self,gname,gprice,balance):
        self.gname = gname
        self.gprice = gprice
        self.balance  = balance
    def __str__(self):
        return f'【Goods】:{self.gname},{self.gprice},{self.balance}'
    __repr__ = __str__