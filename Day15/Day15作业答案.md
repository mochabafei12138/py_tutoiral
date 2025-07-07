1.封装一个函数 验证一个年是否是闰年

```
闰年的条件：1. 能被4整除但是不能被100整除 
					2. 能被400整除
				条件1和条件2 满足一个即可
```

```python
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
     return False
y = leap_year(2010)
```

2.封装一个函数 获取指定月的天数

```python
注意： 闰年和平年下  2月份的天数是不一样的
```

```python
def month_day(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
           return 31
    elif month in [4, 6, 9, 11]:
           return 30
    else:
           if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                return 29
           else:
            	return 28
d = month_day(2020, 4)
print(d)
```

3.封装一个函数 获取指定月所属的季节

```
3、4、5春季 6、7、8夏季 9、10、11秋季  12、1、1冬季
```

```python
def judge_quarter(m):
    if m in [3, 4, 5]:
        return '春季'
    elif m in [6, 7, 8]:
        return '夏季'
    elif m in [9, 10, 11]:
        return '秋季'
    else:
        return '冬季'
s = judge_quarter(2)
print(s)
```

4.封装一个函数 验证指定数是否是质数

```
注意：质数：在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
```

```python
def judge_quality(x):
    if type(x) == int:
        if x < 2:
            return False
        else:
            for n in range(2, x):
                if x % n == 0:
                    return False
            else:
                return True
    else:
        return False
p =  judge_quality(12.5)
print(p)
```

5.封装一个函数 验证一个数是否是回文

```
回文： 颠倒过来 与 自身数据一样的称为回文  例如 111  121  1221 12321
```

```python
def judge_return(x):
    x = str(x)
    return x == x[::-1] 
x = 12320
a = judge_return(x)
print(a)
```

6.封装一个函数，获取多个数中的最大值和平均值

```python
def max_average(*x):
    max_value = max(x)
    average = sum(x)/len(x)
    return max_value,average

print(max_average(6,7,8,45))
```

7.封装一个函数 获取多个数中的平均值并统计其中高于平均数的值个数

```python
def average_count(*x):
    average = sum(x) / len(x)
    for i in x:
        if i > average:
            m +=1
    return average, m

a = average_count(1,2,3,4,5,6,7,8,9)
print(a)
```

8.封装一个函数，获取所有的水仙花数

```
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）
```

```python
def narcissistic_number():
    numlist = []
    for num in range(100, 1000):
        num1 = str(num)
        if int(num1[0]) ** 3 + int(num1[1]) ** 3 + int(num1[2]) ** 3 == num:
            numlist.append(num)
    return numlist
        
print(narcissistic_number())
```

