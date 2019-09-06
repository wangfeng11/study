#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib


# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 检测编码，否则非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


# indent用于缩进显示：
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s:%s' % ('  ' * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s-------------------' % (' ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText:%s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment:%s' % (' ' * indent, content_type))


# 输入邮件地址, 口令和POP3服务器地址:
p = 'pop.qq.com'
email = '447296650@qq.com'
password = 'xrmbtbhlqipfbjch'
# email = input('Email:')
# password = input('Password:')
# pop3_server = input('POP3 server:')
# 连接到POP3服务器
server = poplib.POP3(p)
# server.set_debuglevel(1)#打开或关闭调试信息
# print(server.getwelcome().decode('utf-8'))
# 身份认证
server.user(email)
server.pass_(password)
# start()返回邮件数量和占用空间：
# print('Messages:%s.Size:%s' % server.stat())
resp, mails, octets = server.list()
# print(mails)
# 获取最新一封邮件
index = len(mails)
resp, lines, octets = server.retr(index)
# 获得整个邮件的原始文本：
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件：
msg = Parser().parsestr(msg_content)
server.quit()
print_info(msg)
