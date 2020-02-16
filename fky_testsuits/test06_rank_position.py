# coding=utf-8
import os
import time
import unittest

from framework import generator
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.rankPosition import RankPosit

logger = Logger(logger = "RankPosition").getlog()

class RankPosition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        position = RankPosit(cls.driver)
        position.into_zhiji()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_add_zj(self):
        '''
        编 写 人：  柯洁
        功    能：  验证新增职位名称重复是否能成功新增
                    职级新增
        日    期：  2019-03-19
        修改记录：
        '''
        position = RankPosit(self.driver)
        # position.into_zhiji()
        position.click_add()
        position.edit_zj("经理")
        position.sleep(1)
        tishi1 = position.get_tishi()
        position.click_queding()
        name = generator.random_name()
        position.edit_zj(name)
        position.sleep(1)
        tishi2 = position.get_tishi()
        position.click_queding()
        try:
            self.assertEqual("职级名称已存在，请重新输入！",tishi1,"验证新增职级名字重复失败！")
            logger.info("验证新增职级名字重复成功！")
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        try:
            self.assertEqual("添加成功",tishi2,"新增职级失败！")
            logger.info("新增职级成功！")
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        position.wait(1)

    def test2_amend_zj(self):
        position = RankPosit(self.driver)
        # position.into_zhiji()
        state = position.get_state()
        position.amend()
        try:
            self.assertNotEqual(state,position.get_state(),"%s 失败！" %position.get_state())
            logger.info("%s 成功！" %position.get_state())
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        position.wait(1)

    def test3_export_zj(self):
        position = RankPosit(self.driver)
        # position.into_zhiji()
        position.export()
        position.click_queding()
        name_list = position.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("职级信息.xls",name_list,"导出职级信息失败！")
            logger.info("导出职级信息成功！")
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        position.remover_file("职级信息")
        position.wait(1)

    def test4_query_zj(self):
        position = RankPosit(self.driver)
        # position.into_zhiji()
        name1 = position.get_name()
        position.query()
        names = position.get_names()
        for name in names:
            try:
                self.assertIn(name1, name, "职级查询失败！")
                logger.info("职级查询成功！")
            except NameError as e:
                logger.error("执行错误！%s" % e)
                position.get_windows_img()
        position.wait(1)

    def test5_add_zw(self):
        '''
        编 写 人：  柯洁
        功    能：  验证新增职位名称重复是否能成功新增
                    职级新增
        日    期：  2019-03-19
        修改记录：
        '''
        position = RankPosit(self.driver)
        position.into_zhiwei()
        position.zw_click_add()
        position.edit_zw("职位1")
        position.sleep(1)
        tishi1 = position.get_tishi()
        position.click_queding()
        name = generator.random_name()
        position.edit_zw(name)
        position.sleep(1)
        tishi2 = position.get_tishi()
        position.click_queding()
        try:
            self.assertEqual("职位名称已存在，请重新输入！",tishi1,"验证新增职位名字重复失败！")
            logger.info("验证新增职位名字重复成功！")
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        try:
            self.assertEqual("添加成功",tishi2,"新增职位失败！")
            logger.info("新增职位成功！")
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        position.wait(1)

    def test6_amend_zw(self):
        position = RankPosit(self.driver)
        position.into_zhiwei()
        state = position.zw_get_state()
        position.zw_amend()
        try:
            self.assertNotEqual(state,position.zw_get_state(),"%s 失败！" %position.zw_get_state())
            logger.info("%s 成功！" %position.zw_get_state())
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        position.wait(1)

    def test7_export_zw(self):
        position = RankPosit(self.driver)
        position.into_zhiwei()
        position.zw_export()
        position.click_queding()
        name_list = position.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("职位信息.xls",name_list,"职位信息导出失败！")
            logger.info("职位信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" %e)
            position.get_windows_img()
        position.remover_file("职位信息")
        position.wait(1)

    def test8_query_zw(self):
        position = RankPosit(self.driver)
        position.into_zhiwei()
        name1 = position.zw_get_name()
        position.zw_query()
        names = position.zw_get_names()
        for name in names:
            try:
                self.assertIn(name1, name, "职位查询失败！")
                logger.info("职位查询成功！")
            except NameError as e:
                logger.error("执行错误！%s" % e)
                position.get_windows_img()
        position.wait(1)
if __name__ == '__main__':
    unittest.main()