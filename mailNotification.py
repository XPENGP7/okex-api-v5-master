# 2750265184@qq.com授权码：oumvzgyebrkbdfdc
# luwanspeed@163.com授权码：TUTMCGSJFZPRSNNY

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def mailNotification(i):
    # 设置建立通信的服务器信息
    email_host = 'smtp.163.com'
    # 设置登录邮箱的用户名和密匙
    email_user = 'luwanspeed@163.com'
    email_pass = 'TUTMCGSJFZPRSNNY'
    # 发送邮件的邮箱账户
    sender = 'luwanspeed@163.com'  # 这个其实就是你的用户名+@163.com
    # 接收邮件的邮箱账户
    receivers = ['2874620865@qq.com']  # 这是一个邮箱列表，可以为1到多个

    # 创建一个MIMEMultipart对象，这个对象就相当于一封邮件
    message = MIMEMultipart()
    # 设置发送方
    message['From'] = sender
    # 设置接收方
    message['To'] = ';'.join(receivers)
    # 设置邮件主题，也就是大标题，它是一个字符串
    message['Subject'] = '开仓通知！！！'
    # 文本形式
    content = '快去开仓！！！'
    part1 = MIMEText(content, 'plain', 'utf-8')
    message.attach(part1)

    # 与服务器建立通信并发送邮件
    for i in range(i):
        try:
            receivers = receivers + [sender]
            email_stmp = smtplib.SMTP()
            email_stmp.connect(email_host, 25)  # 请求连接服务器
            email_stmp.login(email_user, email_pass)  # 登录
            email_stmp.sendmail(sender, receivers, message.as_string())  # 发送！
            print('mailNotificationSuccess')
        except smtplib.SMTPException as e:
            print('error', e)