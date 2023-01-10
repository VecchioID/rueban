# -*- coding:utf-8 -*-
# __author__ = 'Vecchio'

from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import argparse


def send_email(sender, send_pwd, receivers, email_server, theme, main_text, if_send_file, path_file, file_name):
    msg = MIMEMultipart()  # 构建主体
    msg['Subject'] = Header(theme, 'utf-8')  # 邮件主题
    msg['From'] = sender  # 发件人
    msg['To'] = Header('python自动发送', 'utf-8')  # 收件人--这里是昵称
    msg.attach(MIMEText(main_text, 'plain', 'utf-8'))  # 构建邮件正文

    # 构建附件 1
    if if_send_file:
        att1 = MIMEText(open(path_file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = file_name
        msg.attach(att1)

    smtp = SMTP_SSL(email_server)  # 指定邮箱服务器
    smtp.ehlo(email_server)  # 部分邮箱需要
    smtp.login(sender, send_pwd)  # 登录邮箱
    smtp.sendmail(sender, receivers, msg.as_string())  # 分别是发件人、收件人、格式
    smtp.quit()  # 结束服务
    print('邮件发送完成--')

'''
demo 如下

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="contents for email")
    parser.add_argument('--main_text', type=str, default='Your Code Finished! Results please see attachment!')
    parser.add_argument('--theme', type=str, default='Notifications for Programs in Server')
    parser.add_argument('--path_to_file', type=str, default='./lrudIR.txt')
    parser.add_argument('--file_name', type=str, default='attachment; filename="test.txt"')
    args = parser.parse_args()

    sender = 'vecchioid@163.com'  # 发件人
    send_pwd = "your 授权码"  # 授权码，邮箱设置
    receivers = ['1715493025@qq.com']  # 接收者
    email_server = "smtp.163.com"
    if_send_file = Fasle
    # 目前为止，下面都是必选参数
    send_email(sender, send_pwd, receivers, email_server, args.theme, args.main_text, if_send_file, args.path_to_file, args.file_name)
    
'''

