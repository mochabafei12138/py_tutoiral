# 1.__slots__:限制对象属性的动态绑定

# 2.__dict__:获取类或对象的所有信息【属性和函数】，返回一个字典   ****
# print(str.__dict__)

# 3.__module__;获取指定对象属于哪个模块，如果时当前模块，则结果为__main__,如果是其他模块，则结果为模块名
print(str.__module__)  # builtins

class Person():
    def __init__(self,age):
        self.age = age
p = Person(45)
# print(p.__module__)  # __main__

# 4. __name__:可以用来判断正在执行的是否是当前文件    ******
# 如果结果为__main__则说明运行的是当前文件，如果是模块名则表示运行的是其他文件
# print(__name__)
import t1

# 适用的场景:当作代码的规范，认为是程序执行的入口
if __name__ == '__main__':
    # 函数的调用
    pass

# 5.__class__：类似于type(),获取指定对象的数据类型
print(type(p))
print(p.__class__)

