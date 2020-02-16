# 我审批的流程
# coding=utf-8

from framework.base_page import BasePage

class MyApprove(BasePage):
    # 选择审批人
    xuanzhespr = 'xpath=>//input[@onchange="checkUser(this)"]'
    xuanzhespr_queding = 'xpath=>//button[@ng-click="onSelected()"]'


    def xuanze_spr(self):
        self.clicked(self.xuanzhespr)
        self.clicked(self.xuanzhespr_queding)

    # 进入首页
    homepage = 'xpath=>//span[text()="首页"]'

    def click_homepage(self):
        self.clicked(self.homepage)

    # 审批项目流程--点击主办
    zhuban = 'xpath=>//tr[1]/td/button[@ng-click="wfMyAgent.host(item.taskId,item.catgId)"]'

    def click_zhuban(self):
        self.clicked(self.zhuban)

    # 审批项目流程--同意
    tongyi = "xpath=>//*[@id='btnAgree']"
    queding = "xpath=>/html/body/div[2]/div[2]/button[2]"

    def click_tongyi(self):
        self.clicked(self.tongyi)
        self.clicked(self.queding)

    # 审批项目流程--驳回
    bohui = "xpath=>//*[@id='btnRejectToStart']"

    def click_bohui(self):
        self.clicked(self.bohui)
        self.clicked(self.queding)
        self.sleep(1)
        self.clicked(self.queding)

    # 反对
    fandui = "xpath=>//*[@id='btnNotAgreeAndEnd']"

    def click_fandui(self):
        self.clicked(self.fandui)
        self.clicked(self.queding)
        self.clicked(self.queding)

    # 审批项目流程--驳回提交
    bohuitj = 'xpath=>//button[text()=" 提交" or text()="提交" or @w5c-form-submit="tab.submit(20)"]'

    def click_bohuitijiao(self, a):
        """
        驳回后得流程再次提交
        :param a:
            a == 1:点完提交需要再点击确定按钮
            a == 0:点完提交后不需要再点击确定按钮
        :return:
        """
        self.clicked(self.bohuitj)
        if a:
            self.clicked(self.queding)
        self.clicked(self.xuanzhespr)
        self.clicked(self.xuanzhespr_queding)
        self.clicked(self.queding)

    # 驳回
    def execute_bohui(self):
        self.click_homepage()
        self.click_zhuban()
        self.switch_to_window()
        self.sleep(2)
        self.click_bohui()
        self.sleep(2)
        self.switch_to_handle()

    # 驳回提交--同意
    def execute_tijiao_tongyi(self, a):
        self.click_homepage()
        self.click_zhuban()
        self.sleep(2)
        self.switch_to_window()
        self.click_bohuitijiao(a)
        self.sleep(2)
        self.switch_to_handle()
        self.click_zhuban()
        self.sleep(2)
        self.switch_to_window()
        self.click_tongyi()
        self.sleep(2)
        self.switch_to_handle()

    # 审批---同意
    def execute_tongyi(self):
        self.click_homepage()
        self.click_zhuban()
        self.sleep(2)
        self.switch_to_window()
        self.click_tongyi()
        self.sleep(2)
        self.switch_to_handle()



    def execute_tongyi_yszlb(self):
        self.click_homepage()
        self.click_zhuban()
        self.switch_to_window()
        self.click_tongyi()
        self.switch_to_handle()

    # 预算主列表
    bohuitj_yszlb = "xpath=>/html/body/div[1]/div[1]/div/div[1]/div/div/button[1]"


    def click_bohuitijiao_yszlb(self):
        self.clicked(self.bohuitj_yszlb)
        self.clicked(self.xuanzhespr)
        self.clicked(self.xuanzhespr_queding)
        self.clicked(self.queding)

    # 反对
    def execute_fandui(self):
        self.click_homepage()
        self.click_zhuban()
        self.switch_to_window()
        self.click_fandui()
        self.switch_to_handle()
        # self.switch_to_window()

    def execute_tijiao_tongyi_yszlb(self):
        self.click_homepage()
        self.click_zhuban()
        self.switch_to_window()
        self.click_bohuitijiao_yszlb()
        self.switch_to_handle()
        # self.switch_to_window()
        self.click_zhuban()
        self.switch_to_window()
        self.click_tongyi()
        self.switch_to_handle()
        # self.switch_to_window()

    # 费用申请
    bhtj_fysq = 'xpath=>/html/body/div[1]/div[1]/div/div[1]/div[2]/button[1]'

    def click_bohuitijiao_fysq(self, a):
        self.clicked(self.bhtj_fysq)
        if a:
            self.clicked(self.queding)
        self.clicked(self.xuanzhespr)
        self.clicked(self.xuanzhespr_queding)
        self.clicked(self.queding)

    # bhtj_fysq = 'xpath=>/html/body/div[1]/div[1]/div/div[1]/div[2]/button[1]'

    def execute_tijiao_tongyi_fysq(self, a):
        self.click_homepage()
        self.click_zhuban()
        self.switch_to_window()
        self.click_bohuitijiao_fysq(a)
        self.switch_to_handle()
        # self.switch_to_window()
        self.sleep(1)
        self.click_zhuban()
        self.switch_to_window()
        self.click_tongyi()
        self.switch_to_handle()
        # self.switch_to_window()
