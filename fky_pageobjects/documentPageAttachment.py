# 单据页面附件设置
# coding=utf-8
import random

from selenium.webdriver.common.by import By

from framework import generator
from framework.base_page import BasePage


class PageAttachment(BasePage):
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    danju_fujian = 'xpath=>//div[text()="单据页面附件设置"]'    # 单据页面附件设置

    def into_danju_fujian(self):
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        self.clicked(self.danju_fujian)

    djpeizhi = 'xpath=>//div[@ng-click="oView.changeTab(item)"][2]'

    def into_djpeizhi(self):
        self.clicked(self.djpeizhi)

    add_btn = 'xpath=>//button[@ng-click="oView.add()"]'        # 新增
    save_btn = 'xpath=>//button[@ng-click="oView.save()"]'
    quxiao_btn = 'xpath=>//button[@ng-click="oView.back()"]'
    tishi = 'xpath=>/html/body/div[2]/div[2]/p'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_add_btn(self):
        self.clicked(self.add_btn)

    def click_save_btn(self):
        self.clicked(self.save_btn)

    def click_quxiao_btn(self):
        self.clicked(self.quxiao_btn)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def click_queding(self):
        self.clicked(self.queding)

    add_fjlx = 'xpath=>//button[@ng-click="oView.addRow()"]'
    djmc = 'xpath=>//select[@ng-model="detail.bisId"]'
    djmc_1 = 'xpath=>//select[@ng-model="detail.bisId"]/option'
    fjmc = 'xpath=>//input[@ng-model="detail.typeName"]'
    xuan_2 = 'xpath=>//div[@ng-repeat="bisrel in oView.bisrellist"]/label'
    xuan_queding = 'xpath=>//button[@ng-click="oView.bisrelsub()"]'

    xuan_del = 'xpath=>//input[@ng-click="oView.check()"]'
    xuan_del_1 = 'css=>table > tbody > tr > td:nth-child(1) > label'
    del_btn = 'xpath=>//button[@ng-click="oView.delDetail()"]'
    kongzhi_state = 'xpath=>//select[@ng-model="detail.control"]'
    feiyong_type = 'xpath=>//span[@ng-click="oView.openCostTypeDialog(detail)"]'
    feiyong_type_1 = 'xpath=>//div[@ng-click="userSelect.ok(x)"]/div/div[2]'
    teshu_tiaojian = 'xpath=>//select[@ng-model="detail.specialCondition"]'
    tiaojian_gongshi = 'xpath=>//select[@ng-model="detail.formula"]'
    tiaojianzhi = 'xpath=>//input[@ng-model="detail.conditionValue"]'

    def click_add_fjlxbt(self):
        self.clicked(self.add_fjlx)
        str1 = self.select_index(self.djmc, self.djmc_1)
        self.clicked(self.fjmc)
        n = random.randint(1, len(self.get_elements(self.xuan_2))) - 1
        el = self.get_elements(self.xuan_2)[n]
        el.click()
        self.clicked(self.xuan_queding)
        str2 = self.get_input_text(self.fjmc)
        return str1 + '-' + str2

    def click_add_fjlx(self):
        self.clicked(self.add_fjlx)
        str1 = self.select_index(self.djmc, self.djmc_1)
        self.clicked(self.fjmc)
        n = random.randint(1, len(self.get_elements(self.xuan_2))) - 1
        el = self.get_elements(self.xuan_2)[n]
        el.click()
        self.clicked(self.xuan_queding)
        str2 = self.get_input_text(self.fjmc)
        return str1 + '#' + str2

    def click_del_fjlx(self):
        if self.get_is_selecet(self.xuan_del) == 0:
            self.clicked(self.xuan_del_1)
        else:
            pass
        self.clicked(self.del_btn)

    def edit_mingxishuju(self):
        self.select_text(
            self.kongzhi_state, generator.randomStr(
                1, False, False, False, False, True, [
                    "必选上传", "可选上传"]))
        self.clicked(self.feiyong_type)
        n = random.randint(1, len(self.get_elements(self.feiyong_type_1))) - 1
        self.get_elements(self.feiyong_type_1)[n].click()
        self.select_text(self.teshu_tiaojian, "报销含税金额")

    def edit_minxishuju_2(self):
        self.select_text(
            self.tiaojian_gongshi, generator.randomStr(
                1, False, False, False, False, True, [
                    "大于", "大于等于"]))
        tiaojianzhi = random.randint(1, 999)
        self.double_clicked(self.tiaojianzhi)
        self.type1(self.tiaojianzhi, tiaojianzhi)
        return tiaojianzhi

    tiaoshu_1 = 'xpath=>//select[@ng-model="$$selector.pageSize"]'
    fjlx_name = 'xpath=>//tbody/tr/td[3]'
    # title = 'css=>#temp-add>.flex-1.pl30>span'
    # title = 'xpath=>//div[@ng-click="oView.changeTab(item)"][2]'

    def get_fjlx_name(self):
        self.select_text(self.tiaoshu_1, "50")
        return self.get_texts(self.fjlx_name)

    def get_title(self):
        return self.wait_element((By.CSS_SELECTOR, '#temp-add>.flex-1.pl30>span' ))

    # 修改
    modify = 'xpath=>//button[@ng-click="oView.modify()"]'
    xuan_4 = 'xpath=>//tbody/tr[1]/td[1]/label/input'
    xuan_5 = 'xpath=>//tbody/tr[1]/td[1]/label'
    tiaojianzhi_1 = 'xpath=>//tbody/tr[1]/td[8]'

    def click_modify_btn(self):
        self.clicked(self.modify)

    def click_is_xuan(self):
        if self.get_is_selecet(self.xuan_4) == 0:
            self.clicked(self.xuan_5)
        else:
            pass

    def get_tiaojianzhi(self):
        return self.get_text(self.tiaojianzhi_1)

    # 查询
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'     # 展开
    clear_btn = 'xpath=>//button[@ng-click="oView.clearall()"]'      # 清空
    # 查询
    query_btn = 'xpath=>//button[@ng-click="oView.query(1,oView.pageBean.pageSize)"]'
    # 输入附件类型
    input_fj_type = 'xpath=>//input[@ng-model="oView.params.typeName"]'
    fj_type = 'xpath=>//tbody/tr/td[3]'     # 获取附件类型
    # 输入单据类型
    input_dj_type = 'xpath=>//input[@ng-model="oView.params.bisName"]'
    dj_type = 'xpath=>//tbody/tr/td[2]'     # 获取单据类型
    # 选择状态
    input_fujianlx = 'xpath=>//input[@ng-model="oView.params.typeName"]'
    fujianlx = 'xpath=>//tbody/tr[1]/td[3]'        # 获取状态

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def get_fj_type_list(self):
        return self.get_texts(self.fj_type)

    def get_dj_type_list(self):
        return self.get_texts(self.dj_type)

    def input_fjlx(self, state):
        self.type(self.input_fujianlx, state)

    def get_fujianlx_list(self):
        return self.get_texts(self.fujianlx)

    def input_fj(self, fj_type):
        self.type(self.input_fj_type, fj_type)

    def input_dj(self, dj_type):
        self.type(self.input_dj_type, dj_type)

    def click_query(self):
        self.clicked(self.query_btn)

    def click_clear(self):
        self.clicked(self.clear_btn)
        self.clicked(self.query_btn)
        self.clicked(self.zhankai)

    # 导出
    export = 'xpath=>//button[@ng-click="oView.exportExcel()"]'

    def click_export(self):
        self.clicked(self.export)
