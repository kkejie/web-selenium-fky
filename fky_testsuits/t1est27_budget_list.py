# coding=utf-8
import random
import time
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.budgetList import BudgetList
from fky_pageobjects.myApprove import MyApprove

logger = Logger(logger="Budgetlist").getlog()


class Budgetlist (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        budget = BudgetList(cls.driver)
        budget.into_yszlb()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    # 验证必填项
    def test01_yanzheng_btx(self):
        budget = BudgetList(self.driver)
        budget.click_add_btn()
        budget.click_tijiao()
        tishi = budget.get_tishi()
        budget.click_queding()
        budget.click_fanhui()
        self.assertEqual("请先输入预算名称！", tishi, "验证新增预算主列表必填项失败！")
        logger.info("验证新增预算主列表必填项成功！")

    # 新增草稿
    def test02_add_caogao(self):
        budget = BudgetList(self.driver)
        budget.click_add_btn()
        name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        leixing = budget.edit_taitou(name)
        budget.click_add_hang()
        if leixing == "部门":
            budget.select_yszb_ysbm()
        else:
            budget.select_yszb_ygbm()
        zhouqi = generator.randomStr(1, False, False, False, False, True, ["年度", "季度", "月度"])
        budget.select_gk_zhouqi(zhouqi)
        if zhouqi == "年度":
            jine = budget.input_nd_jine()
        elif zhouqi == "季度":
            jine = budget.input_jd_jine()
        else:
            jine = budget.input_yd_jine()
        ys_zjine = int(budget.get_ys_zjine())
        try:
            self.assertEqual(jine, ys_zjine, "所填写的预算金额与页面统计的预算总金额不相等!")
            logger.info("所填写的预算金额与页面统计的预算总金额相等!")
        except Exception as e:
            logger.error("执行失败！", e)
            budget.get_windows_img()
        budget.sleep(1)
        budget.click_save_caogao()
        budget.click_queding()
        budget.click_add_btn()
        budget.click_zairucg()
        cg_name_list = budget.get_cg_ys_name()
        self.assertIn(name, cg_name_list, "保存草稿失败！")
        logger.info("保存草稿成功！")
        budget.click_close_btn()
        budget.click_fanhui()

    # 载入草稿驳回提交-同意
    def test03_zairucaogao_bhtj(self):
        budget = BudgetList(self.driver)
        budget.click_add_btn()
        budget.click_zairucg()
        ys_name = budget.xuanze_cg()
        try:
            self.assertIn(ys_name, budget.get_input_ys_name(), "载入草稿失败！")
            logger.info("载入草稿成功！")
        except Exception as e:
            logger.error("执行失败！", e)
            budget.get_windows_img()
        name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        leixing = budget.edit_taitou(name)
        budget.click_add_hang()
        if leixing == "部门":
            budget.select_yszb_ysbm()
        else:
            budget.select_yszb_ygbm()
        zhouqi = generator.randomStr(1, False, False, False, False, True, ["年度", "季度", "月度"])
        budget.select_gk_zhouqi(zhouqi)
        if zhouqi == "年度":
            jine = budget.input_nd_jine()
        elif zhouqi == "季度":
            jine = budget.input_jd_jine()
        else:
            jine = budget.input_yd_jine()
        ys_zjine = int(budget.get_ys_zjine())
        try:
            self.assertEqual(jine, ys_zjine, "所填写的预算金额与页面统计的预算总金额不相等!")
            logger.info("所填写的预算金额与页面统计的预算总金额相等!")
        except Exception as e:
            logger.error("执行失败！", e)
            budget.get_windows_img()
        budget.sleep(1)
        budget.click_tijiao()
        myapprove = MyApprove(self.driver)
        myapprove.xuanze_spr()
        budget.click_queding()
        ys_name_list = budget.get_ys_name_list()
        try:
            self.assertIn(name, ys_name_list, "新增预算失败！")
            logger.info("新增预算成功！")
        except Exception as e:
            logger.error("新增预算失败！", e)
            budget.get_windows_img()
        # 驳回
        myapprove.execute_bohui()
        budget.into_yszlb()
        n = -1
        for ys_name_1 in ys_name_list:
            n = n + 1
            if name == ys_name_1:
                ys_state = budget.get_dj_state()[n]
                try:
                    self.assertEqual("驳回", ys_state, "驳回失败！")
                    logger.info("驳回成功！")
                except Exception as e:
                    logger.error("驳回失败！", e)
                    budget.get_windows_img()
                # 审批借款流程--同意
                myapprove.execute_tijiao_tongyi_yszlb()
                budget.into_yszlb()
                ys_state_tongyi = budget.get_dj_state()[n]
                self.assertEqual("审批完成", ys_state_tongyi, "审核失败！")
                logger.info("审核通过！")
                break

    # 调整-同意
    def test04_tiaozheng_tongyi(self):
        budget = BudgetList(self.driver)
        state_list = budget.get_dj_state()
        n = -1
        for state in state_list:
            if state in ["驳回", "审批完成"]:
                n = n + 1
                if state == "审批完成":
                    budget.get_caozuo_elements()[n].click()
                    name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                    budget.input_ys_name(name)
                    # zhouqi = generator.randomStr(1, False, False, False, False, True, ["年度", "季度", "月度"])
                    # budget.select_gk_zhouqi(zhouqi)
                    # if zhouqi == "年度":
                    #     jine = budget.input_nd_jine()
                    # elif zhouqi == "季度":
                    #     jine = budget.input_jd_jine()
                    # else:
                    #     jine = budget.input_yd_jine()
                    # ys_zjine = int(budget.get_ys_zjine())
                    # try:
                    #     self.assertEqual(jine, ys_zjine, "所填写的预算金额与页面统计的预算总金额不相等!")
                    #     logger.info("所填写的预算金额与页面统计的预算总金额相等!")
                    # except Exception as e:
                    #     logger.error("执行失败！", e)
                    #     budget.get_windows_img()
                    budget.sleep(1)
                    budget.click_tijiao()
                    # budget.sleep(1)
                    myapprove = MyApprove(self.driver)
                    myapprove.xuanze_spr()
                    budget.click_queding()
                    # 同意
                    myapprove.execute_tongyi_yszlb()
                    budget.into_yszlb()
                    ys_name_list = budget.get_ys_name_list()
                    self.assertIn(name, ys_name_list, "调整预算失败！")
                    logger.info("调整预算成功！")
                    break
                else:
                    logger.info("%s: 当前状态不可调整" % state)
            else:
                logger.info("%s: 当前状态不可操作" % state)

    # 调整-反对
    def test05_tiaozheng_fandui(self):
        budget = BudgetList(self.driver)
        state_list = budget.get_dj_state()
        n = -1
        m = -1
        for state in state_list:
            m = m + 1
            if state in ["驳回", "审批完成"]:
                n = n + 1
                if state == "审批完成":
                    budget.get_caozuo_elements()[n].click()
                    name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
                    budget.input_ys_name(name)
                    # zhouqi = generator.randomStr(1, False, False, False, False, True, ["年度", "季度", "月度"])
                    # budget.select_gk_zhouqi(zhouqi)
                    # if zhouqi == "年度":
                    #     jine = budget.input_nd_jine()
                    # elif zhouqi == "季度":
                    #     jine = budget.input_jd_jine()
                    # else:
                    #     jine = budget.input_yd_jine()
                    # ys_zjine = int(budget.get_ys_zjine())
                    # try:
                    #     self.assertEqual(jine, ys_zjine, "所填写的预算金额与页面统计的预算总金额不相等!")
                    #     logger.info("所填写的预算金额与页面统计的预算总金额相等!")
                    # except Exception as e:
                    #     logger.error("执行失败！", e)
                    #     budget.get_windows_img()
                    budget.sleep(1)
                    budget.click_tijiao()
                    myapprove = MyApprove(self.driver)
                    myapprove.xuanze_spr()
                    budget.click_queding()
                    # 反对
                    myapprove.execute_fandui()
                    budget.into_yszlb()
                    ys_state = budget.get_dj_state()[m]
                    self.assertEqual("驳回", ys_state, "驳回失败！")
                    logger.info("驳回成功！")
                    break
                else:
                    logger.info("%s: 当前状态不可调整" % state)
            else:
                logger.info("%s: 当前状态不可操作" % state)

    # 新增-驳回提交-反对
    def test06_add_bhtj(self):
        budget = BudgetList(self.driver)
        budget.click_add_btn()
        name = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        budget.input_ys_name(name)
        # budget.click_add_hang()
        # if leixing == "部门":
        #     budget.select_yszb_ysbm()
        # else:
        #     budget.select_yszb_ygbm()
        # zhouqi = generator.randomStr(1, False, False, False, False, True, ["年度", "季度", "月度"])
        # budget.select_gk_zhouqi(zhouqi)
        # if zhouqi == "年度":
        #     jine = budget.input_nd_jine()
        # elif zhouqi == "季度":
        #     jine = budget.input_jd_jine()
        # else:
        #     jine = budget.input_yd_jine()
        # ys_zjine = int(budget.get_ys_zjine())
        # try:
        #     self.assertEqual(jine, ys_zjine, "所填写的预算金额与页面统计的预算总金额不相等!")
        #     logger.info("所填写的预算金额与页面统计的预算总金额相等!")
        # except Exception as e:
        #     logger.error("执行失败！", e)
        #     budget.get_windows_img()
        budget.sleep(1)
        budget.click_tijiao()
        myapprove = MyApprove(self.driver)
        myapprove.xuanze_spr()
        budget.click_queding()
        ys_name_list = budget.get_ys_name_list()
        try:
            self.assertIn(name, ys_name_list, "新增预算失败！")
            logger.info("新增预算成功！")
        except Exception as e:
            logger.error("新增预算失败！", e)
            budget.get_windows_img()
        # 驳回
        myapprove.execute_bohui()
        budget.into_yszlb()
        n = -1
        for ys_name_1 in ys_name_list:
            n = n + 1
            if name == ys_name_1:
                ys_state = budget.get_dj_state()[n]
                self.assertEqual("驳回", ys_state, "驳回失败！")
                logger.info("驳回成功！")
                break

    # 通过编号查询
    def test07_query_ys_bianhao(self):
        budget = BudgetList(self.driver)
        budget.click_zhankai()
        n = random.randint(1, len(budget.get_ys_bianhao())) - 1
        bianhao_n = budget.get_ys_bianhao()[n]
        budget.input_ys_bianhao(bianhao_n)
        budget.click_query()
        bianhao_list = budget.get_ys_bianhao()
        for bianhao in bianhao_list:
            self.assertEqual(bianhao_n, bianhao, "通过预算编号查询预算主列表失败！")
            logger.info("通过预算编号查询预算主列表成功！")
        budget.click_clear()

    # 通过预算类型查询
    def t_est08_query_ys_type(self):
        budget = BudgetList(self.driver)
        budget.click_zhankai()
        n = random.randint(1, len(budget.get_ys_type())) - 1
        type_n = budget.get_ys_type()[n]
        budget.select_ys_type(type_n)
        budget.click_query()
        type_list = budget.get_ys_type()
        for type in type_list:
            self.assertEqual(type_n, type, "通过预算类型查询预算主列表失败！")
            logger.info("通过预算类型查询预算主列表成功！")
        budget.click_clear()

    # 通过单据状态查询
    def test09_query_dj_state(self):
        budget = BudgetList(self.driver)
        budget.click_zhankai()
        n = random.randint(1, len(budget.get_dj_state())) - 1
        state_n = budget.get_dj_state()[n]
        budget.select_dj_state(state_n)
        budget.click_query()
        state_list = budget.get_dj_state()
        for state in state_list:
            self.assertEqual(state_n, state, "通过单据状态查询预算主列表失败！")
            logger.info("通过单据状态查询预算主列表成功！")
        budget.click_clear()

    # 删除
    def test10_del_ys(self):
        budget = BudgetList(self.driver)
        state_list = budget.get_dj_state()
        n = -1
        m = -1
        for state in state_list:
            m = m + 1
            if state in ["驳回", "审批完成"]:
                n = n + 1
                if state == "驳回":
                    name = budget.get_ys_name_list()[m]
                    budget.get_caozuo_elements()[n].click()
                    budget.sleep(1)
                    budget.click_queding()
                    self.assertNotIn(name, budget.get_ys_name_list(), "删除驳回的预算失败！")
                    logger.info("删除驳回的预算成功！")
                    break
                else:
                    logger.info("%s: 当前状态不可删除" % state)
            else:
                logger.info("%s: 当前状态不可操作" % state)

    # 导出预算主列表
    def test11_export(self):
        budget = BudgetList(self.driver)
        budget.click_export()
        budget.click_queding()
        name_list = budget.file_name("C:\\Users\Kejie\Downloads")
        self.assertIn("部门_员工预算信息表.xls", name_list, "部门_员工预算信息表导出失败！")
        logger.info("部门_员工预算信息表导出成功！")
        budget.remover_file("部门_员工预算信息表")
        budget.wait(1)

    # 导出批量导入模板
    def t1est12_export_pldrmb(self):
        budget = BudgetList(self.driver)
        budget.click_add_btn()
        budget.click_download()
        budget.click_queding()
        name_list = budget.file_name("C:\\Users\Administrator\Downloads")
        self.assertIn("部门_员工预算信息表批量导入模板.xls", name_list, "部门_员工预算信息表批量导入模板导出失败！")
        logger.info("部门_员工预算信息表批量导入模板导出成功！")
        budget.remover_file("部门_员工预算信息表批量导入模板")
        budget.wait(1)


if __name__ == '__main__':
    unittest.main()