# coding=utf-8

import configparser
import os.path
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    ff_driver_path = dir + '\\tools\\geckodriver.exe'
    chrome_driver_path = dir + '\\tools\\chromedriver.exe'
    ie_driver_path = dir + '\\tools\\IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file ,return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + "/config/config.ini"
        file_path = os.path.dirname(os.path.abspath('.')) + '\\config\\config.ini'
        # file_path = 'D:\\Users\Administrator\PycharmProjects\\automation_framework\config\config.ini'
        # file_path = 'C:\\Users\Administrator\\automation_fky\config\config.ini'
        config.read(file_path)
        # 如果代码中有中文注释，用这个，不然报解码错误
        config.read(file_path, encoding='UTF-8')
        browser = config.get("browserType", "browserName")
        logger.info("你选择了 %s 浏览器" % browser)
        url = config.get("testServer", "URL")
        logger.info("测试服务器的URL是 : %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox(self.ff_driver_path)
            logger.info("打开Firefox浏览器。")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("打开Chrome浏览器。")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("打开IE浏览器。")

        driver.maximize_window()
        driver.get(url)
        logger.info("打开网址:%s" % url)
        driver.implicitly_wait(20)
        return driver

    def quit_browser(self):
        logger.info("现在，关闭并退出浏览器。")
        self.driver.quit()
