# 需求：根据已知的员工信息，批量生成每个员工的离职证明文件，每个人的文件以该员工的姓名命名
from docx import  Document
# 将真实的员工信息保存在字典中
person_list = [
    {
        "name":"杨天偿",
        "id":"333222199909120987",
        "sdate":"2017年7月1日",
        "edate":"2021年11月1日",
        "department":"技术部",
        "position":"架构师",
        "company":"深圳华为技术有限公司"
    },
    {
        "name":"刘一奇",
        "id":"110120198909120937",
        "sdate":"2016年3月1日",
        "edate":"2020年10月1日",
        "department":"行政部",
        "position":"保镖",
        "company":"黑龙江"
    },
    {
        "name":"张国涛",
        "id":"111222199908120987",
        "sdate":"2015年4月1日",
        "edate":"2019年11月1日",
        "department":"后厨部",
        "position":"试吃员",
        "company":"深圳市金威源餐饮有限公司"
    },
    {
        "name":"欧阳",
        "id":"112221199909120987",
        "sdate":"2016年7月1日",
        "edate":"2020年11月1日",
        "department":"后勤部",
        "position":"主管",
        "company":"深圳市abc有限公司"
    },
    {
        "name":"张三",
        "id":"112221199909120987",
        "sdate":"2016年7月1日",
        "edate":"2020年11月1日",
        "department":"后勤部",
        "position":"主管",
        "company":"深圳市abc有限公司"
    },
    {
        "name":"李四",
        "id":"112221199909120987",
        "sdate":"2016年7月1日",
        "edate":"2020年11月1日",
        "department":"后勤部",
        "position":"主管",
        "company":"深圳市abc有限公司"
    }
]

# 实现思路：读取离职证明的模板文件 ，将其中的占位符替换为已知数据中的值
# 遍历列表，批量读取离职证明的模板文件，批量生成离职证明文件
for person in person_list:
    # 1.读取离职证明的模板文件
    doc = Document(r'data/离职证明模板.docx')

    # 2.遍历段落，进行数据的处理【将包含占位符的run筛选出来】
    for p in doc.paragraphs:
        if '{' not in p.text:
            continue
       # 3.遍历每个段落中的runs
        for run in p.runs:
            if '{' not in run.text:
                continue
            # 4.完成替换操作：将离职证明模板中的{xxx}的内容替换为字段中指定key对应的值
            # '{name}'------>'name'---->对应的就是字典中的key
            # '{department}'------>'{department}'----->对应的就是字典中的key
            # print(run.text)
            # 字符串切片
            # print(run.text[1:-1],type(run.text[1:-1]))
            key = run.text[1:-1]
            print(person[key])
            # 替换：xxx.repalce():因为字符串是不可变的，所以替换之后会生成一个新的字符串，将新的字符串重新赋值给run.text
            # {name} ---->张三
            run.text = run.text.replace(run.text,person[key])

    # 将处理之后的数据进行保存，生成新的doc文件
    doc.save(rf'data/{person["name"]}的离职证明.docx')
    print(f'{person["name"]}的离职证明文件已生成~~~~~')


