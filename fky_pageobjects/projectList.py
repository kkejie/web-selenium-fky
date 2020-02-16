# 项目主列表
from framework.base_page import BasePage
from framework import generator


class ProjectList(BasePage):

    # 进入首页
    shouye = 'xpath=>//span[text()="首页"]'

    def click_homePage(self):
        self.clicked(self.shouye)

    # 审批项目流程--点击主办
    zhuban = 'xpath=>//tr[1]/td/button[@ng-click="wfMyAgent.host(item.taskId,item.catgId)"]'

    def click_zhuban(self):
        self.clicked(self.zhuban)

    # 审批项目流程--同意
    tongyi="xpath=>//*[@id='btnAgree']"
    tongyi1="xpath=>/html/body/div[2]/div[2]/button[2]"

    def click_tongyi(self):
        self.clicked(self.tongyi)
        self.clicked(self.tongyi1)

    # 审批项目流程--驳回
    bohui="xpath=>//*[@id='btnRejectToStart']"
    bohui1="xpath=>/html/body/div[2]/div[2]/button[2]"

    def click_bohui(self):
        self.clicked(self.bohui)
        self.clicked(self.bohui1)
        self.clicked(self.tongyi1)

    # 审批项目流程--驳回提交
    bohuitj="xpath=>/html/body/div[1]/div[1]/form/div[1]/div/div[2]/button[1]"
    bohuiqueding="xpath=>//*[@id='ngdialog1']/div[2]/div/div[1]/div/button[1]"

    def click_bohuitijiao(self):
        self.clicked(self.bohuitj)
        self.clicked(self.xuanzheSpr)
        self.clicked(self.bohuiqueding)
        self.clicked(self.chenggong)

    # 进入项目主列表
    xiangmuGl = 'xpath=>//span[text()="项目管理"]'
    xiangmuZlb = 'xpath=>//span[text()="项目主列表"]'

    def click_projectList(self):
        self.clicked(self.xiangmuGl)
        self.clicked(self.xiangmuZlb)

    # 新增按钮
    xinzeng = 'xpath=>//button[@ng-click="tab.onClick(4)"]'
    def click_addproject(self):
        self.clicked(self.xinzeng)

    # 新增项目
    xiangmuMc = 'xpath=>//input[@name="projName"]'
    xiangmuJc = 'xpath=>//input[@name="projShortName"]'
    xiangmuSsd = 'xpath=>//span[@ng-click="tab.showAreaSelectDialog=true"]/i'
    xiangmuSsd1 = 'xpath=>//*[@id="100000"]/i'
    xiangmuSsd2 = 'xpath=>//*[@id="210000_anchor"]/i[1]'
    xiangmuSsd3 = 'xpath=>//button[@ng-click="tree.ok()"]'
    xiangmuJl = 'xpath=>//span[@ng-click="tab.showSelectUserDialog=true"]/i'
    xiangmuJl1 = 'xpath=>//label[@ng-click="userSelect.clickItem(employeeItem,$event)"]/i'
    xiangmuJl2 = 'xpath=>//button[@ng-click="userSelect.ok()"]'
    hetongMc = "xpath=>//span[@ng-click='tab.showContractSelectDialog=true']/i"
    hetongMc1 = 'xpath=>//tr[@ng-click="contractInfoSelect.clickItem(item,$event)"][1]/td[1]/label/i'
    # hetongMc1 = 'xpath=>//tr[1][@class="ng-scope"]'
    hetongMc2 = 'xpath=>//button[@ng-click="contractInfoSelect.save()"]'
    hetonghanshuiJe = 'xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[9]/div[2]/div/input'
    kehuMc = 'xpath=>//span[@ng-click="tab.showCustSupSelectDialog=true"]/i '
    kehuMc1 = 'xpath=>//tr[@ng-click="custSupInfoSelect.selectSingleItem(item)"][1]/td[1]/input'
    kehuMc2 = 'xpath=>//button[@ng-click="custSupInfoSelect.save()"]'
    kehuLxr = 'xpath=>//input[@name="linkName"]'
    kehuLxrdh = 'xpath=>//input[@name="contactPhone"]'
    kehuLxryx = 'xpath=>//input[@name="contactEmail"]'
    kehuDz = 'xpath=>//input[@name="contactAddress"]'
    xiangmuHsje = 'xpath=>//input[@name="projectTaxAmount"]'
    xiangmuyujiQssj = 'xpath=>//input[@name="projectStartDate"]'
    xiangmuyujiQssj1 = '''xpath=>//button[@ng-click="select('today', $event)"]'''
    xiangmuyujiJssj = 'xpath=>//input[@name="projectEndDate"]'
    xiangmuyujiJssj1 = '''xpath=>//button[@ng-click="select('today', $event)"]'''
    xiangmuMs = 'xpath=>//textarea[@name="projectRemark"]'
    tijiao = 'xpath=>//button[@w5c-form-submit="tab.verifyProjectInfo()"]'
    baoCun = 'xpath=>//button[@ng-click="tab.saveDraft()"]'
    xuanzheSpr = 'xpath=>//input[@onchange="checkUser(this)"]'
    xuanzheSpr1 = 'xpath=>//button[@ng-click="onSelected()"]'
    chenggong = 'xpath=>//button[@class="confirm"]'

    def add_xinzengXm(self, xmmc):
        self.type(self.xiangmuMc, xmmc)
        self.type(self.xiangmuJc, "项目")
        self.clicked(self.xiangmuSsd)
        self.clicked(self.xiangmuSsd1)
        self.clicked(self.xiangmuSsd2)
        self.clicked(self.xiangmuSsd3)
        self.clicked(self.xiangmuJl)
        self.is_selecet(self.xiangmuJl1)
        self.clicked(self.xiangmuJl2)
        self.clicked(self.hetongMc)
        self.clicked(self.hetongMc1)
        self.clicked(self.hetongMc2)
        self.clicked(self.kehuMc)
        self.clicked(self.kehuMc1)
        self.clicked(self.kehuMc2)
        self.type(self.kehuLxrdh, generator.random_phone_number())
        self.type(self.kehuLxryx, generator.random_email())
        self.type(self.kehuDz, "南昌")
        i = generator.randomStr(2)
        self.type(self.xiangmuHsje, "1"+i)
        self.clicked(self.xiangmuyujiQssj)
        self.clicked(self.xiangmuyujiQssj1)
        self.clicked(self.xiangmuyujiJssj)
        self.clicked(self.xiangmuyujiJssj1)
        self.type(self.xiangmuMs, "lalalaal")
        self.clicked(self.tijiao)

    # 获取项目名称
    hqxmmc = 'xpath=>//tr[@class="ng-scope"][1]/td[4]'
    def gain_xmmc(self):
        return self.get_text(self.hqxmmc)

    # 获取审批状态
    hqspzt = 'xpath=>//tr[@class="ng-scope"][1]/td[8]'
    def gain_spzt(self):
        return self.get_text(self.hqspzt)

    # 获取项目状态
    hqxmzt = 'xpath=>//tr[@class="ng-scope"][1]/td[7]'
    def gain_xmzt(self):
        return self.get_text(self.hqxmzt)

    # 查询项目
    zhankai = 'xpath=>//div[@ng-click="isCollapsed = !isCollapsed"]/a'
    xiangmumccx = 'xpath=>//input[@ng-model="tab.params.projName"]'
    chaxun = 'xpath=>//button[@ng-click="tab.onClick(1)"]'
    clear = 'xpath=>//button[@ng-click="tab.onClick(2)"]'

    def click_chaxun(self, xmmc):
        self.clicked(self.zhankai)
        self.type(self.xiangmumccx, xmmc)
        self.clicked(self.chaxun)

    def click_clear(self):
        self.clicked(self.clear)
        self.clicked(self.chaxun)
        self.clicked(self.zhankai)

    sp_states = 'xpath=>//tr[@class="ng-scope"]/td[8]'
    xm_states = 'xpath=>//tr[@class="ng-scope"]/td[7]'
    jinyongs = 'xpath=>//tr/td/button[@title="禁用"]'
    hqxmmcs = 'xpath=>//tr[@class="ng-scope"]/td[4]'
    tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'
    qiyongs = 'xpath=>//tr/td/button[@title="启用"]'
    xiugais = 'xpath=>//tr/td/button[@title="修改"]'

    def get_sp_states(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.sp_states)

    def get_xm_states(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.xm_states)

    def get_jinyongs_elements(self):
        return self.get_elements(self.jinyongs)

    def get_hqxmmcs(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.hqxmmcs)

    def get_qiyongs_elements(self):
        return self.get_elements(self.qiyongs)

    def get_xiugai_elements(self):
        return self.get_elements(self.xiugais)

    # 禁用
    jinyong = 'xpath=>//tr[1]/td/button[@title="禁用"]'
    jinyong1 = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_jingyong(self):
        self.clicked(self.jinyong)
        self.clicked(self.jinyong1)

    # 启用
    qiyong='xpath=>//tr[1]/td/button[@title="启用"]'

    def click_qiyong(self):
        self.clicked(self.qiyong)
        self.clicked(self.jinyong1)

    # 修改
    # xiugai='xpath=>//tr[1]/td/button[@title="修改"]'
    # xiugai='css=>tr:nth-child(1) > td.ng-scope > button:nth-child(1)'

    def amend_projectList(self, xmmc1):
        # self.clicked(self.xiugai)
        self.add_xinzengXm(xmmc1)

    # 导入
    into = 'xpath=>//button[@ng-click="tab.showImportExcelDialog=true"]'
    into_title = 'xpath=>//h3[@class="modal-title ng-binding"]'
    close = 'xpath=>//button[@ng-click="import.close()"]'

    def click_input(self):
        self.clicked(self.into)

    def get_into_title(self):
        return self.get_text(self.into_title)

    def click_close(self):
        self.clicked(self.close)

    # 导出
    export = 'xpath=>//button[@ng-click="tab.onClick(3)"]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_export(self):
        self.clicked(self.export)

    def click_queding(self):
        self.clicked(self.queding)









