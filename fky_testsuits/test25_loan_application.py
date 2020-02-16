# coding=utf-8

import time
import unittest
import random
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.loanApplication import LoanApplication
from fky_pageobjects.myApprove import MyApprove
from fky_pageobjects.financialPayment import FinancialPayment

logger = Logger(logger="LoanApplicat").getlog()


class LoanApplicat(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        jkgl = LoanApplication(cls.driver)
        jkgl.into_jiekuansq()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_add_jiekuan(self):
        jkgl = LoanApplication(self.driver)
        jkgl.click_jk_btn()
        jkgl.click_tijiao()
        jkgl.click_queding()
        self.assertEqual("事由必填", jkgl.get_shiyou_tishi(), "验证借款必填项失败！")
        logger.info("验证借款必填项成功！")
        jkgl.click_quxiao()

    # 借款申请
    def test02_add_jiekuan(self):
        jkgl = LoanApplication(self.driver)
        jkgl.click_jk_btn()
        shiyou = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        jkgl.edit_jiekuan(shiyou)
        jkgl.click_tijiao()
        myapprove = MyApprove(self.driver)
        myapprove.xuanze_spr()
        jkgl.click_queding()
        try:
            self.assertIn(shiyou, jkgl.get_shiyou_list(), "新增借款失败！")
            logger.info("验证借款必填项成功！")
        except Exception as e:
            logger.error("新增借款失败！", e)
            jkgl.get_windows_img()
        myapprove.execute_bohui()
        jkgl.into_jiekuansq()
        try:
            self.assertEqual("审核中", jkgl.get_jk_state(), "驳回失败！")
            logger.info("驳回成功！")
        except Exception as e:
            logger.error("驳回失败！", e)
            jkgl.get_windows_img()
        # 审批借款流程--同意
        myapprove.execute_tijiao_tongyi(0)
        jkgl.into_jiekuansq()
        self.assertEqual("已审核", jkgl.get_jk_state(), "审核失败！")
        logger.info("审核通过！")

    # 财务支付
    def test03_caiwuzhifu(self):
        jk = LoanApplication(self.driver)
        cwzf = FinancialPayment(self.driver)
        jk.select_200()
        state_list = jk.get_dj_state()
        n = -1
        for state in state_list:
            n = n + 1
            if state == "已审核":
                danju_n = jk.get_danju_list()[n]
                cwzf.into_cwzf()
                danju_list = cwzf.get_danjubianhao_list()
                m = -1
                for danju in danju_list:
                    m = m + 1
                    if danju == danju_n:
                        cwzf.get_xuan_elements()[m].click()
                        cwzf.click_fukuan()
                        cwzf.click_tijiao()
                        cwzf.click_queding()
                        jk.into_jiekuansq()
                        jk.select_200()
                        self.assertEqual("已支付", jk.get_dj_state()[n], "支付失败！")
                        logger.info("支付成功！")
                        break
                break
            else:
                logger.info("%s: 该单据无需支付" % jk.get_danju_list()[n])

    # 还款
    def test03_huankuan(self):
        hk = LoanApplication(self.driver)
        hk.select_200()
        state_list = hk.get_dj_state()
        n = -1
        for state in state_list:
            n = n + 1
            whkje = hk.get_whkje()[n]
            if "," not in whkje:
                by = ""
                value = whkje
            else:
                by = whkje.split(",")[0]
                value = whkje.split(",")[1]
            str_whkje = by + value
            whqje = float(str_whkje)
            if state == "已支付" and whqje > 0:
                hk.get_xuan_elements()[n].click()
                danju = hk.get_danju_list()[n]
                hk.click_huankuan()
                jine = hk.edit_huankuan()
                hk.click_tijiao()
                myapprove = MyApprove(self.driver)
                myapprove.xuanze_spr()
                hk.click_queding()
                hk.click_zhankai()
                hk.input_danju(danju)
                hk.click_query()
                try:
                    self.assertEqual(jine, hk.get_spzhk(), "提交还款单据失败！")
                    logger.info("提交还款单据成功！")
                except Exception as e:
                    logger.error("提交还款单据失败！", e)
                    hk.get_windows_img()
                myapprove.execute_bohui()
                hk.into_jiekuansq()
                hk.select_200()
                try:
                    # self.assertEqual("未还清", hk.get_dj_state()[n], "驳回失败！")
                    self.assertEqual("已支付", hk.get_dj_state()[n], "驳回失败！")
                    logger.info("驳回成功！")
                except Exception as e:
                    logger.error("驳回失败！", e)
                    hk.get_windows_img()
                # 审批借款流程--同意
                myapprove.execute_tijiao_tongyi(0)
                hk.into_jiekuansq()
                hk.select_200()
                self.assertEqual("已还清", hk.get_dj_state()[n], "审核失败！")
                logger.info("审核通过！")
                break
            # elif state == "未还清" and whqje > 0:
            #     hk.get_xuan_elements()[n].click()
            #     danju = hk.get_danju_list()[n]
            #     hk.click_huankuan()
            #     jine = hk.edit_huankuan()
            #     hk.click_tijiao()
            #     myapprove = MyApprove(self.driver)
            #     myapprove.xuanze_spr()
            #     hk.click_queding()
            #     hk.click_zhankai()
            #     hk.input_danju(danju)
            #     hk.click_query()
            #     try:
            #         self.assertEqual(jine, hk.get_spzhk(), "提交还款单据失败！")
            #         logger.info("提交还款单据成功！")
            #     except Exception as e:
            #         logger.error("提交还款单据失败！", e)
            #         hk.get_windows_img()
            #     myapprove.execute_bohui()
            #     hk.into_jiekuansq()
            #     hk.select_200()
            #     try:
            #         self.assertEqual("未还清", hk.get_dj_state()[n], "驳回失败！")
            #         logger.info("驳回成功！")
            #     except Exception as e:
            #         logger.error("驳回失败！", e)
            #         hk.get_windows_img()
            #     # 审批借款流程--同意
            #     myapprove.execute_tijiao_tongyi(0)
            #     hk.into_jiekuansq()
            #     hk.select_200()
            #     self.assertEqual("已还清", hk.get_dj_state()[n], "审核失败！")
            #     logger.info("审核通过！")
            #     break
            else:
                logger.info("单据:%s 不可支付" % hk.get_danju_list()[n])

    # 事由-查询
    def test04_query_shiyou(self):
        jk = LoanApplication(self.driver)
        n = random.randint(1, len(jk.get_shiyou_list())) - 1
        shiyou_n = jk.get_shiyou_list()[n]
        jk.click_zhankai()
        jk.input_shiyou(shiyou_n)
        jk.click_query()
        shiyou_list = jk.get_shiyou_list()
        for shiyou in shiyou_list:
            self.assertEqual(shiyou_n, shiyou, "通过事由查询借款单据失败！")
            logger.info("通过事由查询借款单据成功！")
        jk.click_clear()

    # 状态-查询
    def test05_query_state(self):
        jk = LoanApplication(self.driver)
        n = random.randint(1, len(jk.get_dj_state())) - 1
        state_n = jk.get_dj_state()[n]
        jk.click_zhankai()
        jk.select_query_state(state_n)
        jk.click_query()
        state_list = jk.get_dj_state()
        for state in state_list:
            self.assertEqual(state_n, state, "通过状态查询借款单据失败！")
            logger.info("通过状态查询借款单据成功！")
        jk.click_clear()

    # 导出
    def test06_export(self):

        jk = LoanApplication(self.driver)
        jk.click_export()
        jk.click_queding()
        name_list = jk.file_name(r"C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("借款申请信息.xls", name_list, "借款申请信息导出失败！")
            logger.info("借款申请信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            jk.get_windows_img()
        jk.remover_file("借款申请信息")
        jk.wait(1)


if __name__ == '__main__':
    unittest.main()
