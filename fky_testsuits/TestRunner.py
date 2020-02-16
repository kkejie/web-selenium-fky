# coding=utf-8
import sys
sys.path.append("C:\\Users\\Kejie\\AppData\\Local\\Programs\\Python\\Python37\\Lib")
sys.path.append("W:\\PycharmProjects\\automation_fky")
sys.path.append("C:\\Users\\Kejie\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages")
sys.path.append("W:\\PycharmProjects\\automation_fky\\framework")
import HTMLTestRunner_PY3
import unittest
import os
import time
from framework.send_email import sendEmail
from framework.send_email import new_report

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+'/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + 'HTMLtemplate.html'
fp = open(HtmlFile, 'wb')
# 构建suit
suite = unittest.TestLoader().discover("fky_testsuits")                 # discover() 一次加载一个路径下所有的测试用例

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title=u'费控云自动化测试', description=u'用例测试情况')
    # 开始执行测试套件
    runner.run(suite)
    fp.close()
    new_report = new_report(report_path)
    # 发送邮件
    sendEmail(new_report, HtmlFile)
