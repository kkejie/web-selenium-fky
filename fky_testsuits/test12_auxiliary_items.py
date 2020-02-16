# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger="AuxiliaryItems").getlog()


class AuxiliaryItems (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_fuzhuhsx()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_into_auxiliary(self):
        feecontrol = FeecontrolManage(self.driver)
        title = feecontrol.get_hs_title()
        try:
            self.assertEqual("辅助核算项", title, "进入辅助核算项页面失败！")
            logger.info("进入辅助核算项页面成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test2_save_auxiliary(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_hs_save()
        tishi = feecontrol.get_tishi()
        try:
            self.assertEqual("保存成功！", tishi, "保存失败！")
            logger.info("保存成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()


if __name__ == '__main__':
    unittest.main()
