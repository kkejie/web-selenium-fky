# 公司信息
# coding=utf-8

from framework.base_page import BasePage
from framework import generator

class CompInfo(BasePage):
    company_name1 = 'css=>.dropdown > .header-qh.ml30>span'
    def get_company_name1(self):
        return self.get_text(self.company_name1)

    # 开票信息
    # bill_info = '''xpath=>ng-class="{'info-active':item.id==tab.infoTabItem.id}"'''
    bill_info = '''xpath=>//div[@ng-class="{'info-active':item.id==tab.infoTabItem.id}"][2]'''
    company_name = 'xpath=>//input[@ng-model="tab.bill.orgName"]'
    units_addr = 'xpath=>//input[@ng-model="tab.bill.address"]'
    tel = 'xpath=>//input[@ng-model="tab.bill.mobile"]'
    kaihuyh = 'xpath=>//input[@ng-model="tab.bill.bankName"]'
    yinhangid = 'xpath=>//input[@ng-model="tab.bill.bankAccount"]'
    queding1 = 'css=>button.btn.m-b-xs.w-xs.btn-default.btn-success'
    queding2 = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_bill_info(self):
        self.clicked(self.bill_info)

    def get_company_name(self):
        return self.get_input_text(self.company_name)

    # 输入开票信息
    def modification_bill(self, addr):
        self.type(self.units_addr, addr)
        self.type(self.tel, generator.random_phone_number())
        self.type(self.kaihuyh, generator.randomStr(1, False, False, False, False, True, ["中国工商银行南昌北京西路支行",
                                                  "中国邮政银行", "中国建设银行", "中国中信银行", "中国招商银行"]))
        self.type(self.yinhangid, generator.randomStr(22))

    def queding_btn(self):
        # self.execute_script_click(self.queding1)
        self.clicked(self.queding1)

    def queding_btn2(self):
        self.clicked(self.queding2)

    def get_addr(self):
        return self.get_input_text(self.units_addr)

    # 银行账户
    bank_zhanghu = '''xpath=>//div[@ng-class="{'info-active':item.id==tab.infoTabItem.id}"][3]'''
    kaihu_name = 'xpath=>//input[@ng-model="tab.account.name"]'
    kaihu_bank = 'xpath=>//input[@ng-model="tab.account.bankName"]'
    bankid = 'xpath=>//input[@ng-model="tab.account.bankAccount"]'
    moren_currency = 'xpath=>//select[@ng-model="tab.account.accountCurrency"]'
    zhanghu_type = 'xpath=>//select[@ng-model="tab.account.accountType"]'
    is_moren = '''xpath=>//input[@ng-checked="tab.account.isDefault == '1'"]/parent::label'''
    not_moren = 'xpath=>//form/div[1]/div[6]/div/div[2]/span/label'
    is_qidong = '''xpath=>//input[@checked="tab.account.startStatus == '1'"]/parent::label'''
    not_qiyong = '''xpath=>//input[@checked="tab.account.startStatus == '2'"]/parent::label'''
    save_btn = 'xpath=>//button[@w5c-form-submit="tab.saveBankAccount()"]'
    bank_id = 'xpath=>//table/tbody/tr[1]/td[3]'
    bank_list = 'xpath=>//table/tbody/tr/td[3]'
    # tishi = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[4]/form/div[1]/div[2]/div/span'
    tishi = 'xpath=>//span[@class="w5c-error"]'
    save_tishi = 'xpath=>/html/body/div[2]/div[2]/p'

    def click_bank_zhanghu(self):
        self.clicked(self.bank_zhanghu)

    def get_company_name3(self):
        return self.get_input_text(self.kaihu_name)

    def click_save(self):
        self.clicked(self.save_btn)

    def get_tishis(self):
        return self.get_texts(self.tishi)

    def get_save_tishi(self):
        return self.get_text(self.save_tishi)

    def get_bankid(self):
        return self.get_text(self.bank_id)

    def get_bankid_list(self):
        return self.get_texts(self.bank_list)

    # 输入银行账户
    def create_bank(self, bankid, type):
        self.type(self.kaihu_bank, generator.randomStr(1, False, False, False, False, True, ["中国工商银行", "九江银行",
                                                  "中国邮政银行", "中国建设银行", "中国中信银行", "中国招商银行"]))
        self.type(self.bankid, bankid)
        self.select_text(self.moren_currency, "CNY-中国人民币")
        self.select_text(self.zhanghu_type, type)

    def select_is(self):
        self.clicked(self.is_moren)

    def select_not(self):
        self.clicked(self.not_moren)

    def select_qiyong(self):
        self.clicked(self.is_qidong)

    def select_jinyong(self):
        self.clicked(self.not_qiyong)

    def select_zhanghutype(self, type):
        self.select_text(self.zhanghu_type, type)

    xiugai_btn = 'xpath=>//table/tbody/tr[2]/td[8]/button[1]'
    del_btn = 'xpath=>//table/tbody/tr[2]/td[8]/button[2]'
    bank_id2 = 'xpath=>//table/tbody/tr[2]/td[3]'   # 修改后的账户

    def click_xiugai(self):
        self.clicked(self.xiugai_btn)

    def click_del(self):
        self.clicked(self.del_btn)

    def get_bank_id2(self):
        return self.get_text(self.bank_id2)


