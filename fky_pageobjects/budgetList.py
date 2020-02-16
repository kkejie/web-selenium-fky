# 预算主列表
# coding=utf-8
import random

from framework.base_page import BasePage
from framework import generator

class BudgetList(BasePage):
    bumenys = 'xpath=>//span[text()="部门预算"]'
    ys_zlb = 'xpath=>//span[text()="预算主列表"]'

    def into_yszlb(self):
        self.clicked(self.bumenys)
        self.clicked(self.ys_zlb)

    # 新增
    add_btn = 'xpath=>//button[@ng-click="onClick(3)"]'

    def click_add_btn(self):
        self.clicked(self.add_btn)

    ys_name_list = 'xpath=>//tbody/tr/td[5]'

    def get_ys_name_list(self):
        return self.get_texts(self.ys_name_list)

    # 保存草稿
    tijiao = 'xpath=>//button[@ng-click="onClick(1);"]'
    save_caogao = 'xpath=>//button[@ng-click="onClick(2);"]'
    tishi = 'xpath=>/html/body/div[2]/div[2]/p'
    fanhui = 'xpath=>//button[@ng-click="onClick(5);"]'

    def click_tijiao(self):
        self.clicked(self.tijiao)

    def click_save_caogao(self):
        self.clicked(self.save_caogao)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def click_fanhui(self):
        self.clicked(self.fanhui)

    # 载入草稿
    zairucg = 'xpath=>//button[@ng-click="onClick(3);"]'
    cg_ys_name = 'xpath=>/html/body/div[5]/div[2]/div/div/div[4]/div/table/tbody/tr/td[3]'
    cg_tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'

    def click_zairucg(self):
        self.clicked(self.zairucg)

    def get_cg_ys_name(self):
        self.select_text(self.cg_tiaoshu, '200')
        return self.get_texts(self.cg_ys_name)

    # 选择草稿
    cg_xuan = 'xpath=>/html/body/div[5]/div[2]/div/div/div[4]/div/table/tbody/tr/td[1]/input'
    cg_queding = 'xpath=>//button[@ng-click="tab.getResult()"]'

    def xuanze_cg(self):
        self.select_text(self.cg_tiaoshu, '200')
        n = random.randint(1, len(self.get_elements(self.cg_xuan))) - 1
        self.get_elements(self.cg_xuan)[n].click()
        ys_name = self.get_texts(self.cg_ys_name)[n]
        self.clicked(self.cg_queding)
        return ys_name

    caozuo = 'xpath=>//button[@ng-click="operation.del(item)"]'

    def get_caozuo_elements(self):
        return self.get_elements(self.caozuo)

    # 抬头
    # ys_leixing = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/select'
    ys_name = 'xpath=>//input[@ng-model="fmBudgetPlanDTO.budgetName"]'
    ys_niandu = 'xpath=>//select[@ng-model="fmBudgetPlanDTO.budgetYear"]'
    ys_niandu_option = 'xpath=>//select[@ng-model="fmBudgetPlanDTO.budgetYear"]/option'

    # 获取预算名称输入框内容
    def get_input_ys_name(self):
        return self.get_input_text(self.ys_name)

    def input_ys_name(self, name):
        self.type(self.ys_name, name)

    def edit_taitou(self, name):
        leixing = generator.randomStr(1, False, False, False, False, True, ["部门", "员工"])
        self.select_text(self.ys_leixing, leixing)
        if self.get_tishi() == "重新选择预算抬头信息，将会清除预算编制行信息，请确认？":
            self.click_queding()
        self.type(self.ys_name, name)
        self.select_index(self.ys_niandu, self.ys_niandu_option)
        if self.get_tishi() == "重新选择预算抬头信息，将会清除预算编制行信息，请确认？":
            self.click_queding()
        return leixing

    # 添加行
    add_hang = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/button[1]'
    del_hang = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/button[2]'
    xuan = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/thead/tr/th[1]/input'

    def click_add_hang(self):
        self.clicked(self.add_hang)
        self.clicked(self.xuan)
        self.clicked(self.del_hang)
        self.clicked(self.add_hang)

    # 下载批量导入模板
    download = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/button[4]'

    def click_download(self):
        self.clicked(self.download)

    # 填写预算指标预算部门/人员选择
    ys_zhibiao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[3]/span/a'
    ys_bumen = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[4]/span/a'
    tanc_1 = 'xpath=>/html/body/div[5]/div[2]/div[3]/div/div/div/div[1]/div[1]/i'
    tanc_2 = 'xpath=>/html/body/div[5]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/span/div'
    tanc_queding = 'xpath=>/html/body/div[5]/div[2]/div[1]/div[2]/button[1]'
    renyuan = 'xpath=>/html/body/div[5]/div[2]/div/div[3]/div/div[2]/div/label'
    renyuan_queding = 'xpath=>/html/body/div[5]/div[2]/div/div[4]/div/button'

    def execute_tanc(self):
        self.clicked(self.tanc_1)
        n = random.randint(1, len(self.get_texts(self.tanc_2))) - 1
        self.get_elements(self.tanc_2)[n].click()
        self.clicked(self.tanc_queding)

    def select_yszb_ysbm(self):
        self.clicked(self.ys_zhibiao)
        self.execute_tanc()
        self.clicked(self.ys_bumen)
        self.execute_tanc()
        if self.get_tishi() == "存在相同的预算行信息! 行号：1":
            self.click_queding()
            self.execute_tanc()

    def select_yszb_ygbm(self):
        self.clicked(self.ys_zhibiao)
        self.execute_tanc()
        self.clicked(self.ys_bumen)
        n = random.randint(1, len(self.get_texts(self.renyuan))) - 1
        self.get_elements(self.renyuan)[n].click()
        self.clicked(self.renyuan_queding)

    # 管控周期
    gk_zhouqi = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[5]/select'

    def select_gk_zhouqi(self, zhouqi):
        self.select_text(self.gk_zhouqi, zhouqi)

    # 年度
    ys_jine = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[6]/input'

    def input_nd_jine(self):
        jine = random.randint(50000, 100000)
        self.type(self.ys_jine, jine)
        return jine

    # 季度
    tianbao = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/table/tbody/tr/td[6]/a'
    jidu_1 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[1]/td[2]/input'
    jidu_2 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[1]/td[4]/input'
    jidu_3 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[2]/td[2]/input'
    jidu_4 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[2]/td[4]/input'
    save = 'xpath=>/html/body/div[5]/div[2]/div/div/div[1]/div/button[3]'

    def input_jd_jine(self):
        self.clicked(self.tianbao)
        jine_1 = random.randint(10000, 20000)
        jine_2 = random.randint(10000, 20000)
        jine_3 = random.randint(10000, 20000)
        jine_4 = random.randint(10000, 20000)
        self.type(self.jidu_1, jine_1)
        self.type(self.jidu_2, jine_2)
        self.type(self.jidu_3, jine_3)
        self.type(self.jidu_4, jine_4)
        self.clicked(self.save)
        jine = jine_1 + jine_2 + jine_3 + jine_4
        return jine

    # 月度
    yuedu_1 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[1]/td[2]/input'
    yuedu_2 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[1]/td[4]/input'
    yuedu_3 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[1]/td[6]/input'
    yuedu_4 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[2]/td[2]/input'
    yuedu_5 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[2]/td[4]/input'
    yuedu_6 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[2]/td[6]/input'
    yuedu_7 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[3]/td[2]/input'
    yuedu_8 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[3]/td[4]/input'
    yuedu_9 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[3]/td[6]/input'
    yuedu_10 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[4]/td[2]/input'
    yuedu_11 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[4]/td[4]/input'
    yuedu_12 = 'xpath=>/html/body/div[5]/div[2]/div/div/div[3]/div/form/table/tbody/tr[4]/td[6]/input'

    def input_yd_jine(self):
        self.clicked(self.tianbao)
        jine_1 = random.randint(10000, 20000)
        jine_2 = random.randint(10000, 20000)
        jine_3 = random.randint(10000, 20000)
        jine_4 = random.randint(10000, 20000)
        jine_5 = random.randint(10000, 20000)
        jine_6 = random.randint(10000, 20000)
        jine_7 = random.randint(10000, 20000)
        jine_8 = random.randint(10000, 20000)
        jine_9 = random.randint(10000, 20000)
        jine_10 = random.randint(10000, 20000)
        jine_11 = random.randint(10000, 20000)
        jine_12 = random.randint(10000, 20000)
        self.type(self.yuedu_1, jine_1)
        self.type(self.yuedu_2, jine_2)
        self.type(self.yuedu_3, jine_3)
        self.type(self.yuedu_4, jine_4)
        self.type(self.yuedu_5, jine_5)
        self.type(self.yuedu_6, jine_6)
        self.type(self.yuedu_7, jine_7)
        self.type(self.yuedu_8, jine_8)
        self.type(self.yuedu_9, jine_9)
        self.type(self.yuedu_10, jine_10)
        self.type(self.yuedu_11, jine_11)
        self.type(self.yuedu_12, jine_12)
        self.clicked(self.save)
        jine = jine_1 + jine_2 + jine_3 + jine_4 + jine_5 + jine_6 + jine_7 + jine_8 + jine_9 + jine_10 + jine_11 + jine_12
        return jine

    ys_zjine = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div/button[5]/span'

    def get_ys_zjine(self):
        return self.get_text(self.ys_zjine)

    close_btn = 'xpath=>/html/body/div[5]/div[2]/div/div/div[1]/div/button[3]'

    def click_close_btn(self):
        self.clicked(self.close_btn)

    # 查询
    tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'
    ys_bianhao = 'xpath=>//tbody/tr/td[2]'
    dj_state = 'xpath=>//tbody/tr/td[10]'
    ys_type = 'xpath=>//tbody/tr/td[10]'
    query_ys_bianhao = 'xpath=>//input[@ng-model="query.budgetNo"]'
    query_ys_type = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[3]/div[3]/form/div[1]/div[2]/div/select'
    query_dj_state = 'xpath=>//select[@ng-model="query.processStatus"]'

    def get_ys_bianhao(self):
        self.select_text(self.tiaoshu, '200')
        return self.get_texts(self.ys_bianhao)

    def get_dj_state(self):
        self.select_text(self.tiaoshu, '200')
        return self.get_texts(self.dj_state)

    def get_ys_type(self):
        self.select_text(self.tiaoshu, '200')
        return self.get_texts(self.ys_type)

    def input_ys_bianhao(self, bianhao):
        self.type(self.query_ys_bianhao, bianhao)

    def select_dj_state(self, state):
        self.select_text(self.query_dj_state, state)

    def select_ys_type(self, type):
        self.select_text(self.query_ys_type, type)

    zhankai = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[3]/div[2]/a'
    clear = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[1]/div/button[3]'
    query = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[1]/div/button[4]'

    def click_zhankai(self):
        self.clicked(self.zhankai)

    def click_query(self):
        self.clicked(self.query)

    def click_clear(self):
        self.clicked(self.clear)
        self.clicked(self.query)
        self.clicked(self.zhankai)

    # 导出
    export = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div/div[1]/div/button[2]'
    queding = 'xpath=>/html/body/div[2]/div[2]/button[2]'

    def click_export(self):
        self.clicked(self.export)

    def click_queding(self):
        self.clicked(self.queding)