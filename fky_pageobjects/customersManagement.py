# coding=utf-8

from framework.base_page import BasePage
from framework import generator

# 客商管理


class CustomersManagement(BasePage):
    # 进入客商管理
    shouye = 'xpath=>//span[text()="首页"]'
    keshangguanli = 'xpath=>//span[text()="客商管理"]'

    def click_customersManagement(self):
        self.clicked(self.shouye)
        self.clicked(self.keshangguanli)

    # 点击新增客商按钮
    xinzhenng = 'xpath=>//button[text()="新增"]'

    def click_xinzengKS(self):
        self.clicked(self.xinzhenng)

    # 新增客商
    keshangfenlei = 'xpath=>//select[@name="type"]'
    keshangmincheng = 'xpath=>//input[@name="name"]'
    danweixinzhi = 'xpath=>//select[@name="status"]'
    suoshudiyu = 'xpath=>//span[@ng-click="tab.showAreaSelectDialog=true"]/i'
    suoshudiyu1 = "xpath=>//*[@id='100000']/i"
    suoshudiyu2 = "xpath=>//*[@id='220000_anchor']/i[1]"
    suoshudiyu3 = 'xpath=>//button[@ng-click="tree.ok()"]'
    xiangxidizi = 'xpath=>//input[@name="address"]'
    tongyidaima = 'xpath=>//input[@name="creditCode"]'
    tongyidaimariqi = 'xpath=>//input[@ng-model="tab.params.creditEndtime"]'
    tongyidaimariqi1 = '''xpath=>//button[@ng-disabled="isDisabled('today')"]'''
    fujian = 'xpath=>//button[@ng-click="addUpload()"]'
    fujian1 = 'xpath=>//select[@ng-model="item.typeInstId"]'
    fujian2 = 'xpath=>//span[@ng-click="uploadFile(item)"]'
    xinzenghang = 'xpath=>//button[@ng-click="addContact()"]'
    xuanzhehang = 'xpath=>//tr/th/label/i'
    delhang = 'xpath=>//button[@ng-click="removeContact()"]'
    lianxixinngming = 'xpath=>//input[@ng-model="contact.contactName"]'
    lianxidianhua = 'xpath=>//input[@ng-model="contact.phone"]'
    lianxirenyx = 'xpath=>//input[@ng-model="contact.contactCode"]'
    baocun = 'xpath=>//button[@w5c-form-submit="tab.save()"]'
    queding = "xpath=>/html/body/div[2]/div[2]/button[2]"

    def add_customers(self, ksmc):
        self.select_text(
            self.keshangfenlei, generator.randomStr(
                1, False, False, False, False, True, [
                    "客商", "客户", "供应商", "拓展", "合作伙伴"]))
        self.type(self.keshangmincheng, ksmc)
        self.select_text(
            self.danweixinzhi, generator.randomStr(
                1, False, False, False, False, True, [
                    "国企", "民企", "合资企业", "军队", "外国企业", "外企（境内注册）", "盈利性事业单位", "非盈利性事业单位", "政府机关", "个人"]))
        self.clicked(self.suoshudiyu)
        self.clicked(self.suoshudiyu1)
        self.clicked(self.suoshudiyu2)
        self.clicked(self.suoshudiyu3)
        self.type(self.xiangxidizi, generator.random_address())
        self.type(self.tongyidaima, "91310000775785552L")
        self.clicked(self.tongyidaimariqi)
        self.clicked(self.tongyidaimariqi1)
        # 添加附件
        # self.clicked(self.fujian)
        # self.select_text(self.fujian1,"统一社会信用代码附件")
        # self.type(self.fujian2,"E:\\1.jpg")
        self.clicked(self.xinzenghang)
        self.clicked(self.xuanzhehang)
        self.clicked(self.delhang)
        self.clicked(self.xinzenghang)
        self.type(self.lianxixinngming, generator.random_name())
        self.type(self.lianxidianhua, generator.random_phone_number())
        self.type(self.lianxirenyx, generator.random_email())
        self.clicked(self.baocun)
        self.clicked(self.queding)

    def click_save(self):
        self.clicked(self.baocun)

    # 必填提示
    tishi = 'xpath=>//span[@class="w5c-error"]'

    def get_tishis(self):
        return self.get_texts(self.tishi)

    # 获取客商名称
    hqksmc = "xpath=>//table/tbody/tr/td[3]"
    tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'

    def select_200(self):
        self.select_text(self.tiaoshu, "200")

    def get_ksmcs(self):
        # self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.hqksmc)

    # 获取客商分类
    ksfenlei = 'xpath=>//table/tbody/tr/td[4]'

    def get_ksfenleis(self):
        # self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.ksfenlei)

    # 获取客商编码
    ksbianma = "xpath=>//table/tbody/tr/td[2]"

    def get_ksbianmas(self):
        # self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.ksbianma)

    # 查询
    chaxun = 'xpath=>//button[text()="查询"]'
    zhankaicx = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    keshangminchengcx = 'xpath=>//input[@ng-model="tab.params.name"]'
    keshangfenleicx = 'xpath=>//select[@ng-model="tab.params.type"]'
    keshangbianma = 'xpath=>//input[@ng-model="tab.params.code"]'

    # 客商名称
    def click_chaxunmc(self, ksmc):
        self.clicked(self.zhankaicx)
        self.type(self.keshangminchengcx, ksmc)
        self.clicked(self.chaxun)

    # 客商分类
    def click_chaxunfl(self, ksfl):
        self.clicked(self.zhankaicx)
        self.select_text(self.keshangfenleicx, ksfl)
        self.clicked(self.chaxun)

    # 客商编码
    def click_chaxunbm(self, ksbm):
        self.clicked(self.zhankaicx)
        self.type(self.keshangbianma, ksbm)
        self.clicked(self.chaxun)

    # 清空
    qingkong = 'xpath=>//button[text()="清空"]'

    def click_qingkong(self):
        self.clicked(self.qingkong)
        self.clicked(self.chaxun)
        self.clicked(self.zhankaicx)

    # 获取客商状态
    kszhuangtai = 'xpath=>//table/tbody/tr/td[7]'

    def get_kszhuangtais(self):
        # self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.kszhuangtai)

    # 禁用
    jinyongs = 'xpath=>//button[@title="禁用"]'

    def get_jinyongs_elements(self):
        return self.get_elements(self.jinyongs)

    # 启用
    qiyongs = 'xpath=>//button[@title="启用"]'

    def get_qiyongs_elements(self):
        return self.get_elements(self.qiyongs)

    def click_queding(self):
        self.clicked(self.queding)

    # 修改
    xiugais = 'xpath=>//button[@title="修改"]'

    def get_xiugai_elements(self):
        return self.get_elements(self.xiugais)


    # 导入
    into = 'xpath=>//button[@ng-click="tab.showImportExcelDialog=true"]'
    into_title = 'css=>.modal-title.ng-binding'
    close = 'xpath=>//button[@ng-click="import.close()"]'

    def click_input(self):
        self.clicked(self.into)

    def get_into_title(self):
        return self.get_text(self.into_title)

    def click_close(self):
        self.clicked(self.close)

    # 导出
    export = 'xpath=>//button[text()="导出"]'

    def click_export(self):
        self.clicked(self.export)

    def click_queding(self):
        self.clicked(self.queding)
