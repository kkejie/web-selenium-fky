# coding=utf-8
# 合同管理
import time
import unittest
from fky_pageobjects.contractManagement import ContractManagement
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from framework import generator
from framework.logger import Logger
from fky_pageobjects.myApprove import MyApprove


logger = Logger(logger="Contract").getlog()


class Contract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        ht = ContractManagement(cls.driver)
        ht.into_contract_management()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    # 合同新增---驳回---提交---同意
    def test01_add_contract(self):
        ht = ContractManagement(self.driver)
        # 调用合同新增方法，并断言
        htid = generator.randomStr(10, True, False, False, False, False, None)
        ht.click_xinZeng()
        ht.add_contract(htid)
        myapprove = MyApprove(self.driver)
        myapprove.xuanze_spr()
        ht.click_queding()
        try:
            self.assertEqual(ht.get_sp_states()[0], "审批中")
            logger.info("发起审批合同成功！")
        except Exception as e:
            logger.error("发起审批合同失败！", e)
            ht.get_windows_img()
        # 审批项目流程--驳回
        myapprove.execute_bohui()
        # pj.click_queding()
        ht.into_contract_management()
        try:
            self.assertEqual(ht.get_sp_states()[0], "驳回")
            logger.info("驳回合同成功！")
        except Exception as e:
            logger.error("驳回合同失败！", e)
            ht.get_windows_img()
        # 审批项目流程--同意
        myapprove.execute_tijiao_tongyi(0)
        ht.into_contract_management()
        try:
            self.assertEqual(ht.get_sp_states()[0], "审批通过")
            logger.info("新增合同成功！")
        except Exception as e:
            logger.error("新增合同失败！", e)
            ht.get_windows_img()

    # 调用禁用，启用方法，并断言
    def test02_jinyong_contract(self):
        ht = ContractManagement(self.driver)
        n = -1
        for ht_state in ht.get_ht_states():
            n = n + 1
            if ht_state == "启用" and ht.get_sp_states()[n] == "审批通过":
                ht.get_jinyongs_elements()[n].click()
                time.sleep(1)
                ht.click_queding()
                try:
                    self.assertEqual(ht.get_ht_states()[n], "禁用")
                    logger.info("合同:%s 禁用成功！" % ht.gain_contractId()[n])
                except Exception as e:
                    logger.error("合同禁用失败！", e)
                    ht.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法禁用" % ht.gain_contractId()[n])

    # 启用
    def test03_qiyong_contract(self):
        ht = ContractManagement(self.driver)
        n = -1
        for ht_state in ht.get_ht_states():
            n = n + 1
            if ht_state == "禁用" and ht.get_sp_states()[n] == "审批通过":
                ht.get_qiyongs_elements()[n].click()
                time.sleep(1)
                ht.click_queding()
                try:
                    self.assertEqual(ht.get_ht_states()[n], "启用")
                    logger.info("合同:%s 启用成功！" % ht.gain_contractId()[n])
                except Exception as e:
                    logger.error("合同启用失败！", e)
                    ht.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法启用" % ht.gain_contractId()[n])

    # 合同修改---反对
    def test04_modify_contract(self):
        ht = ContractManagement(self.driver)
        n = -1
        for ht_state in ht.get_ht_states():
            n = n + 1
            if ht_state == "启用" and ht.get_sp_states()[n] == "审批通过":
                ht.get_xiugais_elements()[n].click()
                time.sleep(1)
                htid = generator.randomStr(
                    10, True, False, False, False, False, None)
                ht.add_contract(htid)
                myapprove = MyApprove(self.driver)
                myapprove.xuanze_spr()
                ht.click_queding()
                try:
                    self.assertEqual(ht.get_sp_states()[n], "审批中")
                    self.assertEqual(ht.get_ht_states()[n], "禁用")
                    logger.info("发起审批合同修改成功！")
                except Exception as e:
                    logger.error("发起审批合同修改失败！", e)
                    ht.get_windows_img()
                # 审批项目流程--反对
                myapprove.execute_fandui()
                ht.into_contract_management()
                try:
                    self.assertEqual(ht.get_sp_states()[n], "审批通过")
                    self.assertEqual(ht.get_ht_states()[n], "启用")
                    logger.info("反对合同修改成功！")
                except Exception as e:
                    logger.error("反对合同修改失败！", e)
                    ht.get_windows_img()
                # # 审批项目流程--同意
                # myapprove.execute_tijiao_tongyi(0)
                # ht.into_contract_management()
                # try:
                #     self.assertEqual(ht.get_sp_states()[0], "审批通过")
                #     logger.info("修改合同成功！")
                # except Exception as e:
                #     logger.error("修改合同失败！", e)
                #     ht.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法修改" % ht.gain_contractId()[n])

    # 合同修改---同意
    def test05_modify_contract(self):
        ht = ContractManagement(self.driver)
        n = -1
        for ht_state in ht.get_ht_states():
            n = n + 1
            if ht_state == "启用" and ht.get_sp_states()[n] == "审批通过":
                ht.get_xiugais_elements()[n].click()
                time.sleep(1)
                htid = generator.randomStr(
                    10, True, False, False, False, False, None)
                ht.add_contract(htid)
                myapprove = MyApprove(self.driver)
                myapprove.xuanze_spr()
                ht.click_queding()
                try:
                    self.assertEqual(ht.get_sp_states()[n], "审批中")
                    self.assertEqual(ht.get_ht_states()[n], "禁用")
                    logger.info("发起审批合同修改成功！")
                except Exception as e:
                    logger.error("发起审批合同修改失败！", e)
                    ht.get_windows_img()
                # 审批项目流程--同意
                myapprove.execute_tongyi()
                ht.into_contract_management()
                try:
                    self.assertEqual(ht.gain_contractId()[n], htid)
                    self.assertEqual(ht.get_ht_states()[n], "启用")
                    self.assertEqual(ht.get_sp_states()[n], "审批通过")
                    logger.info("修改合同成功！")
                except Exception as e:
                    logger.error("修改合同失败！", e)
                    ht.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法修改" % ht.gain_contractId()[n])

    # 查询---合同编号
    def test06_query_htbh(self):
        ht = ContractManagement(self.driver)
        ht.click_zhankai()
        htbh_1 = ht.gain_contractId()[0]
        ht.input_sr_htbh(htbh_1)
        ht.click_query_btn()
        htbh_list = ht.gain_contractId()
        for htbh in htbh_list:
            self.assertEqual(htbh, htbh_1, "按合同编号查询合同失败！")
            logger.info("按合同编号查询合同成功！")
        ht.click_clear_btn()

    def test07_query_htmc(self):
        ht = ContractManagement(self.driver)
        ht.click_zhankai()
        htmc_1 = ht.get_htmc()[0]
        ht.input_sr_htmc(htmc_1)
        ht.click_query_btn()
        htmc_list = ht.get_htmc()
        for htmc in htmc_list:
            self.assertIn(htmc_1, htmc, "按合同名称查询合同失败！")
            logger.info("按合同名称查询合同成功！")
        ht.click_clear_btn()

    # 查询---合同状态
    def test08_query_htzt(self):
        ht = ContractManagement(self.driver)
        ht.click_zhankai()
        htzt_1 = ht.gain_contractState()[0]
        ht.select_sr_htzt(htzt_1)
        ht.click_query_btn()
        htzt_list = ht.gain_contractState()
        for htzt in htzt_list:
            self.assertEqual(htzt, htzt_1, "按合同状态查询合同失败！")
            logger.info("按合同状态查询合同成功！")
        ht.click_clear_btn()

    # 导入
    def test09_import_contract(self):
        ht = ContractManagement(self.driver)
        ht.click_input()
        title = ht.get_into_title()
        try:
            self.assertEqual("导入数据", title, "点击导入按钮失败！")
            logger.info("点击导入按钮成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            ht.get_windows_img()
        ht.click_close()
        ht.wait(1)

    # 导出
    def test10_export_contract(self):
        ht = ContractManagement(self.driver)
        ht.click_export()
        ht.click_queding()
        name_list = ht.file_name(r"C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("合同信息.xls", name_list, "合同信息导出失败！")
            logger.info("合同信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            ht.get_windows_img()
        ht.remover_file("合同信息")
        ht.wait(1)
