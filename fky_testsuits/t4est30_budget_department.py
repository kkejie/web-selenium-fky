# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.budgetDepartment import Budgetdepartment

logger = Logger(logger = "BudgetDepartment").getlog()

class BudgetDepartment (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        department = Budgetdepartment(cls.driver)
        department.into_bmys()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_query_ysbm(self):
        department = Budgetdepartment(self.driver)
        department.click_zhankai()
        bm_n = department.get_ysbm_n()
        department.click_query()
        bm_list = department.get_bm_list()
        for bm in bm_list:
            self.assertEqual(bm_n, bm, "通过预算部门查询员工预算报表失败！")
            logger.info("通过预算部门查询员工预算报表成功！")
        department.click_clear()

    def test02_query_yszb(self):
        department = Budgetdepartment(self.driver)
        department.click_zhankai()
        zb_n = department.get_yszb_n()
        department.click_query()
        zb_list = department.get_zb_list()
        for zb in zb_list:
            self.assertEqual(zb_n, zb, "通过预算指标查询员工预算报表失败！")
            logger.info("通过预算指标查询员工预算报表成功！")
        department.click_clear()

    def test03_query_kzfs(self):
        department = Budgetdepartment(self.driver)
        department.click_zhankai()
        fs_n = department.select_kz_type()
        department.click_query()
        fs_list = department.get_kz_type()
        for fs in fs_list:
            self.assertEqual(fs_n, fs, "通过控制方式查询员工预算报表失败！")
            logger.info("通过控制方式查询员工预算报表成功！")
        department.click_clear()

    def test04_export(self):
        department = Budgetdepartment(self.driver)
        department.click_export()
        department.click_queding()
        name_list = department.file_name("C:\\Users\\Administrator\\Downloads")
        self.assertIn("员工预算报表信息.xls", name_list, "员工预算报表信息导出失败！")
        logger.info("员工预算报表信息导出成功！")
        department.remover_file("员工预算报表信息")
        department.wait(1)

if __name__ == '__main__':
    unittest.main()