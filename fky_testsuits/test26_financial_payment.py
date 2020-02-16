# coding=utf-8
import random
import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.financialPayment import FinancialPayment

logger = Logger(logger="Payment").getlog()


class Payment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        cwzf = FinancialPayment(cls.driver)
        cwzf.into_cwzf()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    # 收款人-查询
    def test01_query_sker(self):
        cwzf = FinancialPayment(self.driver)
        cwzf.click_zhankai()
        n = random.randint(1, len(cwzf.get_sker_list())) - 1
        sker_n = cwzf.get_sker_list()[n]
        cwzf.input_query_sker(sker_n)
        cwzf.click_query()
        if cwzf.get_data():
            sker_list = cwzf.get_sker_list()
            for sker in sker_list:
                self.assertIn(sker_n, sker, "通过收款人查询财务支付单据失败！")
                logger.info("通过收款人查询财务支付单据成功！")
        else:
            self.assertEqual(['单据编号',
                              '单据类型',
                              '应付金额',
                              '已支付金额',
                              '未支付金额',
                              '申请部门',
                              '申请人',
                              '创建日期',
                              '收款人'],
                             cwzf.get_biaotou(),
                             "通过单据类型查询财务支付单据失败！")
        cwzf.click_clear()

    # 单据类型-查询
    def test02_query_type(self):
        cwzf = FinancialPayment(self.driver)
        cwzf.click_zhankai()
        n = random.randint(1, len(cwzf.get_dj_type())) - 1
        type_n = cwzf.get_dj_type()[n]
        cwzf.select_query_type("社保缴纳单")
        cwzf.click_query()
        if cwzf.get_data():
            self.assertEqual("社保缴纳单", cwzf.get_dj_type()[0], "通过单据类型查询财务支付单据失败！")
            logger.info("通过单据类型查询财务支付单据成功！")
            print(cwzf.get_biaotou())
        else:
            self.assertEqual(['单据编号',
                              '单据类型',
                              '应付金额',
                              '已支付金额',
                              '未支付金额',
                              '申请部门',
                              '申请人',
                              '创建日期',
                              '收款人'],
                             cwzf.get_biaotou(),
                             "通过单据类型查询财务支付单据失败！")
        # 获取列表数据时出现问题无法解决
        # type_list = cwzf.get_dj_type()
        # for type in type_list:
        #     self.assertEqual("社保缴纳单", type, "通过单据类型查询财务支付单据失败！")
        #     logger.info("通过单据类型查询财务支付单据成功！")
        cwzf.click_clear()

    def test03_query_sqr(self):
        cwzf = FinancialPayment(self.driver)
        cwzf.click_zhankai()
        n = random.randint(1, len(cwzf.get_sqr())) - 1
        print(cwzf.get_sqr())
        sqr_n = cwzf.get_sqr()[n]
        cwzf.input_query_sqr(sqr_n)
        cwzf.click_query()
        if cwzf.get_data():
            sker_list = cwzf.get_sqr()
            for sqr in sker_list:
                self.assertIn(sqr_n, sqr, "通过申请人查询财务支付单据失败！")
                logger.info("通过申请人查询财务支付单据成功！")
        else:
            self.assertEqual(['单据编号',
                              '单据类型',
                              '应付金额',
                              '已支付金额',
                              '未支付金额',
                              '申请部门',
                              '申请人',
                              '创建日期',
                              '收款人'],
                             cwzf.get_biaotou(),
                             "通过申请人查询财务支付单据失败！")
        cwzf.click_clear()

    """
    def test04_query_sqbm(self):
        cwzf = FinancialPayment(self.driver)
        cwzf.click_zhankai()
        n = random.randint(1, len(cwzf.get_sqbm())) - 1
        sqbm_n = cwzf.get_sqbm()[n]
        cwzf.input_query_sqbm(sqbm_n)
        cwzf.click_query()
        if cwzf.get_data():
            sqbm_list = cwzf.get_sqbm()
            for sqbm in sqbm_list:
                self.assertIn(sqbm_n, sqbm, "通过申请部门查询财务支付单据失败！")
                logger.info("通过申请部门查询财务支付单据成功！")
        else:
            self.assertEqual(['单据编号',
                              '单据类型',
                              '应付金额',
                              '已支付金额',
                              '未支付金额',
                              '申请部门',
                              '申请人',
                              '创建日期',
                              '收款人'],
                             cwzf.get_biaotou(),
                             "通过申请部门查询财务支付单据失败！")
        cwzf.click_clear()
        """

    # 导出
    def test04_export(self):
        cwzf = FinancialPayment(self.driver)
        cwzf.click_export()
        cwzf.click_queding()
        name_list = cwzf.file_name(r"C:\\Users\Kejie\Downloads")
        self.assertIn("财务支付待付款信息.xls", name_list, "财务支付待付款信息导出失败！")
        logger.info("财务支付待付款信息导出成功！")
        cwzf.remover_file("财务支付待付款信息")
        cwzf.wait(1)


if __name__ == '__main__':
    unittest.main()
