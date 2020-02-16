# 部门预算功能配置
# coding=utf-8
import random
from framework import generator
from framework.base_page import BasePage

class FunctionalAllocation(BasePage):
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    bumenys = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[2]'

    def into_funcall(self):
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        self.clicked(self.bumenys)

    add_bumenys = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[1]/div/button[1]'
    tishi = 'xpath=>/html/body/div[2]/div[2]/p'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'
    add_tijiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[1]/div/div/button[1]'
    add_hang = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/button[1]'

    def click_add_bumenys(self):
        self.clicked(self.add_bumenys)

    def click_add_tijiao(self):
        self.clicked(self.add_tijiao)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def click_queding(self):
        self.clicked(self.queding)

    def click_add_hang(self):
        self.clicked(self.add_hang)

    bumen_name = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[2]/span/a' # 部门名称
    bumen_1 = 'xpath=>/html/body/div[5]/div[2]/div[3]/div/div/div/div/div[1]/i'         # "+"
    bumen_2 = 'xpath=>/html/body/div[5]/div[2]/div[3]/div/div/div/div/div[2]/div/div/span/div'        # 部门
    bumen_3 = 'xpath=>/html/body/div[5]/div[2]/div[1]/div[2]/button[1]'             # 确认
    feiyong_type = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[3]/span/a'   # 费用类型
    feiyong_1 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[2]/div/div/div[2]'     # 类型
    ys_bumen_name = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[4]/span/a'      # 预算部门名称
    ys_zhibiao_name = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[5]/span/a'    # 预算指标名称
    qy_time_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[6]/div/div/i'       # 开始日期
    qy_time_2 = 'xpath=>/html/body/div[3]/ul/li[2]/span/button[1]'      # 今天
    js_time_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[7]/div/div/i'       # 结束日期
    js_time_2 = 'xpath=>/html/body/div[4]/ul/li[1]/div/div/div/table/thead/tr[1]/th[3]/button'      # 下一页
    js_time_3 = 'xpath=>/html/body/div[4]/ul/li[1]/div/div/div/table/tbody/tr[2]/td[1]/button/span'     # 选中日期
    state = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[8]/select'      # 状态

    # 随机选择部门
    def select_bumen(self):
        self.clicked(self.bumen_1)
        n = random.randint(1, len(self.get_texts(self.bumen_2))) - 1
        self.get_elements(self.bumen_2)[n].click()
        self.clicked(self.bumen_3)

    def select_feiyong_type(self):
        self.clicked(self.feiyong_type)
        n = random.randint(1, len(self.get_texts(self.feiyong_1))) - 1
        self.get_elements(self.feiyong_1)[n].click()

    def edit_hang(self):
        self.clicked(self.bumen_name)
        self.select_bumen()
        self.select_feiyong_type()
        self.sleep(1)
        self.clicked(self.ys_bumen_name)
        self.select_bumen()
        self.clicked(self.ys_zhibiao_name)
        self.select_bumen()
        self.clicked(self.qy_time_1)
        self.clicked(self.qy_time_2)
        self.clicked(self.js_time_1)
        self.clicked(self.js_time_2)
        self.clicked(self.js_time_3)
        self.select_text(self.state, generator.randomStr(1, False, False, False, False, True, ["启用", "禁用"]))

    # 修改
    modify = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[1]/div/button[2]'
    xuan_1 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[4]/div/table/tbody/tr[1]/td[1]/label/input'
    xuan_2 = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[4]/div/table/tbody/tr[1]/td[1]/label'

    def click_xuan(self):
        if self.get_is_selecet(self.xuan_1) == 0:
            self.clicked(self.xuan_2)
        else:
            pass

    def click_modify(self):
        self.clicked(self.modify)

    # 查询
    zhankai = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[2]/a'        # 展开
    query_bumen_name = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[3]/form/div[1]/div[1]/div/input'        # 部门名称
    query_state = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[3]/form/div[1]/div[2]/div/select'        # 状态
    query_feiyong_name = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[3]/form/div[1]/div[3]/div/input'      # 费用名称
    clear_btn = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[1]/div/button[4]'     # 清空
    query_btn = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[1]/div/button[5]'     # 查询

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query(self):
        self.clicked(self.query_btn)

    def click_clear(self):
        self.clicked(self.clear_btn)
        self.clicked(self.query_btn)
        self.clicked(self.zhankai)

    def input_bumen_name(self, bumen):
        self.type(self.query_bumen_name, bumen)

    def select_state(self, state):
        self.select_text(self.query_state, state)

    def input_feiyong_name(self, feiyong):
        self.type(self.query_feiyong_name, feiyong)

    bumen_name_list = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[4]/div/table/tbody/tr/td[2]/a'
    feiyong_name_list = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[4]/div/table/tbody/tr/td[3]'
    state_list = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[4]/div/table/tbody/tr/td[8]'

    def get_bumen_list(self):
        return self.get_texts(self.bumen_name_list)

    def get_feiyong_list(self):
        return self.get_texts(self.feiyong_name_list)

    def get_state_list(self):
        return self.get_texts(self.state_list)

    # 导出
    export = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[1]/div/button[3]'

    def click_export(self):
        self.clicked(self.export)