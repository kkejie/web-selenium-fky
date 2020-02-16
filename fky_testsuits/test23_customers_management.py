# coding=utf-8
# 客商管理
import time
import unittest
from fky_pageobjects.customersManagement import CustomersManagement
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from framework import generator
from framework.logger import Logger

logger = Logger(logger="Customersmanagement").getlog()


class Customersmanagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        cm = CustomersManagement(cls.driver)
        cm.click_customersManagement()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_customers(self):
        # 新增
        cm = CustomersManagement(self.driver)
        cm.click_xinzengKS()
        cm.click_save()
        try:
            self.assertEqual(len(cm.get_tishis()), 2)
            logger.info("验证必填项成功！")
        except Exception as e:
            logger.error("验证必填项失败！", e)
            cm.get_windows_img()
        i = generator.randomStr(4)
        ksmc = "客商" + i
        cm.add_customers(ksmc)
        cm.click_chaxunmc(ksmc)
        try:
            self.assertEqual(cm.get_ksmcs()[0], ksmc)
            logger.info("新增客商成功！")
        except Exception as e:
            logger.error("新增客商失败！", e)
            cm.get_windows_img()
        cm.click_qingkong()  # 清空

    # 查询---客商名称
    def test2_query_customers(self):
        cm = CustomersManagement(self.driver)
        cm.select_200()
        ksmc = cm.get_ksmcs()[0]
        cm.click_chaxunmc(ksmc)
        for ksmc_1 in cm.get_ksmcs():
            try:
                self.assertIn(ksmc, ksmc_1)
                logger.info("按客商名称查询成功！")
            except Exception as e:
                logger.error("按客商名称查询失败！", e)
                cm.get_windows_img()
        cm.click_qingkong()         # 清空

    # 查询---客商分类
    def test3_query_customers(self):
        cm = CustomersManagement(self.driver)
        cm.select_200()
        ksfl = generator.randomStr(
            1, False, False, False, False, True, [
                "客商", "客户", "供应商", "拓展", "合作伙伴"])
        cm.click_chaxunfl(ksfl)
        for ksfl_1 in cm.get_ksfenleis():
            try:
                self.assertEqual(ksfl, ksfl_1)
                logger.info("按客商分类查询成功！")
            except Exception as e:
                logger.error("按客商分类查询失败！", e)
                cm.get_windows_img()
        cm.click_qingkong()  # 清空

    # 查询---客商编码
    def test4_query_customers(self):
        cm = CustomersManagement(self.driver)
        cm.select_200()
        ksbm = cm.get_ksbianmas()[0]
        cm.click_chaxunbm(ksbm)
        for ksbm_1 in cm.get_ksbianmas():
            try:
                self.assertIn(ksbm, ksbm_1)
                logger.info("查询客商成功！")
            except Exception as e:
                logger.error("查询客商失败！", e)
                cm.get_windows_img()
        cm.click_qingkong()  # 清空

    # 禁用
    def test3_jinyong_customers(self):
        cm = CustomersManagement(self.driver)
        cm.select_200()
        n = -1
        for ks_state in cm.get_kszhuangtais():
            n = n + 1
            if ks_state == "启用":
                cm.get_jinyongs_elements()[n].click()
                cm.click_queding()
                time.sleep(1)
                try:
                    self.assertEqual("禁用", cm.get_kszhuangtais()[n])
                    logger.info("禁用客商成功！")
                except Exception as e:
                    logger.error("禁用客商失败！", e)
                    cm.get_windows_img()
                break
            else:
                logger.info("%s: 该客商无法禁用" % cm.get_ksmcs()[n])

    # 启用
    def test4_qiyong_customers(self):
        cm = CustomersManagement(self.driver)
        cm.select_200()
        n = -1
        for ks_state in cm.get_kszhuangtais():
            n = n + 1
            if ks_state == "禁用":
                cm.get_qiyongs_elements()[n].click()
                cm.click_queding()
                time.sleep(1)
                try:
                    self.assertEqual("启用", cm.get_kszhuangtais()[n])
                    logger.info("启用客商成功！")
                except Exception as e:
                    logger.error("启用客商失败！", e)
                    cm.get_windows_img()
                break
            else:
                logger.info("%s: 该客商无法启用" % cm.get_ksmcs()[n])

    # 修改
    def test5_modify_customers(self):
        cm = CustomersManagement(self.driver)
        i2 = generator.randomStr(3)
        ksmc2 = "客商" + i2
        cm.select_200()
        n = -1
        for ks_state in cm.get_kszhuangtais():
            n = n + 1
            if ks_state == "启用":
                cm.get_xiugai_elements()[n].click()
                cm.add_customers(ksmc2)
                cm.click_chaxunmc(ksmc2)
                try:
                    self.assertEqual(cm.get_ksmcs()[0], ksmc2)
                    logger.info("修改客商成功！")
                except Exception as e:
                    logger.error("修改客商失败！", e)
                    cm.get_windows_img()
                break
            else:
                logger.info("%s: 该客商无法修改" % cm.get_ksmcs()[n])

    # 导入
    def test6_import_customers(self):
        cm = CustomersManagement(self.driver)
        cm.click_input()
        title = cm.get_into_title()
        try:
            self.assertEqual("导入数据", title, "点击导入按钮失败！")
            logger.info("点击导入按钮成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            cm.get_windows_img()
        cm.click_close()
        cm.wait(1)

    def test7_export_customers(self):
        cm = CustomersManagement(self.driver)
        cm.click_export()
        cm.click_queding()
        name_list = cm.file_name(r"C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("客商信息.xls", name_list, "客商信息导出失败！")
            logger.info("客商信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            cm.get_windows_img()
        cm.remover_file("客商信息")
        cm.wait(1)

    if __name__ == '__main__':
        unittest.main()
