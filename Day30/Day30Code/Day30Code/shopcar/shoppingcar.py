'''
购物车类：
	商品字典：程序初始状态时，购物车肯定为空
		    后期操作过程中，向购物车中添加商品的时候，商品对象作为key,数量作为value
'''
class ShoppingCar():
    __slots__ = ('goods_dict',)
    def __init__(self):
        self.goods_dict = {}
    def __str__(self):
        return f'【ShoppingCar】：{self.goods_dict}'
    __repr__ = __str__