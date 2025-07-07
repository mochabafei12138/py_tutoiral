# 2.已知数据’aaa‘,'bbb','ccc',用一个print输出，最终结果为aaa=bbb=ccc
print('aaa','bbb','ccc',sep='=')
print('%s=%s=%s' % ('aaa','bbb','ccc'))
print('{}={}={}'.format('aaa','bbb','ccc'))
print(f'{"aaa"}={"bbb"}={"ccc"}')

# 4.从控制台输入圆的半径，计算该圆的周长和面积，圆周率可以定义为3.14
PI = 3.14
r = float(input('请输入圆的半径：'))
length = 2 * PI * r
area = PI * r * r   # r ** 2 或者 pow(r,2)
print(f'该圆的周长:{length:.2f},面积:{area:.2f}')
