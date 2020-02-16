# coding=utf-8
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.homePage import HomePage

logger = Logger(logger = "Homepage").getlog()


class Homepage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_into_notice(self):
        homepage = HomePage(self.driver)
        homepage.click_into_gonggao()
        self.assertEqual("新增公告", homepage.get_gonggao(), "进入公告页面失败")
        logger.info("进入公告页面成功。")
        homepage.sleep(1)

    def test2_into_report(self):
        homepage = HomePage(self.driver)
        homepage.click_into_baogao()
        self.assertEqual("新增报告", homepage.get_baogao(), "进入报告页面失败")
        logger.info("进入报告页面成功。")
        homepage.sleep(1)


if __name__ == '__main__':
    unittest.main()