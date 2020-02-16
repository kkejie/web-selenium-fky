# coding=utf-8

import random
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.proceduralModel import ProceduralModel

logger = Logger(logger="ProcedModel").getlog()


class ProcedModel (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        proceduralmodel = ProceduralModel(cls.driver)
        proceduralmodel.into_lc_guanli()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_into_lcgl(self):
        proceduralmodel = ProceduralModel(self.driver)
        proceduralmodel.click_lc_model()
        self.assertEqual(
            "业务流程模型",
            proceduralmodel.get_lcm_title(),
            "进入流程管理页面失败！")
        logger.info("进入流程管理页面成功！")

    def test02_query_daiban(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_dbshixiang()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_lcsl_list())) - 1
        lcsl_n = dbsx.get_lcsl_list()[n]
        dbsx.input_lcsl_name(lcsl_n)
        dbsx.click_query()
        lcsl_list = dbsx.get_lcsl_list()
        for lcsl in lcsl_list:
            self.assertIn(lcsl_n, lcsl, "通过流程实例查询我的待办事项失败！")
            logger.info("通过流程实例查询我的待办事项成功！")
        dbsx.click_clear()

    def test03_query_daiban(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_dbshixiang()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_lcdy_list())) - 1
        lcdy_n = dbsx.get_lcdy_list()[n]
        dbsx.input_lcdy_name(lcdy_n)
        dbsx.click_query()
        lcdy_list = dbsx.get_lcdy_list()
        for lcdy in lcdy_list:
            self.assertIn(lcdy_n, lcdy, "通过流程定义查询我的待办事项失败！")
            logger.info("通过流程定义查询我的待办事项成功！")
        dbsx.click_clear()

    def test04_query_daiban(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_dbshixiang()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_rwmc_list())) - 1
        rwmc_n = dbsx.get_rwmc_list()[n]
        dbsx.input_rwmc_str(rwmc_n)
        dbsx.click_query()
        rwmc_list = dbsx.get_rwmc_list()
        for rwmc in rwmc_list:
            self.assertIn(rwmc_n, rwmc, "通过任务名称查询我的待办事项失败！")
            logger.info("通过任务名称查询我的待办事项成功！")
        dbsx.click_clear()

    def test05_query_daiban(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_dbshixiang()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fqr_list())) - 1
        fqr_n = dbsx.get_fqr_list()[n]
        dbsx.input_fqr_str(fqr_n)
        dbsx.click_query()
        fqr_list = dbsx.get_fqr_list()
        for fqr in fqr_list:
            self.assertIn(fqr_n, fqr, "通过发起人查询我的待办事项失败！")
            logger.info("通过发起人查询我的待办事项成功！")
        dbsx.click_clear()

    def test06_query_faqi(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_faqi()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fq_lcsl())) - 1
        lcsl_n = dbsx.get_fq_lcsl()[n]
        dbsx.input_lcsl_name(lcsl_n)
        dbsx.click_query()
        lcsl_list = dbsx.get_fq_lcsl()
        for lcsl in lcsl_list:
            self.assertIn(lcsl_n, lcsl, "通过流程实例查询我发起的流程失败！")
            logger.info("通过流程实例查询我发起的流程成功！")
        dbsx.click_clear()

    def test07_query_faqi(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_faqi()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fq_lcdy())) - 1
        lcdy_n = dbsx.get_fq_lcdy()[n]
        dbsx.input_lcdy_name(lcdy_n)
        dbsx.click_query()
        lcdy_list = dbsx.get_fq_lcdy()
        for lcdy in lcdy_list:
            self.assertIn(lcdy_n, lcdy, "通过流程定义查询我发起的流程失败！")
            logger.info("通过流程定义查询我发起的流程成功！")
        dbsx.click_clear()

    def test08_query_faqi(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_faqi()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fq_state())) - 1
        state_n = dbsx.get_fq_state()[n]
        dbsx.select_fq_state(state_n)
        dbsx.click_query()
        state_list = dbsx.get_fq_state()
        for state in state_list:
            self.assertIn(state_n, state, "通过任务状态查询我发起的流程失败！")
            logger.info("通过任务状态查询我发起的流程成功！")
        dbsx.click_clear()

    def test09_query_splc(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_splc()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fq_lcsl())) - 1
        lcsl_n = dbsx.get_fq_lcsl()[n]
        dbsx.input_lcsl_name(lcsl_n)
        dbsx.click_query()
        lcsl_list = dbsx.get_fq_lcsl()
        for lcsl in lcsl_list:
            self.assertIn(lcsl_n, lcsl, "通过流程实例查询我审批的流程失败！")
            logger.info("通过流程实例查询我审批的流程成功！")
        dbsx.click_clear()

    def test10_query_splc(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_splc()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fq_lcdy())) - 1
        lcdy_n = dbsx.get_fq_lcdy()[n]
        dbsx.input_lcdy_name(lcdy_n)
        dbsx.click_query()
        lcdy_list = dbsx.get_fq_lcdy()
        for lcdy in lcdy_list:
            self.assertIn(lcdy_n, lcdy, "通过流程定义查询我审批的流程失败！")
            logger.info("通过流程定义查询我审批的流程成功！")
        dbsx.click_clear()

    def test11_query_splc(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_splc()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_fq_state())) - 1
        state_n = dbsx.get_fq_state()[n]
        dbsx.select_fq_state(state_n)
        dbsx.click_query()
        state_list = dbsx.get_fq_state()
        for state in state_list:
            self.assertIn(state_n, state, "通过任务状态查询我审批的流程失败！")
            logger.info("通过任务状态查询我审批的流程成功！")
        dbsx.click_clear()

    def test12_query_splc(self):
        dbsx = ProceduralModel(self.driver)
        dbsx.click_splc()
        dbsx.click_zhankai()
        n = random.randint(1, len(dbsx.get_sp_fqr())) - 1
        fqr_n = dbsx.get_sp_fqr()[n]
        dbsx.input_fqr_str(fqr_n)
        dbsx.click_query()
        fqr_list = dbsx.get_sp_fqr()
        for fqr in fqr_list:
            self.assertIn(fqr_n, fqr, "通过发起人查询我审批的流程失败！")
            logger.info("通过发起人查询我审批的流程成功！")
        dbsx.click_clear()


if __name__ == '__main__':
    unittest.main()
