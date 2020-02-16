# coding=utf-8
import random
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger="CurrencySet").getlog()


class CurrencySet (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        # feecontrol.js("window.scrollTo(200,1000);")
        # print("--------")
        feecontrol.into_bizhong()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.quit_browser()

    # 币种配置
    def test01_add_bizhong(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.bizhongpeizhi()
        bizhong_list = feecontrol.get_bizhong_list()
        n = random.randint(1, len(bizhong_list)) - 1
        bizhong = bizhong_list[n]
        feecontrol.input_bizhong(bizhong)
        feecontrol.save_queding()
        try:
            self.assertIn(bizhong, feecontrol.get_show_bizhongs(), "增加币种失败！")
            logger.info("增加币种成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test02_add_bizhong(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.bizhongpeizhi()
        bizhong_list = feecontrol.get_bizhong_list()
        n = random.randint(1, len(bizhong_list)) -1
        bizhong = bizhong_list[n]
        feecontrol.input_bizhong(bizhong)
        feecontrol.save_queding()
        try:
            self.assertIn(bizhong, feecontrol.get_show_bizhongs(), "增加币种失败！")
            logger.info("增加币种成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test03_del_bizhong(self):
        feecontrol = FeecontrolManage(self.driver)
        bizhong_name = feecontrol.get_bizhong_name()
        feecontrol.click_del_bz()
        feecontrol.click_queding()
        feecontrol.sleep(1)
        feecontrol.click_queding_1()
        try:
            self.assertNotIn(bizhong_name, feecontrol.get_show_bizhongs(), "删除币种失败！")
            logger.info("删除币种成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.sleep(1)


if __name__ == '__main__':
    unittest.main()