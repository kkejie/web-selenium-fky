# coding=utf-8

import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.workStatement import WorkStatement

logger = Logger(logger = "Report").getlog()


class Report(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        report = WorkStatement(cls.driver)
        report.into_baogao()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_dayreport(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        report = WorkStatement(self.driver)
        report.add_btn()
        summarize = generator.randomStr(100, False, False, True, True)
        plan = generator.randomStr(100, False, False, True, True)
        report.add_weekly(summarize, plan)
        report.submit()
        if report.get_tishi() == "每日只可填写一次日报":
            self.assertIn("每日只可填写一次日报", report.get_tishi())
            logger.info("每日只可填写一次日报。")
            report.click_queding()
            report.click_quxiao()
        else:
            report.click_queding()
            self.assertIn(summarize, report.get_summarize(), "周报新增失败！")
            logger.info("周报新增成功。")
        report.sleep(1)

    def test2_save_dayreport(self):
        report = WorkStatement(self.driver)
        report.add_btn()
        summarize = generator.randomStr(100, False, False, True, True)
        plan = generator.randomStr(100, False, False, True, True)
        report.add_weekly(summarize, plan)
        report.save_report()
        report.into_draft()
        try:
            self.assertIn(summarize, report.get_summarize(), "周报保存失败！")
            logger.info("周报保存成功。")
        except Exception as e:
            logger.error("周报保存失败！", e)
            report.get_windows_img()
        report.sleep(1)

    def test3_edit_dayreport(self):
        report = WorkStatement(self.driver)
        report.into_draft()
        report.click_summarize()
        summarize = generator.randomStr(100, False, False, True, True)
        plan = generator.randomStr(100, False, False, True, True)
        report.add_weekly(summarize, plan)
        report.submit()
        try:
            self.assertIn("每日只可填写一次日报", report.get_tishi())
            logger.info("周报修改成功。")
        except Exception as e:
            logger.error("周报修改失败！", e)
            report.get_windows_img()
        report.click_queding()
        report.click_quxiao()
        report.sleep(1)

    # 导出
    def test4_export_report(self):
        report = WorkStatement(self.driver)
        report.click_wotijiaode()
        report.click_export()
        report.click_queding()
        name_list = report.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("工作报告信息.xls", name_list, "工作报告信息导出失败！")
            logger.info("工作报告信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            report.get_windows_img()
        report.remover_file("工作报告信息")
        report.wait(1)

if __name__ == '__main__':
    unittest.main()