# 财务支付
# coding=utf-8
from selenium.webdriver.common.by import By

from framework.base_page import BasePage


class FinancialPayment(BasePage):
    # 支付
    caiwugl = 'xpath=>//span[text()="财务管理"]'
    caiwuzf = 'xpath=>//span[text()="财务支付"]'
    # danjubh = 'css=>.link.ng-binding.ng-scope'
    # danjubh = 'xpath=>//*[@class="ui-grid-canvas"]/div/div/div[3]/div[@class="ui-grid-cell-contents ng-scope"]'
    # 单据编号
    danjubh = 'css=>.left>.ui-grid-viewport>.ui-grid-canvas >.ng-scope >.ng-isolate-scope >:nth-child(3) >.ui-grid-cell-contents.ng-scope'
    # 单据类型
    # dj_type = 'css=>.left>.ui-grid-viewport>.ui-grid-canvas >.ng-scope >.ng-isolate-scope >:nth-child(4) >.ui-grid-cell-contents.ng-binding.ng-scope'
    xuan = 'xpath=>//div[@ng-click="selectButtonClick(row, $event)"]'
    fukuan_btn = 'xpath=>//button[@ng-click="tab.payment()"]'
    tijiao = 'xpath=>//button[@ng-click="tab.submit()"]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'
    tiaoshu = 'xpath=>//select[@ng-model="grid.options.paginationPageSize"]'

    def into_cwzf(self):
        self.clicked(self.caiwugl)
        self.clicked(self.caiwuzf)

    def get_danjubianhao_list(self):
        self.select_text(self.tiaoshu, "20")
        return self.get_texts(self.danjubh)

    def get_xuan_elements(self):
        self.select_text(self.tiaoshu, "20")
        return self.get_elements(self.xuan)

    def click_fukuan(self):
        self.clicked(self.fukuan_btn)

    def click_tijiao(self):
        self.clicked(self.tijiao)

    def click_queding(self):
        self.clicked(self.queding)

    # 查询
    sker = 'xpath=>//div[@role="rowgroup"]/div/div/div/div[7]/div'
    dj_type = 'xpath=>//div[@class="left ui-grid-render-container-left ui-grid-render-container"]/div[2]/div/div/div/div[4]/div'
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    clear = 'xpath=>//button[@ng-click="tab.clear()"]'
    query = 'xpath=>//button[@ng-click="tab.ajaxQuery()"]'

    def get_sker_list(self):
        self.select_text(self.tiaoshu, "20")
        return self.get_texts(self.sker)

    def get_dj_type(self):
        # self.select_text(self.tiaoshu, "20")
        return self.get_texts(self.dj_type)

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query(self):
        self.clicked(self.query)

    def click_clear(self):
        self.clicked(self.clear)
        self.clicked(self.query)
        self.clicked(self.zhankai)

    def get_data(self):
        return self.wait_element(
            (By.XPATH,
             '//div[@class="left ui-grid-render-container-left ui-grid-render-container"]/div[2]/div/div/div/div[4]/div'))

    biaotou = 'xpath=>//div[@tabindex="0"]/span[1]'

    def get_biaotou(self):
        return self.get_texts(self.biaotou)

    query_sker = 'xpath=>//input[@ng-model="tab.params.payees"]'
    query_type = 'xpath=>//select[@ng-model="tab.params.recordType"]'

    def input_query_sker(self, sker):
        self.type(self.query_sker, sker)

    def select_query_type(self, leixing):
        self.select_text(self.query_type, leixing)

    # 查询---申请人
    sqr = 'xpath=>//div[@role="rowgroup"]/div/div/div/div[5]/div'

    def get_sqr(self):
        return self.get_texts(self.sqr)

    query_sqr = 'xpath=>//input[@ng-model="tab.params.applyManName"]'

    def input_query_sqr(self, sqr):
        self.type(self.query_sqr, sqr)

    # 查询---申请部门
    sqbm = 'xpath=>//div[@role="rowgroup"]/div/div/div/div[4]/div'

    def get_sqbm(self):
        return self.get_texts(self.sqbm)

    query_sqbm = 'xpath=>//input[@ng-model="tab.params.applyOrgName"]'

    def input_query_sqbm(self, sqbm):
        self.type(self.query_sqbm, sqbm)

    # 导出
    # export = 'xpath=>//button[@ng-click="tab.exportWaitPaymentExcell()"]'
    export = 'xpath=>//button[@ng-click="tab.setPasswordImport()"]'

    def click_export(self):
        self.clicked(self.export)
