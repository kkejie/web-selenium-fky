# coding=utf-8

import time
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.documentPageField import PageField

logger = Logger(logger = "DocumentPageField").getlog()

class DocumentPageField (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        pagefield = PageField(cls.driver)
        pagefield.into_danju_ziduan()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_page_field(self):
        pagefield = PageField(self.driver)
        zhichuxj_list = pagefield.get_zhichuxj()
        for zcxj in zhichuxj_list:
            zcxj.click()
            ziduan_count = pagefield.get_ziduan_count()
            self.assertLess(0, ziduan_count, "%s 支出小计字段显示错误！" %zcxj.text)
            logger.info("%s 支出小计字段显示成功！" %zcxj.text)

if __name__ == '__main__':
    unittest.main()