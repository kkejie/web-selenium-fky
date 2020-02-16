# 公司预算报表
# coding=utf-8
import random

from framework.base_page import BasePage

class Budgetcomany(BasePage):
    bumenys = 'xpath=>//span[text()="部门预算"]'
    gongsi_ys = 'xpath=>//span[text()="公司预算报表"]'

    def into_gsys(self):
        self.clicked(self.bumenys)
        self.clicked(self.gongsi_ys)

    zhankai = '=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[2]/a'
    clear = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[1]/div/button[2]'
    query = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[1]/div/button[3]'

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query(self):
        self.clicked(self.query)

    def click_clear(self):
        self.clicked(self.clear)
        self.clicked(self.query)
        self.clicked(self.zhankai)

    tiaoshu = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/footer/div/div/div/div[1]/select'

    def select_200(self):
        self.select_text(self.tiaoshu, '200')

    ys_queding = 'xpath=>/html/body/div[4]/div[2]/div[1]/div[2]/button[1]'
    ys_zhibiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/table/tbody/tr/td[3]'
    yszb = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[3]/form/div/div[1]/div/button'
    yszb_1 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div[1]/div[1]/i'
    yszb_2 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/span/div'

    def get_zb_list(self):
        self.select_200()
        return self.get_texts(self.ys_zhibiao)

    def get_yszb_n(self):
        self.select_200()
        n = random.randint(1, len(self.get_texts(self.ys_zhibiao))) - 1
        zb_n = self.get_texts(self.ys_zhibiao)[n]
        self.clicked(self.yszb)
        self.clicked(self.yszb_1)
        zb_list = self.get_texts(self.yszb_2)
        n = -1
        for zb in zb_list:
            n = n + 1
            if zb == zb_n:
                self.get_elements(self.yszb_2)[n].click()
                self.clicked(self.ys_queding)
                break
        return zb_n

    kz_type = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/table/tbody/tr/td[4]'
    kz_fangshi = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[3]/form/div/div[3]/div/select'

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
    export = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[1]/div/button[1]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_export(self):
        self.clicked(self.export)

    def click_queding(self):
        self.clicked(self.queding)
