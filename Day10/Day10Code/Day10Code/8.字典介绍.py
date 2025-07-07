# 除了列表之外，Python中另一个比较重要的数据类型是字典

# 1.需求：存储5个学生的成绩
# 用列表表示，问题：如果需要定位或匹配数据，则用列表存储有缺陷
scores_list = [88,99,60,59,100]
print(scores_list)

# 解决：字典【dict】
# 语法：dic = {key1:value1,key2:value2.......}
scores_dict = {'张三':88,'李四':99,'小明':60,'王五':59,'小花':100}
print(scores_dict)

# 2.访问字典中的键值
# a.获取值，
# 方式一：语法：字典[key]
# 注意：通过索引获取列表中的元素，通过key获取字典中对应的value
# 需求：获取小明的成绩
score1 = scores_dict['小明']
print(score1)

# 缺点：如果访问了一个不存在的key，则报错KeyError: '小丽'
# score2 = scores_dict['小丽']

# 方式二：字典.get(key),推荐
score1 = scores_dict.get('小明')
print(score1)

# 优点：当key不存在时，不会报错，会返回None
score2 = scores_dict.get('小丽')
print(score2)

# b.修改值
# 注意：字典和列表一样，都属于可变的数据类型，但是在字典中，一般修改的是指定key对应的值
# 语法：字典[key] = 值

# 1>当key存在时，表示修改指定key对应的值
print(scores_dict)
scores_dict['小明'] = 80
print(scores_dict)

# 2>当key不存在时，表示向字典中添加一对键值对   *******
scores_dict['小丽'] = 77
print(scores_dict)