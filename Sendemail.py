#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

import smtplib


# 格式化一个邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))  # 如果包含中文，需要通过Header对象进行编码


from_addr = "447296650@qq.com"
password = "xrmbtbhlqipfbjch"
to_addr = "feng.wang@cienet.com.cn"
# 发送方的SMTP
smtp_server = "smtp.qq.com"

msg = MIMEText(
    '<html><body><h1>你好，我是Wangfeng</h1>' + '<p><a href = "http://www.python.org">这是一个多媒体内容</a></p>' + '</body></html>',
    'html', 'utf-8')
msg['From'] = _format_addr('Python爱好者<%s> ' % from_addr)
msg['To'] = _format_addr('接收者<%s>' % to_addr)
msg['Subject'] = Header('你好，我是Wangfeng,这是我通过Python发送的邮件', 'utf-8')

server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
print("mail has been sent successfully.")
server.quit()
