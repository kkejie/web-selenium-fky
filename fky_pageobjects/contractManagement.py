# 合同管理
# coding=utf-8

from framework.base_page import BasePage
from framework import generator
import random

class ContractManagement(BasePage):
    # 进入合同主列表
    hetongGl = 'xpath=>//span[text()="合同管理"]'
    def into_contract_management(self):
        self.clicked(self.hetongGl)

    # 新增合同
    xinzengHt = 'xpath=>//button[@ng-click="tab.onClick(3)"]'
    hetongBh="name=>contCode"
    hetongMc="name=>contName"
    hetongLx='xpath=>//select[@ng-model="tab.params.contType"]'
    shouzhiLx='xpath=>//select[@ng-model="tab.params.paymentType"]'
    qianyueFang='xpath=>//span[@ng-click="tab.showCustSupSelectDialog=true"]/i'
    qianyueFang1="xpath=>//table/tbody/tr/td[1]"
    qianyueFang2 = 'xpath=>//button[@ng-click="custSupInfoSelect.save()"]'
    qianyueFanglxr='xpath=>//input[@ng-model="tab.params.partiesLinkmen"]'
    guishuBumen0='xpath=>//span[@ng-click="tab.showOrgSelectDialog=true"]/i'
    guishuBumen1="css=>div.tree.tree-selectable > div.tree-folder.ng-scope > div.tree-folder-header.ng-scope > i"
    guishuBumen2="css=>.tree.tree-selectable>.tree-folder>.tree-folder-content>.tree-folder:first-child"
    guishuBumen3='xpath=>//button[@ng-click="tree.ok()"]'
    hetongQianshuren='xpath=>//span[@ng-click="tab.showSelectUserDialog=true"]/i'
    hetongQianshuren1="css=>div.checkbox > label.i-checks > i"
    hetongQianshuren2='xpath=>//button[@ng-click="userSelect.ok()"]'
    hetonghanshuiJe='xpath=>//input[@name="taxAmount"]'
    hetongqianshuSj='xpath=>//input[@ng-model="tab.params.signTime"]'
    hetongqianshuSj1='''xpath=>//button[@ng-disabled="isDisabled('today')"]'''
    hanshuiJiner = 'xpath=>//input[@name="tax"]'
    shuiLv = 'xpath=>//input[@name="notTaxAmount"]'
    baoCun='xpath=>//button[@w5c-form-submit="tab.save()"]'
    xinzengqueDing="xpath=>/html/body/div[2]/div[2]/button[2]"

    def add_contract(self,htid):
        self.type(self.hetongBh, htid)
        str = '测试合同'+ generator.randomStr(4)
        self.type(self.hetongMc, str)
        self.select_text(self.hetongLx, "其他类")
        self.select_text(self.shouzhiLx, "支出")
        self.clicked(self.qianyueFang)
        self.clicked(self.qianyueFang1)
        self.clicked(self.qianyueFang2)
        self.type(self.qianyueFanglxr, generator.random_name())
        self.clicked(self.guishuBumen0)
        self.clicked(self.guishuBumen1)
        self.clicked(self.guishuBumen2)
        self.clicked(self.guishuBumen3)
        self.clicked(self.hetongQianshuren)
        self.is_selecet(self.hetongQianshuren1)
        self.clicked(self.hetongQianshuren2)
        hthsje = random.randint(100000, 200000)
        self.type(self.hetonghanshuiJe, hthsje)
        self.clicked(self.hetongqianshuSj)
        self.clicked(self.hetongqianshuSj1)
        sje = random.randint(1000, 2000)
        self.type(self.hanshuiJiner, sje)
        bhsje = hthsje - sje
        self.type(self.shuiLv, bhsje)
        self.clicked(self.baoCun)

    # 新增按钮
    def click_xinZeng(self):
        self.clicked(self.xinzengHt)

    shzt = 'xpath=>//table/tbody/tr/td[14]'
    def get_sp_states(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.shzt)

    tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'
    htzt = 'xpath=>//table/tbody/tr/td[13]'

    def get_ht_states(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.htzt)


    # 禁用
    jinyongs = 'xpath=>//tr/td/button[@title="禁用"]'
    jinyongQueding="xpath=>/html/body/div[2]/div[2]/button[2]"
    qiYongs = 'xpath=>//tr/td/button[@title="启用"]'

    # 获取禁用元素
    def get_jinyongs_elements(self):
        return self.get_elements(self.jinyongs)

    # 获取启用元素
    def get_qiyongs_elements(self):
        return self.get_elements(self.qiYongs)

    # 获取合同状态
    contractState="xpath=>//tbody/tr/td[13]"
    def gain_contractState(self):
        return self.get_texts(self.contractState)

    # 获取合同编号
    hqhetongBh='xpath=>//a[@ng-click="tab.show(item)"]'

    def gain_contractId(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.hqhetongBh)

    # 修改合同
    xiuGais = 'xpath=>//tr/td/button[@title="修改"]'

    def get_xiugais_elements(self):
        return self.get_elements(self.xiuGais)

    # 查询
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    clear_btn = 'xpath=>//button[text()="清空"]'
    query_btn = 'xpath=>//button[text()="查询"]'

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query_btn(self):
        self.clicked(self.query_btn)

    def click_clear_btn(self):
        self.clicked(self.clear_btn)
        self.clicked(self.query_btn)
        self.clicked(self.zhankai)

    sr_htbh = 'xpath=>//input[@ng-model="tab.params.contCode"]'
    sr_htmc = 'xpath=>//input[@ng-model="tab.params.contName"]'
    sr_htzt = 'xpath=>//select[@ng-model="tab.params.status"]'

    def input_sr_htbh(self, htbh):
        self.type(self.sr_htbh, htbh)

    def input_sr_htmc(self, htmc):
        self.type(self.sr_htmc, htmc)

    def select_sr_htzt(self, htzt):
        self.select_text(self.sr_htzt, htzt)

    # 获取合同名称
    htmc = 'xpath=>//tbody/tr/td[3]'

    def get_htmc(self):
        return self.get_texts(self.htmc)

    # 导入
    into = 'xpath=>//button[text()="导入"]'
    into_title = 'xpath=>//h3[text()="导入数据"]'
    close = 'xpath=>//button[text()="关闭"]'

    def click_input(self):
        self.clicked(self.into)

    def get_into_title(self):
        return self.get_text(self.into_title)

    def click_close(self):
        self.clicked(self.close)

    # 导出
    export = 'xpath=>//button[text()="导出"]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_export(self):
        self.clicked(self.export)

    def click_queding(self):
        self.clicked(self.queding)
