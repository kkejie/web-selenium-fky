# coding=utf-8

import time
from framework.logger import Logger
from framework.base_page import BasePage
from PIL import Image
from framework.get_code import get_code

logger = Logger(logger = "Login").getlog()

class Login():

    @staticmethod
    def log_in(self):
        username = self.driver.find_element_by_xpath('//input[@name="login_account"]')
        username.clear()
        username.send_keys('17607025447')
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.clear()
        password.send_keys('Ke123456')

        """
        pic = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/form/div[3]/button/img')
        # 截图保存地址
        screenImg = "D:\\Users\Administrator\PycharmProjects\\automation_framework\images\screenImg.png"
        self.driver.get_screenshot_as_file(screenImg)
        # 定位验证码位置及大小
        location = pic.location
        size = pic.size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        # 从文件读取截图，截取验证码位置再次保存
        img = Image.open(screenImg).crop((left, top, right, bottom))
        img.save(screenImg)
        img.close()
        # 再次读取识别验证码
        code = get_code(screenImg)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/form/div[3]/div/input').send_keys(code)
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        time.sleep(1)
        global a
        a = 0
        for a in range(0,10):
            time.sleep(1)
            if self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/p').text:
                print("验证码错误 ", a)
                self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/button[2]').click()
                pic = self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[2]/form/div[3]/button/img')
                # 截图保存地址
                screenImg = "D:\\Users\Administrator\PycharmProjects\\automation_framework\images\screenImg.png"
                self.driver.get_screenshot_as_file(screenImg)
                # 定位验证码位置及大小
                location = pic.location
                size = pic.size
                left = location['x']
                top = location['y']
                right = location['x'] + size['width']
                bottom = location['y'] + size['height']
                # 从文件读取截图，截取验证码位置再次保存
                img = Image.open(screenImg).crop((left, top, right, bottom))
                img.save(screenImg)
                img.close()
                code = get_code(screenImg)
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/div[2]/form/div[3]/div/input').send_keys(code)
                self.driver.find_element_by_xpath('//*[@id="login"]').click()
                a = a + 1
            else:
                a = 12
                break

        time.sleep(1)
        """
        self.driver.find_element_by_xpath('//*[@id="login"]').click()
        txt = self.driver.find_element_by_xpath('//a[text()="简体中文"]').text
        loginpage = BasePage(self.driver)
        try:
            assert "简体中文" in txt
            logger.info("登录成功。")
        except Exception as e:
            loginpage.get_windows_img()  # 调用基类截图方法
            logger.error("登录失败。", e)