# coding=utf-8

import unittest
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from fky_common.login import Login
from fky_common.logout import Logout
from fky_pageobjects.documentPageAttachment import PageAttachment

logger = Logger(logger="DocumentPageAttachment").getlog()


class DocumentPageAttachment (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        # 登录
        login = Login()
        login.log_in(cls)
        pageattachment = PageAttachment(cls.driver)
        pageattachment.into_danju_fujian()

    @classmethod
    def tearDownClass(cls):
        # 登出
        logout = Logout()
        logout.log_out(cls)
        cls.driver.quit()

    def test1_verify_required_1(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.sleep(1)
        pageattachment.click_add_btn()
        pageattachment.sleep(1)
        pageattachment.click_save_btn()
        self.assertEqual(
            "请添加附件上传配置数据",
            pageattachment.get_tishi(),
            "单据页面附件设置必填项验证失败！")
        logger.info("单据页面附件设置必填项验证成功！")
        pageattachment.click_queding()
        pageattachment.click_quxiao_btn()

    def test2_verify_required_2(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_add_btn()
        pageattachment.click_add_fjlx()     # 添加行
        pageattachment.click_del_fjlx()     # 删除行
        str = pageattachment.click_add_fjlxbt()
        pageattachment.edit_mingxishuju()   # 编辑行信息
        pageattachment.click_save_btn()
        self.assertEqual(
            "%s条件公式必填\n%s条件值必填" %
            (str, str), pageattachment.get_tishi(), "单据页面附件设置必填项验证失败！")
        logger.info("单据页面附件设置必填项验证成功！")
        pageattachment.click_queding()
        pageattachment.click_quxiao_btn()

    def test3_add_fujianpeizhi(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_add_btn()
        str = pageattachment.click_add_fjlx()
        str_1 = str.split("#")[1]
        pageattachment.edit_mingxishuju()
        pageattachment.edit_minxishuju_2()
        pageattachment.click_save_btn()
        global a
        a = 0
        for a in range(0, 30):
            if "%s,附件配置已存在" % str in pageattachment.get_tishi():
                pageattachment.click_queding()
                pageattachment.click_del_fjlx()  # 删除行
                str = pageattachment.click_add_fjlx()  # 添加行
                str_1 = str.split("#")[1]
                pageattachment.edit_mingxishuju()
                pageattachment.edit_minxishuju_2()
                pageattachment.click_save_btn()
                a = a + 1
                print(str_1)
            else:
                a = 33
                break
        pageattachment.click_queding()
        pageattachment.sleep(5)
        if pageattachment.get_title():
            pageattachment.click_quxiao_btn()
            logger.info("没有可以新增的单据类型！！！")
        else:
            try:
                self.assertIn(
                    str_1,
                    pageattachment.get_fjlx_name(),
                    "新增单据页面附件设置失败！")
                logger.info("新增单据页面附件设置成功！")
            except Exception as e:
                logger.error("新增单据页面附件设置失败！", e)
                pageattachment.get_windows_img()

    def test4_modify_fujianpeizhi(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_is_xuan()
        pageattachment.click_modify_btn()
        pageattachment.edit_mingxishuju()
        tiaojianzhi = pageattachment.edit_minxishuju_2()
        pageattachment.click_save_btn()
        pageattachment.click_queding()
        try:
            self.assertEqual(
                '%s.00' %
                tiaojianzhi,
                pageattachment.get_tiaojianzhi(),
                "修改单据页面附件设置失败！")
            logger.info("修改单据页面附件设置成功！")
        except Exception as e:
            logger.error("修改单据页面附件设置失败！", e)
            pageattachment.get_windows_img()

    def test5_query_fjlx(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_zhankai()
        fj_type = pageattachment.get_fj_type_list()[0]
        pageattachment.input_fj(fj_type)
        pageattachment.click_query()
        fj_type_list = pageattachment.get_fj_type_list()
        try:
            for fj in fj_type_list:
                self.assertIn(fj_type, fj, "通过附件类型查询单据页面附件设置失败！")
                logger.info("通过附件类型查询单据页面附件设置成功！")
        except Exception as e:
            logger.error("通过附件类型查询单据页面附件设置失败！", e)
            pageattachment.get_windows_img()
        pageattachment.click_clear()

    def test6_query_djlx(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_zhankai()
        dj_type = pageattachment.get_dj_type_list()[0]
        pageattachment.input_dj(dj_type)
        pageattachment.click_query()
        dj_type_list = pageattachment.get_dj_type_list()
        try:
            for dj in dj_type_list:
                self.assertIn(dj_type, dj, "通过单据类型查询单据页面附件设置失败！")
                logger.info("通过单据类型查询单据页面附件设置成功！")
        except Exception as e:
            logger.error("通过单据类型查询单据页面附件设置失败！", e)
            pageattachment.get_windows_img()
        pageattachment.click_clear()

    def test7_query_state(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_zhankai()
        fjlx = pageattachment.get_fujianlx_list()[0]
        pageattachment.input_fjlx(fjlx)
        pageattachment.click_query()
        fjlx_list = pageattachment.get_fujianlx_list()
        try:
            for fjlx_1 in fjlx_list:
                self.assertEqual(fjlx, fjlx_1, "通过附件类型查询单据页面附件设置失败！")
                logger.info("通过附件类型查询单据页面附件设置成功！")
        except Exception as e:
            logger.error("通过附件类型查询单据页面附件设置失败！", e)
            pageattachment.get_windows_img()
        pageattachment.click_clear()

    def test8_export_fujianpeizhi(self):
        pageattachment = PageAttachment(self.driver)
        pageattachment.into_djpeizhi()
        pageattachment.click_export()
        pageattachment.click_queding()
        name_list = pageattachment.file_name(r"C:\\Users\Kejie\Downloads")
        self.assertIn("单据页面附件信息.xls", name_list, "单据页面附件信息导出失败！")
        logger.info("单据页面附件信息导出成功！")
        pageattachment.remover_file("单据页面附件信息")


if __name__ == '__main__':
    unittest.main()
