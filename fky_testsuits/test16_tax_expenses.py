# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger="TaxExpenses").getlog()


class TaxExpenses (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_lz_sqlzbz()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_into_sqlzbz(self):
        feecontrol = FeecontrolManage(self.driver)
        self.assertEqual("启用税前列支标准:", feecontrol.get_lz_title(), "进入税前列支标准页面失败！")

    def test2_save_sqlzbz(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_lz_isqiyong()
        feecontrol.edit_lz_sqlzbz()
        feecontrol.click_lz_tijiao()
        tishi = feecontrol.get_tishi()
        feecontrol.click_queding()
        self.assertEqual("保存成功！", tishi, "进入税前列支标准页面失败！")


if __name__ == '__main__':
    unittest.main()