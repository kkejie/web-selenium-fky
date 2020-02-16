# 切换公司
from framework.base_page import BasePage
from framework import generator

class SwitchCompany(BasePage):
    homepage = 'xpath=>//span[text()="首页"]'
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    company_name = "css=>.header-qh.ml30>span"
    qiehuan_company = "xpath=>//span[text()='切换公司']"
    name_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[3]/div[4]/div/div[1]'
    logo_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[3]/div[4]/img'
    name_2 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[3]/div[5]/div/div[1]'
    logo_2 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[3]/div[5]/img'
    queding = "xpath=>/html/body/div[2]/div[2]/button[2]"

    def get_company_name(self):
        return self.get_text(self.company_name)

    def switch_company(self):
        self.clicked(self.qiehuan_company)
        xz = self.get_company_name()
        if xz == "江西省通信产业服务有限公司宇创网络科技开发分公司":
            self.double_clicked(self.logo_2)
        elif xz == "雪中悍刀行":
            self.double_clicked(self.logo_1)
        self.clicked(self.queding)

    chuangjian_company = "xpath=>//span[text()='创建公司']"
    message_1 = "xpath=>//label[text()='公司简称']/following-sibling::div/input"       # 公司简称
    message_2 = "xpath=>//label[text()='公司名称']/following-sibling::div/input"       # 公司名称
    message_3 = "xpath=>//label[text()='所在城市']/following-sibling::div/div[1]/select"       # 所在国家
    message_4 = "xpath=>//label[text()='所在城市']/following-sibling::div/div[2]/select"       # 省
    message_5 = "xpath=>//label[text()='所在城市']/following-sibling::div/div[3]/select"       # 市
    message_6 = "xpath=>//label[text()='详细地址']/following-sibling::div/input"       # 详细地址
    message_7 = "xpath=>//label[text()='公司类型']/following-sibling::div/select"      # 公司类型
    message_8 = "xpath=>//label[text()='邮政编码']/following-sibling::div/input"      # 邮政编码
    message_9 = "xpath=>//label[text()='默认语言']/following-sibling::div/select"     # 默认语言
    message_10 = "xpath=>//label[text()='联系人']/following-sibling::div/input"     # 联系人
    message_11 = "xpath=>//label[text()='联系邮箱']/following-sibling::div/input"     # 联系邮箱
    message_12 = "xpath=>//label[text()='法人姓名']/following-sibling::div/input"     # 法人姓名
    message_13 = "xpath=>//label[text()='统一信用代码证']/following-sibling::div/input"     # 统一信用代码证
    message_14 = "xpath=>//label[text()='其他证件号码']/following-sibling::div/input"     # 其他证件号码
    message_15 = "xpath=>//label[text()='公司行业']/following-sibling::div/select"     # 公司行业
    message_15_1 = "xpath=>//label[text()='公司行业']/following-sibling::div/select/option"     # 公司行业
    message_16 = "xpath=>//label[text()='员工人数']/following-sibling::div/input"      # 员工人数
    message_17 = "xpath=>//label[text()='默认币种']/following-sibling::div/select"     # 默认币种
    message_18 = "xpath=>//label[text()='联系电话']/following-sibling::div/input"      # 联系电话
    message_19 = "xpath=>//label[text()='纳税人类型']/following-sibling::div/select"    # 纳税人类型
    message_20 = "xpath=>//label[text()='法人身份证号']/following-sibling::div/input"     # 法人身份证号
    cj_queding = "'#app-content > div.app-content-body > div > div > div.ng-scope > form > div:nth-child(3) > div > button.btn.m-b-xs.w-xs.btn-default.btn-success'"
    # cj_queding = "xpath=>(//form[@name='companyForm']/div[2]/div/button[2])[0]"

    tishi = "xpath=>//*[@id='app-content']/div[2]/div/div/div[4]/form/div[1]/div[1]/div[1]/div/span"
    # tishi = 'xpath=>//span[@class="w5c-error"]'

    xieyi = 'xpath=>//input[@type="checkbox"]'

    def select_xieyi(self):
        self.is_selecet(self.xieyi)

    def save_btn(self):
        self.is_selecet(self.xieyi)
        self.execute_script_click(self.cj_queding)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def into_gongsigg(self):
        self.clicked(self.homepage)
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)

    def create_com(self):
        self.clicked(self.chuangjian_company)

    def create_com_bitian(self, name1, name2):
        self.type(self.message_1, name1)
        self.type(self.message_2, name2)
        self.select_text(self.message_3, "中国")
        self.select_text(self.message_4, "江西省")
        self.select_text(self.message_5, "南昌市")
        self.type(self.message_6, generator.random_address())
        self.select_text(self.message_7, "个体户")
        self.type(self.message_8, generator.randomStr(6))
        self.select_text(self.message_9, "简体中文")
        self.type(self.message_10, generator.random_name())
        self.type(self.message_11, generator.random_email())
        self.type(self.message_12, generator.random_name())
        self.type(self.message_13, generator.randomStr(18))
        self.type(self.message_14, generator.randomStr(18))
        # self.select_index(self.message_15, self.message_15_1)
        self.select_text(self.message_15, generator.randomStr(1, False, False, False, False, True,
                                                              ['农、林、牧、渔业\n                                ',
                                                               '采矿业\n                                ',
                                                               '制造业\n                                ',
                                                               '电力、热力、燃气及水生产和供应业\n                                ',
                                                               '建筑业\n                                ',
                                                               '批发和零售业\n                                ']))
        self.type(self.message_16, generator.randomStr(2))
        self.select_text(self.message_17, "CNY-中国人民币")
        self.type(self.message_18, generator.random_phone_number())
        self.select_text(self.message_19, "一般纳税人")
        self.type(self.message_20, generator.randomStr(18))

    save_queding = "xpath=>/html/body/div[2]/div[2]/button[2]"
    save_tishi = "xpath=>/html/body/div[2]/div[2]/p"

    def save_baocun(self):
        self.clicked(self.save_queding)

    def get_save_tishi(self):
        return self.get_text(self.save_tishi)

    # 公司列表
    company_list = "xpath=>//span[text()='公司列表']"
    zhankai = "xpath=>//*[@id='app-content']/div[2]/div/div/div[3]/div[2]/a"
    input_name = "xpath=>//*[@id='app-content']/div[2]/div/div/div[3]/div[3]/form/div[1]/div[2]/div/input"
    comp_name = "xpath=>//*[@id='app-content']/div[2]/div/div/div[4]/div/table/tbody/tr/td[1]/a"
    query = "xpath=>//*[@id='app-content']/div[2]/div/div/div[1]/div/button[4]"

    def query_company(self):
        self.clicked(self.company_list)
        name = self.get_text(self.company_name)
        self.clicked(self.zhankai)
        self.type(self.input_name, name)
        self.clicked(self.query)

    def get_name(self):
        return self.get_text(self.comp_name)

    export_comp = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[1]/div/button[2]'

    def click_export(self):
        self.clicked(self.company_list)
        self.clicked(self.export_comp)

    company_info = 'xpath=>//div[text()="公司信息"]'

    def into_company_info(self):
        self.clicked(self.homepage)
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        self.clicked(self.company_info)

    def get_compid(self):
        return self.get_input_text(self.message_1)