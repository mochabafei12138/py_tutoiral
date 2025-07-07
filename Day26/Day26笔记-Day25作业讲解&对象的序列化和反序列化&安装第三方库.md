### Day25作业讲解

> ```Python
> # 1.邮编查询，读取 youbian.txt 文件中的数据， 完成邮编查询的操作，从控制台输入邮编号，
> # 如果有此邮编，请输出对应的城市，否则提示无此邮编
> 
> def read_data():
>     # 读取已知文件
>     with open(r'data/youbian.txt', 'r', encoding='utf-8') as f:
>         data_list = f.readlines()
>     return  data_list
> 
> # 方式一：切片
> def get_city1(code):
>     data_list = read_data()
>     # 查询
>     for data in data_list:
>         if code == data[1:7]:
>             print(f'邮编{code}对应的地区为：{data[9:-4]}')   # start和end不同的符号，以start为准
>             break
>     else:
>         print('无此邮编')
> 
> # 方式二：eval()
> def get_city2(code):
>     data_list = read_data()
>     # 查询
>     for data in data_list:
>         # data  [610202,"陕西省铜川市城区"],\n ----->[610202,"陕西省铜川市城区"]
>         # a.切片实现
>         # new_data = data[:-2]
>         # b.rstrip()
>         new_data = data.rstrip(',\n')
> 
>         # 通过eval将上述形似列表的字符串识别并转化
>         info_list = eval(new_data)
> 
>         if str(info_list[0]) == code:
>             print(f'邮编{code}对应的地区为：{info_list[1]}')
>             break
>     else:
>         print('无此邮编')
> 
> # 2.将一个英文语句以单词为单位逆序排放到指定的文件中
> def reverse_data(data):
>     data_list = data.split(' ')
>     data_list.reverse()
>     new_data = ' '.join(data_list)
>     with open(r'data/words.txt','w',encoding='utf-8') as f:
>         f.write(new_data)
>         f.flush()
> 
> if __name__ == '__main__':
>     # code = input('请输入需要查询的邮编：')
>     # get_city2(code)
> 
>     data = input('请输入一个英文句子：')
>     reverse_data(data)
> ```
>
> ```Python
> # 3.开房查询，从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，
> # 如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中
> # a.读取已知文件中的数据
> def read_data():
>     with open(r'data/kaifanglist.txt','r',encoding='utf-8') as f:
>         all_list = f.readlines()
>     return all_list
> 
> # b.查询
> # 思路：根据指定的姓名查询数据，如果存在，则将数据单独保存到一个新的列表
> def search_data(name):
>     single_list = []
>     all_list = read_data()
>     for row in all_list:
>         if name == row.split(',')[0]:
>             single_list.append(row)
>     write_data(single_list,name)
> 
> # c.将查询后的结果写入到指定文件中
> def write_data(single_list,name):
>     if single_list:
>         print(f'{name}果然去了~~~~~')
>         des_path = rf'data/{name}.txt'
>         # 如果是多次open，为了不丢失原数据，建议使用a，但是如果文件只open一次，循环写入，w也是可以的
>         with open(des_path,'w',encoding='utf-8') as f:
>             for row in single_list:
>                 f.write(row)
>                 f.flush()
>     else:
>         print(f'未查到{name}的信息')
> 
> if __name__ == '__main__':
>     name = input('请输入需要查询的人的姓名：')
>     search_data(name)
> ```

### 一、对象的序列化和反序列化

> Python中一切皆对象

> 对象的序列化：将Python中的对象持久化到磁盘上
>
> 对象的反序列化：将磁盘上一个文件中的内容转换为Python对象
>
> 注意：
>
> ​	1.对象的序列化【写入】和反序列化【读取】通过pickle模块和json模块完成
> 	2.Python中一切皆对象，包括类型：数字，字符串，列表，字典。元组，集合，类，函数，模块等
>
> ​	3.pickle可以序列化一切类型，json常用于操作字典和列表

#### 1.pickle模块

> ```Python
> # 1.f.write():使用普通文件的写入方式，只能操作字符串
> class Person():
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
> per = Person("小明",10)
> 
> # TypeError: write() argument must be str, not list
> # with open(r'data/f1.txt','w',encoding='utf-8') as f1:
> #     f1.write(per)
> 
> # 2.对象的序列化：相当于写入
> import pickle
> 
> '''
> 注意：
>     a.pickle.dump(obj,f)进行序列化，相当于write()
>     b.pickle.load(f)进行反序列化，相当于read()
>     c.python对象被序列化之后，是二进制数据，所以打开文件使用wb或rb的模式
> '''
> with open(r'data/f1.txt','wb') as f1:
>     pickle.dump(per,f1)
> 
> # 3.对象的反序列化：相当于读取
> with open(r'data/f1.txt','rb') as f2:
>     r = pickle.load(f2)
>     print(r)  # <__main__.Person object at 0x0000018105C03D60>
>     print(r.name,r.age)
> ```

#### 2.json模块

> JSON和Python中数据类型的对应关系
> JSON            Python      表示
> object           dict             {}
> array            list               []

> json.dump():将Python中的字典或列表对象序列化到指定的文件中
> json.dumps()：将Python中的字典或列表对象序列化为json字符串
>
> json.load():将指定的文件中的json字符串反序列化为Python中的字典或列表对象
> json.loads()：将json字符串反序列化为Python中的字典或列表对象
>
> ```Python
> import json
> data = {
>     "name": "中国",
>     "province": [{
>         "name": "黑龙江",
>         "cities": {
>             "city": ["哈尔滨", "大庆"]
>         }
>     }, {
>         "name": "广东",
>         "cities": {
>             "city": ["广州", "深圳", "珠海"]
>         }
>     }, {
>         "name": "台湾",
>         "cities": {
>             "city": ["台北", "高雄"]
>         }
>     }, {
>         "name": "新疆",
>         "cities": {
>             "city": ["乌鲁木齐"]
>         }
>     }]
> }
> print(data)
> print(type(data))
> 
> # 1.序列化
> # json.dumps()：将Python中的字典或列表对象序列化为json字符串
> # 注意：ensure_ascii的默认只未True，表示对中文进行编码，如果希望中文能正常显示，则可以设置ensure_ascii为False
> r1 = json.dumps(data,ensure_ascii=False)
> print(r1)
> print(type(r1))
> 
> # json.dump():将Python中的字典或列表对象序列化到指定的文件中
> with open(r'data/city.json','w',encoding='utf-8') as f1:
>     json.dump(data,f1,ensure_ascii=False)
> 
> # 2.反序列化
> # json.loads()：将json字符串反序列化为Python中的字典或列表对象
> r2 = json.loads(r1)
> print(r2)
> print(type(r2))
> 
> # json.load():将指定的文件中的json字符串反序列化为Python中的字典或列表对象
> with open(r'data/city.json','r',encoding='utf-8') as f2:
>     r3 = json.load(f2)
>     print(r3)
>     print(type(r3))
> ```

### 二、安装第三方库

> 模块，也被称为库，其实相当于是一个工具
>
> Python中的模块/库分为三大类
>
> ​	a.系统模块，特点：只需要import导入就可以使用，如：random  math   string   csv  pickle  json等
>
> ​	b.自定义模块，特点：需要自己创建py文件，在该文件自定义函数或类
>
> ​	c.第三方模块,特点：需要先安装，然后再import导入使用，如：openpyxl  docx   requests   bs4等
>
> ```Python
> import  openpyxl
> 
> '''
> 1.
>     原生Python：比较干净的环境，其中默认只包含了pip,setuptools等
>     Anaconda:其中包含了绝大多数的第三方库，常用的第三方库可能也已经包含在内了，但是不排除有的库不包含
>     
> 2.如何安装第三方库
>     方式一：在pycharm直接添加
>         windows:File---->Settings---->Project:xxx---->Python Intepreter---->  +【install】--->搜索----》install Package
>         Mac:Pycharm--->Perference---->Project:xxx---->Python Intepreter---->  +【install】--->搜索----》install Package
>     方式二：在cmd中
>         Windows:pip  install xxx
>         Mac:pip3 install xxx
>     方式三：Terminal【作用等同于cmd】
>         Windows:pip  install xxx
>         Mac:pip3 install xxx
> 
> 3.问题说明
>     问题一：pip不是内部或外部的命令
>         原因：没有配置环境变量
>         解决方案：将Python或Anaconda对应的路径全部添加到环境变量中
>         D:\software\Anaconda
>         D:\software\Anaconda\Library\mingw-w64\bin
>         D:\software\Anaconda\Library\usr\bin
>         D:\software\Anaconda\Library\bin
>         D:\software\Anaconda\Scripts
>     问题二：timed out
>         原因：网络不好
>         解决方案：切换网络  或者  切换镜像【pip  install xxx -i  镜像】
>      
>     国内 pip 镜像源包括但不限于以下几种：   
>         阿里云Python镜像源：https://mirrors.aliyun.com/pypi/simple/
>         豆瓣Python镜像源：https://pypi.douban.com/simple/
>         清华大学Python镜像源：https://pypi.tuna.tsinghua.edu.cn/simple/
>         中国科学技术大学Python镜像源：http://pypi.mirrors.ustc.edu.cn/simple/
>         华中科技大学Python镜像源：http://pypi.hustunique.com/   
>         
>     命令：pip install pandas -i   https://pypi.douban.com/simple/          
> '''
> ```
