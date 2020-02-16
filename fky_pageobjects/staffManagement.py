# 管理员工
from selenium.webdriver.common.by import By

from framework.base_page import BasePage
from framework import generator

class StaffManag(BasePage):
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    guanligg = "xpath=>//div[text()='员工管理']"
    name = "css=>.fs-14 > .color-33.ng-binding"
    input_query = 'xpath=>//input[@ng-model="tab.params.empNameOrPhone"]'
    query_btn = 'xpath=>//button[@ng-click="tab.ajaxQuery()"]'
    name_list = "xpath=>//tr/td[2]/a"

    def get_name(self):
        return self.get_text(self.name)

    def into_staffgl(self):
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        self.clicked(self.guanligg)

    def query_name(self):
        name1 = self.get_name()
        self.type(self.input_query, name1)
        self.clicked(self.query_btn)

    def get_naemlist(self):
        return self.get_texts(self.name_list)

    def clear_query_input(self):
        self.clear(self.input_query)
        self.clicked(self.query_btn)

    add_btn = 'xpath=>//button[@ng-click="tab.addEmployeeInfo()"]'
    queding = 'xpath=>//button[@w5c-form-submit="tab.submit()"]'
    quxiao = 'xpath=>//button[@ng-click="tab.cancel()"]'
    tishi = 'xpath=>//span[@class="w5c-error"]'

    def get_tishi(self):
        return self.get_texts(self.tishi)

    def click_add(self):
        self.clicked(self.add_btn)

    def queding_btn(self):
        self.clicked(self.queding)

    def quxiao_btn(self):
        self.clicked(self.quxiao)

    name_add = 'xpath=>//input[@name="userName"]'
    yinwen = 'xpath=>//input[@name="englishName"]'
    sex_man = 'xpath=>//label[text()="性别: "]/following-sibling::div/div[1]/span/label'
    sex_woman = 'xpath=>//label[text()="性别: "]/following-sibling::div/div[2]/span/label'
    tel_add = 'xpath=>//input[@name="phone"]'
    tel_add2 = 'xpath=>//input[@name="empInfo_landlineNumber"]'
    zhengjian = 'xpath=>//select[@ng-model="tab.user.credentialType"]'
    gonghao = 'xpath=>//input[@ng-model="tab.employee.empNo"]'
    chepai = 'xpath=>//input[@name="emp_licensePlateNum"]'
    pic = "xpath=>//*[@id='employeeLogoPic']"
    pic_btn = "xpath=>/html/body/div[2]/div[2]/button[2]"
    email = 'xpath=>//input[@name="email"]'
    addr = 'xpath=>//input[@ng-model="tab.employee.addrss"]'
    zhengjian_id = 'xpath=>//input[@name="emp_credentialNum"]'
    save_tishi = "xpath=>/html/body/div[2]/div[2]/p"
    save_btn = "xpath=>/html/body/div[2]/div[2]/button[2]"
    save_btn1 = "/html/body/div[2]/div[2]/p"

    def staff_add(self, tel):
        self.type(self.name_add, generator.random_name())
        self.type(self.yinwen, "test"+generator.randomStr(2))
        self.is_selecet(self.sex_woman)
        self.is_selecet(self.sex_man)
        self.type(self.tel_add, tel)
        # self.type(self.tel_add2, generator.random_phone_number())
        self.select_text(self.zhengjian, "身份证")
        # self.type(self.gonghao, generator.randomStr(5))
        # self.type(self.chepai, "京A88888")
        # self.type(self.email, generator.random_email())
        # self.type(self.addr, generator.random_address())
        self.type(self.zhengjian_id, generator.randomStr(18))

    def get_save_tishi(self):
        return self.get_text(self.save_tishi)

    def save_queding(self):
        self.clicked(self.save_btn)

    def query_tel(self, tel):
        self.type(self.input_query, tel)
        self.clicked(self.query_btn)

    tel = "xpath=>//tr[1]/td[3]"

    def get_tel(self):
        return self.get_text(self.tel)

    xuanzhong = "xpath=>//tr[4]/td[1]/label/input"
    xuanzhong_1 = "xpath=>//tr[4]/td[1]/label"

    zhuagntai_xz = "xpath=>//tr[4]/td[8]"
    jinyong_btn = '''xpath=>//button[@ng-click="tab.batchUpdateEmpStatus('0')"]'''
    qiyong_btn = '''xpath=>//button[@ng-click="tab.batchUpdateEmpStatus('1')"]'''
    def state_edit(self):
        if self.get_is_selecet(self.xuanzhong)==0:
            self.clicked(self.xuanzhong_1)
        else:
            pass
        xz = self.get_state()
        if xz == "启用":
            self.clicked(self.jinyong_btn)
            self.clicked(self.save_btn)
            self.sleep(1)
            if "修改成功!" == self.get_text(self.save_btn1):
                self.clicked(self.save_btn)
            else:
                pass
        elif xz == "禁用":
            self.clicked(self.qiyong_btn)
            self.clicked(self.save_btn)
            self.sleep(1)
            if "修改成功!" == self.get_text(self.save_btn1):
                self.clicked(self.save_btn)
            else:
                pass
            # self.clicked(self.save_btn)

    def state_qiyong1(self):
        if self.get_is_selecet(self.xuanzhong) == 0:
            self.clicked(self.xuanzhong_1)
        else:
            pass
        self.clicked(self.qiyong_btn)
        self.clicked(self.save_btn)
        self.clicked(self.save_btn)

    def get_state(self):
        return self.get_text(self.zhuagntai_xz)

    xiugai = 'xpath=>//button[@ng-click="tab.editEmployeeInfo()"]'  # 修改
    dq_name = 'xpath=>//tr[2]/td[2]/a'
    shoukuanyh = 'xpath=>//li[@heading="收款银行"]'
    sk_name = 'xpath=>//input[@ng-model="bankAccountTab.orgBankAccountItem.name"]'
    kaihuyh = 'xpath=>//input[@ng-model="bankAccountTab.orgBankAccountItem.bankName"]'
    yinhangzh = 'xpath=>//input[@ng-model="bankAccountTab.orgBankAccountItem.bankAccount"]'
    is_moren = 'xpath=>//select[@ng-model="bankAccountTab.orgBankAccountItem.isDefault"]'
    yh_save_btn = 'xpath=>//button[@w5c-form-submit="bankAccountTab.submit()"]'
    # yh_quxiao_btn = '''xpath=>//button[@ng-click="closeThisDialog('cancel')"]'''
    yh_quxiao_btn = 'xpath=>//button[@ng-click="bankAccountTab.cancel()"]'
    yh_zhanghus = 'xpath=>//input[@ng-model="item.bankAccount"]'
    yh_zhanghu = 'xpath=>//tr[2]/td/input[@ng-model="item.bankAccount"]'
    yh_del = 'xpath=>//tr[2]/td/button[@ng-click="bankAccountTab.deleteBankAccount(item)"]'
    yh_del_queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def into_xiugaiyh(self):
        if self.get_is_selecet(self.xuanzhong) == 0:
            self.clicked(self.xuanzhong_1)
        else:
            pass
        self.clicked(self.xiugai)
        self.clicked(self.shoukuanyh)

    def click_queding(self):
        self.clicked(self.yh_save_btn)

    def click_quxiao(self):
        self.clicked(self.yh_quxiao_btn)

    def add_yinhangzh(self, zhanghu, moren):
        # self.type(self.sk_name, self.get_text(self.dq_name))
        self.type(self.kaihuyh,  generator.randomStr(1, False, False, False, False, True, ["中国工商银行南昌北京西路支行",
                                                  "中国邮政银行", "中国建设银行", "中国中信银行", "中国招商银行"]))
        self.type(self.yinhangzh, zhanghu)
        self.select_text(self.is_moren, moren)

    def get_yinhang_tishi(self):
        return self.get_text(self.save_tishi)

    def get_zhanghus(self):
        return self.get_input_texts(self.yh_zhanghus)

    def get_zhanghu(self):
        return self.get_input_text(self.yh_zhanghu)

    def del_yinhang(self):
        self.clicked(self.yh_del)
        self.clicked(self.yh_del_queding)

    export = 'xpath=>//button[@ng-click="tab.exportEmployee()"]'

    def export_staff(self):
        self.clicked(self.export)
        self.clicked(self.save_btn)

    # 邀请员工
    yaoqing = 'xpath=>//button[@ng-click="tab.inviteStaff()"]'
    yaoqing_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[1]/div/div'

    def click_yaoqing(self):
        self.clicked(self.yaoqing)

    def get_yaoqing_1(self):
        return self.get_text(self.yaoqing_1)

    yqlj = 'xpath=>//button[@ng-click="tab.inviteLink()"]'
    yqlj_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[1]/div/div'
    fanhui = 'xpath=>//button[@ng-click="goBack()"]'

    def click_yqlj(self):
        self.clicked(self.yqlj)

    def get_yqlj_1(self):
        return self.get_text(self.yqlj_1)

    def click_back(self):
        self.clicked(self.fanhui)

    zgyq = 'xpath=>//button[@ng-click="tab.invite()"]'
    zgyq_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div'

    def click_zgyq(self):
        self.clicked(self.zgyq)

    def get_zgyq_1(self):
        return self.get_text(self.zgyq_1)
