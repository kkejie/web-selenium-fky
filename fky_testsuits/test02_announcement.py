# coding=utf-8

import time
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.announcement import Announcement

logger = Logger(logger = "Announce").getlog()


class Announce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        announce = Announcement(cls.driver)
        announce.into_gonggao()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    # 发布
    def test1_add_notice(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        announce = Announcement(self.driver)
        announce.add_btnn()
        title1 = generator.randomStr(10, False, False, True, True)
        content = generator.randomStr(100, False, False, True, True)
        announce.add_gonggao(title1, content)
        announce.issue_gonggao()
        self.assertEqual(title1, announce.get_notice_title(), "公告新增失败")
        try:
            assert title1 in announce.get_notice_title()
            logger.info("公告新增成功。")
        except Exception as e:
            logger.error("公告新增失败！", e)
            announce.get_windows_img()
        time.sleep(1)

    # 查询
    def test2_query_notice(self):
        announce = Announcement(self.driver)
        title1 = announce.get_notice_title()
        announce.input_query(title1)
        self.assertEqual(title1, announce.get_notice_title(), "公告查询失败")
        try:
            assert title1 in announce.get_notice_title()
            logger.info("公告查询成功。")
        except Exception as e:
            logger.error("公告查询失败！", e)
            announce.get_windows_img()
        time.sleep(1)

    # 保存
    def test3_save_notice(self):
        announce = Announcement(self.driver)
        announce.add_btnn()
        title1 = generator.randomStr(10, False, False, True, True)
        content = generator.randomStr(100, False, False, True, True)
        announce.add_gonggao(title1, content)
        announce.save_gonggao()
        time.sleep(1)
        self.assertEqual(title1, announce.get_notice_title(), "公告保存失败")
        try:
            assert title1 in announce.get_notice_title()
            logger.info("公告保存成功。")
        except Exception as e:
            logger.error("公告保存失败！", e)
            announce.get_windows_img()
        time.sleep(1)

    # 修改
    def test4_change_notice(self):
        announce = Announcement(self.driver)
        announce.change_gonggao()
        title1 = generator.randomStr(10, False, False, True, True)
        content = generator.randomStr(100, False, False, True, True)
        announce.add_gonggao(title1, content)
        announce.save_gonggao()
        time.sleep(1)
        self.assertEqual(title1, announce.get_notice_title(), "公告修改失败")
        try:
            assert title1 in announce.get_notice_title()
            logger.info("公告修改成功。")
        except Exception as e:
            logger.error("公告修改失败！", e)
            announce.get_windows_img()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()