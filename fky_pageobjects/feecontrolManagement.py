# 费控管理功能配置
# coding=utf-8
import random
from selenium.webdriver.common.action_chains import ActionChains
from framework import generator
from framework.base_page import BasePage

class FeecontrolManage(BasePage):
    xitonggl = 'xpath=>//span[text()="系统管理"]'
    gongsigl = 'xpath=>//span[text()="公司管理"]'
    zhankai = 'css=>div.bocc-divider.mb30.mt10.draft_info1 > a'

    def into_feikonggl(self):
        self.clicked(self.xitonggl)
        self.clicked(self.gongsigl)
        # self.clicked(self.feikonggl)

    bizhongshezhi = 'xpath=>//div[text()="币种设置"]'

    def into_bizhong(self):
        self.clicked(self.bizhongshezhi)

    bizhong = 'xpath=>//input[@ng-click="tab.saveBaseCurrency()"]'
    bizhong_1 = "'form > div.row.mlr0.add-pr110 > div:nth-child(2) > div > input'"
    xuanze = 'xpath=>//span[@ng-click="tab.showCurrencySelectDialog=true"]'
    zhankai_1 = 'xpath=>//a[contains(text(),"展开")]'
    tiaoshu = 'xpath=>//select[@ng-model="$$selector.pageSize"]'
    tiaoshu_bz = 'xpath=>/html/body/div[3]/div[2]/div[3]/div[2]/div/footer/div/div/div/div[1]/select'
    bizhongma = 'xpath=>/html/body/div[3]/div[2]/div[3]/div[2]/div/table/tbody/tr/td[2]'
    input_bizhongma = 'xpath=>/html/body/div[3]/div[2]/div[3]/div[1]/div[3]/form/div[1]/div[1]/div/input'
    gouxuan = 'xpath=>/html/body/div[3]/div[2]/div[3]/div[2]/div/table/tbody/tr/td[1]/input'
    query_btn = 'xpath=>/html/body/div[3]/div[2]/div[2]/div/button[3]'
    clear_btn = 'xpath=>/html/body/div[3]/div[2]/div[2]/div/button[2]'
    queding1 = 'xpath=>/html/body/div[3]/div[2]/div[2]/div/button[1]'
    save_btn = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/form/div[2]/div/button'
    queding2 = 'xpath=>/html/body/div[2]/div[2]/button[2]'
    show_bizhong = 'xpath=>//table/tbody/tr/td[1]'
    tishi = 'xpath=>/html/body/div[2]/div[2]/p'
    fanhui = 'xpath=>//*[@id="app-content"]/div[2]/div/div[1]/div[1]/div/div[2]/button'

    # 币种配置
    def bizhongpeizhi(self):
        if self.get_is_selecet(self.bizhong) == 0:
            self.execute_script_click(self.bizhong_1)
            self.clicked(self.queding2)
            if self.find_element(self.queding2) == 1:
                self.clicked(self.queding2)
            else:
                pass
        else:
            pass
        self.clicked(self.xuanze)
        self.clicked(self.clear_btn)
        self.clicked(self.query_btn)
        self.select_text(self.tiaoshu_bz, "200")
        self.sleep(2)
        self.clicked(self.zhankai_1)

    def get_bizhong_list(self):
        return self.get_texts(self.bizhongma)

    def input_bizhong(self, bizhongma):
        self.type(self.input_bizhongma, bizhongma)
        self.clicked(self.query_btn)
        self.clicked(self.gouxuan)
        self.clicked(self.queding1)

    def get_show_bizhongs(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.show_bizhong)

    def get_tishi(self):
        return self.get_text(self.tishi)

    def save_queding(self):
        self.clicked(self.save_btn)
        self.clicked(self.queding2)

    def click_queding(self):
        self.clicked(self.queding2)

    def click_queding_1(self):
        if self.get_text(self.tishi) in ['删除成功!', '删除成功']:
            self.clicked(self.queding2)
        else:
            pass

    def click_fanhui(self):
        self.clicked(self.fanhui)

    # 删除币种
    bizhong_name = 'xpath=>//tr[1][@class="ng-scope"]/td[1]'
    bz_del_btn = 'xpath=>//tr[1][@class="ng-scope"]/td[5]/button'

    def get_bizhong_name(self):
        return self.get_text(self.bizhong_name)

    def click_del_bz(self):
        self.clicked(self.bz_del_btn)

    # 城市地域

    # 费用类型

    # feikong_pz = 'xpath=>//div[text()="费控云配置"]'
    feikong_pz = "css=>div.display-flex.flex-wrap > div:nth-child(1) > div.news-flip > div.cp"
    feiyongleixing = 'xpath=>//div[text()="费用类型设置"]'
    jiahao = 'xpath=>//tree-view/div/div[2]/div/div[1]/div[1]/i'
    jiahao2 = 'xpath=>//tree-view/div/div[2]/div/div[1]/div[2]/div/div[1]/i'
    fy_suoyou = 'xpath=>//tree-view/div/div[2]/div/div[1]/div[2]/div/div[1]'
    fy_add_btn = 'xpath=>//button[@ng-click="tab.addNextMenu()"]'
    fy_save_btn = 'xpath=>//button[@w5c-form-submit="tab.save()"]'
    fy_name = 'xpath=>//input[@ng-model="tab.item.name"]'
    fy_tishi = 'xpath=>//span[@class="w5c-error"]'
    fy_qiyong_list = 'xpath=>//tree-view/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/span/div'
    fy_last = "'div.tree-folder-content.ng-scope > div > div.tree-folder-content.ng-scope > div:nth-last-child(1) > div'"
    fy_last_css = 'css=>div.tree-folder-content.ng-scope > div > div.tree-folder-content.ng-scope > div:nth-last-child(1) > div'
    fy_fanhui = 'xpath=>//button[@ng-click="goBack()"]'


    def click_fy_fanhui(self):
        self.clicked(self.fy_fanhui)

    def into_feiyongleixing(self):
        # self.clicked(self.feikong_pz)
        self.suspend(self.feikong_pz)       # 鼠标悬浮
        self.clicked(self.feikong_pz)
        self.clicked(self.feiyongleixing)

    def click_jiahao(self):
        self.clicked(self.jiahao)
        self.clicked(self.jiahao2)

    def click_jianhao(self):
        self.clicked(self.jiahao2)
        self.clicked(self.jiahao)

    icon = 'xpath=>//span[@ng-click="tab.clickUrlList()"]'
    icon_1 = 'css=>svg.icon'

    def add_fyleixing(self, name):
        self.clicked(self.jiahao)
        self.clicked(self.jiahao2)
        self.clicked(self.fy_suoyou)
        self.clicked(self.fy_add_btn)
        self.clear(self.fy_name)
        self.clicked(self.fy_save_btn)
        fy_tishi = len(self.get_texts(self.fy_tishi))
        self.type(self.fy_name, name)
        self.clicked(self.icon)
        n = random.randint(1, len(self.get_texts(self.icon_1))-1)
        el = self.get_elements(self.icon_1)[n]
        ActionChains(self.driver).double_click(el).perform()
        self.clicked(self.fy_save_btn)
        self.clicked(self.queding2)
        return fy_tishi

    def get_last_name(self):
        return self.get_text(self.fy_last_css)

    def get_fy_tishi(self):
        return self.get_text(self.fy_tishi)

    def get_fy_list(self):
        return self.get_texts(self.fy_qiyong_list)

    def click_last(self):
        self.execute_script_click(self.fy_last)

    # 修改
    def modify_fy(self, name):
        self.type(self.fy_name, name)
        self.clicked(self.fy_save_btn)
        self.clicked(self.queding2)

    # 禁用
    jinyong = 'xpath=>//button[@ng-click="tab.close()"]'
    jiahao3 = 'xpath=>//tree-view/div/div[2]/div/div[2]/div[1]/i'
    fy_jinyong_list = 'xpath=>//tree-view/div/div[2]/div/div[2]/div[2]/div/div/span/div'

    def click_jinyong(self):
        self.clicked(self.jinyong)

    def click_jinyong_jiahao(self):
        self.clicked(self.jiahao3)

    def click_jinyong_jianhao(self):
        self.clicked(self.jiahao3)

    def get_jinyong_list(self):
        return self.get_texts(self.fy_jinyong_list)
    # 启用
    qiyong = 'xpath=>//button[@ng-click="tab.open()"]'
    fy_frist = 'css=>div:nth-child(2) > div.tree-folder-content.ng-scope > div:first-child > div'

    def click_qiyong(self):
        self.clicked(self.qiyong)

    def click_fy_frist(self):
        self.clicked(self.fy_frist)

    # 导出
    fy_export = 'xpath=>//button[@ng-click="tab.exportExcel()"]'

    def click_fy_export(self):
        self.clicked(self.fy_export)

    # 导入
    fy_import = 'xpath=>//button[@ng-click="tab.showImportExcelDialog=true"]'
    fy_title = 'xpath=>//div/h3[@class="modal-title ng-binding"]'
    fy_close = 'xpath=>//button[@ng-click="import.close()"]'

    def click_fy_import(self):
        self.clicked(self.fy_import)

    def get_fy_title(self):
        return self.get_text(self.fy_title)

    def click_fy_close(self):
        self.clicked(self.fy_close)

    # 辅助核算项
    fuzhuhsx = 'xpath=>//div[text()="辅助核算设置"]'
    hs_title = 'css=>span.color-5866.pl15.fs-18'
    hs_save = 'xpath=>//button[@ng-click="tab.save()"]'

    def into_fuzhuhsx(self):
        self.clicked(self.fuzhuhsx)

    def get_hs_title(self):
        return self.get_text(self.hs_title)

    def click_hs_save(self):
        self.clicked(self.hs_save)

    # 费用标准
    # 发票敏感字
    fapiaomgz = '''xpath=>//li[@ng-click="tab.go('conf/sensitiveWords')"]'''

    def into_fapiaomgz(self):
        self.clicked(self.fapiaomgz)

    fp_add = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[1]/div/button[1]'
    fp_fpzhonglei = 'xpath=>//select[@ng-model="item.billType"]'
    fp_type = 'xpath=>//select[@ng-model="item.wordsType"]'
    fp_content = 'xpath=>//textarea[@ng-model="item.contents"]'
    fp_fangshi = 'xpath=>//select[@ng-model="item.controlType"]'

    def click_fp_add(self):
        self.clicked(self.fp_add)

    def select_fp_zhonglei(self):
        zhonglei = generator.randomStr(1, False, False, False, False, True, ["增值税专用发票", "增值税普通发票","火车票", "出租车票", "定额发票", "其他发票"])
        self.select_text(self.fp_fpzhonglei, zhonglei)

    def edit_content(self, content):
        self.select_text(self.fp_type, generator.randomStr(1, False, False, False, False, True, ["发票内容", "销售方抬头"]))
        self.type(self.fp_content, content)
        self.select_text(self.fp_fangshi, generator.randomStr(1, False, False, False, False, True, ["强控", "警告"]))

    fp_save = 'xpath=>//button[@ng-click="submit()"]'
    fp_quxiao = '''xpath=>//button[@ng-click="closeThisDialog('cancel')"]'''

    def click_fp_save(self):
        self.clicked(self.fp_save)

    def click_fp_quxiao(self):
        self.clicked(self.fp_quxiao)

    fp_content_show = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[4]/div/table/tbody/tr/td[3]'

    def get_content_list(self):
        self.select_text(self.tiaoshu, '200')
        return self.get_texts(self.fp_content_show)

    # 修改
    fp_xiugai = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[1]/div/button[2]'
    fp_xuan = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[1]/label/input'
    fp_xuan_click = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[4]/div/table/tbody/tr[1]/td[1]/label'

    def click_fp_xuan(self):
        if self.get_is_selecet(self.fp_xuan) == 0:
            self.clicked(self.fp_xuan_click)
        else:
            pass

    def click_fp_xiugai(self):
        self.clicked(self.fp_xiugai)

    # 查询
    fp_input_content = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[3]/div[3]/form/div[1]/div[1]/div/input'
    fp_query = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[1]/div/button[6]'
    fp_clear = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[1]/div/button[5]'

    def click_fp_zhankai(self):
        self.clicked(self.zhankai)

    def input_fp_content(self, content):
        self.type(self.fp_input_content, content)

    def click_fp_clear(self):
        self.clicked(self.fp_clear)
        self.clicked(self.fp_query)

    def click_fp_query(self):
        self.clicked(self.fp_query)

    # 删除
    fp_del = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[1]/div/button[3]'

    def click_fp_del(self):
        self.clicked(self.fp_del)

    # 导出
    fp_export = 'xpath=>//*[@id="app-content"]/div[2]/div/div/div/div/div[3]/div[1]/div/button[4]'

    def click_fp_export(self):
        self.clicked(self.fp_export)

    # 报销关联申请
    bx_shenqing = 'xpath=>//div[text()="事前申请设置"]'

    def into_bx_glshenqing(self):
        self.suspend(self.feikong_pz)       # 鼠标悬浮
        self.clicked(self.feikong_pz)
        self.clicked(self.bx_shenqing)

    bx_add = 'xpath=>//button[@ng-click="tab.onClick(1)"]'
    bx_feiyong_type = 'xpath=>//span[@ng-click="tab.showSelectCostDialog=true"]'
    feiyong_type_1 = 'xpath=>//div[@class="ecp-icon"]/following-sibling::div'
    bx_is_qiangzhiguanlian = "'div:nth-child(2) > div > span.float-left.pr20.mt5.pl20 > label'"
    bx_not_qiangzhiguanlian = "'div:nth-child(2) > div > span.float-left.ml25.mt5 > label'"
    bx_richang_1 = 'xpath=>//input[@ng-model="item.advanceApproval_1"]'
    bx_chailv_1 = 'xpath=>//input[@ng-model="item.advanceApproval_2"]'
    bx_richang = 'xpath=>//label[text()="事前审批单:"]/following-sibling::div/span[1]/label'
    bx_chailv = 'xpath=>//label[text()="事前审批单:"]/following-sibling::div/span[2]/label'
    bx_gkshunxu = 'xpath=>//input[@ng-model="item.sort"]'
    bx_tiaojian = 'xpath=>//select[@ng-model="item.specialCondition"]'
    bx_shunxu = 'xpath=>//table/tbody/tr/td[5]'
    bx_tiaojian_1 = 'xpath=>//label[text()="条件公式:"]/following-sibling::div/select'
    bx_tiaojian_2 = 'xpath=>//input[@ng-model="item.amountCondition"]'
    bx_tiaojian_3 = 'xpath=>//span[@ng-click="tab.showSelectOrgDialog=true"]'
    bx_tiaojian_4 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div/div[1]/i'
    bx_tiaojian_5 = 'xpath=>/html/body/div[4]/div[2]/div[3]/div/div/div/div/div[2]/div/div/span/div'
    bx_tiaojian_6 = 'xpath=>//button[@ng-click="tree.ok()"]'

    def click_bx_add(self):
        self.clicked(self.bx_add)

    def click_feiyong_type(self):
        self.clicked(self.bx_feiyong_type)
        n = random.randint(1, len(self.get_texts(self.feiyong_type_1))) - 1
        self.get_elements(self.feiyong_type_1)[n].click()

    def edit_bxglsq(self, shunxu, tiaojian):
        self.execute_script_click(self.bx_not_qiangzhiguanlian)
        self.execute_script_click(self.bx_is_qiangzhiguanlian)
        if self.get_is_selecet(self.bx_richang_1) == 0:
            self.clicked(self.bx_richang)
        else:
            pass
        self.clicked(self.bx_chailv)
        self.type(self.bx_gkshunxu, shunxu)
        self.select_text(self.bx_tiaojian, tiaojian)

    def get_bx_shunxu_list(self):
        self.select_text(self.tiaoshu, "200")
        return self.get_texts(self.bx_shunxu)

    def select_bx_tiaojian1(self):
        self.select_text(self.bx_tiaojian_1, generator.randomStr(1, False, False, False, False, True, ["大于等于", "大于"]))
        self.type(self.bx_tiaojian_2, generator.randomStr(3))

    def select_bx_tiaojian2(self):
        self.select_text(self.bx_tiaojian_1, generator.randomStr(1, False, False, False, False, True, ["不包含", "包含"]))
        self.clicked(self.bx_tiaojian_3)
        self.clicked(self.bx_tiaojian_4)
        n = random.randint(1, len(self.get_texts(self.bx_tiaojian_5)))-1
        self.get_elements(self.bx_tiaojian_5)[n].click()
        self.clicked(self.bx_tiaojian_6)

    bx_save = 'xpath=>//button[@ng-click="submit()"]'
    bx_quxiao = '''xpath=>//button[@ng-click="closeThisDialog('cancel')"]'''

    def click_bx_save(self):
        self.clicked(self.bx_save)

    def click_bx_quxiao(self):
        self.clicked(self.bx_quxiao)

    # 修改
    bx_xuan = 'xpath=>//table/tbody/tr/td[1]/label/input'
    bx_xuan_1 = 'xpath=>//table/tbody/tr/td[1]/label'
    bx_xiugai = 'xpath=>//button[@ng-click="tab.onClick(2)"]'

    def click_bx_xuan(self):
        if self.get_is_selecet(self.bx_xuan) == 0:
            self.clicked(self.bx_xuan_1)
        else:
            pass

    def click_bx_xiugai(self):
        self.clicked(self.bx_xiugai)

    # 查询
    bx_query = 'xpath=>//button[@ng-click="tab.ajaxQuery()"]'
    bx_clear = 'xpath=>//button[@ng-click="tab.onClick(5)"]'
    bx_sqspd = 'xpath=>//select[@ng-model="tab.params.advanceApproval"]'

    def click_bx_zhankai(self):
        self.clicked(self.zhankai)

    def click_bx_clear(self):
        self.clicked(self.bx_clear)
        self.clicked(self.bx_query)

    def click_bx_query(self):
        self.clicked(self.bx_query)

    def select_bx_sqspd(self, sqspd):
        self.select_text(self.bx_sqspd, sqspd)

    bx_sqspd_list = 'xpath=>//table/tbody/tr/td[3]'

    def get_bx_sqspd_list(self):
        return self.get_texts(self.bx_sqspd_list)

    # 删除
    bx_del = 'xpath=>//button[@ng-click="tab.onClick(3)"]'

    def click_bx_del(self):
        self.clicked(self.bx_del)

    # 导出
    bx_export = 'xpath=>//button[@ng-click="tab.onClick(4)"]'

    def click_bx_export(self):
        self.clicked(self.bx_export)

    # 发票种类、内容与费用类型
    fz_invoice_type = 'xpath=>//div[text()="发票识别设置"]'

    def into_fz_invoice_type(self):
        self.suspend(self.feikong_pz)       # 鼠标悬浮
        self.clicked(self.feikong_pz)
        self.clicked(self.fz_invoice_type)

    fz_add_fapiao = 'xpath=>//button[@ng-click="tab.add()"]'
    fz_tishi = 'xpath=>//span[@class="w5c-error"]'
    fz_fapiao = 'xpath=>//select[@name="billType"]'
    fz_feiyong_type = 'xpath=>//span[@ng-click="tab.showCostTypeSelectDialog=true"]'
    fz_fapiao_content = 'xpath=>//textarea[@name="billContent"]'

    def click_fz_add_invoic(self):
        self.clicked(self.fz_add_fapiao)

    def select_fz_fapiao(self):
        fapiao = generator.randomStr(1, False, False, False, False, True, ["增值税专用发票", "增值税普通发票", "火车票", "出租车票", "定额发票", "其他发票"])
        self.select_text(self.fz_fapiao, fapiao)

    def edit_fz_fapiao(self):
        self.clicked(self.fz_feiyong_type)
        n = random.randint(1, len(self.get_texts(self.feiyong_type_1))) - 1
        el = self.get_elements(self.feiyong_type_1)[n]
        el.click()
        fz_feiyong_text = generator.random_str(10, 20)
        self.type(self.fz_fapiao_content, fz_feiyong_text)
        return fz_feiyong_text

    def get_fz_tishi(self):
        return self.get_text(self.fz_tishi)

    fz_save = 'xpath=>//button[@w5c-form-submit="tab.save()"]'
    fz_quxiao = 'xpath=>//button[@ng-click="goBack()"]'

    def click_fz_save(self):
        self.clicked(self.fz_save)

    def click_fz_quxiao(self):
        self.clicked(self.fz_quxiao)

    fz_content_list = 'xpath=>//table/tbody/tr/td[4]'

    def get_fz_content_list(self):
        self.select_text(self.tiaoshu, '200')
        return self.get_texts(self.fz_content_list)

    # 修改
    fz_xiugai = 'xpath=>//table/tbody/tr[1]/td[6]/button'

    def click_fz_xiugai(self):
        self.clicked(self.fz_xiugai)

    # 查询

    fz_query = 'xpath=>//button[@ng-click="tab.ajaxQuery(1)"]'
    fz_clear = 'xpath=>//button[@ng-click="tab.clear()"]'
    fz_content_input = 'xpath=>//input[@ng-model="tab.params.billContent"]'

    def click_fz_zhankai(self):
        self.clicked(self.zhankai)

    def click_fz_clear(self):
        self.clicked(self.fz_clear)
        self.clicked(self.fz_query)

    def click_fz_query(self):
        self.clicked(self.fz_query)

    def input_fz_content(self, content):
        self.type(self.fz_content_input, content)

    # 删除
    fz_xuan = 'xpath=>//table/tbody/tr[1]/td[1]/label/input'
    fz_xuan_1 = 'xpath=>//table/tbody/tr[1]/td[1]/label'
    fz_del = 'xpath=>//button[@ng-click="tab.deletebillCostTypeRelation()"]'

    def click_fz_xuan(self):
        if self.get_is_selecet(self.fz_xuan) == 0:
            self.clicked(self.fz_xuan_1)
        else:
            pass

    def click_fz_del(self):
        self.clicked(self.fz_del)

    # 导出
    fz_export = 'xpath=>//button[@ng-click="tab.exportExcel()"]'

    def click_fz_export(self):
        self.clicked(self.fz_export)

    # 税前列支标准
    lz_sqlzbz = 'xpath=>//div[text()="税前列支标准设置"]'

    def into_lz_sqlzbz(self):
        self.clicked(self.lz_sqlzbz)

    lz_title = 'css=>#temp-add > div.flex-1.pl30 > label'

    def get_lz_title(self):
        return self.get_text(self.lz_title)

    lz_is_qiyong = 'css=>#temp-add > div.flex-1.pl30 > input'
    lz_is_qiyong_1 = "'#temp-add > div.flex-1.pl30 > input'"

    def click_lz_isqiyong(self):
        if self.get_is_selecet(self.lz_is_qiyong) == 0:
            self.execute_script_click(self.lz_is_qiyong_1)
        else:
            pass

    lz_guankong = 'xpath=>//select[@ng-model="tab.params.controlMode"]'
    lz_yujiyinshou = 'name=>yearincome'
    lz_jieshouer = 'xpath=>//span[@ng-click="tab.openSelectPayees(item)"]'
    lz_jieshouer_1 = 'css=>div.ps-con > div> label'
    lz_jieshouer_2 = 'xpath=>//button[@ng-click="userSelect.ok()"]'

    def edit_lz_sqlzbz(self):
        self.select_text(self.lz_guankong, generator.randomStr(1, False, False, False, False, True, ["强控", "警告"]))
        self.double_clicked(self.lz_yujiyinshou)
        self.type1(self.lz_yujiyinshou, generator.randomStr(4))
        self.clicked(self.lz_jieshouer)
        n = random.randint(1, len(self.get_texts(self.lz_jieshouer_1))) - 1
        self.get_elements(self.lz_jieshouer_1)[n].click()
        self.clicked(self.lz_jieshouer_2)

    lz_tijiao = 'xpath=>//button[@w5c-form-submit="tab.saveBaseCurrency()"]'

    def click_lz_tijiao(self):
        self.clicked(self.lz_tijiao)

    # 重置报销
    cz_chongzhibx = 'xpath=>//div[text()="报销数据重置"]'
    cz_title = 'class=>ml15'

    def into_cz_chongzhibx(self):
        self.suspend(self.feikong_pz)       # 鼠标悬浮
        self.clicked(self.feikong_pz)
        self.clicked(self.cz_chongzhibx)

    def get_cz_title(self):
        return self.get_text(self.cz_title)