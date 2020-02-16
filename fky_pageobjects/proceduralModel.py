# 流程
# coding=utf-8

from framework.base_page import BasePage

class ProceduralModel(BasePage):
    lc_guanli = 'xpath=>//span[text()="流程管理"]'
    lc_model = 'xpath=>//span[text()="流程模型"]'
    lcm_title = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[1]/div/h2'

    def into_lc_guanli(self):
        self.clicked(self.lc_guanli)

    def click_lc_model(self):
        self.clicked(self.lc_model)

    def get_lcm_title(self):
        return self.get_text(self.lcm_title)

    # 待办事项
    dbshixiang = 'xpath=>//span[text()="我的待办事项"]'
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    query_btn = 'xpath=>//*[@id="queryButton"]'
    clear_btn = 'xpath=>//button[@ng-click="view.params={}"]'
    lcsl_name = 'xpath=>//input[@ng-model="view.params.processTitle"]'
    lcdy_name = 'xpath=>//input[@ng-model="view.params.processTitle"]'
    rwmc_str = 'xpath=>//input[@ng-model="view.params.taskName"]'
    fqr_str = 'xpath=>//input[@ng-model="view.params.processCreateName"]'

    def click_dbshixiang(self):
        self.clicked(self.dbshixiang)

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query(self):
        self.clicked(self.query_btn)

    def click_clear(self):
        self.clicked(self.clear_btn)
        self.clicked(self.query_btn)
        self.clicked(self.zhankai)

    def input_lcsl_name(self, lcsl):
        self.type(self.lcsl_name, lcsl)

    def input_lcdy_name(self, lcdy):
        self.type(self.lcdy_name, lcdy)

    def input_rwmc_str(self, rwmc):
        self.type(self.rwmc_str, rwmc)

    def input_fqr_str(self, fqr):
        self.type(self.fqr_str, fqr)

    lcsl = 'xpath=>//table/tbody/tr/td[2]/a'
    lcdy = 'xpath=>//table/tbody/tr/td[3]'
    rwmc = 'xpath=>//table/tbody/tr/td[4]'
    fqr = 'xpath=>//table/tbody/tr/td[5]'

    def get_lcsl_list(self):
        return self.get_texts(self.lcsl)

    def get_lcdy_list(self):
        return self.get_texts(self.lcdy)

    def get_rwmc_list(self):
        return self.get_texts(self.rwmc)

    def get_fqr_list(self):
        return self.get_texts(self.fqr)

    # 发起流程
    faqi = 'xpath=>//span[text()="我发起的流程"]'
    select_state = 'xpath=>//select[@ng-model="view.params.processStatus"]'
    fq_lcsl = 'xpath=>//table/tbody/tr/td[1]/a'
    fq_lcdy = 'xpath=>//table/tbody/tr/td[2]'
    fq_state = 'xpath=>//table/tbody/tr/td[8]/font'

    def select_fq_state(self, state):
        self.select_text(self.select_state, state)

    def click_faqi(self):
        self.clicked(self.faqi)

    def get_fq_lcsl(self):
        return self.get_texts(self.fq_lcsl)

    def get_fq_lcdy(self):
        return self.get_texts(self.fq_lcdy)

    def get_fq_state(self):
        return self.get_texts(self.fq_state)

    # 审批的流程
    splc = 'xpath=>//span[text()="我审批的流程"]'
    sp_fqr = 'xpath=>//table/tbody/tr/td[3]'

    def click_splc(self):
        self.clicked(self.splc)

    def get_sp_fqr(self):
        return self.get_texts(self.sp_fqr)