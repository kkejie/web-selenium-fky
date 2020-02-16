# coding=utf-8
import random
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger = "InvoiceType").getlog()

class InvoiceType (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_fz_invoice_type()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_invoicetype(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fz_add_invoic()
        feecontrol.click_fz_save()
        tishi = feecontrol.get_fz_tishi()
        try:
            self.assertEqual("该选项不能为空", tishi, "新增发票种类、内容与费用类型必填项验证失败！")
            logger.info("新增发票种类、内容与费用类型必填项验证成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_fz_quxiao()

    def test2_add_invoicetype(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fz_add_invoic()
        feecontrol.select_fz_fapiao()
        feiyong_text = feecontrol.edit_fz_fapiao()
        feecontrol.click_fz_save()
        feecontrol.click_queding()
        try:
            self.assertIn(feiyong_text, feecontrol.get_fz_content_list(), "新增发票种类、内容与费用类型失败！")
            logger.info("新增发票种类、内容与费用类型成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test2_add_invoicetype2(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fz_add_invoic()
        feecontrol.select_fz_fapiao()
        feiyong_text = feecontrol.edit_fz_fapiao()
        feecontrol.click_fz_save()
        feecontrol.click_queding()
        try:
            self.assertIn(feiyong_text, feecontrol.get_fz_content_list(), "新增发票种类、内容与费用类型失败！")
            logger.info("新增发票种类、内容与费用类型成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test3_modify_invoicetype(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fz_xiugai()
        feiyong_text = feecontrol.edit_fz_fapiao()
        feecontrol.click_fz_save()
        feecontrol.click_queding()
        try:
            self.assertIn(feiyong_text, feecontrol.get_fz_content_list(), "修改发票种类、内容与费用类型失败！")
            logger.info("修改发票种类、内容与费用类型成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()

    def test4_query_invoicetype(self):
        feecontrol = FeecontrolManage(self.driver)
        n = random.randint(1, len(feecontrol.get_fz_content_list())) - 1
        content = feecontrol.get_fz_content_list()[n]
        feecontrol.click_fz_zhankai()
        feecontrol.input_fz_content(content)
        feecontrol.click_fz_query()
        content_list = feecontrol.get_fz_content_list()
        for content_1 in content_list:
            try:
                self.assertEqual(content, content_1, "按发票内容查询发票种类、内容与费用类型失败！")
                logger.info("按发票内容查询发票种类、内容与费用类型成功。")
            except Exception as e:
                logger.error("执行失败！", e)
                feecontrol.get_windows_img()
        feecontrol.click_fz_clear()

    def test5_del_invoicetype(self):
        feecontrol = FeecontrolManage(self.driver)
        content = feecontrol.get_fz_content_list()[0]
        feecontrol.click_fz_xuan()
        feecontrol.click_fz_del()
        feecontrol.click_queding()
        feecontrol.sleep(1)
        feecontrol.click_queding_1()
        # try:
        self.assertNotIn(content, feecontrol.get_fz_content_list(), "删除发票内容查询发票种类、内容与费用类型失败！")
        logger.info("删除发票内容查询发票种类、内容与费用类型成功。")
        # except Exception as e:
        #     logger.error("执行失败！", e)
        #     feecontrol.get_windows_img()

    def test6_export_invoicetype(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fz_export()
        feecontrol.click_queding()
        name_list = feecontrol.file_name("C:\\Users\Kejie\Downloads")
        # try:
        self.assertIn("发票种类、内容与费用类型信息.xls", name_list, "发票种类、内容与费用类型信息导出失败！")
        logger.info("发票种类、内容与费用类型信息导出成功！")
        # except NameError as e:
        #     logger.error("执行错误！%s" % e)
        #     feecontrol.get_windows_img()
        feecontrol.remover_file("发票种类、内容与费用类型信息")


if __name__ == '__main__':
    unittest.main()