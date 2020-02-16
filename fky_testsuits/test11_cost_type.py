# coding=utf-8

import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger="CostType").getlog()


class CostType (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_feiyongleixing()


    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_add_feiyongleixing(self):
        feecontrol = FeecontrolManage(self.driver)
        name = generator.random_name()
        tishi = feecontrol.add_fyleixing(name)
        try:
            self.assertEqual(2, tishi, "验证费用类型必填项失败！")
            logger.info("验证费用类型必填项成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_jiahao()
        try:
            self.assertIn(name, feecontrol.get_fy_list(), "新增费用类型失败！")
            logger.info("新增费用类型成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_jianhao()

    def test02_modify_fyleixing(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_jiahao()
        feecontrol.click_last()
        name = generator.random_name()
        feecontrol.modify_fy(name)
        feecontrol.click_jiahao()
        try:
            self.assertIn(name, feecontrol.get_fy_list(), "修改费用类型失败！")
            logger.info("修改费用类型成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_jianhao()


    def test03_jinyong_fyleixing(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_jiahao()
        qiyong_list = feecontrol.get_fy_list()
        name = qiyong_list[23]
        feecontrol.click_last()
        feecontrol.click_jinyong()
        feecontrol.click_queding()
        feecontrol.click_jinyong_jiahao()
        try:
            self.assertIn(name, feecontrol.get_jinyong_list(), "禁用费用类型：%s 失败！" % name)
            logger.info("禁用费用类型：%s 成功！" % name)
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_jinyong_jianhao()


    def test04_qiyong_fyleixing(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_jinyong_jiahao()
        jinyong_list = feecontrol.get_jinyong_list()
        name = jinyong_list[0]
        feecontrol.click_fy_frist()
        feecontrol.click_qiyong()
        feecontrol.click_queding()
        feecontrol.click_jiahao()
        try:
            self.assertIn(name, feecontrol.get_fy_list(), "启用费用类型：%s 失败！" % name)
            logger.info("启用费用类型：%s 成功！" % name)
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test05_export_fy(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fy_export()
        feecontrol.click_queding()
        name_list = feecontrol.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("费用类型信息.xls", name_list, "费用类型信息导出失败！")
            logger.info("费用类型信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            feecontrol.get_windows_img()
        feecontrol.remover_file("费用类型信息")
        feecontrol.wait(1)

    def test06_import_fy(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fy_import()
        title = feecontrol.get_fy_title()
        try:
            self.assertEqual("导入数据", title, "点击导入按钮失败！")
            logger.info("点击导入按钮成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            feecontrol.get_windows_img()
        feecontrol.click_fy_close()
        feecontrol.wait(1)

if __name__ == '__main__':
    unittest.main()