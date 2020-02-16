# 公司预算报表
# coding=utf-8
import random

from framework.base_page import BasePage

class Budgetcomany1(BasePage):
    xie_tong_ban_gong = 'xpath=>//span[text()="协同办公"]'
    gong_gao = 'xpath=>//span[text()="公告"]'
    xinzeng = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[4]/div/div[1]/div/button'

    def click_xinzeng(self):
        self.clicked(self.xie_tong_ban_gong)
        self.clicked(self.gong_gao)
        self.clicked(self.xinzeng)

    yanzheng ='xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[1]/div[1]/text()'

    def get_text1(self):
        self.get_text(self.yanzheng)