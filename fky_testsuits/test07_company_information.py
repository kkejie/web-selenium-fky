# coding=utf-8

import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.switchCompany import SwitchCompany
from fky_pageobjects.companyInformation import CompInfo

logger = Logger(logger="CompanyInfo").getlog()


class CompanyInfo (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        company = SwitchCompany(cls.driver)
        company.into_company_info()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_modification(self):
        '''
        编 写 人：柯洁
        功    能：修改公司信息
        日    期：2019-03-21
        修改记录：
        '''
        company = SwitchCompany(self.driver)
        name1 = generator.random_name()
        name2 = company.get_company_name()
        company.create_com_bitian(name1, name2)
        company.save_btn()
        company.sleep(1)
        company.save_baocun()
        name3 = company.get_compid()
        try:
            self.assertIn(name1, name3,"公司信息修改失败！")
            logger.info("公司信息修改成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            company.get_windows_img()
        company.wait(1)

    def test2_billing_info(self):
        billing = CompInfo(self.driver)
        name1 = billing.get_company_name1()
        billing.click_bill_info()
        name2 = billing.get_company_name()
        try:
            self.assertEqual(name1, name2, "公司名称自动带出失败！")
            logger.info("公司名称自动带出成功。")
        except AssertionError as e:
            logger.error(str(e))
            billing.get_windows_img()
            raise AssertionError("公司名称自动带出失败！")
        addr = generator.random_address()
        billing.modification_bill(addr)
        billing.queding_btn()
        billing.sleep(1)
        billing.queding_btn2()
        addr2 = billing.get_addr()
        try:
            self.assertEqual(addr, addr2, "开票信息修改失败！")
            logger.info("开票信息修改成功。")
        except Exception as e:
            logger.error(str(e))
            billing.get_windows_img()
            raise AssertionError("开票信息修改失败！")
        billing.wait(1)

    def test3_verify_bitian(self):
        bank = CompInfo(self.driver)
        name1 = bank.get_company_name1()
        bank.click_bank_zhanghu()
        name2 = bank.get_company_name3()
        try:
            self.assertEqual(name1, name2,"公司名称自动带出失败！")
            logger.info("公司名称自动带出成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()
        bank.click_save()
        print(bank.get_tishis())
        try:
            self.assertEqual(4, len(bank.get_tishis()), "验证必填项失败！")
            logger.info("验证必填项成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()
        bank.wait(1)

    def test4_verify_bank(self):
        bank = CompInfo(self.driver)
        bank.click_bank_zhanghu()
        bank.create_bank(bank.get_bankid(), "收入户")
        bank.click_save()
        tishi = bank.get_save_tishi()
        bank.queding_btn2()
        try:
            self.assertEqual("存在相同银行账户，保存失败", tishi, "银行账户唯一性验证失败！")
            logger.info("银行账户唯一性验证成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()
        bank.wait(1)

    def test5_verify_jibenhu(self):
        bank = CompInfo(self.driver)
        bank.click_bank_zhanghu()
        bankid = generator.randomStr(22)
        bank.create_bank(bankid, "基本户")
        bank.click_save()
        try:
            self.assertEqual("只能有一个基本户账户类型，保存失败", bank.get_save_tishi(), "银行账户基本户只能有一个验证失败！")
            logger.info("银行账户基本户只能有一个验证成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()
        bank.queding_btn2()
        bank.select_zhanghutype("支出户")
        bank.select_is()
        bank.click_save()
        try:
            self.assertEqual("存在默认账户，保存失败", bank.get_save_tishi(), "银行账户只能有一个默认账户验证失败！")
            logger.info("银行账户只能有一个默认账户验证成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()
        bank.queding_btn2()
        bank.wait(1)

    def test6_add_bank(self):
        bank = CompInfo(self.driver)
        bank.click_bank_zhanghu()
        bankid = generator.randomStr(22)
        bank.create_bank(bankid, "支出户")
        bank.select_is()
        bank.select_not()
        bank.select_jinyong()
        bank.select_qiyong()
        bank.click_save()
        bank.queding_btn2()
        bankid_list = bank.get_bankid_list()
        try:
            self.assertIn(bankid, bankid_list, "新增银行账户失败！")
            logger.info("新增银行账户成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()

    # 修改银行账户
    def test7_modification_bank(self):
        bank = CompInfo(self.driver)
        bank.click_bank_zhanghu()
        bank.click_xiugai()
        bankid = generator.randomStr(22)
        bank.create_bank(bankid, "支出户")
        bank.click_save()
        bank.queding_btn2()
        try:
            self.assertEqual(bankid, bank.get_bank_id2(), "修改银行账户失败！")
            logger.info("修改银行账户成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()

    # 删除银行账户
    def test8_del_bank(self):
        bank = CompInfo(self.driver)
        bank.click_bank_zhanghu()
        bankid = bank.get_bank_id2()
        bank.click_del()
        bank.queding_btn2()
        bank.sleep(1)
        if bank.get_save_tishi() == "删除成功":
            bank.queding_btn2()
        else:
            pass
        bankid_list = bank.get_bankid_list()
        try:
            self.assertNotIn(bankid, bankid_list, "删除银行账户失败！")
            logger.info("删除银行账户成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            bank.get_windows_img()


if __name__ == '__main__':
    unittest.main()