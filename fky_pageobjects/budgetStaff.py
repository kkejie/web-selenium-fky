# 部门预算报表
# coding=utf-8
import random
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class Budgetstaff(BasePage):
    bumenys = 'xpath=>//span[text()="部门预算"]'
    bumen_ys = 'xpath=>//span[text()="部门预算报表"]'
    gongsi_ys = 'xpath=>//span[text()="公司预算报表"]'

    def into_bmys(self):
        self.clicked(self.bumenys)
        self.clicked(self.bumen_ys)

    def into_gsys(self):
        self.clicked(self.bumenys)
        self.clicked(self.gongsi_ys)

    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    clear = 'xpath=>//button[text()="清空"]'
    query = 'xpath=>//button[text()="查询"]'

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query(self):
        self.clicked(self.query)

    def click_clear(self):
        self.clicked(self.clear)
        self.clicked(self.query)
        self.clicked(self.zhankai)

    tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'

    def select_200(self):
        self.select_text(self.tiaoshu, '200')

    ys_bumen = 'xpath=>//table/tbody/tr/td[2]'
    ysbm = 'xpath=>//button[@ng-click="openOrg()"]'
    ysbm_1 = 'css=>div.modal-body.pre-scrollable > div > div > div > div > div.tree-folder-header.ng-scope > i'
    ysbm_2 = 'css=>div.modal-body.pre-scrollable > div > div > div > div > div.tree-folder-content.ng-scope > div:nth-child(1) > div > span > div'
    ys_queding = 'xpath=>//button[@ng-click="tree.ok()"]'

    def get_data(self):
        # el = self.driver.find_element_by_xpath(self.ys_bumen1)
        return self.wait_element((By.XPATH, '//table/tbody/tr/td[2]'))

    biaotou = 'xpath=>//table/thead/tr/th'

    def get_biaotou(self):
        return self.get_texts(self.biaotou)

    def get_bm_list(self):
        self.select_200()
        return self.get_texts(self.ys_bumen)

    def get_ysbm_n(self):
        self.select_200()
        n = random.randint(1, len(self.get_texts(self.ys_bumen))) - 1
        bm_n = self.get_texts(self.ys_bumen)[n]
        self.clicked(self.ysbm)
        self.clicked(self.ysbm_1)
        bm_list = self.get_texts(self.ysbm_2)
        n = -1
        for bm in bm_list:
            n = n + 1
            if bm == bm_n:
                self.get_elements(self.ysbm_2)[n].click()
                self.clicked(self.ys_queding)
                break
        return bm_n

    # 查询条件预算指标输入框
    yszb = 'xpath=>//input[@ng-model="tab.params.bugRelationLineName"]'

    def input_yszb(self, yszb):
        self.type(self.input_yszb(), yszb)

    # 部门预算指标
    ys_zhibiao_bm = 'xpath=>//table/tbody/tr/td[5]'

    def get_zb_list_bm(self):
        self.select_200()
        return self.get_texts(self.ys_zhibiao_bm)

    def get_yszb_n_bm(self):
        self.select_200()
        n = random.randint(1, len(self.get_texts(self.ys_zhibiao_bm))) - 1
        zb_n = self.get_texts(self.ys_zhibiao)[n]

    # 公司预算指标
    ys_zhibiao_gs = 'xpath=>//table/tbody/tr/td[4]'

    def get_zb_list_gs(self):
        self.select_200()
        return self.get_texts(self.ys_zhibiao_gs)

    def get_yszb_n_gs(self):
        self.select_200()
        n = random.randint(1, len(self.get_texts(self.ys_zhibiao_gs))) - 1
        zb_n = self.get_texts(self.ys_zhibiao)[n]
        return zb_n

    kz_type = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/table/tbody/tr/td[5]'
    kz_fangshi = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[3]/form/div[2]/div/div/select'

    def get_kz_type(self):
        self.select_200()
        return self.get_texts(self.kz_type)

    def select_kz_type(self):
        self.select_200()
        n = random.randint(1, len(self.get_texts(self.kz_type))) - 1
        zb_n = self.get_texts(self.kz_type)[n]
        self.select_text(self.kz_fangshi, zb_n)
        return zb_n

    # 导出
    export = 'xpath=>//button[text()="导出Excel"]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_export(self):
        self.clicked(self.export)

    def click_queding(self):
        self.clicked(self.queding)

    tishi = 'xpath=>/html/body/div[2]/div[2]/p'

    def get_tishi(self):
        return self.get_text(self.tishi)
