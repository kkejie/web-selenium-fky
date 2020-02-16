# 职级职位
from framework.base_page import BasePage
from framework import generator

class RankPosit(BasePage):
    homepage = 'xpath=>//span[text()="首页"]'
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    zhiweizj = 'xpath=>//div[text()="职级职位"]'
    zhiji_text = "xpath=>//ul/li[1]/a"
    zhiji_add_btn = 'xpath=>//button[@ng-click="rankTab.addOrUpdateRankInfo()"]'
    zhiji_name = 'xpath=>//input[@name="rankName"]'
    zhiwei_name = 'xpath=>//input[@name="postName"]'
    jinyong = 'xpath=>//input[@value="0"]/following-sibling::i'
    qiyong = 'xpath=>//input[@value="1"]/following-sibling::i'
    save_btn = 'xpath=>//button[@w5c-form-submit="submit()"]'
    tishi = 'xpath=>/html/body/div[2]/div[2]/p'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def into_zhiji(self):
        self.clicked(self.homepage)
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        self.clicked(self.zhiweizj)
        self.clicked(self.zhiji_text)

    def click_add(self):
        self.clicked(self.zhiji_add_btn)

    # 编辑职级
    def edit_zj(self, name):
        self.type(self.zhiji_name, name)
        self.is_selecet(self.jinyong)
        self.is_selecet(self.qiyong)
        self.clicked(self.save_btn)

    # 编辑职位
    def edit_zw(self, name):
        self.type(self.zhiwei_name, name)
        self.is_selecet(self.jinyong)
        self.is_selecet(self.qiyong)
        self.clicked(self.save_btn)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def click_queding(self):
        self.clicked(self.queding)

    xiugai = 'xpath=>//div[1]/div[4]/table/tbody/tr[2]/td[4]/button'
    state = 'xpath=>//div[1]/div[4]/table/tbody/tr[2]/td[3]'
    def amend(self):
        state = self.get_text(self.state)
        self.clicked(self.xiugai)
        if state == "启用":
            self.clicked(self.jinyong)
        elif state == "禁用":
            self.clicked(self.qiyong)
        self.clicked(self.save_btn)
        self.clicked(self.queding)

    def get_state(self):
        return self.get_text(self.state)

    export_btn = 'xpath=>//button[@ng-click="rankTab.exportRank()"]'
    def export(self):
        self.clicked(self.export_btn)

    zhankai = 'xpath=>//div[1]/div[2]/a'
    query_name = 'xpath=>//input[@ng-model="rankTab.params.rankName"]'
    query_state = 'xpath=>//select[@ng-model="rankTab.params.status"]'
    clear = 'xpath=>//button[@ng-click="rankTab.clearQuery()"]'
    query_btn = 'xpath=>//button[@ng-click="rankTab.ajaxQuery(1)"]'
    zhijis = 'xpath=>//div[1]/div[4]/table/tbody/tr/td[1]'
    zhiji = 'xpath=>//div[1]/div[4]/table/tbody/tr[1]/td[1]'
    def get_name(self):
        return self.get_text(self.zhiji)

    def get_names(self):
        return self.get_texts(self.zhijis)

    def query(self):
        self.clicked(self.zhankai)
        self.type(self.query_name, self.get_name())
        self.clicked(self.query_btn)



    zhiwei_text = 'xpath=>//a[text()="职位信息"]'
    zhiwei = 'xpath=>//div[2]/div[4]/table/tbody/tr[1]/td[1]'
    zw_add_btn = 'xpath=>//button[@ng-click="postTab.addOrUpdatePostInfo()"]'

    def into_zhiwei(self):
        self.clicked(self.zhiwei_text)

    def zw_click_add(self):
        self.clicked(self.zw_add_btn)

    def zw_edit_content(self, name):
        self.type(self.zhiji_name, name)
        self.is_selecet(self.jinyong)
        self.is_selecet(self.qiyong)
        self.clicked(self.save_btn)

    def zw_get_tishi(self):
        return self.get_text(self.tishi)

    def zw_click_queding(self):
        self.clicked(self.queding)

    zw_xiugai = 'xpath=>//div[2]/div[4]/table/tbody/tr[1]/td[4]/button'
    zw_state = 'xpath=>//div[2]/div[4]/table/tbody/tr[1]/td[3]'
    def zw_amend(self):
        state = self.get_text(self.zw_state)
        self.clicked(self.zw_xiugai)
        if state == "启用":
            self.clicked(self.jinyong)
        elif state == "禁用":
            self.clicked(self.qiyong)
        self.clicked(self.save_btn)
        self.clicked(self.queding)

    def zw_get_state(self):
        return self.get_text(self.zw_state)

    zw_zhankai = 'xpath=>//div[2]/div[2]/a'
    zw_query_name = 'xpath=>//input[@ng-model="postTab.params.postName"]'
    zw_query_state = 'xpath=>//select[@ng-model="postTab.params.status"]'
    zw_clear = 'xpath=>//button[@ng-click="postTab.clearQuery()"]'
    zw_query_btn = 'xpath=>//button[@ng-click="postTab.ajaxQuery(1)"]'
    zhiweis = 'xpath=>//div[2]/div[4]/table/tbody/tr/td[1]'
    zw_export_btn = 'xpath=>//div/button[@ng-click="postTab.exportPost()"]'

    def zw_get_name(self):
        return self.get_text(self.zhiwei)

    def zw_get_names(self):
        return self.get_texts(self.zhiweis)

    def zw_query(self):
        # self.clicked(self.zw_zhankai)
        self.type(self.zw_query_name, self.zw_get_name())
        self.clicked(self.zw_query_btn)

    def zw_export(self):
        self.clicked(self.zw_export_btn)

