# 单据页面字段设置
# coding=utf-8
from framework.base_page import BasePage

class PageField(BasePage):
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    danju_ziduan = 'xpath=>//div[text()="单据页面字段设置"]'

    def into_danju_ziduan(self):
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        self.clicked(self.danju_ziduan)

    danju_type = 'xpath=>//li[@role="treeitem"]/ul/li/a'

    def get_zhichuxj(self):
        return self.get_elements(self.danju_type)

    ziduan_name = 'css=>.ng-scope.true>.ng-binding'

    def get_ziduan_count(self):
        return len(self.get_texts(self.ziduan_name))
