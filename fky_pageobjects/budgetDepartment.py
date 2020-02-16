# 员工预算报表
# coding=utf-8
import random
from framework.base_page import BasePage

class Budgetdepartment(BasePage):
    bumenys = 'xpath=>//span[text()="部门预算"]'
    yuangong_ys = 'xpath=>//span[text()="员工预算报表"]'

    def into_bmys(self):
        self.clicked(self.bumenys)
        self.clicked(self.yuangong_ys)

    zhankai = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[2]/a'
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

    ys_bumen = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/table/tbody/tr/td[3]'
    ysbm = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[3]/form/div[1]/div[1]/div/button'
    ysbm_1 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div/div[1]/i'
    ysbm_2 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div/div[2]/div/div/span/div'
    ys_queding = 'xpath=>/html/body/div[4]/div[2]/div[1]/div[2]/button[1]'

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

    ys_zhibiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/table/tbody/tr/td[4]'
    yszb = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[3]/form/div/div[3]/div/button'
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

    kz_type = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[4]/div/table/tbody/tr/td[6]'
    kz_fangshi = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div/div[3]/div[3]/form/div/div[5]/div/select'

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
