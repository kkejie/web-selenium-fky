# 公告
# coding=utf-8
import random

from framework.base_page import BasePage

class Announcement(BasePage):

    homepage = 'xpath=>//span[text()="首页"]'
    xietongbg = 'xpath=>//span[text()="协同办公"]'
    gonggao = 'xpath=>//span[text()="公告"]'

    # 进入公告页面
    def into_gonggao(self):
        self.clicked(self.xietongbg)
        self.clicked(self.gonggao)

    add_btn = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div/div[1]/div/button"

    # 点击新增按钮
    def add_btnn(self):
        self.clicked(self.add_btn)

    fabufanwei = 'xpath=>//span[@class="search position-absolute"]'
    fbfw_1 = 'css=>div.modal-body.pre-scrollable > div > div > div > div > div.tree-folder-header.ng-scope > i'
    fbfw_2 = 'xpath=>//div[@class="tree-folder-name ng-binding"]'
    fbfw_queding = 'xpath=>//button[@ng-click="tree.ok()"]'
    notice_title = 'xpath=>//input[@name="noticeTitle"]'
    guoqi_time = 'xpath=>//input[@ng-model="tab.coPublicNotice.deadlineDate"]'
    guoqi_time_1 = '''xpath=>//button[@ng-disabled="isDisabled('today')"]'''
    # guoqi_time_2 = "xpath=>/html/body/div[3]/ul/li[1]/div/div/div/table/tbody/tr[2]/td[4]/button/span"
    frame1 = '//iframe[@name="editIFrame"]'
    frame2 = '//iframe[@class="ke-edit-iframe"]'
    notice_content = 'xpath=>//body[@class="ke-content"]'
    # fujian_add = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div/form/div[6]/div/file-upload/div/table/tbody/tr/td/button"
    # notice_fujian = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div/form/div[6]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[1]/select"
    # select_fujian = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div/form/div[6]/div/file-upload/div/table/tbody/tr[1]/td/form/div/div/div[2]/div/span/a"


    # 新增公告
    def add_gonggao(self, title1, content):
        self.clicked(self.fabufanwei)
        self.clicked(self.fbfw_1)
        n = random.randint(1, len(self.get_texts(self.fbfw_2))) - 1
        print(n)
        if self.get_texts(self.fbfw_2)[n] == '':
            n = random.randint(1, len(self.get_texts(self.fbfw_2))) - 1
        self.get_elements(self.fbfw_2)[n].click()
        self.clicked(self.fbfw_queding)

        self.type(self.notice_title, title1)
        self.clicked(self.guoqi_time)
        self.clicked(self.guoqi_time_1)
        # self.clicked(self.guoqi_time_2)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame1))
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.frame2))
        self.type(self.notice_content, content)
        self.driver.switch_to.default_content()

    issue = 'xpath=>//button[@ng-click="tab.submit(20)"]'
    issue_1 = "xpath=>/html/body/div[2]/div[2]/button[2]"
    issue_2 = "xpath=>/html/body/div[2]/div[2]/button[2]"

    # 发布操作
    def issue_gonggao(self):
        self.clicked(self.issue)
        self.clicked(self.issue_1)
        self.clicked(self.issue_2)

    notice_title_1 = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div/div[2]/div[1]/div/ul/li[1]"
    # 获取公告标题
    def get_notice_title(self):
        return self.get_text(self.notice_title_1)

    save_notice = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div/div/div[2]/button[2]"
    caogao = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[3]/div[1]"

    # 保存公告
    def save_gonggao(self):
        self.clicked(self.save_notice)
        self.clicked(self.issue_1)
        self.clicked(self.issue_2)
        self.clicked(self.caogao)

    # 修改公告
    def change_gonggao(self):
        self.clicked(self.caogao)
        self.clicked(self.notice_title_1)

    query = "xpath=>/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div/div[1]/div/div/input"
    # 查询框输入公告标题
    def input_query(self, title1):
        self.type(self.query, title1)