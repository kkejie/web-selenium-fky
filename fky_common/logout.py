# coding=utf-8

from framework.base_page import BasePage
import time
from framework.logger import Logger

logger = Logger(logger = "Logout").getlog()

class Logout():
    @staticmethod
    def log_out(self):
        self.driver.find_element_by_xpath('//a[@ng-click="logout()"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/button[2]').click()
        time.sleep(1)
        txt = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/button[1]').text
        logoutpage = BasePage(self.driver)
        try:
            assert "注册" in txt
            logger.info("登出成功。")
        except Exception as e:
            logoutpage.get_windows_img()  # 调用基类截图方法
            logger.error("登出失败。", e)