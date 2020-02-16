# coding=utf-8
import random
import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.feecontrolManagement import FeecontrolManage

logger = Logger(logger = "ReimburPropose").getlog()

class ReimburPropose (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        feecontrol = FeecontrolManage(cls.driver)
        feecontrol.into_feikonggl()
        feecontrol.into_bx_glshenqing()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_bxglsq(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_bx_add()
        feecontrol.click_bx_save()
        tishi = feecontrol.get_tishi()
        try:
            self.assertEqual("请选择费用类型！", tishi, "报销关联申请必填项验证失败！")
            logger.info("报销关联申请必填项验证成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            feecontrol.get_windows_img()
        feecontrol.click_queding()
        feecontrol.click_bx_quxiao()

    def test2_add_bxglsq(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_bx_add()
        feecontrol.click_feiyong_type()
        shunxu = str(random.randint(100, 999))
        tiaojian = generator.randomStr(1, False, False, False, False, True, ["不设置", "报销含税金额", "报销部门"])
        feecontrol.edit_bxglsq(shunxu, tiaojian)
        if tiaojian == "报销部门":
            feecontrol.select_bx_tiaojian2()
        elif tiaojian == "报销含税金额":
            feecontrol.select_bx_tiaojian1()
        else:
            pass
        feecontrol.click_bx_save()
        feecontrol.click_queding()
        self.assertIn(shunxu, feecontrol.get_bx_shunxu_list(), "新增报销关联申请失败！")
        logger.info("新增报销关联申请成功。")

    # def test2_add_bxglsq_2(self):
    #     feecontrol = FeecontrolManage(self.driver)
    #     feecontrol.click_bx_add()
    #     feecontrol.click_feiyong_type()
    #     shunxu = str(random.randint(100, 999))
    #     tiaojian = generator.randomStr(1, False, False, False, False, True, ["不设置", "报销含税金额", "报销部门"])
    #     feecontrol.edit_bxglsq(shunxu, tiaojian)
    #     if tiaojian == "报销部门":
    #         feecontrol.select_bx_tiaojian2()
    #     elif tiaojian == "报销含税金额":
    #         feecontrol.select_bx_tiaojian1()
    #     else:
    #         pass
    #     feecontrol.click_bx_save()
    #     feecontrol.click_queding()
    #     self.assertIn(shunxu, feecontrol.get_bx_shunxu_list(), "新增报销关联申请失败！")
    #     logger.info("新增报销关联申请成功。")

    def test3_modify_bxglsq(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_bx_xuan()
        feecontrol.click_bx_xiugai()
        shunxu = str(random.randint(100, 999))
        tiaojian = generator.randomStr(1, False, False, False, False, True, ["不设置", "报销含税金额", "报销部门"])
        feecontrol.edit_bxglsq(shunxu, tiaojian)
        if tiaojian == "报销部门":
            feecontrol.select_bx_tiaojian2()
        elif tiaojian == "报销含税金额":
            feecontrol.select_bx_tiaojian1()
        else:
            pass
        feecontrol.click_bx_save()
        feecontrol.click_queding()
        self.assertIn(shunxu, feecontrol.get_bx_shunxu_list(), "修改报销关联申请失败！")
        logger.info("修改报销关联申请成功。")

    def test4_query_bxglsq(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_bx_zhankai()
        feecontrol.click_bx_clear()
        sqspd = generator.randomStr(1, False, False, False, False, True, ["日常费用申请", "差旅费用申请"])
        feecontrol.select_bx_sqspd(sqspd)
        feecontrol.click_bx_query()
        sqspd_list = feecontrol.get_bx_sqspd_list()
        for sqspd_a in sqspd_list:
            self.assertIn(sqspd, sqspd_a, "按事前审批单查询报销关联申请失败！")
            logger.info("按事前审批单查询报销关联申请成功。")
        feecontrol.click_bx_clear()

    def test5_del_bxglsq(self):
        feecontrol = FeecontrolManage(self.driver)
        shunxu = feecontrol.get_bx_shunxu_list()[0]
        feecontrol.click_bx_xuan()
        feecontrol.click_bx_del()
        feecontrol.click_queding()
        feecontrol.sleep(1)
        feecontrol.click_queding_1()
        self.assertNotIn(shunxu, feecontrol.get_bx_shunxu_list(), "删除报销关联申请失败！")
        logger.info("删除报销关联申请成功。")

    def test6_export_bxglsq(self):
        feecontrol = FeecontrolManage(self.driver)
        feecontrol.click_bx_export()
        feecontrol.click_queding()
        name_list = feecontrol.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("报销关联申请.xls", name_list, "报销关联申请导出失败！")
            logger.info("报销关联申请导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            feecontrol.get_windows_img()
        feecontrol.remover_file("报销关联申请")


if __name__ == '__main__':
    unittest.main()