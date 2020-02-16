# coding=utf-8

import random
import time
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.expensesRequisition import ExpensesRequisition
from fky_pageobjects.myApprove import MyApprove

logger = Logger(logger="ExpenseRequisition").getlog()


class ExpenseRequisition (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        expenses = ExpensesRequisition(cls.driver)
        expenses.into_fysq()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_rcsq_btzd(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_add_rcsq()
        expenses.click_tijiao()
        self.assertEqual(5, len(expenses.get_zdbts()), "验证必填字段失败！")
        logger.info("验证必填字段成功！")
        expenses.click_quxiao()
        expenses.click_queding()

    def test02_submit_rcsq(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_add_rcsq()
        shiyou_1 = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        expenses.edit_richang_fysq(shiyou_1, 'xinzeng')
        if expenses.get_is_jiekuan():
            # expenses.input_zf_jine(jine)
            expenses.select_fk_id()
        elif expenses.get_no_jiekuan():
            pass
        expenses.click_tijiao()
        expenses.click_queding()
        myapprove = MyApprove(self.driver)
        myapprove.xuanze_spr()
        expenses.click_queding()
        shiyou_list = expenses.get_shiyou_list()
        try:
            self.assertIn(shiyou_1, shiyou_list, "提交日常审批单失败！")
            logger.info("提交日常审批单成功！")
        except Exception as e:
            logger.error("提交预算失败！", e)
            expenses.get_windows_img()
        # 驳回
        myapprove.execute_bohui()
        expenses.into_fysq()
        n = -1
        for shiyou in shiyou_list:
            n = n + 1
            if shiyou_1 == shiyou:
                fy_state = expenses.get_dj_state()[n]
                try:
                    self.assertEqual("驳回", fy_state, "驳回失败！")
                    logger.info("驳回成功！")
                except Exception as e:
                    logger.error("驳回失败！", e)
                    expenses.get_windows_img()
                # 审批借款流程--同意
                myapprove.execute_tijiao_tongyi(1)
                expenses.into_fysq()
                fy_state_tongyi = expenses.get_dj_state()[n]
                self.assertEqual("审批完成", fy_state_tongyi, "审核失败！")
                logger.info("审核通过！")
                break

    def test03_save_rcsq(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_add_rcsq()
        shiyou_1 = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        expenses.edit_richang_fysq(shiyou_1, 'xinzeng')
        if expenses.get_is_jiekuan():
            expenses.select_fk_id()
        elif expenses.get_no_jiekuan():
            pass
        expenses.click_save()
        expenses.click_queding()
        expenses.click_queding()
        shiyou_list = expenses.get_shiyou_list()
        try:
            self.assertIn(shiyou_1, shiyou_list, "保存日常审批单失败！")
            logger.info("保存日常审批单成功！")
        except Exception as e:
            logger.error("保存预算失败！", e)
            expenses.get_windows_img()

    def test04_edit_rcsq(self):
        expenses = ExpensesRequisition(self.driver)
        state_list = expenses.get_dj_state()
        i = -1
        for state in state_list:
            i = i + 1
            if state == "草稿":
                expenses.get_dj_shiyou()[i].click()
                shiyou_1 = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                expenses.edit_richang_fysq(shiyou_1, 'xiugai')
                if expenses.get_is_jiekuan():
                    expenses.select_fk_id()
                elif expenses.get_no_jiekuan():
                    pass
                expenses.click_save()
                expenses.click_queding()
                expenses.click_queding()
                shiyou_list = expenses.get_shiyou_list()
                try:
                    self.assertIn(shiyou_1, shiyou_list, "修改日常审批单失败！")
                    logger.info("修改日常审批单成功！")
                except Exception as e:
                    logger.error("修改预算失败！", e)
                    expenses.get_windows_img()
                break
            else:
                logger.error("%s 状态无法修改！", state)

    def test05_del_cgdj(self):
        expenses = ExpensesRequisition(self.driver)
        state_list = expenses.get_dj_state()
        i = -1
        for state in state_list:
            i = i + 1
            if state == "草稿" or state == "驳回":
                shiyou_1 = expenses.get_shiyou_list()[i]
                expenses.get_xuan_dj()[i].click()
                expenses.click_del_btn()
                expenses.click_queding()
                shiyou_list = expenses.get_shiyou_list()
                try:
                    self.assertNotIn(shiyou_1, shiyou_list, ("%s 状态日常审批单删除失败！", state))
                    logger.info("%s 状态日常审批单删除成功！", state)
                except Exception as e:
                    logger.error("删除预算失败！", e)
                    expenses.get_windows_img()
                break
            else:
                logger.error("%s 状态无法删除！", state)

    def test06_query_djbh(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_clear()
        bh = expenses.get_djbh()[random.randint(0, len(expenses.get_djbh())-1)]
        expenses.input_tj_djbh(bh)
        expenses.click_query()
        for bh2 in expenses.get_djbh():
            self.assertIn(bh, bh2, ("按单据编号:%s 查询失败！" % bh))
        logger.info("按单据编号:%s 查询成功！", bh)
        expenses.click_clear()

    def test07_query_shiyou(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_clear()
        sy = expenses.get_shiyou_list()[random.randint(0, len(expenses.get_shiyou_list())-1 )]
        expenses.input_tj_shiyou(sy)
        expenses.click_query()
        for sy2 in expenses.get_shiyou_list():
            self.assertIn(sy, sy2, ("按事由:%s 查询失败！" % sy))
        logger.info("按事由:%s 查询成功！", sy)
        expenses.click_clear()

    def test07_query_djzt(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_clear()
        zt_list = expenses.get_dj_state()
        zt = zt_list[random.randint(0, len(zt_list)-1)]
        expenses.select_tj_djzt(zt)
        expenses.click_query()
        for zt2 in expenses.get_dj_state():
            self.assertEqual(zt, zt2, ("按单据状态:%s 查询失败！", zt))
        logger.info("按单据状态:%s 查询成功！" % zt)
        expenses.click_clear()

    def test07_export(self):
        expenses = ExpensesRequisition(self.driver)
        expenses.click_export()
        expenses.click_queding()
        name_list = expenses.file_name("C:\\Users\Kejie\Downloads")
        self.assertIn("费用申请信息.xls", name_list, "费用申请信息导出失败！")
        logger.info("费用申请信息导出成功！")
        expenses.remover_file("费用申请信息")
        expenses.wait(1)


if __name__ == '__main__':
    unittest.main()
