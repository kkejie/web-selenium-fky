# 部门信息

# coding=utf-8

from framework.base_page import BasePage

class DepartmentInfo(BasePage):
    homepage = 'xpath=>//span[text()="首页"]'
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    def into_gongsigg(self):
        self.clicked(self.homepage)
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)

    bumeninfo = 'xpath=>//div[text()="部门信息"]'
    chakanzzlb = 'xpath=>//button[@ng-click="orgTab.switchTab(2)"]'
    def into_bumen(self):
        self.clicked(self.bumeninfo)
        self.clicked(self.chakanzzlb)

    creat_bumen_btn = 'xpath=>//button[@ng-click="orgTab.addOrgDept()"]'
    bumen_name = 'xpath=>//input[@ng-model="tab.item.orgName"]'
    bumen_type = 'xpath=>//select[@ng-model="tab.item.deptType"]'
    shangji_bumen = 'css=>span.search > i'
    shangji_bumen_1 = 'css=>div.tree-mid.scroll2.ng-scope > div > div > div.tree-folder-header.ng-scope > span > div'
    shangji_bumen_2 = 'xpath=>//input[@ng-model="$$lastSelected[textField]"]'
    shangji_bumen_3 = 'xpath=>//button[@ng-click="ok()"]'
    creater = 'xpath=>//input[@ng-model="tab.item.createName"]'
    tishi = 'xpath=>//span[@class="w5c-error"]'
    save_btn = 'xpath=>//button[@w5c-form-submit="tab.submit()"]'
    tishi2 = 'xpath=>/html/body/div[2]/div[2]/p'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'
    name_list = 'xpath=>//table/tbody/tr/td[3]'
    def click_creat_bumen(self):
        self.clicked(self.creat_bumen_btn)

    def get_tishis(self):
        return self.get_texts(self.tishi)

    def get_tishi2(self):
        return self.get_text(self.tishi2)

    def creat_bumen(self, name, type):
        self.type(self.bumen_name, name)
        self.select_text(self.bumen_type, type)
        self.clicked(self.shangji_bumen)
        self.clicked(self.shangji_bumen_1)
        self.clicked(self.shangji_bumen_3)

    def click_save(self):
        self.clicked(self.save_btn)

    def click_queding(self):
        self.clicked(self.queding)

    def get_name_list(self):
        return self.get_texts(self.name_list)

    # 修改
    xuanzhong = 'xpath=>//table/tbody/tr[1]/td[1]/label/input'
    xuanzhong_1 = 'xpath=>//table/tbody/tr[1]/td[1]/label/i'
    xiugai_btn = 'xpath=>//button[@ng-click="orgTab.editOrgDept()"]'
    def xiugai_bumen(self):
        if self.get_is_selecet(self.xuanzhong) == 0:
            self.clicked(self.xuanzhong_1)
        else:
            pass
        self.clicked(self.xiugai_btn)

    # 批量修改
    xuanzhongs = 'xpath=>//table/thead/tr/th[1]/label/input'
    xuanzhongs_1 = 'xpath=>//table/thead/tr/th[1]/label/i'
    piliang_btn = 'xpath=>//button[@ng-click="orgTab.batchModifyDept()"]'
    content = 'xpath=>//div[@class="title"]/div/div[1]'
    quxiao = '''xpath=>//button[@ng-click="closeThisDialog('cancel')"]'''
    def xiugai_piliang(self):
        if self.get_is_selecet(self.xuanzhongs) == 0:
            self.clicked(self.xuanzhongs_1)
        else:
            pass
        self.clicked(self.piliang_btn)

    def get_content(self):
        return self.get_text(self.content)

    def click_quxiao(self):
        self.clicked(self.quxiao)

    # 导出部门信息
    export_bumen = 'xpath=>//button[@ng-click="orgTab.exportOrg()"]'
    def click_export(self):
        self.clicked(self.export_bumen)

    # 查询
    zhankai = 'css=>div.ng-scope>div.bocc-divider>a'
    query_input = 'xpath=>//input[@ng-model="orgTab.params.orgName"]'
    query_btn = 'xpath=>//button[@ng-click="orgTab.ajaxQueryPage(1)"]'
    def query_bumen(self, bumen):
        self.clicked(self.zhankai)
        self.type(self.query_input, bumen)
        self.clicked(self.query_btn)

