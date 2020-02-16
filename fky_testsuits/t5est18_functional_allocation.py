# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.functionalAllocation import FunctionalAllocation

logger = Logger(logger="ResetReimbursement").getlog()


class ResetReimbursement (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        function = FunctionalAllocation(cls.driver)
        function.into_funcall()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_functional(self):
        function = FunctionalAllocation(self.driver)
        function.click_add_bumenys()
        function.click_add_tijiao()
        try:
            self.assertEqual("请添加预算关系维护行信息", function.get_tishi(),"验证部门预算功能配置必填项失败")
            logger.info("验证部门预算功能配置必填项成功")
        except AssertionError as e:
            logger.error(str(e))
            function.get_windows_img()
            raise AssertionError("验证部门预算功能配置必填项失败")
        function.click_queding()
        function.click_add_hang()
        function.edit_hang()
        function.click_add_tijiao()
        try:
            self.assertEqual("保存成功", function.get_tishi(),"新增部门预算功能配置失败")
            logger.info("新增部门预算功能配置成功")
        except AssertionError as e:
            logger.error(str(e))
            function.get_windows_img()
            raise AssertionError("新增部门预算功能配置失败")
        function.click_queding()

    def test2_modify_functional(self):
        function = FunctionalAllocation(self.driver)
        function.click_xuan()
        function.click_modify()
        function.edit_hang()
        function.click_add_tijiao()
        self.assertEqual("保存成功", function.get_tishi(),"修改部门预算功能配置失败")
        logger.info("修改部门预算功能配置成功")
        function.click_queding()

    def test3_query_bumen(self):
        function = FunctionalAllocation(self.driver)
        function.click_zhankai()
        bumen_1 = function.get_bumen_list()[0]
        function.input_bumen_name(bumen_1)
        function.click_query()
        bumen_list = function.get_bumen_list()
        for bumen in bumen_list:
            self.assertEqual(bumen_1, bumen, "按部门名称查询部门预算功能配置失败")
            logger.info("按部门名称查询部门预算功能配置成功")
        function.click_clear()

    def test4_query_feiyong(self):
        function = FunctionalAllocation(self.driver)
        function.click_zhankai()
        feiyong_1 = function.get_feiyong_list()[0]
        function.input_feiyong_name(feiyong_1)
        function.click_query()
        feiyong_list = function.get_feiyong_list()
        for feiyong in feiyong_list:
            self.assertEqual(feiyong_1, feiyong, "按费用名称查询部门预算功能配置失败")
            logger.info("按费用名称查询部门预算功能配置成功")
        function.click_clear()

    def test5_query_state(self):
        function = FunctionalAllocation(self.driver)
        function.click_zhankai()
        state_1 = function.get_state_list()[0]
        function.select_state(state_1)
        function.click_query()
        state_list = function.get_state_list()
        for state in state_list:
            self.assertEqual(state_1, state, "按状态查询部门预算功能配置失败")
            logger.info("按状态查询部门预算功能配置成功")
        function.click_clear()

    def test6_export_functional(self):
        function = FunctionalAllocation(self.driver)
        function.click_export()
        function.click_queding()
        name_list = function.file_name("C:\\Users\Kejie\Downloads")
        self.assertIn("部门预算配置.xls", name_list, "部门预算配置导出失败！")
        logger.info("部门预算配置导出成功！")
        function.remover_file("部门预算配置")


if __name__ == '__main__':
    unittest.main()
