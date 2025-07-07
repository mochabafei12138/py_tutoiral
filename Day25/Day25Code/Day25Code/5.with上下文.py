with open(r'aaa/致橡树.txt','r',encoding='gbk') as f1:
    r = f1.read()
    print(r)

with open(r'aaa/a1.txt','a',encoding='gbk') as f2:
    f2.write('32345674123456789')
    f2.flush()