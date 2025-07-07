> 打开md文件：
>
> 安卓/苹果：markdown
>
> 转化为pdf：打开md文件----》文件-----》导出-----》PDF

### 一、Python操作PDF【了解】

#### 1.pdf 简介

> PDF是Portable Document Format的缩写，这类文件通常使用`.pdf`作为其扩展名。在日常开发工作中，最容易遇到的就是从PDF中读取文本内容以及用已有的内容生成PDF文档这两个任务。
>
> 在Python中，可以使用名为`PyPDF2`的三方库来读取PDF文件，可以使用下面的命令来安装它。
>
> ```
> pip install PyPDF2==2.3.1      # 安装指定版本
> pip install PyPDF2          # 安装最新版本
> ```

#### 2.从PDF中提取文本和加密PDF文件

> `PyPDF2`没有办法从PDF文档中提取图像、图表或其他媒体，但它可以提取文本，并将其返回为Python字符串。
>
> 使用`PyPDF2`中的`PdfFileWriter`或`PdfWriter`对象可以为PDF文档加密，如果需要给一系列的PDF文档设置统一的访问口令，使用Python程序来处理就会非常的方便。
>
> ```Python
> # 注意：安装：pypdf2     导入:PyPDF2
> import PyPDF2
> 
> # 1.读取pdf文件中的文本内容
> # a.获取reader对象
> reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
> # b.获取指定页的字典
> print(reader.pages)   # 列表，其中的元素是字典
> page = reader.pages[0]
> print(page)
> # c.获取指定页的文本内容
> # 废弃的函数
> # text = page.extractText()
> # print(text)
> # 更新之后的函数
> text = page.extract_text()    # *****
> print(text)
> '''
> PyPDF2.errors.DeprecationError: extractText is deprecated废弃 and was removed in PyPDF2 3.0.0. Use extract_text instead.
> '''
> 
> # 2.加密pdf文件
> # a.创建writer对象
> writer = PyPDF2.PdfWriter()
> # b.获取已知文件中的每一页，添加到新的文件对象中去
> for i in range(len(reader.pages)):
>     page = reader.pages[i]
>     writer.add_page(page)
> # c.设置加密
> writer.encrypt('abc123')    # *******
> 
> # d.保存文件
> with open(r'data/XGBoost-加密.pdf','wb') as f:
>     writer.write(f)   # 注意和f.write()区别，f.write()只能传参字符串
> ```

#### 3.旋转和创建空白pdf文件

> 可以获得PDF文档的指定页并得到一个`PageObject`对象，通过`PageObject`对象的`rotateClockwise`和`rotateCounterClockwise`方法可以实现页面的顺时针和逆时针方向旋转，通过`PageObject`对象的`add_blank_page`方法可以添加一个新的空白页
>
> ```Python
> import  PyPDF2
> 
> # 1.旋转
> # a.创建reader和writer对象
> reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
> writer = PyPDF2.PdfWriter()
> 
> # b.旋转
> # 需求1：将第0页顺时针旋转180
> # page_0 = reader.pages[0]
> # # page_0.rotate(angle),angle为正数：顺时针旋转   angle为负数：逆时针旋转
> # page_0.rotate(-90)
> # writer.add_page(page_0)
> 
> # 需求2：批量旋转
> for i in range(len(reader.pages)):
>     page = reader.pages[i]
>     if i % 2 == 0:
>         page.rotate(90)     # ******
>     else:
>         page.rotate(-90)
>     writer.add_page(page)
> 
> # c.添加空白pdf
> writer.add_blank_page()
> 
> # 注意：如果打开新生成的文件，报错文件损坏，则可能是writer是空的
> with open(r'data/XGBoost-旋转.pdf','wb') as f:
>     writer.write(f)
> 
> ```

#### 4.批量添加水印【掌握】

> 上面提到的`PageObject`对象还有一个名为`mergePage`的方法，可以两个PDF页面进行叠加，通过这个操作，我们很容易实现给PDF文件添加水印的功能。例如要给上面的“XGBoost.pdf”文件添加一个水印，我们可以先准备好一个提供水印页面的PDF文件，然后将包含水印的`PageObject`读取出来，然后再循环遍历“XGBoost.pdf”文件的每个页，获取到`PageObject`对象，然后通过`mergePage`方法实现水印页和原始页的合并
>
> ```Python
> import PyPDF2
> 
> # 1.创建reader和writer对象
> src_reader = PyPDF2.PdfReader(r'data/XGBoost.pdf')
> water_reader = PyPDF2.PdfReader(r'data/watermark.pdf')
> writer = PyPDF2.PdfWriter()
> 
> # 2.遍历已知文件的每一页对象，和水印页进行合并，最终将合并之后的结果添加到writer中
> water_page = water_reader.pages[0]  # 获取水印页对象
> for i in range(len(src_reader.pages)):
>     src_page = src_reader.pages[i]  # 获取原文件每一页的对象
>     # 合并
>     # a.merge_page(b):将b合并到a上
>     src_page.merge_page(water_page)   # *****
>     # 将合并之后的对象添加给writer
>     writer.add_page(src_page)
> 
> with open(r'data/XGBoost-添加水印.pdf','wb') as f:
>     writer.write(f)
> ```

### 二、发送邮件【重要】

#### 1.概念

> SMTP(Simple Mail Transfer Protocol)，即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。 
>
> python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。
>
> Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
>
> Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负 责发送邮件。

#### 2.邮件服务器设置

> 1.设置发送方的qq 邮箱
>
> - 选取邮箱设置
>
>   ![发送邮件1](Day29-images/发送邮件1.png)
>
> - 开启smtp协议
>
>   ![发送邮件2](Day29-images/%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B62.png)
>
> - 发送短信获取授权码
>
>   ![发送邮件3](Day29-images/发送邮件3.png)
>
> - 获取qq邮箱授权码
>
>   ![发送邮件4](Day29-images/发送邮件4.png)



> 2.设置发送方163 邮箱
>
> - 选取邮箱设置
>
>   ![网易邮箱1](Day29-images/网易邮箱1.png)
>
> - 开启smtp协议
>
>   ![网易邮箱2](Day29-images/网易邮箱2.png)
>
>   ![网易邮箱3](Day29-images/网易邮箱3.png)
>
> - 打开网易邮箱大师，扫码发送短信获取授权码
>
>   ![网易邮箱4](Day29-images/网易邮箱4.png)
>
> - 获取qq邮箱授权码
>
>   ![网易邮箱5](Day29-images/网易邮箱5.png)

#### 3.发送邮件流程

> 1. 登录邮箱
>
>    ```
>     import smtplib 
>    1. 连接邮箱服务器
>    	 连接对象 = smtplip.SMTP_SSL(服务器地址, 邮箱服务端口)
>       - 服务器地址:smtp.163.com(163邮箱)、smtp.qq.com(qq邮箱) - 邮箱服务端口:465
>    2. 登录邮箱
>       	连接对象.login(邮箱账号, 授权码)
>    ```
>
> 2. 准备数据
>
>    ```
>    数据指的需要发送的内容。邮件内容的构建需要涉及到另外一个库email，它可以用来构建邮件主题以及各种形式的邮件内容，包括文字内容、图片内容、html内容、附件等
>    
>    from email.mime.multipart
>    import MIMEMultipart
>    from email.mime.text import MIMEText
>    from email.header import Header
>    1. 创建邮件对象
>    		邮件对象 = MIMEMultipart()
>    2. 设置邮件主题
>    		主题对象 = Header(邮件标题, 编码方式).encode()
>    		邮件对象['Subject'] = 主题对象
>    3.设置邮件发送者
>    		邮件对象['From'] = '用户名 <用户名>' 4.设置邮件接受者
>    		邮件对象['To'] = '收件人1;收件人2;收件人3...' 5. 添加文文字内容
>    		文字内容对象 = MIMEText(内容, 类型, 编码方式) - 内容:就是文字符串串
>    		- 类型:plain(简单的文字内容)、html(超文本)
>    		邮件对象.attach(文字对象)
>    ```
>
> 3. 发送邮件
>
>    ```
>    1.连接对象.sendmail(发件人, 收件人, 邮件对象.as_string()) 
>    2.连接对象.quit()
>    ```

#### 4.实现

##### 4.1发送文本

> 注意：有时候会涉及到发送 html邮件，html格式的邮件本质还是文本格式的邮件，所有文件的构建方式和普通文本文件的构建方式差不多:
>
> ```
> from email.mime.text import MIMEText
> 文本对象 = MIMEText(内容字符串, 'html', 编码方式) 
> 邮件对象.attach(文本对象)
> ```

> ```Python
> '''
> 获取发送方邮箱的授权码：
>     qq授权码：qzoepkfnqecxhddc
>     163授权码:HRHVSCXKGSVWYRKG
> 
> 发送方的SMTP服务器:
>     smtp.163.com
>     smtp.qq.com
>     smtp.126.com
> '''
> 
> # 需求：发送方：163邮箱  接受方：qq，同学的qq，163
> # 一、导入模块
> import  smtplib   # 发送邮件
> from email.mime.text import MIMEText    # emial:构建邮件      MIMEText：文本对象
> 
> # 二、封装函数：
> # 发送方账号
> sender_account = '18501970795@163.com'
> # 接收方账号
> recivers_acount = ['1490980468@qq.com','2440311490@qq.com']
> # a.构建邮件
> def form_email():
>     # 创建MIMEText对象
>     data = MIMEText('今天星期四，天气很好~~~~')
>     # 主题
>     data['Subject'] = '通过Python发送纯文本文件'
>     # 发送方
>     data["From"] = sender_account
>     # 接收方
>     data["To"] = ';'.join(recivers_acount)
>     return data
> 
> # b.发送邮件
> def send_email():
>     data = form_email()
> 
>     # smtp服务器
>     mail_host = 'smtp.163.com'
>     # 创建连接对象
>     smtp_obj = smtplib.SMTP_SSL(mail_host,465)
>     # 登录发送方的邮箱账号，需要给定授权码,注意：不是邮箱的登录密码
>     sender_allow_pwd  = 'HRHVSCXKGSVWYRKG'
>     smtp_obj.login(sender_account,sender_allow_pwd)
>     print('邮箱登录成功~~~~~~')
>     # 发送邮件
>     smtp_obj.sendmail(sender_account,recivers_acount,data.as_string())
>     # 退出
>     smtp_obj.quit()
>     print('邮件发送成功~~~~~~')
> 
> if __name__ == '__main__':
>     send_email()
> 
>     # 注意：运行该程序之前，可以先关闭防火墙，杀毒软件
> ```

##### 4.2发送html

> ```Python
> # 需求：发送方：163邮箱  接受方：qq，同学的qq，163
> # 一、导入模块
> import  smtplib   # 发送邮件
> from email.mime.text import MIMEText    # emial:构建邮件      MIMEText：文本对象
> from email.mime.multipart import MIMEMultipart   # 构建多个内容
> 
> # 二、封装函数：
> # 发送方账号
> sender_account = '18501970795@163.com'
> # 接收方账号
> recivers_acount = ['1490980468@qq.com','2440311490@qq.com']
> 
> # a.构建邮件
> def form_email():
>     # 创建MIMEText对象
>     data = MIMEMultipart()
>     # 主题
>     data['Subject'] = '通过Python发送html文本文件'
>     # 发送方
>     data["From"] = sender_account
>     # 接收方
>     data["To"] = ';'.join(recivers_acount)
>     # 正文：html文本
>     html_str = '''
>     <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>Title</title>
> </head>
> <body>
> <h1>html邮件正文内容</h1>
> <ol>
>     <li>教学部</li>
>     <li>行政部</li>
>     <li>财务部</li>
>     <li>运营部</li>
> </ol>
> <table width="500" border="1" cellspacing="0">
>     <tr align="center">
>         <td>姓名</td>
>         <td>年龄</td>
>         <td>性别</td>
>         <td>地址</td>
>     </tr>
>     <tr align="center">
>         <td>张明</td>
>         <td>10</td>
>         <td>male</td>
>         <td>上海</td>
>     </tr>
>     <tr align="center">
>         <td>小王</td>
>         <td>11</td>
>         <td>female</td>
>         <td>北京</td>
>     </tr>
> </table>
> </body>
> </html>
>     '''
>     text = MIMEText(html_str,'html','utf-8')   # utf-8是文本内容的编码格式
>     data.attach(text)
>     return data
> 
> # b.发送邮件
> def send_email():
>     data = form_email()
> 
>     # smtp服务器
>     mail_host = 'smtp.163.com'
>     # 创建连接对象
>     smtp_obj = smtplib.SMTP_SSL(mail_host,465)
>     # 登录发送方的邮箱账号，需要给定授权码,注意：不是邮箱的登录密码
>     sender_allow_pwd  = 'HRHVSCXKGSVWYRKG'
>     smtp_obj.login(sender_account,sender_allow_pwd)
>     print('邮箱登录成功~~~~~~')
>     # 发送邮件
>     smtp_obj.sendmail(sender_account,recivers_acount,data.as_string())
>     # 退出
>     smtp_obj.quit()
>     print('邮件发送成功~~~~~~')
> 
> if __name__ == '__main__':
>     send_email()
> 
>     # 注意：运行该程序之前，可以先关闭防火墙，杀毒软件
> ```

##### 4.3发送图片

> ```
> from email.mime.image import MIMEImage
> 图片对象 = MIMEImage(图片二进制数据)
> ```

> ```Python
> # 需求：发送方：163邮箱  接受方：qq，同学的qq，163
> # 一、导入模块
> import  smtplib   # 发送邮件
> from email.mime.text import MIMEText    # emial:构建邮件      MIMEText：文本对象
> from email.mime.multipart import MIMEMultipart   # 构建多个内容
> from email.mime.image import MIMEImage   # 图片
> 
> # 二、封装函数：
> # 发送方账号
> sender_account = '18501970795@163.com'
> # 接收方账号
> recivers_acount = ['1490980468@qq.com','2440311490@qq.com']
> 
> # a.构建邮件
> def form_email():
>     # 创建MIMEText对象
>     data = MIMEMultipart()
>     # 主题
>     data['Subject'] = '通过Python发送html文本文件'
>     # 发送方
>     data["From"] = sender_account
>     # 接收方
>     data["To"] = ';'.join(recivers_acount)
> 
>     # 正文内容：图片
>     with open(r'data/logo.png','rb') as f:
>         img_data = f.read()
>     # 构建图片对象
>     img = MIMEImage(img_data)
>     img.add_header('Content-ID','testimg')
>     html_str = """
>     <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>Title</title>
> </head>
> <body>
> <h1>图片邮件内容</h1>
> <p>
>     <img src="cid:testimg">
> </p>
> </body>
> </html>
>     """
>     text = MIMEText(html_str, 'html', 'utf-8')
>     # 附加文本
>     data.attach(text)
>     # 附加图片
>     data.attach(img)
>     return data
> 
> # b.发送邮件
> def send_email():
>     data = form_email()
> 
>     # smtp服务器
>     mail_host = 'smtp.163.com'
>     # 创建连接对象
>     smtp_obj = smtplib.SMTP_SSL(mail_host,465)
>     # 登录发送方的邮箱账号，需要给定授权码,注意：不是邮箱的登录密码
>     sender_allow_pwd  = 'HRHVSCXKGSVWYRKG'
>     smtp_obj.login(sender_account,sender_allow_pwd)
>     print('邮箱登录成功~~~~~~')
>     # 发送邮件
>     smtp_obj.sendmail(sender_account,recivers_acount,data.as_string())
>     # 退出
>     smtp_obj.quit()
>     print('邮件发送成功~~~~~~')
> 
> if __name__ == '__main__':
>     send_email()
> 
>     # 注意：运行该程序之前，可以先关闭防火墙，杀毒软件
> ```

##### 4.4发送文件附件

> ```
> from email.mime.text import MIMEText
> 文件对象 = MIMEText(文件二进制数据, 'base64', 编码方式) 
> 文件对象["Content-Disposition"] = 'attachment; filename="文件名"' 
> 邮件对象.attach(文件对象)
> ```

> ```Python
> # 需求：发送方：163邮箱  接受方：qq，同学的qq，163
> # 一、导入模块
> import  smtplib   # 发送邮件
> from email.mime.text import MIMEText    # emial:构建邮件      MIMEText：文本对象
> from email.mime.multipart import MIMEMultipart   # 构建多个内容
> 
> # 二、封装函数：
> # 发送方账号
> sender_account = '18501970795@163.com'
> # 接收方账号
> recivers_acount = ['1490980468@qq.com','2440311490@qq.com']
> 
> # a.构建邮件
> def form_email():
>     # 创建MIMEText对象
>     data = MIMEMultipart()
>     # 主题
>     data['Subject'] = '通过Python发送html文本文件'
>     # 发送方
>     data["From"] = sender_account
>     # 接收方
>     data["To"] = ';'.join(recivers_acount)
> 
>     # 附件
>     with open(r'data/致橡树.txt','r',encoding='gbk') as f:
>         file_data = f.read()
>     # 构建文本对象
>     text = MIMEText(file_data, 'base64', 'gbk')  # gbk是文件的编码格式
>     # 将文本对象设置为附件
>     text["Content-Disposition"] = 'attachment; filename="lianxi.txt"'
>     # 附加文本
>     data.attach(text)
>     return data
> 
> # b.发送邮件
> def send_email():
>     data = form_email()
> 
>     # smtp服务器
>     mail_host = 'smtp.163.com'
>     # 创建连接对象
>     smtp_obj = smtplib.SMTP_SSL(mail_host,465)
>     # 登录发送方的邮箱账号，需要给定授权码,注意：不是邮箱的登录密码
>     sender_allow_pwd  = 'HRHVSCXKGSVWYRKG'
>     smtp_obj.login(sender_account,sender_allow_pwd)
>     print('邮箱登录成功~~~~~~')
>     # 发送邮件
>     smtp_obj.sendmail(sender_account,recivers_acount,data.as_string())
>     # 退出
>     smtp_obj.quit()
>     print('邮件发送成功~~~~~~')
> 
> if __name__ == '__main__':
>     send_email()
> 
>     # 注意：运行该程序之前，可以先关闭防火墙，杀毒软件
> 
> ```