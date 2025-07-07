'''
用户类：
	姓名   用户id【唯一的】  密码    购物车
	用户登录状态【默认为未登录状态，表示为False,如果登录成功，则需要修改登录状态为True】
'''
class User():
    __slots__ = ('uid','uname','pwd','shopcar','islogin')
    # 设置在参数部分的变量，意味着需要从外界传参，但是，登录状态不是由外界决定，无需从外界传参
    def __init__(self,uid,uname,pwd,shopcar):
        self.uid = uid
        self.uname = uname
        self.pwd = pwd
        self.shopcar = shopcar
        self.islogin = False
    def __str__(self):
        return f'【User】:{self.uid},{self.uname},{self.islogin}'
    __repr__ = __str__

