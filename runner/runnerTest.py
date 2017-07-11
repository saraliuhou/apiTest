# -*- coding: utf-8 -*-
import unittest

import testcase.distribute.v02.test_passenger as passenger
import testcase.distribute.v02.test_rides as rides
import testcase.distribute.v02.test_login as login

import testcase.distribute.v02.test_cancelReason as cancelReason
import testcase.distribute.v02.test_driver as driver
import testcase.distribute.v02.test_freight as freight
import testcase.distribute.v02.test_routes as route
import testcase.distribute.v02.test_reassignReason as reassignReason
import testcase.distribute.v02.test_ratingComment as rateComment
import testcase.distribute.v02.test_carpool as carpool
import runner.HTMLTestRunner as HTMLTestRunner
import time

import smtplib
# import email.MIMEMultipart
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import  MIMEText
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import os.path


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login.loginTest))
suite.addTest(unittest.makeSuite(passenger.S2PassengerTest))
suite.addTest(unittest.makeSuite(rides.rideTest))
suite.addTest(unittest.makeSuite(cancelReason.CancelReasonTest))
suite.addTest(unittest.makeSuite(freight.FreightTest))
suite.addTest(unittest.makeSuite(driver.DriverTest))
# suite.addTest(unittest.makeSuite(route.RoutesTest))
suite.addTest(unittest.makeSuite(reassignReason.ReassignReasonTest))
suite.addTest(unittest.makeSuite(rateComment.RateCommentTest))
suite.addTest(unittest.makeSuite(carpool.Carpool))

nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
filename = "apitest.html"
print(filename)
fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title ='顺道嘉接口测试报告',
        description = '顺道嘉接口测试报告')

runner.run(suite)#执行测试
fp.close()#关闭文件，否则会无法生成文件

# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

# from_addr = 'sunsy@shundaojia.com'
# password = 'hahaheihei@22'
# to_addr = 'sunsy@shundaojia.com'
# smtp_server = 'smtp.exmail.qq.com'

# 格式化邮件地址
# def _formar_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))

# 发送内容为html格式
# msg = MIMEText('<html><body><h1>apiTest</h1></body></html>', 'html', 'utf-8')

# # 发送内容为纯文本
# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
# contype = 'application/octet-stream'
# maintype, subtype = contype.split('/', 1)
# file_msg = MIMEBase(maintype, subtype)
# data = open("/Users/yangyouyou/PycharmProjects/apiTest/test_report/report2017-04-10 12:19:07.html", 'rb')
# file_msg.set_payload(data.read())
# data.close()
# encoders.encode_base64(file_msg)
# ## 设置附件头
# basename = os.path.basename("report2017-04-10 12:19:07.html")
# file_msg.add_header('Content-Disposition',
#                     'attachment', filename=basename)
#
# msg.attach(file_msg)
#
# # # 设置传输内容（发件人、收件人、主题），（'<%s>' % 值）---把值传进字符串
# msg['From'] = _formar_addr('sunsy<%s>' % from_addr)
# msg['To'] = _formar_addr('judy<%s>' % to_addr)
# msg['Subject'] = Header('test', 'utf-8').encode()
# msg['Date'] = formataddr()

# server = smtplib.SMTP(smtp_sercer, 25)    # 默认端口25
# server = smtplib.SMTP_SSL(smtp_server, 465)     # ssl加密
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# # 读入文件内容并格式化
# data = open(file_name, 'rb')
# file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
# file_msg.set_payload(data.read())
# data.close()
# email.Encoders.encode_base64(file_msg)
#
# ## 设置附件头
# basename = os.path.basename(file_name)
# file_msg.add_header('Content-Disposition',
#                     'attachment', filename=basename)
# main_msg.attach(file_msg)
#
# # 设置根容器属性
# main_msg['From'] = From
# main_msg['To'] = To
# main_msg['Subject'] = "attach test "
# main_msg['Date'] = email.Utils.formatdate()
#
# # 得到格式化后的完整文本
# fullText = main_msg.as_string()
#
# # 用smtp发送邮件
# try:
#         server.sendmail(From, To, fullText)
# finally:
#         server.quit()

