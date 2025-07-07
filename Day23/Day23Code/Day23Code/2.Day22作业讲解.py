'''
学生类Student:
		属性:学号，姓名，年龄，性别，成绩

班级类 Grade:
 		属性:班级名称，班级中的学生 【使用列表存储学生】

		方法:
			1.查看该班级中的所有学生的信息
			2.查看指定学号的学生信息
			3.查看班级中成绩不及格的学生信息
			4.将班级中的学生按照成绩降序排序
'''

class Student():
    __slots__ = ('sid','name','age','score')
    def __init__(self,sid,name,age,score):
        self.sid = sid
        self.name = name
        self.age = age
        self.score = score
    def __repr__(self):
        return f'{self.sid}-{self.name}-{self.score}'

class Grade():
    __slots__ = ('grade_name','stus_list')
    def __init__(self,grade_name,stus_list):
        self.grade_name = grade_name
        self.stus_list = stus_list   # 将学生的对象添加到列表中
    def show_all(self):
        print('所有学生的信息如下：')
        for stu in self.stus_list:
            print(stu)  # 调用__init__或__repr__
    def show_single(self,sid):
        print(f'学号为{sid}的学生的信息如下：')
        for stu in self.stus_list:
            if stu.sid == sid:
                print(stu)
                break
        else:
            print('不存在')
    def show_low(self):
        print('不及格学生的信息如下：')
        for stu in self.stus_list:
            if stu.score < 60:
                print(stu)
    def sort_by_score(self):
        print('降序排序之后的信息如下：')
        self.stus_list.sort(reverse=True,key=lambda stu:stu.score)
        self.show_all()

if __name__ == '__main__':
    s1 = Student('1003','小明',19,88)
    s2 = Student('1001', '小王', 17, 100)
    s3 = Student('1005', '小李', 19, 56)
    s4 = Student('1006', '小张', 20, 99)
    s5 = Student('1002', '小赵', 18, 60)

    grade = Grade('千锋2401',[s1,s2,s3,s4,s5])
    grade.show_all()
    grade.show_single('1006')
    grade.show_low()
    grade.sort_by_score()