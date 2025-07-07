### Day27作业讲解

> ```Python
> # 方式一
> import  openpyxl,os
> # 获取数据，然后整合数据
> result_list = []
> header_list = []
> def read_data(xlpath):
>     # old_wb = openpyxl.load_workbook(fr'data/小宝剑大药房（{xlname}）2018年销售数据.xlsx')
>     old_wb = openpyxl.load_workbook(xlpath)  # xlpath表示文件路径
>     old_sheet = old_wb.active
>     global  header_list
>     header_list = [cell.value for cell in old_sheet[2]]
>     for row in range(3,old_sheet.max_row + 1):
>         sublist = [cell.value for cell in old_sheet[row] if cell.value != None]
>         if sublist:
>             result_list.append(sublist)
> 
> # 写入数据
> def write_data():
>     new_wb = openpyxl.Workbook()
>     new_sheet = new_wb.active
>     new_sheet.title = '药店汇总数据'
>     # 写入表头
>     new_sheet.append(header_list)
>     # 写入正文
>     for row in result_list:
>         new_sheet.append(row)
> 
>     # 保存
>     new_wb.save(r'data/药店汇总数据.xlsx')
> 
> if __name__ == '__main__':
>     # 文件较少的情况，可以手动书写
>     # xlnames_list = ['高新店','犀浦店','新津店']
>     # 文件较多，则借助于os/glob模块
>     '''
>     import glob
>     xlnames_list = glob.glob('data/*.xlsx')
>     for xlname in xlnames_list:
>         read_data(xlname)
>     '''
>     path = r'data'
>     xlnames_list = os.listdir(path)
>     for xlname in xlnames_list:
>         filepath = os.path.join(path,xlname)
>         read_data(filepath)
>     write_data()
> ```

### 一、操作Word

#### 1.简介

> ​	在日常工作中，有很多简单重复的劳动其实完全可以交给Python程序，比如根据样板文件（模板文件）批量的生成很多个Word文件或PowerPoint文件。Word是微软公司开发的文字处理程序，相信大家都不陌生，日常办公中很多正式的文档都是用Word进行撰写和编辑的，目前使用的Word文件后缀名一般为`.docx`。PowerPoint是微软公司开发的演示文稿程序，是微软的Office系列软件中的一员，被商业人士、教师、学生等群体广泛使用，通常也将其称之为“幻灯片”。在Python中，可以使用名为`python-docx` 的三方库来操作Word

> 我们可以先通过下面的命令来安装`python-docx`三方库。
>
> ```python
> # 一般情况下
> pip install python-docx
> # 注意：我们在安装此模块使用的是pip install python-docx，但是在导入的时候是 docx
> # 说明：只需要执行pip install python-docx，会自动安装lxml
>
> # 可能出现问题：
> 高版本lxml没有etree模块。有网友确定lxml4.2.5版本带有etree模块，且该版本lxml支持python3.7.4版本。安装命令：
> pip install lxml==4.2.5  (若python-docx 使用有问题,需要查看lxml版本)
> ```

#### 2.向Word写入内容

> ```Python
> # 注意1：我们在安装此模块使用的是pip install python-docx，但是在导入的时候是 docx
> # 注意2：一般情况下，如果安装了A库，同时自动安装了依赖B库，如果A库更新了，如果使用过程中报错，则可以更新依赖库
> 
> # C:\Users\19621>pip install python-docx
> # Collecting python-docx
> #   Downloading python_docx-1.1.0-py3-none-any.whl (239 kB)
> #      |████████████████████████████████| 239 kB 930 kB/s
> # Requirement already satisfied: lxml>=3.1.0 in d:\software\anaconda\lib\site-packages (from python-docx) (4.6.3)
> # Requirement already satisfied: typing-extensions in d:\software\anaconda\lib\site-packages (from python-docx) (4.9.0)
> # Installing collected packages: python-docx
> # Successfully installed python-docx-1.1.0
> 
> # 比如：安装python-docx的过程中，自动安装了依赖库lxml和typing-extensions
> 
> from docx import  Document
> from docx.shared import Cm
> 
> # 1.创建doc文档对象
> doc = Document()
> # 2.添加标题
> doc.add_heading('今天星期二~~~~')
> # 3.添加段落
> p = doc.add_paragraph('第一个段落~~~~')
> # 注意：一个段落可以由很多个run组成
> run1 = p.add_run('this is a test')
> run2 = p.add_run('Python是一门面向对象的语言')
> run3 = p.add_run('Python是跨平台的')
> 
> # 给每个run可以单独设置样式
> run1.bold = True
> run2.underline = True
> 
> # 4.添加图片
> doc.add_picture(r'data/3.png',width=Cm(10))
> 
> # 5.添加列表
> # a.有序列表
> doc.add_paragraph('教学部',style='List Number')
> doc.add_paragraph('运营部',style='List Number')
> doc.add_paragraph('财务部',style='List Number')
> doc.add_paragraph('行政部',style='List Number')
> doc.add_paragraph('市场部',style='List Number')
> 
> # b.无序列表
> doc.add_paragraph('教学部',style='List Bullet')
> doc.add_paragraph('运营部',style='List Bullet')
> doc.add_paragraph('财务部',style='List Bullet')
> doc.add_paragraph('行政部',style='List Bullet')
> doc.add_paragraph('市场部',style='List Bullet')
> 
> # 保存文件
> doc.save(r'data/Python操作word.docx')
> ```

#### 3.读取Word内容

> ```Python
> from docx import  Document
> 
> # 1.打开doc
> doc = Document(r'data/占勇辉的离职证明.docx')
> 
> # 2.获取doc中的所有内容，返回一个列表，其中的元素是段落对象
> print(doc.paragraphs)
> 
> # 3.遍历列表，获取每个段落对象
> for para in doc.paragraphs:
>     # 获取每个段落的文本
>     # print(para.text)
>     # 获取组成每个段落的run，返回一个列表
>     print(para.runs)
>     for run in para.runs:
>         # 获取每个run的文本
>         print(run.text)
> 
> ```

#### 4.批量生成Word文件【掌握】

> 试想，我们如果把上面的离职证明制作成一个模板文件，把姓名、身份证号、入职和离职日期等信息用占位符代替，这样通过对占位符的替换，就可以根据实际需要写入对应的信息，这样就可以批量的生成Word文档。

> 实现思路：
>
> 1. 首先编辑一个离职证明的模板文件，如下图所示。
>
>    ![离职证明模板](data/离职证明模板.png)
>
> 2. 接下来我们读取该文件，将占位符替换为真实信息，就可以生成一个新的Word文档，如下所示。
>
>    ```python
>    # 将真实的员工信息保存在字典中
>    person_list = [
>        {
>            "name":"杨天偿",
>            "id":"333222199909120987",
>            "sdate":"2017年7月1日",
>            "edate":"2021年11月1日",
>            "department":"技术部",
>            "position":"架构师",
>            "company":"深圳华为技术有限公司"
>        },
>        {
>            "name":"刘一奇",
>            "id":"110120198909120937",
>            "sdate":"2016年3月1日",
>            "edate":"2020年10月1日",
>            "department":"行政部",
>            "position":"保镖",
>            "company":"黑龙江"
>        },
>        {
>            "name":"张国涛",
>            "id":"111222199908120987",
>            "sdate":"2015年4月1日",
>            "edate":"2019年11月1日",
>            "department":"后厨部",
>            "position":"试吃员",
>            "company":"深圳市金威源餐饮有限公司"
>        },
>        {
>            "name":"欧阳",
>            "id":"112221199909120987",
>            "sdate":"2016年7月1日",
>            "edate":"2020年11月1日",
>            "department":"后勤部",
>            "position":"主管",
>            "company":"深圳市abc有限公司"
>        },
>    ]
>    ```

> ```Python
> # 需求：根据已知的员工信息，批量生成每个员工的离职证明文件，每个人的文件以该员工的姓名命名
> from docx import  Document
> # 将真实的员工信息保存在字典中
> person_list = [
>     {
>         "name":"杨天偿",
>         "id":"333222199909120987",
>         "sdate":"2017年7月1日",
>         "edate":"2021年11月1日",
>         "department":"技术部",
>         "position":"架构师",
>         "company":"深圳华为技术有限公司"
>     },
>     {
>         "name":"刘一奇",
>         "id":"110120198909120937",
>         "sdate":"2016年3月1日",
>         "edate":"2020年10月1日",
>         "department":"行政部",
>         "position":"保镖",
>         "company":"黑龙江"
>     },
>     {
>         "name":"张国涛",
>         "id":"111222199908120987",
>         "sdate":"2015年4月1日",
>         "edate":"2019年11月1日",
>         "department":"后厨部",
>         "position":"试吃员",
>         "company":"深圳市金威源餐饮有限公司"
>     },
>     {
>         "name":"欧阳",
>         "id":"112221199909120987",
>         "sdate":"2016年7月1日",
>         "edate":"2020年11月1日",
>         "department":"后勤部",
>         "position":"主管",
>         "company":"深圳市abc有限公司"
>     },
>     {
>         "name":"张三",
>         "id":"112221199909120987",
>         "sdate":"2016年7月1日",
>         "edate":"2020年11月1日",
>         "department":"后勤部",
>         "position":"主管",
>         "company":"深圳市abc有限公司"
>     },
>     {
>         "name":"李四",
>         "id":"112221199909120987",
>         "sdate":"2016年7月1日",
>         "edate":"2020年11月1日",
>         "department":"后勤部",
>         "position":"主管",
>         "company":"深圳市abc有限公司"
>     }
> ]
> 
> # 实现思路：读取离职证明的模板文件 ，将其中的占位符替换为已知数据中的值
> # 遍历列表，批量读取离职证明的模板文件，批量生成离职证明文件
> for person in person_list:
>     # 1.读取离职证明的模板文件
>     doc = Document(r'data/离职证明模板.docx')
> 
>     # 2.遍历段落，进行数据的处理【将包含占位符的run筛选出来】
>     for p in doc.paragraphs:
>         if '{' not in p.text:
>             continue
>        # 3.遍历每个段落中的runs
>         for run in p.runs:
>             if '{' not in run.text:
>                 continue
>             # 4.完成替换操作：将离职证明模板中的{xxx}的内容替换为字段中指定key对应的值
>             # '{name}'------>'name'---->对应的就是字典中的key
>             # '{department}'------>'{department}'----->对应的就是字典中的key
>             # print(run.text)
>             # 字符串切片
>             # print(run.text[1:-1],type(run.text[1:-1]))
>             key = run.text[1:-1]
>             print(person[key])
>             # 替换：xxx.repalce():因为字符串是不可变的，所以替换之后会生成一个新的字符串，将新的字符串重新赋值给run.text
>             # {name} ---->张三
>             run.text = run.text.replace(run.text,person[key])
> 
>     # 将处理之后的数据进行保存，生成新的doc文件
>     doc.save(rf'data/{person["name"]}的离职证明.docx')
>     print(f'{person["name"]}的离职证明文件已生成~~~~~')
> ```