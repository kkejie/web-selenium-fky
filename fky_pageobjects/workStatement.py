# 工作报告
from framework.base_page import BasePage

class WorkStatement(BasePage):
    homepage = 'xpath=>//span[text()="首页"]'
    xietongbg = 'xpath=>//span[text()="协同办公"]'
    zhoubao = 'xpath=>//span[text()="工作报告"]'

    def into_baogao(self):
        self.clicked(self.xietongbg)
        self.clicked(self.zhoubao)

    report_add = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div/div[1]/div/button[1]"
    def add_btn(self):
        self.clicked(self.report_add)

    report_day = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[2]/div/div[1]/div[1]/i"
    day_time = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[2]/div/div[4]/div/input"
    day_time_1 = "xpath=>/html/body/div[3]/ul/li[2]/span/button[1]"
    summarize_day = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[4]/div/textarea"
    plan_tomorrow = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[6]/div/textarea"
    fujian_add1 = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[8]/div/file-upload/div/table/tbody/tr/td/button"
    select_reportfj = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[8]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[1]/select"
    select_reportfj_1 = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[8]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[2]/div/span/a"
    approver = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[10]/div/div/div[1]/i"
    approver_1 = "xpath=>/html/body/div[7]/div[2]/div/div[3]/div[1]/div[2]/div/label/i"
    approver_2 = "xpath=>/html/body/div[7]/div[2]/div/div[4]/div/button"


    def add_weekly(self, summarize, plan):
        self.clicked(self.report_day)
        self.clicked(self.day_time)
        self.clicked(self.day_time_1)
        self.type(self.summarize_day, summarize)
        self.type(self.plan_tomorrow, plan)
        self.clicked(self.approver)
        self.is_selecet(self.approver_1)
        self.clicked(self.approver_2)

    copyto = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/form/div[12]/div/div/div[1]/i"
    submit_btn = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div/div[2]/button[1]"
    queding = "xpath=>/html/body/div[2]/div[2]/button[2]"

    def submit(self):
        self.clicked(self.submit_btn)

    def click_queding(self):
        self.clicked(self.queding)

    summarize = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div/div[2]/div[1]/div/ul/li[3]"
    def get_summarize(self):
        return self.get_text(self.summarize)

    def click_summarize(self):
        self.clicked(self.summarize)

    save_btn = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div/div[2]/button[2]"
    def save_report(self):
        self.clicked(self.save_btn)
        self.clicked(self.queding)

    draft = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[4]/div[1]"
    def into_draft(self):
        self.clicked(self.draft)

    tishi = "xpath=>/html/body/div[2]/div[2]/p"

    def get_tishi(self):
        return self.get_text(self.tishi)

    # 取消
    quxiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div/div[2]/button[3]'

    def click_quxiao(self):
        self.clicked(self.quxiao)

    # 导出
    wotijiaode = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[1]/div[1]/div[1]'
    export = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[4]/div/div[1]/div/button[2]'

    def click_wotijiaode(self):
        self.clicked(self.wotijiaode)

    def click_export(self):
        self.clicked(self.export)