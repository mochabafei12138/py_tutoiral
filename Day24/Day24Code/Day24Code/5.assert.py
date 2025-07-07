# assert
# 语法：assert 表达式,异常描述信息
# 工作原理：如果表达式成立，则代码正常执行，但是如果表达式不成立，则会出现AssertionError
def div(x,y):
    assert y != 0,'y不能为0'
    return x / y
r = div(3,0)
print(r)