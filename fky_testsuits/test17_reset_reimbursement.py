# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger="ResetReimbursement").getlog()

class ResetReimbursement (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_cz_chongzhibx()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_into_sqlzbz(self):
        feecontrol = FeecontrolManage(self.driver)
        self.assertEqual("重置报销数据", feecontrol.get_cz_title(), "进入重置报销数据页面失败！")


if __name__ == '__main__':
    unittest.main()