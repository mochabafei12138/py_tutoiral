import  openpyxl

'''
1.
    原生Python：比较干净的环境，其中默认只包含了pip,setuptools等
    Anaconda:其中包含了绝大多数的第三方库，常用的第三方库可能也已经包含在内了，但是不排除有的库不包含
    
2.如何安装第三方库
    方式一：在pycharm直接添加
        windows:File---->Settings---->Project:xxx---->Python Intepreter---->  +【install】--->搜索----》install Package
        Mac:Pycharm--->Perference---->Project:xxx---->Python Intepreter---->  +【install】--->搜索----》install Package
    方式二：在cmd中
        Windows:pip  install xxx
        Mac:pip3 install xxx
    方式三：Terminal【作用等同于cmd】
        Windows:pip  install xxx
        Mac:pip3 install xxx

3.问题说明
    问题一：pip不是内部或外部的命令
        原因：没有配置环境变量
        解决方案：将Python或Anaconda对应的路径全部添加到环境变量中
    问题二：timed out
        原因：网络不好
        解决方案：切换网络  或者  切换镜像【pip  install xxx -i  镜像】
     
    国内 pip 镜像源包括但不限于以下几种：   
        阿里云Python镜像源：https://mirrors.aliyun.com/pypi/simple/
        豆瓣Python镜像源：https://pypi.douban.com/simple/
        清华大学Python镜像源：https://pypi.tuna.tsinghua.edu.cn/simple/
        中国科学技术大学Python镜像源：http://pypi.mirrors.ustc.edu.cn/simple/
        华中科技大学Python镜像源：http://pypi.hustunique.com/   
        
    命令：pip install pandas -i   https://pypi.douban.com/simple/          
'''