# coding=utf-8

import os.path
import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import time
from framework.logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有的页面都继承这个基类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器并结束测试
    def quit_browser(self):
        self.driver.quit()
        logger.info("关闭浏览器.")

    # 浏览器前进操作
    def forword(self):
        self.driver.forword()
        logger.info("执行前进操作.")

    def back(self):
        self.driver.back()
        logger.info("执行后退操作")

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("隐性等待时间：%d 秒" % seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info("关闭浏览器.")
        except NameError as e:
            logger.error("关闭浏览器失败：%s" % e)
            self.get_windows_img()

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\images 下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/images/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        # print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("截屏并保存到文件夹: /images")
        except NameError as e:
            logger.error("截图失败! %s" % e)
        time.sleep(1)

    # 显示等待
    def wait_element(self, el):
        time.sleep(1)
        """
        等待元素显示。
        """
        try:
            WebDriverWait(self.driver, 20, 1).until(
                EC.presence_of_element_located(el)
            )
        except TimeoutException:
            return False
        else:
            return True

    def find_element(self, xpath):
        """
        判断元素定位方式，返回元素。
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "语法错误，参考：: 'id=>useranme'.")

        time_out_error = "定位元素超时，请尝试其他定位方式"
        if by == "id":
            req = self.wait_element((By.ID, value))
            if req is True:
                element = self.driver.find_element_by_id(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "name":
            req = self.wait_element((By.NAME, value))
            if req is True:
                element = self.driver.find_element_by_name(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "class":
            req = self.wait_element((By.CLASS_NAME, value))
            if req is True:
                element = self.driver.find_element_by_class_name(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "link_text":
            req = self.wait_element((By.LINK_TEXT, value))
            if req is True:
                element = self.driver.find_element_by_link_text(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "xpath":
            req = self.wait_element((By.XPATH, value))
            if req is True:
                element = self.driver.find_element_by_xpath(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "css":
            req = self.wait_element((By.CSS_SELECTOR, value))
            if req is True:
                element = self.driver.find_element_by_css_selector(value)
            else:
                raise TimeoutException(time_out_error)
        else:
            raise NameError(
                "请输入正确的目标元素,'id','name','class','link_text','xpath','css'.")
        return element

    def find_elements(self, xpath):
        """
        判断元素定位方式，返回元素。
        """
        if "=>" not in xpath:
            by = "xpath"
            value = xpath
        else:
            by = xpath.split("=>")[0]
            value = xpath.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "语法错误，参考 : 'id=>useranme'.")

        time_out_error = "定位元素超时，请尝试其他定位方式"
        if by == "id":
            req = self.wait_element((By.ID, value))
            if req is True:
                element = self.driver.find_elements_by_id(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "name":
            req = self.wait_element((By.NAME, value))
            if req is True:
                element = self.driver.find_elements_by_name(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "class":
            req = self.wait_element((By.CLASS_NAME, value))
            if req is True:
                element = self.driver.find_elements_by_class_name(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "link_text":
            req = self.wait_element((By.LINK_TEXT, value))
            if req is True:
                element = self.driver.find_elements_by_link_text(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "xpath":
            req = self.wait_element((By.XPATH, value))
            if req is True:
                element = self.driver.find_elements_by_xpath(value)
            else:
                raise TimeoutException(time_out_error)
        elif by == "css":
            req = self.wait_element((By.CSS_SELECTOR, value))
            if req is True:
                element = self.driver.find_elements_by_css_selector(value)
            else:
                raise TimeoutException(time_out_error)
        else:
            raise NameError(
                "请输入正确的目标元素,'id','name','class','link_text','xpath','css'.")
        return element

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("在输入框中输入：%s" % text)
        except NameError as e:
            logger.error("输入失败： %s" % e)
            self.get_windows_img()
        time.sleep(1)

    def type1(self, selector, text):
        el = self.find_element(selector)
        try:
            el.send_keys(text)
            logger.info("在输入框中输入：%s" % text)
        except NameError as e:
            logger.error("输入失败： %s" % e)
            self.get_windows_img()
        time.sleep(1)

    # 清楚文本框
    def clear(self, selector):
        el = self.find_element(selector)
        self.sleep(1)
        try:
            el.clear()
            logger.info("在输入框中清除文本后再输入。")
        except NameError as e:
            logger.error("清除输入框失败： %s" % e)
            self.get_windows_img()

    # 点击元素
    def clicked(self, selector):
        el = self.find_element(selector)
        try:
            text = el.text
            el.click()
            logger.info("点击元素：%s 成功." % text)
        except NameError as e:
            logger.error("点击元素 %s 失败！" % e)
            self.get_windows_img()
        time.sleep(1)

    # 选中选择框
    def is_selecet(self, selector):
        el = self.find_element(selector)
        if el.is_selected() == 0:
            try:
                el.click()
                logger.info("选择元素成功.")
            except NameError as e:
                logger.error("选择元素失败！" % e)
                self.get_windows_img()
            time.sleep(1)
        else:
            logger.info("选择元素成功.")

    def get_is_selecet(self, selector):
        el = self.find_element(selector)
        return el.is_selected()

    # 双击元素
    def double_clicked(self, selector):
        el = self.find_element(selector)
        try:
            text = el.text
            ActionChains(self.driver).double_click(el).perform()
            logger.info("双击元素：%s 。" % text)
        except NameError as e:
            logger.error("双击元素 %s 失败。" % e)
            self.get_windows_img()
        time.sleep(1)

    # 获取网页标题
    def get_page_title(self):
        logger.info("当前页面标题为：%s" % self.driver.title)
        time.sleep(1)
        return self.driver.title

    # 获取元素text
    def get_text(self, selector):
        el = self.find_element(selector)
        try:
            text = el.text
            logger.info("获取元素文本：%s 成功。" % text)
            return text
        except NameError as e:
            logger.error("获取元素文本成功。" % e)
            self.get_windows_img()
        time.sleep(1)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("等待 %s 秒" % seconds)

    # 下拉框选择
    def select_text(self, selector, text):
        el = Select(self.find_element(selector))
        try:
            el.select_by_visible_text(text)
            logger.info("产品分类中选择了 \'%s\'" % text)
        except NameError as e:
            logger.error("选择分类失败" % e)
            self.get_windows_img()
        time.sleep(1)

    # 随机选择下拉框内容
    def select_index(self, selector1, selector2):
        el = Select(self.find_element(selector1))
        n = random.randint(1, len(self.get_texts(selector2))) - 1
        try:
            el.select_by_index(n)
            logger.info("下拉选择框中选择了 \'%s\'" % self.get_texts(selector2)[n])
        except NameError as e:
            logger.error("下拉选择框选择失败" % e)
            self.get_windows_img()
        time.sleep(1)
        return self.get_texts(selector2)[n]

    # 随机选择附件类型
    def select_from_2(self, selector1, selector2):
        el = Select(self.find_element(selector1))
        n = random.randint(2, len(self.get_texts(selector2))) - 1
        try:
            el.select_by_index(n)
            logger.info("下拉选择框中选择了 \'%s\'" % self.get_texts(selector2)[n])
        except NameError as e:
            logger.error("下拉选择框选择失败" % e)
            self.get_windows_img()
        time.sleep(1)

    # 切换到当前最新打开的窗口
    def switch_to_window(self):
        # time.sleep(1)
        # 获得打开的第一个窗口句柄
        window_1 = self.driver.current_window_handle
        # 获得打开的所有的窗口句柄
        windows = self.driver.window_handles
        # 切换到最新的窗口
        for current_window in windows:
            if current_window != window_1:
                # self.driver.close()
                self.driver.switch_to.window(current_window)
                logger.info("切换到句柄为" + current_window + "的窗口")
        time.sleep(1)

    def switch_to_handle(self):
        handle = self.driver.window_handles[0]
        self.driver.switch_to.window(handle)
        logger.info("切换到句柄为" + handle + "的窗口")

    def refresh(self):
        """
        Refresh the current page.
        Usage:
        driver.F5()
        """
        self.driver.refresh()

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def execute_script_click(self, select):
        """
        编 写 人：柯洁
        功    能：使用js代码实现点击操作
        输入参数：select     页面元素copy selector
        日    期：2019-03-18
        修改记录：
        :param select:
        :return:
        """
        click = "document.querySelector(" + select + ").click()"
        self.driver.execute_script(click)
        time.sleep(1)

    def execute_script_input(self, select, text):
        """
        编 写 人：柯洁
        功    能：执行前端代码
        输入参数：select     页面元素copy selector
                  text       输入内容
        日    期：2019-03-18
        修改记录：
        :param select:
        :return:
        """
        clear = "document.querySelector(" + select + ").value=''"
        self.driver.execute_script(clear)
        input = "document.querySelector(" + select + ").value=" + text + ""
        self.driver.execute_script(input)
        time.sleep(1)

    @staticmethod
    def file_name(file_dir):
        """
        编 写 人：柯洁
        功    能：获取 file_dir 目录下文件名存入输入 L
        输入参数：file_dir     目录
        日    期：2019-03-19
        修改记录：
        :return:
        """
        time.sleep(1)
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.xls':
                    L.append(os.path.join(file))
                    # print(file)
        logger.info("成功获取文件名列表 %s " % L)
        time.sleep(1)
        return L

    @staticmethod
    def remover_file(filename):
        """
        编 写 人：柯洁
        功    能：删除文件 file_dir
        日    期：2019-03-19
        修改记录：
        :param filename: 文件名
        :return:
        """
        os.remove("C:\\Users\Kejie\Downloads\\" + filename + ".xls")
        logger.info("删除文件 %s.xls成功" % filename)
        time.sleep(1)

    def get_texts(self, selector):
        """
        编 写 人：柯洁
        功    能：获取一组元素的文本存入text数组中
        日    期：2019-03-20
        修改记录：
        :param selector: 这组元素的xpath
        :return:
        """
        els = self.find_elements(selector)
        try:
            text = []
            for el in els:
                text.append(el.text)
            logger.info("获取元素文本：%s 成功。" % text)
            return text
        except NameError as e:
            logger.error("获取元素文本失败。" % e)
            self.get_windows_img()
        time.sleep(1)

    def get_elements(self, selector):
        """
        编 写 人：柯洁
        功    能：获取一组元素的文本存入text数组中
        日    期：2019-03-20
        修改记录：
        :param selector: 这组元素的xpath
        :return:
        """
        els = self.find_elements(selector)
        try:
            element = []
            element_text = []
            for el in els:
                element.append(el)
                element_text.append(el.text)
            logger.info("获取元素：%s 成功。" % element_text)
            return element
        except NameError as e:
            logger.error("获取元素失败。" % e)
            self.get_windows_img()
        time.sleep(1)

    def get_input_text(self, selector):
        """
        编 写 人：柯洁
        功    能：获取input输入框内的文本
        日    期：2019-03-20
        修改记录：
        :param selector: xpath
        :return:
        """
        el = self.find_element(selector)
        try:
            text = el.get_attribute('value')
            logger.info("获取元素文本：%s 成功。" % text)
            return text
        except NameError as e:
            logger.error("获取元素文本失败。" % e)
            self.get_windows_img()
        time.sleep(1)

    def get_input_texts(self, selector):
        """
        编 写 人：柯洁
        功    能：获取一组input元素的文本存入text数组中
        日    期：2019-03-20
        修改记录：
        :param selector: 这组元素的xpath
        :return:
        """
        els = self.find_elements(selector)
        try:
            text = []
            for el in els:
                text.append(el.get_attribute('value'))
            logger.info("获取元素文本：%s 成功。" % text)
            return text
        except NameError as e:
            logger.error("获取元素文本失败。" % e)
            self.get_windows_img()
        time.sleep(1)

    def suspend(self, selector):
        """
        编 写 人：柯洁
        功    能：鼠标悬浮
        日    期：2019-09-23
        修改记录：
        :param selector: 元素的xpath
        :return:
        """
        el = self.find_element(selector)
        try:
            text = el.text
            ActionChains(driver=self.driver).move_to_element(el).perform()
            logger.info("鼠标悬浮在元素：%s 上成功." % text)
        except NameError as e:
            logger.error("鼠标悬浮在元素 %s 上失败！" % e)
            self.get_windows_img()
        time.sleep(1)
