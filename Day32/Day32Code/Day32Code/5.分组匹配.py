"""
x|y      |表示或，匹配的是x或y
(xyz)    匹配小括号内的xyz(作为一个整体去匹配)
"""

import re

# 1
print(re.findall(r'\d+','d3464-kfghj23747abv485'))
print(re.findall(r'[a-z]+','d3464-kfghj23747abv485'))
'''
['3464', '23747', '485']
['d', 'kfghj', 'abv']
'''

# 2.
print(re.findall(r'\d+|[a-z]+','d3464-kfghj23747abv485'))
# ['d', '3464', 'kfghj', '23747', 'abv', '485']

# 3.
print(re.findall(r'(\d+)|[a-z]+','d3464-kfghj23747abv485'))
print(re.findall(r'\d+|([a-z]+)','d3464-kfghj23747abv485'))
'''
['', '3464', '', '23747', '', '485']
['d', '', 'kfghj', '', 'abv', '']
'''

r1 = re.finditer(r'(\d+)|[a-z]+','d3464-kfghj23747abv485')
print([obj.group() for obj in r1])   # ['d', '3464', 'kfghj', '23747', 'abv', '485']

r2 = re.finditer(r'\d+|([a-z]+)','d3464-kfghj23747abv485')
print([obj.group() for obj in r2])  # ['d', '3464', 'kfghj', '23747', 'abv', '485']

# 4.
# a.捕获型分组：正则表达式中有(),findall查找完毕之后只显示()中匹配的内容    *******
print(re.findall(r'(\d+)|[a-z]+','d3464-kfghj23747abv485'))
print(re.findall(r'\d+|([a-z]+)','d3464-kfghj23747abv485'))
'''
['', '3464', '', '23747', '', '485']
['d', '', 'kfghj', '', 'abv', '']
'''

# b.非捕获分组：格式：(?:xxx)
print(re.findall(r'(?:\d+)|[a-z]+','d3464-kfghj23747abv485'))
print(re.findall(r'\d+|(?:[a-z]+)','d3464-kfghj23747abv485'))
'''
['d', '3464', 'kfghj', '23747', 'abv', '485']
['d', '3464', 'kfghj', '23747', 'abv', '485']
'''