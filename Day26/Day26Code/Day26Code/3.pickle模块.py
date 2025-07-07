# 1.f.write():使用普通文件的写入方式，只能操作字符串
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
per = Person("小明",10)

# TypeError: write() argument must be str, not list
# with open(r'data/f1.txt','w',encoding='utf-8') as f1:
#     f1.write(per)

# 2.对象的序列化：相当于写入
import pickle

'''
注意：
    a.pickle.dump(obj,f)进行序列化，相当于write()
    b.pickle.load(f)进行反序列化，相当于read()
    c.python对象被序列化之后，是二进制数据，所以打开文件使用wb或rb的模式
'''
with open(r'data/f1.txt','wb') as f1:
    pickle.dump(per,f1)

# 3.对象的反序列化：相当于读取
with open(r'data/f1.txt','rb') as f2:
    r = pickle.load(f2)
    print(r)  # <__main__.Person object at 0x0000018105C03D60>
    print(r.name,r.age)






