# coding=utf-8

from framework.base_page import BasePage

# 首页
class HomePage(BasePage):
    # 公告
    homepage = 'xpath=>//span[text()="首页"]'
    notice_more = 'xpath=>//span[@ng-click="message.publicNoticeMore()"]'
    gonggao_title = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[4]/div/div[1]/div/button'

    def click_into_gonggao(self):
        self.clicked(self.homepage)
        self.clicked(self.notice_more)

    def get_gonggao(self):
        return self.get_text(self.gonggao_title)

    # 报告
    bao_more = 'xpath=>//span[@ng-click="message.coWorkReportMore()"]'
    baogao_title = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[4]/div/div[1]/div/button[1]'

    def click_into_baogao(self):
        self.clicked(self.homepage)
        self.clicked(self.bao_more)

    def get_baogao(self):
        return self.get_text(self.baogao_title)