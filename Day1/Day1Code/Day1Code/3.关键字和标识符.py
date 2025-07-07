# 1.关键字
import  keyword
print(keyword.kwlist)

# 2.标识符：自定义
# 快捷键：缩进多行代码：选中----》tab
# 取消缩进：选中----》shift + tab
'''
合法标识符的命名规则：
    - 只能由数字，字母和下划线组成   如 abc%y不合法
    - 不可以是除了下划线之外的其他特殊字符
    - 开头不能是数字或者空格，如：1abc不合法
    - 不能是Python的关键字
    - 严格区分大小写，如：age和Age是两个不同的标识符

标识符的命名规范：
    - 尽量做到见名知意【具有描述性】：尽量使用简单的英文单词表示，安装有道词典/百度翻译
    - 遵守一定的命名规范
      - Python官方推荐的命名方式：变量名，函数名和文件名全小写，使用下划线连接，如：stu_name     check_qq
      - 驼峰命名法：不同的单词之间使用首字母大写的方式进行分隔，又分为大驼峰和小驼峰，比如：stuName就是小驼峰，StuName就是大驼峰，小驼峰常用于变量或者函数的命名，大驼峰常用于类的命名
'''
name1 = 'hdja'
# 1name = 'hdja'
#  name1 = 'gsg'
name_1 = 'err'
# name@1 = '355'

stu_name = 'zhangsan'   # 推荐
stuName = 'faf'      # 小驼峰，不推荐
StuName = 'zhgwerg'  # 大驼峰，在定义类的时候会用到

name = 'aqgtw'