# coding=utf-8

import unittest
import random
from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.departmentInformation import DepartmentInfo

logger = Logger(logger = "DepartMentInfo").getlog()

class DepartMentInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        depart = DepartmentInfo(cls.driver)
        depart.into_gongsigg()
        depart.into_bumen()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        depart = DepartmentInfo(cls.driver)
        depart.quit_browser()

    def test1_creat_bumen(self):
        '''
        编 写 人：柯洁
        功    能：创建部门
        日    期：2019-03-25
        修改记录：
        '''
        depart = DepartmentInfo(self.driver)
        depart.click_creat_bumen()
        depart.click_save()
        tishi = len(depart.get_tishis())
        try:
            self.assertEqual(4, tishi, "验证必填项失败！")
            logger.info("验证必填项成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            depart.get_windows_img()
        name = "测试部"
        type = generator.randomStr(1, False, False, False, False, True, ["管理", "销售", "生产", "研发"])
        depart.creat_bumen(name, type)
        depart.click_save()
        tishi2 = depart.get_tishi2()
        try:
            self.assertEqual("部门名称已存在，请重新输入部门名称！", tishi2, "部门名称不能重复验证失败！")
            logger.info("部门名称不能重复验证成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            depart.get_windows_img()
        depart.click_queding()
        name2 = generator.random_name()
        type = generator.randomStr(1, False, False, False, False, True, ["管理", "销售", "生产", "研发"])
        depart.creat_bumen(name2, type)
        depart.click_save()
        depart.click_queding()
        name_list = depart.get_name_list()
        try:
            self.assertIn(name2, name_list, "部门新增失败！")
            logger.info("部门新增成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            depart.get_windows_img()
        depart.sleep(1)

    def test2_modifiy_bumen(self):
        """
        编 写 人：柯洁
        功    能：修改部门
        日    期：2019-03-26
        修改记录：
        """
        depart = DepartmentInfo(self.driver)
        depart.xiugai_bumen()
        name = generator.random_name()
        type = generator.randomStr(1, False, False, False, False, True, ["管理", "销售", "生产", "研发"])
        depart.creat_bumen(name, type)
        depart.click_save()
        depart.sleep(5)
        depart.click_queding()
        name_list = depart.get_name_list()
        try:
            self.assertIn(name, name_list, "部门修改失败！")
            logger.info("部门修改成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            depart.get_windows_img()
        depart.sleep(1)

    def test3_modifiy_batch(self):
        """
        编 写 人：柯洁
        功    能：批量修改部门
        日    期：2019-03-26
        修改记录：
        :return:
        """
        depart = DepartmentInfo(self.driver)
        depart.xiugai_piliang()
        content = depart.get_content()
        try:
            self.assertIn("批量修改部门", content, "点击批量修改失败！")
            logger.info("点击批量修改成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            depart.get_windows_img()
        depart.click_quxiao()

    # 导出部门信息
    def test4_export_bumen(self):
        depart = DepartmentInfo(self.driver)
        depart.click_export()
        depart.click_queding()
        name_list = depart.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("部门信息.xls", name_list, "部门信息导出失败！")
            logger.info("部门信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            depart.get_windows_img()
        depart.remover_file("部门信息")
        depart.wait(1)

    # 查询部门
    def test5_query_bumen(self):
        depart = DepartmentInfo(self.driver)
        bumen_list1 = depart.get_name_list()
        n = random.randint(1, len(bumen_list1)) - 1
        depart.query_bumen(bumen_list1[n])
        bumen_list2 = depart.get_name_list()
        try:
            self.assertEqual(bumen_list1[n], bumen_list2[0], "部门查询失败！")
            logger.info("部门查询成功。")
        except Exception as e:
            logger.error("执行失败！", e)
            depart.get_windows_img()


if __name__ == '__main__':
    unittest.main()