# 需求：发送方：163邮箱  接受方：qq，同学的qq，163
# 一、导入模块
import  smtplib   # 发送邮件
from email.mime.text import MIMEText    # emial:构建邮件      MIMEText：文本对象
from email.mime.multipart import MIMEMultipart   # 构建多个内容

# 二、封装函数：
# 发送方账号
sender_account = '18501970795@163.com'
# 接收方账号
recivers_acount = ['1490980468@qq.com','2440311490@qq.com']

# a.构建邮件
def form_email():
    # 创建MIMEText对象
    data = MIMEMultipart()
    # 主题
    data['Subject'] = '通过Python发送html文本文件'
    # 发送方
    data["From"] = sender_account
    # 接收方
    data["To"] = ';'.join(recivers_acount)
    # 正文：html文本
    html_str = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>html邮件正文内容</h1>
<ol>
    <li>教学部</li>
    <li>行政部</li>
    <li>财务部</li>
    <li>运营部</li>
</ol>
<table width="500" border="1" cellspacing="0">
    <tr align="center">
        <td>姓名</td>
        <td>年龄</td>
        <td>性别</td>
        <td>地址</td>
    </tr>
    <tr align="center">
        <td>张明</td>
        <td>10</td>
        <td>male</td>
        <td>上海</td>
    </tr>
    <tr align="center">
        <td>小王</td>
        <td>11</td>
        <td>female</td>
        <td>北京</td>
    </tr>
</table>
</body>
</html>
    '''
    text = MIMEText(html_str,'html','utf-8')   # utf-8是文本内容的编码格式
    data.attach(text)
    return data

# b.发送邮件
def send_email():
    data = form_email()

    # smtp服务器
    mail_host = 'smtp.163.com'
    # 创建连接对象
    smtp_obj = smtplib.SMTP_SSL(mail_host,465)
    # 登录发送方的邮箱账号，需要给定授权码,注意：不是邮箱的登录密码
    sender_allow_pwd  = 'HRHVSCXKGSVWYRKG'
    smtp_obj.login(sender_account,sender_allow_pwd)
    print('邮箱登录成功~~~~~~')
    # 发送邮件
    smtp_obj.sendmail(sender_account,recivers_acount,data.as_string())
    # 退出
    smtp_obj.quit()
    print('邮件发送成功~~~~~~')

if __name__ == '__main__':
    send_email()

    # 注意：运行该程序之前，可以先关闭防火墙，杀毒软件
