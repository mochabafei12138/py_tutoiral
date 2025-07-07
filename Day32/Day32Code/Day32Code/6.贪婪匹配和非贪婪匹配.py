import re

'''
*和+：贪婪匹配
?:非贪婪匹配

*?和+?：将贪婪匹配转换为非贪婪匹配，只要遇到限制的条件则会停止贪婪匹配
'''

# 1.
print(re.findall(r'd\w+','d3464_kfghj23747abdv485k'))
print(re.findall(r'\w+k','d3464_kfghjk23747abdv485k'))
print(re.findall(r'd\w+k','d3464_kfghjk23747abdv485k'))
'''
['d3464_kfghj23747abdv485k']
['d3464_kfghjk23747abdv485k']
['d3464_kfghjk23747abdv485k']
'''

# 2.
print(re.findall(r'd\w+?','d3464_kfghj23747abdv485k'))
print(re.findall(r'\w+?k','d3464_kfghjk23747abdv485k'))
print(re.findall(r'd\w+?k','d3464_kfghjk23747abdv485k'))
'''
['d3', 'dv']
['d3464_k', 'fghjk', '23747abdv485k']
['d3464_k', 'dv485k']
'''

# 3.
print(re.findall(r'd\w*','d3464_kfghj23747abdv485k'))
print(re.findall(r'\w*k','d3464_kfghjk23747abdv485k'))
print(re.findall(r'd\w*k','d3464_kfghjk23747abdv485k'))
'''
['d3464_kfghj23747abdv485k']
['d3464_kfghjk23747abdv485k']
['d3464_kfghjk23747abdv485k']
'''

# 4.
print(re.findall(r'd\w*?','d3464_kfghj23747abdv485k'))
print(re.findall(r'\w*?k','d3464_kfghjk23747abdv485k'))
print(re.findall(r'd\w*?k','d3464_kfghjk23747abdv485k'))
'''
['d', 'd']
['d3464_k', 'fghjk', '23747abdv485k']
['d3464_k', 'dv485k']
'''