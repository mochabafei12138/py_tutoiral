1.已知有文件test.txt里面的内容如下，查找文件中以1000phone开头的语句，并保存到列表中

```
1000phone hello python
mobiletrain 大数据
1000phone java
mobiletrain html5
mobiletrain 云计算
```

> ```Python
> """
> 分析：
>     读取文件中的内容 因为文件中的数据是一行一行的 所以每行读取更方便
>     每一行都要检验一下 是否是以1000phone开头的  是的话将其保存在列表中
> """
> import re
> 
> def check_start(src_str):
>     """
>     检验指定字符串是否以1000phone开头
>     :param src_str: 指定的字符串
>     :return:返回是否合法
>     """
>     pattern = re.compile('1000phone')
>     result = pattern.match(src_str)
>     return False if result is None else True
> 
> if __name__ == '__main__':
>     # 读取文件  并将指定的内容存放于指定列表中
>     values = []
>     with open(r'test.txt', 'r', encoding="UTF-8") as handle:
>         contens = handle.readlines()
>         # 列表生成式 在生成元素是 调用函数检验 是否合法
>         values = [ele for ele in contens if check_start(ele)]
> 
>     print(values)
> ```

2.提取用户输入数据中的数值 (数值包括正负数 还包括整数和小数在内) 并求和 

```
例如:“-3.14good87nice19bye” =====> -3.14 + 87 + 19 = 102.86
```

> ```Python
> """
> 提取用户输入数据中的数值 (数值包括正负数  还包括整数和小数在内)   并求和
> 分析：
>     整数：
>         1位数  0-9
>         2位数以上  [1-9]+[0-9]
>     小数：
>         整数为有1位  [0-9].[0-9]*
>         整数位有2位及以上 [1-9][0-9].[0-9]*
> 
>         -表示负数 可有可无
> """
> import re
> 
> def get_sum(src_str):
>   	"""
>   	分析：
>   	有可能是负数 也有可能不是 所以负号可有可无 有也是最多1个 因此表达式为 -？
>   	整数部分，可以是1位数 也可以是多位数，1位数是0到9， 多位数的起始位是1到9 剩余位是0到9
>   		因此可以写为 (0|[1-9]\d*)
>   	小数部分 小数点后至少一位数 可有可无 (\.\d+)?
>   	整理为[-]?(0|[1-9]\d*)(\.\d+)?
>   	"""
>     pattern = re.compile(r'[-]?(0|[1-9]\d*)(\.\d+)?')
>     # 列表中存放的是 根据正则表达式匹配到的match对象
>     match_list = pattern.finditer(src_str)   # 也可以用findall，但是会捕获分组
>     # for ele in match_list:
>         #print(ele) # <re.Match object; span=(4, 12), match='-12.2134'>
>     # 用于存放提取match对象中包含的数据
>     value_list = [ele.group() for ele in  match_list]
>     #print(value_list) # ['-12.2134', '38992', '-132', '0.2378', '97']
>     # 因为求和 使用+将列表中的数据拼接
>     express_str = '+'.join(value_list)
>     #print(express_str) #-12.2134+38992+-132+0.2378+97
>     # eval求和并返回
>     return  eval(express_str)
> 
> if __name__ == '__main__':
>     value = input("请输入包含数字的字符串：")
>     res = get_sum(value)
>     print('{}中提取的数值之和为{}'.format(value,res))
> ```