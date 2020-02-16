# coding=utf-8

import time
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.budgetStaff import Budgetstaff

logger = Logger(logger="BudgetStaff").getlog()


class BudgetStaff (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        staff = Budgetstaff(cls.driver)
        staff.into_bmys()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_query_ysbm(self):
        staff = Budgetstaff(self.driver)
        staff.click_zhankai()
        if staff.get_data():        # 判断列表是否有数据
            bm_n = staff.get_ysbm_n()
            staff.click_query()
            bm_list = staff.get_bm_list()
            for bm in bm_list:
                self.assertEqual(bm_n, bm, "通过预算部门查询部门预算报表失败！")
                logger.info("通过预算部门查询部门预算报表成功！")
            staff.click_clear()
        else:
            biaotou = staff.get_biaotou()
            self.assertEqual(['',
                              '公司',
                              '使用部门',
                              '预算年度',
                              '预算周期',
                              '预算指标',
                              '预算币种',
                              '预算金额',
                              '已用金额',
                              '占用金额',
                              '可用金额',
                              '占用比'], biaotou, "进入部门预算报表失败！")

    def test02_query_yszb(self):
        staff = Budgetstaff(self.driver)
        staff.click_zhankai()
        if staff.get_data():  # 判断列表是否有数据
            zb_n = staff.get_yszb_n_bm()
            staff.input_yszb(zb_n)
            staff.click_query()
            zb_list = staff.get_zb_list_bm()
            for zb in zb_list:
                self.assertIn(zb_n, zb, "通过预算指标查询部门预算报表失败！")
                logger.info("通过预算指标查询部门预算报表成功！")
            staff.click_clear()

    # def test03_query_kzfs(self):
    #     staff = Budgetstaff(self.driver)
    #     staff.click_zhankai()
    #     fs_n = staff.select_kz_type()
    #     staff.click_query()
    #     fs_list = staff.get_kz_type()
    #     for fs in fs_list:
    #         self.assertEqual(fs_n, fs, "通过控制方式查询部门预算报表失败！")
    #         logger.info("通过控制方式查询部门预算报表成功！")
    #     staff.click_clear()

    def test04_export(self):
        staff = Budgetstaff(self.driver)
        if staff.get_data():        # 判断列表是否有数据
            staff.click_export()
            staff.click_queding()
            name_list = staff.file_name(r"C:\\Users\Administrator\Downloads")
            self.assertIn("部门预算报表信息.xls", name_list, "部门预算报表信息导出失败！")
            logger.info("部门预算报表信息导出成功！")
            staff.remover_file("部门预算报表信息")
            staff.wait(1)
        else:
            staff.click_export()
            tishi = staff.get_tishi()
            self.assertEqual("没有数据可导出!", tishi, "部门预算报表信息导出失败！")
            staff.click_queding()

if __name__ == '__main__':
    unittest.main()
