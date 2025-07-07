# 为了解决实际生活中的特定场景，系统的异常类满足不了需求，则需要自定义异常

# 1.自定义一个类，继承自BaseException或Exception
# class CustomException(BaseException):
#     # 2.书写构造函数，在其中定义实例属性
#     def __init__(self,msg):
#         # 调用父类的构造函数，主要是为了使用异常类的机制
#         super().__init__()
#         self.msg = msg
#
#     # 3.重写__str__函数
#     def __str__(self):
#         return self.msg
#
#     # 4.定义一个实例函数，用来解决出现的问题
#     def handle(self):
#         print('问题已解决')
#
# try:
#     raise CustomException('出现了异常')
# except CustomException as e:
#     print(e)
#     e.handle()

# 练习：
class LateException(BaseException):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return self.msg

    def handle(self):
        print('下次一定在八点之前起床')
hour = float(input('请输入你起床的时间：'))
try:
    if hour >= 8:
        raise LateException('上课/上班迟到了')
    else:
        print('正常上课/上班')
except LateException as e:
    print(e)
    e.handle()