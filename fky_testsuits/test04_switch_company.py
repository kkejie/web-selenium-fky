# coding=utf-8
import random
import time
import unittest

from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.switchCompany import SwitchCompany

logger = Logger(logger = "Switchcompany").getlog()


class Switchcompany (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        switchcompany = SwitchCompany(cls.driver)
        switchcompany.into_gongsigg()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_switch_company(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        switchcompany = SwitchCompany(self.driver)
        name_1 = switchcompany.get_company_name()
        switchcompany.switch_company()
        try:
            self.assertNotEqual(name_1, switchcompany.get_company_name())
            logger.info("切换公司：%s 成功." % switchcompany.get_company_name())
        except NameError as e:
            logger.error( "切换公司：%s 失败！" % switchcompany.get_company_name())
            switchcompany.get_windows_img()
        switchcompany.wait(1)

    def test2_switch_company(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        switchcompany = SwitchCompany(self.driver)
        name_2 = switchcompany.get_company_name()
        switchcompany.switch_company()
        try:
            self.assertNotEqual(name_2, switchcompany.get_company_name())
            logger.info("切换公司：%s 成功." % switchcompany.get_company_name())
        except NameError as e:
            logger.error( "切换公司：%s 失败！" % switchcompany.get_company_name())
            switchcompany.get_windows_img()
        switchcompany.wait(1)

    def test3_create_company(self):
        switchcompany = SwitchCompany(self.driver)
        switchcompany.create_com()
        switchcompany.save_btn()
        tishi = switchcompany.get_tishi()
        try:
            self.assertEqual("该选项不能为空", tishi)
            logger.info("验证成功。")
        except Exception as e:
            logger.error("验证失败！", e)
            switchcompany.get_windows_img()
        name = "测试公司" + str(random.randint(10, 99))
        switchcompany.create_com_bitian("测试公司", "测试公司99")
        switchcompany.save_btn()
        switchcompany.sleep(10)
        save_tishi = switchcompany.get_save_tishi()
        switchcompany.save_baocun()
        try:
            self.assertEqual("保存成功", save_tishi)
            logger.info("公司创建成功。")
        except Exception as e:
            if save_tishi == '公司名称已存在，请换其他公司名称!':
                logger.error(save_tishi)
            else:
                logger.error("公司创建失败！", e)
            switchcompany.get_windows_img()
        switchcompany.into_gongsigg()
        switchcompany.wait(1)

    def test4_query_companylist(self):
        switchcompany = SwitchCompany(self.driver)
        name1 = switchcompany.get_company_name()
        switchcompany.query_company()
        name2 = switchcompany.get_name()
        try:
            self.assertIn(name1, name2)
            logger.info("查询成功。")
        except Exception as e:
            logger.error("查询失败！", e)
            switchcompany.get_windows_img()
        switchcompany.into_gongsigg()
        switchcompany.wait(1)

    def test5_export_comp(self):
        switchcompany = SwitchCompany(self.driver)
        switchcompany.click_export()
        name_list = switchcompany.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("公司列表.xls", name_list, "公司列表导出失败！")
            logger.info("公司列表导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            switchcompany.get_windows_img()
        switchcompany.remover_file("公司列表")
        switchcompany.wait(1)


if __name__ == '__main__':
    unittest.main()
