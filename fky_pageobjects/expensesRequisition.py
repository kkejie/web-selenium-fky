# 费用申请
import os
import random
from framework.base_page import BasePage
from framework import generator

class ExpensesRequisition(BasePage):
    bxgl = 'xpath=>//span[text()="报销管理"]'
    fysq = 'xpath=>//span[text()="费用申请"]'

    def into_fysq(self):
        self.clicked(self.bxgl)
        self.clicked(self.fysq)

    rcsq = 'xpath=>//button[text()="日常申请"]'

    def click_add_rcsq(self):
        self.clicked(self.rcsq)

    shiyou = 'xpath=>//input[@name="mainContent"]'
    sqbm = 'xpath=>//input[@name="applyOrgName"]'
    jhrq = 'xpath=>//input[@ng-model="tab.expensesApply.planDate"]'
    today = '''xpath=>//button[@ng-click="select('today', $event)"]'''
    cyry = 'xpath=>//input[@autocomplete="off"]'
    xuanren = 'xpath=>//*[@id="select_employee_value"]/div/auto-complete/div/ul/li[1]'
    jzbm = 'xpath=>//span[@ng-click="tab.showOrgSelectDialog=true"]'
    jzbm_1 = 'css=>div.modal-body.pre-scrollable > div > div > div > div > div.tree-folder-header.ng-scope > i'
    jzbm_2 = 'css=>div.modal-body.pre-scrollable > div > div > div > div > div.tree-folder-content.ng-scope > div:nth-child(1) > div > span > div'
    jzbm_queding = 'xpath=>//button[@ng-click="tree.ok()"]'

    gsxm = 'xpath=>//i[@ng-click="tab.showProjectSelectDialog=true"]'
    gsxm_tiaoshu = 'xpath=>//select[@ng-change="$$selector.change();"]'
    gsxm_name = 'xpath=>//td[3][@class="ng-binding"]'
    gsxm_queding = 'xpath=>//button[@ng-click="projectInfoSelect.save()"]'
    shuoming = 'xpath=>//textarea[@type="text"]'

    fujian = 'css=>button.add'
    fj_2 = 'xpath=>//select[@ng-model="item.typeInstId"]'
    fj_2_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/form[1]/div[5]/div/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[1]/select/option'
    fj_3 = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/form[1]/div[5]/div/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[2]/div/span'

    fylx = 'xpath=>//select[@ng-model="expensesApplyConsu.costCode"]'
    fylx_1 = 'xpath=>//option[@ng-repeat="item in costCodeList"]'
    jine = 'xpath=>//input[@ng-change="tab.countMoney()"]'

    def edit_richang_fysq(self, shiyou, value):
        self.type(self.shiyou, shiyou)
        sqbm = self.get_input_text(self.sqbm)
        self.clicked(self.jhrq)
        self.clicked(self.today)
        self.clicked(self.cyry)
        a = random.randint(1, len(self.get_texts(self.xuanren))) - 1
        self.get_elements(self.xuanren)[a].click()
        if value == "xinzeng":
            self.clicked(self.jzbm)
            self.clicked(self.jzbm_1)
            bm_list = self.get_texts(self.jzbm_2)
            n = -1
            for bm in bm_list:
                n = n + 1
                if bm == sqbm:
                    self.get_elements(self.jzbm_2)[n].click()
                    self.clicked(self.jzbm_queding)
                    break
        self.clicked(self.gsxm)
        self.select_text(self.gsxm_tiaoshu, '200')
        m = random.randint(1, len(self.get_texts(self.gsxm_name))) - 1
        self.get_elements(self.gsxm_name)[m].click()
        self.clicked(self.gsxm_queding)
        self.type(self.shuoming, generator.random_str(100, 200))
        # 添加附件
        # self.clicked(self.fujian)
        # self.select_from_2(self.fj_2, self.fj_2_1)
        # self.clicked(self.fj_3)
        # os.system("C:\\Users\Administrator\Desktop\\update.exe")
        self.select_from_2(self.fylx, self.fylx_1)
        jine = random.randint(10000, 20000)
        self.double_clicked(self.jine)
        self.type1(self.jine, jine)
        i = random.randint(1, len(self.get_texts(self.sf_jiekuan))) - 1
        print(i)
        if i == 0:
            self.execute_script_click(self.sf_jiekuan_is)
            self.input_hkrq()
        elif i == 1:
            self.execute_script_click(self.sf_jiekuan_no)
        # return jine

    sf_jiekuan = 'xpath=>//label[@class="i-checks "]'
    sf_jiekuan_is = "'div.row> div.add-form > div.add-element > span:nth-child(1) > label'"
    sf_jiekuan_no = "'div.row> div.add-form > div.add-element > span:nth-child(2) > label'"
    is_jiekuan = 'xpath=>//input[@value="1"]'
    no_jiekuan = 'xpath=>//input[@value="2"]'
    zf_jine = 'xpath=>//input[@ng-change="tab.countMoney()"]'
    huankuanrq = 'xpath=>//input[@ng-model="tab.expensesApply.expectedRepaymentDate"]'
    hk_today = '''xpath=>//button[@ng-click="select('today', $event)"]'''

    fk_id = 'xpath=>//select[@ng-model="tab.banks.bankId"]'
    fk_id_1 = 'xpath=>//option[@ng-repeat="bank in tab.bankList"]'

    def input_hkrq(self):
        self.clicked(self.huankuanrq)
        self.clicked(self.hk_today)

    def get_is_jiekuan(self):
        return self.get_is_selecet(self.is_jiekuan)

    def get_no_jiekuan(self):
        return self.get_is_selecet(self.is_jiekuan)

    def input_zf_jine(self, jine):
        self.type(self.zf_jine, jine)

    def select_fk_id(self):
        self.select_from_2(self.fk_id, self.fk_id_1)

    tijiao = 'xpath=>//button[@w5c-form-submit="tab.submit(20)"]'

    def select_tiaoshu_200(self):
        self.select_text(self.shiyou_tiaoshu, '200')

    save = 'xpath=>//button[text()="保存"]'
    quxiao = 'xpath=>//button[text()="取消"]'

    def click_tijiao(self):
        self.clicked(self.tijiao)

    def click_save(self):
        self.clicked(self.save)

    def click_quxiao(self):
        self.clicked(self.quxiao)

    zdbt = 'css=>span.w5c-error' # 字段必填
    tishi = 'xpath=>//p[@style="display: block;"]'
    queding = 'xpath=>//button[@tabindex="1"]'

    def get_zdbts(self):
        return self.get_texts(self.zdbt)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def click_queding(self):
        self.clicked(self.queding)

    shiyou_tiaoshu = 'xpath=>//select[@ng-change="$$selector.change();"]'
    shiyou_list = 'xpath=>//td[6]/a[@class="link ng-binding"]'

    def get_shiyou_list(self):
        self.select_tiaoshu_200()
        return self.get_texts(self.shiyou_list)

    djzt = 'xpath=>//td[9][@class="ng-binding"]'

    def get_dj_state(self):
        self.select_tiaoshu_200()
        return self.get_texts(self.djzt)

    def get_dj_shiyou(self):
        return self.get_elements(self.shiyou_list)

    # 删除
    xuan_dj = 'xpath=>//td/label[@class="i-checks"]'
    del_btn = 'xpath=>//button[@ng-click="tab.onClick(5)"]'

    def get_xuan_dj(self):
        return self.get_elements(self.xuan_dj)

    def click_del_btn(self):
        self.clicked(self.del_btn)

    # 查询
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    tj_djbh = 'xpath=>//input[@ng-model="tab.params.recordNo"]'
    tj_shiyou = 'xpath=>//input[@ng-model="tab.params.mainContent"]'
    tj_djzt = 'xpath=>//select[@ng-model="tab.params.bizStatus"]'
    djbh = 'xpath=>//td[2]/a[@ng-click="tab.detail(item)"]'

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def input_tj_djbh(self, bh):
        self.type(self.tj_djbh, bh)

    def input_tj_shiyou(self, sy):
        self.type(self.tj_shiyou, sy)

    def select_tj_djzt(self, zt):
        self.select_text(self.tj_djzt, zt)

    def get_djbh(self):
        self.select_tiaoshu_200()
        return self.get_texts(self.djbh)

    clear_btn = 'xpath=>//button[@ng-click="tab.onClick(3)"]'
    query_btn = 'xpath=>//button[@ng-click="tab.ajaxQuery()"]'

    def click_clear(self):
        self.click_zhankai()
        self.clicked(self.clear_btn)
        self.clicked(self.query_btn)

    def click_query(self):
        self.clicked(self.query_btn)

    export = 'xpath=>//button[text()="导出excel"]'

    def click_export(self):
        self.clicked(self.export)

