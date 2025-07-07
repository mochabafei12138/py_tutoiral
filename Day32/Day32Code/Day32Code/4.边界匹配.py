"""
^     行首匹配/边界匹配，和在[]里的^不是一个意思   *****
$     行尾匹配 /边界匹配         *****

\A    匹配字符串开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z    匹配字符串结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾
"""
import re

# 注意1：默写情况下，字符串使用的是单行模式，哪怕字符串中使用\n表示换行
r1 = re.findall(r'^today','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day')
print(r1)   # ['today']
r2 = re.findall(r'day$','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day')
print(r2)  # ['day']

# 注意2：如果要匹配到多行的行首或行尾，则需要设置flags=re.M或flags=re.MULTILINE，才表示多行模式
r1 = re.findall(r'^today','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.MULTILINE)
print(r1)   # ['today', 'today', 'today']
r2 = re.findall(r'day$','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.M)
print(r2)  # ['day', 'day', 'day']

# 注意3:$经常用来限制位数,^用来匹配字符串的开头  ****
qq = '2557746765226272727'
r = re.match(r'[1-9]\d{4,10}$', qq)
print(r)

# 注意4：即使在re.M模式下也不会匹配它行的行首或行尾
r1 = re.findall(r'\Atoday','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.MULTILINE)
print(r1)   # ['today']
r2 = re.findall(r'day\Z','today is a sunny day\ntoday is a sunny day\ntoday is a sunny day',flags=re.M)
print(r2)  # ['day']

