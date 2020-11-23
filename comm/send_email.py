#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/8/16 9:16
# @Author : Administrator
# @File : send_email.py
# @Project : python_demo
# @title :

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import os


class SendEmail:
    def email(self, body, attach):
        sender = 'student@woniuxy.com'  # 发送邮箱
        receivers = '710957229@qq.com'  # 接收邮箱

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # message = MIMEText('<p style="color: red; font-size: 30px">这是一封来自Python发送的测试邮件的内容...</p>', 'html', 'utf-8')
        # message['Subject'] = Header('一封Python发送的邮件', 'utf-8')

        msg = MIMEMultipart()
        msg['Subject'] = 'WoniuSalesCI测试报告'
        msg['From'] = sender
        msg['To'] = receivers

        content = MIMEText(body, 'html', 'utf-8')
        msg.attach(content)

        attachment = MIMEApplication(open(attach, 'rb').read())
        attachment.add_header('Content-Disposition', 'attachment', filename='report.rar')
        msg.attach(attachment)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect('mail.woniuxy.com', '25')
            smtpObj.login(user='student@woniuxy.com', password='Student123')
            smtpObj.sendmail(sender, receivers, str(msg))
            smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


if __name__ == '__main__':
    SM=SendEmail()
    path=(os.path.abspath('../testreport/report.html'))
    with open(path,'r',encoding="utf-8") as file:
        body=file.read()
    SM.email(body,r"../testreport/\report.rar")
