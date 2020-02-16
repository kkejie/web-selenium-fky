# coding=utf-8
# 项目主列表
import time
import unittest
from fky_pageobjects.projectList import ProjectList
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from framework import generator
from framework.logger import Logger
from fky_pageobjects.myApprove import MyApprove

logger = Logger(logger="Projectlist").getlog()


class Projectlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        pj = ProjectList(cls.driver)
        pj.click_projectList()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    # 新增
    def test1_add_project(self):
        pj=ProjectList(self.driver)
        pj.click_addproject()
        a = generator.randomStr(3)
        xmmc = "项目" + a
        print(xmmc)
        pj.add_xinzengXm(xmmc)
        myapprove = MyApprove(self.driver)
        myapprove.xuanze_spr()
        pj.click_queding()

        # 审批项目流程--驳回
        myapprove.execute_bohui()
        # pj.click_queding()
        pj.click_projectList()
        try:
            self.assertEqual(pj.gain_spzt(), "驳回")
            logger.info("驳回项目成功！")
        except Exception as e:
            logger.error("驳回项目失败！", e)
            pj.get_windows_img()
        # 审批项目流程--同意
        myapprove.execute_tijiao_tongyi(0)
        pj.click_projectList()
        try:
            self.assertEqual(pj.gain_spzt(), "审批通过")
            logger.info("新增项目成功！")
        except Exception as e:
            logger.error("新增项目失败！", e)
            pj.get_windows_img()

    # 查询
    def test2_query_project(self):
        pj = ProjectList(self.driver)
        xmmc = pj.gain_xmmc()
        pj.click_chaxun(xmmc)
        try:
            self.assertEqual(pj.gain_xmmc(), xmmc)
            logger.info("项目查询成功！")
        except Exception as e:
            logger.error("项目查询失败！", e)
            pj.get_windows_img()
        pj.click_clear()
        time.sleep(1)

    # 禁用
    def test3_jinyong_project(self):
        pj = ProjectList(self.driver)
        n = -1
        for xm_state in pj.get_xm_states():
            n = n + 1
            if xm_state == "启用" and pj.get_sp_states()[n] == "审批通过":
                pj.get_jinyongs_elements()[n].click()
                time.sleep(1)
                pj.click_queding()
                try:
                    self.assertEqual(pj.get_xm_states()[n], "禁用")
                    logger.info("项目:%s 禁用成功！" % pj.get_hqxmmcs()[n])
                except Exception as e:
                    logger.error("项目禁用失败！", e)
                    pj.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法禁用" % pj.get_hqxmmcs()[n])

    # 启用
    def test4_qiyong_project(self):
        pj = ProjectList(self.driver)
        n = -1
        for xm_state in pj.get_xm_states():
            n = n + 1
            if xm_state == "禁用" and pj.get_sp_states()[n] == "审批通过":
                pj.get_qiyongs_elements()[n].click()
                time.sleep(1)
                pj.click_queding()
                try:
                    self.assertEqual(pj.get_xm_states()[n], "启用")
                    logger.info("项目:%s 启用成功！" % pj.get_hqxmmcs()[n])
                except Exception as e:
                    logger.error("项目启用失败！", e)
                    pj.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法禁用" % pj.get_hqxmmcs()[n])

    # 修改项目
    def test5_modify_project(self):

        pj = ProjectList(self.driver)
        n = -1
        for xm_state in pj.get_xm_states():
            n = n + 1
            if xm_state == "启用" and pj.get_sp_states()[n] == "审批通过":
                pj.get_xiugai_elements()[n].click()
                b = generator.randomStr(3)
                xmmc1 = "项目" + b
                pj.amend_projectList(xmmc1)
                myapp = MyApprove(self.driver)
                myapp.xuanze_spr()
                pj.click_queding()
                pj.click_homePage()
                myapp.click_zhuban()
                pj.switch_to_window()
                myapp.click_tongyi()
                pj.switch_to_handle()
                pj.click_projectList()
                try:
                    self.assertEqual(pj.get_hqxmmcs()[n], xmmc1)
                    logger.info("修改项目成功！")
                except Exception as e:
                    logger.error("修改项目失败！", e)
                    pj.get_windows_img()
                break
            else:
                logger.info("%s: 该单据无法修改" % pj.get_hqxmmcs()[n])

    # 导入
    def test6_import_project(self):
        pj = ProjectList(self.driver)
        pj.click_input()
        title = pj.get_into_title()
        try:
            self.assertEqual("导入数据", title, "点击导入按钮失败！")
            logger.info("点击导入按钮成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            pj.get_windows_img()
        pj.click_close()
        pj.wait(1)

    def test7_export_project(self):
        pj = ProjectList(self.driver)
        pj.click_export()
        pj.click_queding()
        name_list = pj.file_name("C:\\Users\Kejie\Downloads")
        try:
            self.assertIn("项目信息.xls", name_list, "项目信息导出失败！")
            logger.info("项目信息导出成功！")
        except NameError as e:
            logger.error("执行错误！%s" % e)
            pj.get_windows_img()
        pj.remover_file("项目信息")
        pj.wait(1)