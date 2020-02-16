# coding=utf-8

import time
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.spendingSubtotal import SpendingSubtotal

logger = Logger(logger = "SpendSubtotal").getlog()

class SpendSubtotal (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        spend = SpendingSubtotal(cls.driver)
        spend.into_zcxj()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_yanzheng_btx(self):
        spend = SpendingSubtotal(self.driver)
        spend.click_add()
        spend.click_baoxiao()
        self.assertEqual("该字段为必填字段", spend.get_zdbt_tishi(), "验证支出小计必填字段失败！")
        logger.info("验证支出小计必填字段成功！")
        spend.click_quxiao()

    def test02_zcxj_save(self):
        spend = SpendingSubtotal(self.driver)
        spend.click_add()
        # spend.edit_zcxj()
        spend.update_huochepiao()

if __name__ == '__main__':
    unittest.main()
