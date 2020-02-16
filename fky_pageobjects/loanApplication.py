# 借款申请
# coding=utf-8
import random

from framework.base_page import BasePage
from framework import generator

class LoanApplication(BasePage):
    jiekuansq = 'xpath=>//span[text()="借款申请"]'

    def into_jiekuansq(self):
        self.clicked(self.jiekuansq)

    jk_btn = '''xpath=>//button[@ng-click="jump('LOAN')"]'''
    tijiao = 'xpath=>//button[@ng-click="save()"]'
    save = 'xpath=>//button[@ng-click="saveDraft()"]'
    quxiao = 'xpath=>//button[@ng-click="back()"]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'
    shiyou_tishi = 'xpath=>//span[@ng-show="view.required.mainContent"]'

    def click_jk_btn(self):
        self.clicked(self.jk_btn)

    def click_tijiao(self):
        self.clicked(self.tijiao)

    def click_save(self):
        self.clicked(self.save)

    def get_shiyou_tishi(self):
        return self.get_text(self.shiyou_tishi)

    def click_queding(self):
        self.clicked(self.queding)

    def click_quxiao(self):
        self.clicked(self.quxiao)

    shiyou = 'xpath=>//input[@ng-model="vo.fmLoanInfo.mainContent"]'        # 事由
    jker = 'xpath=>//span[@ng-click="view.showSelectLoanManDialog=true"]/i'      # 借款人
    jker_1 = 'xpath=>//label[@ng-click="userSelect.clickItem(employeeItem,$event)"]'                # 选择借款人
    jker_queding = 'xpath=>//button[@ng-click="userSelect.ok()"]'                              # 确定
    jk_jine = 'xpath=>//input[@ng-model="vo.fmLoanInfo.localAmount"]'      # 金额
    jz_bumen = 'xpath=>//span[@ng-click="view.showSelectOrgDialog=true"]/i'        # 记账部门
    jz_bumen_1 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div/div[1]/i'                          # 加号
    jz_bumen_2 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div/div[2]/div[1]/div/span/div'      # 选择部门
    jz_bumen_queding = 'xpath=>//button[@ng-click="tree.ok()"]'                        # 确定
    gsxm = 'xpath=>//span[@ng-click="view.showProjectSelectDialog=true"]/i'         # 归属项目
    gsxm_1 = 'xpath=>/html/body/div[6]/div[2]/div[3]/div[2]/div[2]/div/table/tbody/tr/td[3]'        # 选择项目
    gsxm_queding = 'xpath=>//button[@ng-click="projectInfoSelect.save()"]'                        # 确定
    yjhkrq = 'xpath=>//i[@ng-click="tab.createDateStartDialog=true"]'      # 预计还款日期
    yjhkrq_1 = '''xpath=>//button[@ng-disabled="isDisabled('today')"]'''                   # 今天
    shuoming = 'xpath=>//textarea[@ng-model="vo.fmLoanInfo.remark"]'    # 说明
    add_fukuan = "'#app-content > div.app-content-body > div > div > div:nth-child(14) > div > button:nth-child(1)'"           # 添加付款信息
    zhifujine = 'xpath=>//input[@ng-model="item.localAmount"]'    # 金额

    def edit_jiekuan(self, shiyou):
        self.type(self.shiyou, shiyou)
        self.clicked(self.jker)
        self.clicked(self.jker_1)
        self.clicked(self.jker_queding)
        jine = random.randint(10000, 20000)
        self.type(self.jk_jine, jine)
        self.clicked(self.jz_bumen)
        self.clicked(self.jz_bumen_1)
        self.clicked(self.jz_bumen_2)
        self.clicked(self.jz_bumen_queding)
        self.clicked(self.gsxm)
        n = random.randint(1, len(self.get_texts(self.gsxm_1))) - 1
        self.get_elements(self.gsxm_1)[n].click()
        self.clicked(self.gsxm_queding)
        self.clicked(self.yjhkrq)
        self.clicked(self.yjhkrq_1)
        self.type(self.shuoming, generator.random_str(100, 500))
        # self.execute_script_click(self.add_fukuan)
        # self.type(self.zhifujine, jine)

    shiyou_list = 'xpath=>//tr[@ng-click="tab.clickItem(item,$event)"]/td[4]/a'
    jk_state = 'xpath=>//tr[@ng-click="tab.clickItem(item,$event)"][1]/td[12]'

    def get_shiyou_list(self):
        return self.get_texts(self.shiyou_list)

    def get_jk_state(self):
        return self.get_text(self.jk_state)

    dj_state = 'xpath=>//tr[@ng-click="tab.clickItem(item,$event)"]/td[12]'
    xuan = 'xpath=>//tr[@ng-click="tab.clickItem(item,$event)"]/td[1]/label'
    huankuan = 'xpath=>//button[@ng-click="repay()"]'
    tiaoshu = 'xpath=>//select[@ng-change="$$selector.change();"]'
    danju_id = 'xpath=>//tr[@ng-click="tab.clickItem(item,$event)"]/td[2]/a'

    def get_dj_state(self):
        return self.get_texts(self.dj_state)

    def get_xuan_elements(self):
        return self.get_elements(self.xuan)

    def click_huankuan(self):
        self.clicked(self.huankuan)

    def select_200(self):
        self.select_text(self.tiaoshu, "200")

    def get_danju_list(self):
        return self.get_texts(self.danju_id)

    hk_jine = 'xpath=>//tr[@ng-repeat="item in vo.relationList"]/td[9]'
    jine = 'xpath=>//input[@ng-model="item.localAmount"]'
    zhifu_fs = 'xpath=>//select[@ng-model="vo.fmRepaymentInfo.payType"]'

    def edit_huankuan(self):
        self.select_text(self.zhifu_fs, generator.randomStr(1, False, False, False, False, True, ["银行转账", "现金支付"]))
        jine = self.get_text(self.hk_jine)
        self.type(self.jine, jine)
        return jine

    # 未还款金额
    whkje = 'xpath=>//table/tbody/tr/td[10]'

    def get_whkje(self):
        return self.get_texts(self.whkje)

    # 查询
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    clear = '''xpath=>//button[@ng-click="jump('CLEAR')"]'''
    query = '''xpath=>//button[@ng-click="jump('QUERY')"]'''
    query_danju_id = 'xpath=>//input[@ng-model="view.params.recordNo"]'
    query_shiyou = 'xpath=>//input[@ng-model="view.params.mainContent"]'

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def input_danju(self, danju):
        self.type(self.query_danju_id, danju)

    def input_shiyou(self, shiyou):
        self.type(self.query_shiyou, shiyou)

    def click_query(self):
        self.clicked(self.query)

    def click_clear(self):
        self.clicked(self.clear)
        self.clicked(self.query)
        self.clicked(self.zhankai)

    spz_huankuan = 'xpath=>//table/tbody/tr/td[9]'

    def get_spzhk(self):
        return self.get_text(self.spz_huankuan)

    select_state = 'xpath=>//select[@ng-model="view.params.bizStatus"]'

    def select_query_state(self, state):
        self.select_text(self.select_state, state)

    # 导出
    export_btn = '''xpath=>//button[@ng-click="jump('EXPORT')"]'''

    def click_export(self):
        self.clicked(self.export_btn)