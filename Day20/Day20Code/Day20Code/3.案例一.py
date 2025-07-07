'''
需求：开学了，王老师让小明，小花，小丽做自我介绍
    介绍内容包括：姓名，年龄，爱好
    展示一段才艺
'''

'''
分析：
    a.定义教师类和学生类
    b.教师类
        特征：姓名
        行为：让 学生 做自我介绍
    c.学生类
        特征：姓名，年龄，爱好
        行为：做 自我介绍
             才艺展示
'''
# 第一步：定义类
class Teacher():
    # self表示老师对象，stu是一个学生对象,只要一个变量表示的是某个对象，则该变量作为对象使用，可以访问对象的属性或类中的函数
    def let_stu_introduce(self,stu):
        print(stu)
        print(f'{self.name}让{stu.name}做自我介绍')
        # 学生开始执行自己的行为：做自我介绍和才艺战术
        stu.introduce()
        stu.show_talent()

class Student():
    def introduce(self):
        print(f'大家好，我是{self.name},今年{self.age},爱好{self.hobby}')
    def show_talent(self):
        if self.name == '小明':
            print(f'接下来给大家展示一段{self.hobby},我家里有几百头牛，几百头🐏~~~~')
        elif self.name == '小花':
            print(f'接下来给大家展示一段{self.hobby},一起来摇摆~~~~')
        elif self.name == '小丽':
            print(f'接下来给大家展示一段{self.hobby},看谁在唱歌~~~~')

# 第二步：创建对象并描述特征
tea = Teacher()
tea.name = '王老师'

stu1 = Student()
stu1.name = '小明'
stu1.age = 18
stu1.hobby = '吹牛逼'

stu2 = Student()
stu2.name = '小花'
stu2.age = 17
stu2.hobby = '跳舞'

stu3 = Student()
stu3.name = '小丽'
stu3.age = 19
stu3.hobby = '唱歌'

# 第三步：在类中定义函数并调用函数
tea.let_stu_introduce(stu2)
tea.let_stu_introduce(stu1)
tea.let_stu_introduce(stu3)

