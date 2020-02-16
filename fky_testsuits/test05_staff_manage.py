# coding=utf-8

import unittest
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.staffManagement import StaffManag

logger = Logger(logger="StaffManage").getlog()


class StaffManage (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        staff = StaffManag(cls.driver)
        staff.into_staffgl()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test01_query_staff(self):
        '''
        * 测试用例在这里编写
        * 针对不同的测试用例修改类名及日志标识
        '''
        staff = StaffManag(self.driver)
        name1 = staff.get_name()
        # staff.into_staffgl()
        staff.query_name()
        try:
            for name in staff.get_naemlist():
                self.assertIn(name1, name, "查询失败！")
            logger.info("查询成功！")
        except NameError as e:
            logger.error("查询失败！")
            staff.get_windows_img()
        staff.clear_query_input()
        staff.wait(1)

    def test02_add_bitian(self):
        staff = StaffManag(self.driver)
        # staff.into_staffgl()
        staff.click_add()
        staff.queding_btn()
        tishi = len(staff.get_tishi())
        staff.quxiao_btn()
        try:
            self.assertEqual(4, tishi)
            logger.info("新增员工必填项验证成功.")
        except NameError as e:
            logger.error("新增员工必填项验证失败！")
            staff.get_windows_img()
        staff.wait(1)

    def test03_staff_add(self):
        staff = StaffManag(self.driver)
        # staff.into_staffgl()
        staff.click_add()
        tel = generator.random_phone_number()
        staff.staff_add(tel)
        staff.queding_btn()
        staff.sleep(10)
        try:
            self.assertEqual("保存成功,初始化密码：BS2019xy!@", staff.get_save_tishi())
            logger.info("新增员工成功.")
        except NameError as e:
            logger.error("新增员工失败！")
            staff.get_windows_img()
        staff.save_queding()
        staff.quxiao_btn()
        staff.wait(1)

    def test04_state(self):
        staff = StaffManag(self.driver)
        # staff.into_staffgl()
        state1 = staff.get_state()
        staff.state_edit()
        try:
            self.assertNotEqual(state1, staff.get_state(), "%s 失败！" % staff.get_state())
            logger.info("%s 成功." % staff.get_state())
        except NameError as e:
            logger.error( "%s 失败！" % staff.get_state())
            staff.get_windows_img()
        staff.wait(1)

    def test05_yinhangzhanghu_name(self):
        staff = StaffManag(self.driver)
        staff.into_xiugaiyh()
        staff.click_queding()
        tishi1 = staff.get_save_tishi()
        staff.save_queding()
        staff.click_quxiao()
        try:
            self.assertEqual("收款人账号不能为空！", tishi1, "收款人账号不能为空验证失败！")
            logger.info("收款人账号不能为空验证成功.")
        except NameError as e:
            logger.error( "执行失败！")
            staff.get_windows_img()
        staff.wait(1)

    def test06_yinhangzhanghu_int(self):
        staff = StaffManag(self.driver)
        staff.into_xiugaiyh()
        staff.add_yinhangzh("abc", "是")
        tishi2 = staff.get_save_tishi()
        staff.save_queding()
        staff.click_quxiao()
        try:
            self.assertEqual("请输入数字!", tishi2, "银行账户输入框不能输入字母验证失败！")
            logger.info("银行账户输入框不能输入字母验证成功.")
        except NameError as e:
            logger.error("执行失败！")
            staff.get_windows_img()
        staff.wait(1)

    def test07_yinhangzhanghu(self):
        staff = StaffManag(self.driver)
        staff.into_xiugaiyh()
        cardid = generator.randomStr(22)
        staff.add_yinhangzh(cardid, "是")
        staff.click_queding()
        try:
            self.assertEqual("已存在默认银行卡", staff.get_save_tishi(), "银行账户不能存在两条默认的数据验证失败！")
            logger.info("银行账户不能存在两条默认的数据验证成功.")
        except NameError as e:
            logger.error("执行失败！")
            staff.get_windows_img()
        staff.save_queding()
        staff.click_quxiao()
        staff.wait(1)

    def test08_yinhangzhanghu_add(self):
        staff = StaffManag(self.driver)
        staff.into_xiugaiyh()
        cardid = generator.randomStr(22)
        staff.add_yinhangzh(cardid, "否")
        staff.click_queding()
        staff.save_queding()
        cardid_list = staff.get_zhanghus()
        try:
            self.assertIn(cardid, cardid_list, "银行账户新增失败！")
            logger.info("银行账户新增成功.")
        except NameError as e:
            logger.error( "执行失败！")
            staff.get_windows_img()
        staff.click_quxiao()
        staff.wait(1)

    def test09_yinhangzhanghu_del(self):
        staff = StaffManag(self.driver)
        staff.into_xiugaiyh()
        cardid = staff.get_zhanghu()
        staff.del_yinhang()
        cardids = staff.get_zhanghus()
        try:
            self.assertNotIn(cardid, cardids, "银行账户删除失败！")
            logger.info("银行账户删除成功.")
        except NameError as e:
            logger.error( "执行失败！")
            staff.get_windows_img()
        staff.click_quxiao()
        staff.wait(1)

    def test10_export_staff(self):
        staff = StaffManag(self.driver)
        staff.export_staff()
        name_list = staff.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("员工信息.xls", name_list, "员工信息导出失败！")
            logger.info("员工信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            staff.get_windows_img()
        staff.remover_file("员工信息")
        staff.wait(1)

    def test11_yaoqingyg(self):
        staff = StaffManag(self.driver)
        staff.click_yaoqing()
        try:
            self.assertEqual("邀请链接/二维码", staff.get_yaoqing_1(), "进入邀请员工页面失败！")
            logger.info("进入邀请员工页面成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            staff.get_windows_img()
        staff.click_yqlj()
        try:
            self.assertEqual("邀请链接/二维码", staff.get_yqlj_1(), "进入邀请员工页面失败！")
            logger.info("进入邀请员工页面成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            staff.get_windows_img()
        staff.click_back()
        staff.click_zgyq()
        staff.sleep(1)
        try:
            self.assertEqual("逐个邀请同事", staff.get_zgyq_1(), "进入邀请员工页面失败！")
            logger.info("进入邀请员工页面成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            staff.get_windows_img()


if __name__ == '__main__':
    unittest.main()
