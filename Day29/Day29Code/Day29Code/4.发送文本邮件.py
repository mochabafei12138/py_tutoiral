'''
获取发送方邮箱的授权码：
    qq授权码：qzoepkfnqecxhddc
    163授权码:HRHVSCXKGSVWYRKG

发送方的SMTP服务器:
    smtp.163.com
    smtp.qq.com
    smtp.126.com
'''

# 需求：发送方：163邮箱  接受方：qq，同学的qq，163
# 一、导入模块
import  smtplib   # 发送邮件
from email.mime.text import MIMEText    # emial:构建邮件      MIMEText：文本对象

# 二、封装函数：
# 发送方账号
sender_account = '18501970795@163.com'
# 接收方账号
recivers_acount = ['1490980468@qq.com','2440311490@qq.com']
# a.构建邮件
def form_email():
    # 创建MIMEText对象
    data = MIMEText('今天星期四，天气很好~~~~')
    # 主题
    data['Subject'] = '通过Python发送纯文本文件'
    # 发送方
    data["From"] = sender_account
    # 接收方
    data["To"] = ';'.join(recivers_acount)
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

