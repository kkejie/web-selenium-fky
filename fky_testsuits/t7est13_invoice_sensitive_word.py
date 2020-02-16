# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage
from framework import generator

logger = Logger(logger = "InvoiceSensitiveW").getlog()

class InvoiceSensitiveW (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_fapiaomgz()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_sensitive(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fp_add()
        feecontrol.click_fp_save()
        tishi = feecontrol.get_tishi()
        self.assertEqual("请选择发票种类！", tishi, "发票敏感字必填项验证失败！")
        logger.info("发票敏感字必填项验证成功。")
        feecontrol.click_queding()
        feecontrol.click_fp_quxiao()

    def test2_add_sensitive(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fp_add()
        feecontrol.select_fp_zhonglei()
        content = generator.random_str(10, 20)
        feecontrol.edit_content(content)
        feecontrol.click_fp_save()
        global i
        i = 1
        for i in range(0, 10):
            if feecontrol.get_tishi() == '同一个公司的“同一种发票种类和敏感字类型”组合只允许设置一行':
                feecontrol.click_queding()
                feecontrol.select_fp_zhonglei()
                content = generator.random_str(10, 20)
                feecontrol.edit_content(content)
                feecontrol.click_fp_save()
                i = i + 1
            else:
                i = 11
                break
        feecontrol.click_queding()
        self.assertIn(content, feecontrol.get_content_list(), "新增发票敏感字失败！")
        logger.info("新增发票敏感字成功。")

    def test3_modify_sensitive(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fp_xuan()
        feecontrol.click_fp_xiugai()
        content = generator.random_str(10, 20)
        feecontrol.edit_content(content)
        feecontrol.click_fp_save()
        global i
        i = 1
        for i in range(0, 10):
            if feecontrol.get_tishi() == '同一个公司的“同一种发票种类和敏感字类型”组合只允许设置一行':
                feecontrol.click_queding()
                content = generator.random_str(10, 20)
                feecontrol.edit_content(content)
                feecontrol.click_fp_save()
                i = i + 1
            else:
                i = 11
                break
        feecontrol.click_queding()
        self.assertIn(content, feecontrol.get_content_list(), "修改发票敏感字失败！")
        logger.info("修改发票敏感字成功。")



    def test4_query_sensitive(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fp_zhankai()
        feecontrol.click_fp_clear()
        content = feecontrol.get_content_list()[0]
        feecontrol.input_fp_content(content)
        feecontrol.click_fp_query()
        try:
            self.assertIn(content, feecontrol.get_content_list(), "按敏感字内容查询发票敏感字失败！")
            logger.info("按敏感字内容查询发票敏感字成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_fp_clear()

    def test5_del_sensitive(self):
        feecontrol = FeecontrolManage(self.driver)
        content = feecontrol.get_content_list()[0]
        feecontrol.click_fp_xuan()
        feecontrol.click_fp_del()
        feecontrol.click_queding()
        self.assertNotIn(content, feecontrol.get_content_list(), "删除发票敏感字失败！")
        logger.info("删除发票敏感字成功。")


    def test6_export_sensitive(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_fp_export()
        feecontrol.click_queding()
        name_list = feecontrol.file_name("C:\\Users\Kejie\Downloads")
        self.assertIn("敏感字管控.xls", name_list, "敏感字管控导出失败！")
        logger.info("敏感字管控导出成功！")
        feecontrol.remover_file("敏感字管控")

if __name__ == '__main__':
    unittest.main()