# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.budgetStaff import Budgetstaff

logger = Logger(logger="BudgetComany").getlog()

class BudgetComany(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        comany = Budgetstaff(cls.driver)
        comany.into_gsys()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_query_yszb(self):
        comany = Budgetstaff(self.driver)
        comany.click_zhankai()
        if comany.get_data():        # 判断列表是否有数据
            zb_n = comany.get_yszb_n_gs()

            comany.click_query()
            zb_list = comany.get_zb_list_gs()
            for zb in zb_list:
                self.assertEqual(zb_n, zb, "通过预算指标查询公司预算报表失败！")
                logger.info("通过预算指标查询公司预算报表成功！")
            comany.click_clear()
        else:
            biaotou = comany.get_biaotou()
            self.assertEqual(['',
                              '公司',
                              '预算年度',
                              '预算周期',
                              '预算指标',
                              '预算币种',
                              '预算金额',
                              '已用金额',
                              '占用金额',
                              '可用金额',
                              '占用比'], biaotou, "进入公司预算报表失败！")

    # def test02_query_kzfs(self):
    #     comany = Budgetstaff(self.driver)
    #     comany.click_zhankai()
    #     fs_n = comany.select_kz_type()
    #     comany.click_query()
    #     fs_list = comany.get_kz_type()
    #     for fs in fs_list:
    #         self.assertEqual(fs_n, fs, "通过控制方式查询公司预算报表失败！")
    #         logger.info("通过控制方式查询公司预算报表成功！")
    #     comany.click_clear()

    def test03_export(self):
        comany = Budgetstaff(self.driver)
        if comany.get_data():        # 判断列表是否有数据
            comany.click_export()
            comany.click_queding()
            name_list = comany.file_name("C:\\Users\Kejie\Downloads")
            self.assertIn("公司预算报表信息.xls", name_list, "公司预算报表信息导出失败！")
            logger.info("公司预算报表信息导出成功！")
            comany.remover_file("公司预算报表信息")
            comany.wait(1)
        else:
            comany.click_export()
            tishi = comany.get_tishi()
            self.assertEqual("没有数据可导出!", tishi, "公司预算报表信息导出失败！")
            comany.click_queding()


if __name__ == '__main__':
    unittest.main()