# coding=utf-8
import os

from framework.base_page import BasePage
from framework.generator import *

# 支出小计
class SpendingSubtotal(BasePage):
    bxgl = 'xpath=>//span[text()="报销管理"]'
    zhichuxj = 'xpath=>//span[text()="支出小记"]'

    def into_zcxj(self):
        self.clicked(self.bxgl)
        self.clicked(self.zhichuxj)

    # 添加住宿费
    add_btn = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/button[1]"

    def click_add(self):
        self.clicked(self.add_btn)

    shiyou = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/div/div/div[2]/div[1]/div/input"
    xzxiangmu = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/div/div/div[2]/div[2]/div/span"
    xzxiangmu_1 = "xpath=>//*[@id='ngdialog1']/div[2]/div[3]/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/input"
    xzxiangmu_qd = "xpath=>//*[@id='ngdialog1']/div[2]/div[3]/div[1]/div/button[1]"
    ccity = "xpath=>//*[@id='homecity_name']"
    jiudname = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/div/div/div[6]/div[2]/div/input"
    ruzhutime = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/div/div/div[8]/div[1]/div/input"
    ruzhutime_1 = "xpath=>/html/body/div[3]/ul/li[2]/span/button[1]"
    tuifangtime = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/div/div/div[8]/div[2]/div/input"
    tuifangtime_1 = "xpath=>/html/body/div[4]/ul/li[2]/span/button[1]"
    price = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div/div/div/div[10]/div[2]/div/div[2]/input"

    def edit_zcxj(self):
        self.type(self.shiyou, random_phone_number())
        self.clicked(self.xzxiangmu)
        self.clicked(self.xzxiangmu_1)
        self.clicked(self.xzxiangmu_qd)
        self.type(self.ccity, "北京")
        self.type(self.jiudname, "测试酒店")
        self.clicked(self.ruzhutime)
        self.clicked(self.ruzhutime_1)
        self.clicked(self.tuifangtime)
        self.clicked(self.tuifangtime_1)
        self.type(self.price, "1000")

    fujian_add = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/form/div/div[1]/div/div[2]/div/div[13]/div/file-upload/div/table/tbody/tr/td/button'
    fj_leixing = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/form/div/div[1]/div/div[2]/div/div[13]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[1]/select'
    fj_leixing_option = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/form/div/div[1]/div/div[2]/div/div[13]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[1]/select/option'
    fj_add = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/form/div/div[1]/div/div[2]/div/div[13]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[2]/div/span'

    def update_huochepiao(self):
        self.clicked(self.fujian_add)
        self.select_from_2(self.fj_leixing, self.fj_leixing_option)
        self.clicked(self.fj_add)
        os.system("C:\\Users\Administrator\Desktop\\update.exe")





    # 报销
    baoxiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div[1]/div/div/div[2]/button[1]'
    # 保存
    save = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/div[1]/div/div/div[2]/button[3]"
    # 取消
    quxiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div[1]/div/div/div[2]/button[4]'
    queding = "xpath=>/html/body/div[2]/div[2]/button[2]"

    def click_baoxiao(self):
        self.clicked(self.baoxiao)

    def add_save(self):
        self.clicked(self.save)

    def click_quxiao(self):
        self.clicked(self.quxiao)

    def click_queding(self):
        self.clicked(self.queding)

    # 字段必填提示
    zdbt_tishi = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/form/div/div[1]/div/div[2]/div/div[1]/div/span'

    def get_zdbt_tishi(self):
        return self.get_text(self.zdbt_tishi)
