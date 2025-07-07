with open(r'aaa/3.png','rb') as f1:
    r = f1.read()
    print(r)

with open(r'aaa/img.png','wb') as f2:
    f2.write(r)   # f2.write(字节)
    f2.flush()