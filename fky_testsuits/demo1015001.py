# !/usr/bin/python
# -*- coding:utf-8 -*-
# @Time: 2018/7/26 16:05
# @Author: hychen.cc
import json	    # 因微信企业号返回的格式为json，所以引入json
import requests
import pymssql
import math	    # 引入数学方法
import time
import datetime

server = 'XX.XX.XX.XX'	# 数据库服务器地址
user = 'sa'	# 数据库登录名，可以用sa
password = '******'	# 数据库用户对应的密码
dbName = 'DBNAME'	# 数据库名称
CORP_ID = 'XXXXXX'	# 微信企业号提供的CORP_ID
CORP_SECRET = 'XXXXX'	# 微信企业号提供的CORP_SECRET

"""
因微信接口所需要unix时间戳，所以需要把时间转为为Unix时间戳格式
定义时间转换为Unix时间方法
"""
def datetime_timestamp(dt):
    # dt为字符串
    # 中间过程，一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    ## time.struct_time(tm_year=2018, tm_mon=10, tm_mday=25, tm_hour=10, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=88, tm_isdst=-1)
    # 将"2018-10-25 10:00:00"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

# 定义连接数据库方法
def get_link_server():
    connection = pymssql.connect(server, user, password, database=dbName)
    if connection:
        return connection
    else:
        raise ValueError('Connect DBServer failed.')

""" 
定义获取用户列表，因为微信企业号一次最大只能获取100个，所以需要转换为列表格式，分批次获取
我这里设置是从DB中获取有权限微信打卡的人员(Select * From Table)，换成自己的方式即可
"""
def get_userid_list():
    """
    获取用户列表
    :return:
    """
    conn = get_link_server()
    cursor = conn.cursor()
    sql = "Select * From Table"
    cursor.execute(sql)
    row = cursor.fetchone()
    userlist = []
    while row:
        userlist.append(row[0])
        row = cursor.fetchone()
    if userlist:
        return userlist
    else:
        raise ValueError('Get Userlist failed.')
    conn.close()

"""
获取Access_Token，因为Token有时效（2小时），所以需要存在本地，这样不需要频繁调用，所以我定义了存储过程（sP_GetWX_access_token）来判断之前存储的token是否有效，有效的话就不需要重复获取了
"""
def get_access_token(refresh=False):
    """
    获取Access Token
    :return:
    """
    if not refresh:
        API_ACCESS_TOKEN_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (
            CORP_ID, CORP_SECRET)
        response = requests.get(API_ACCESS_TOKEN_URL, verify=False)
        if response.status_code == 200:
            rep_dict = json.loads(response.text)
            errcode = rep_dict.get('errcode')
            if errcode:
                raise ValueError('Get wechat Access Token failed, errcode=%s.' % errcode)
            else:
                access_token = rep_dict.get('access_token')
                if access_token:
                    conn = get_link_server()
                    cursor = conn.cursor()
                    cursor.execute('exec sP_GetWX_access_token @Access_Token=%s', access_token)
                    conn.commit()
                    conn.close()
                    return access_token
                else:
                    raise ValueError('Get wechat Access Token failed.')
        else:
            raise ValueError('Get wechat Access Token failed.')
    else:
        conn = get_link_server()
        cursor = conn.cursor()
        cursor.execute("Select Access_Token From wx_AccessToken Where ID=1")
        access_token = cursor.fetchone()
        if access_token:
            return access_token[0]
            conn.close()
        else:
            API_ACCESS_TOKEN_URL = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (
                CORP_ID, CORP_SECRET)
            response = requests.get(API_ACCESS_TOKEN_URL, verify=False)
            if response.status_code == 200:
                rep_dict = json.loads(response.text)
                errcode = rep_dict.get('errcode')
                if errcode:
                    raise ValueError('Get wechat Access Token failed, errcode=%s.' % errcode)
                else:
                    access_token = rep_dict.get('access_token')
                    if access_token:
                        conn = get_link_server()
                        cursor = conn.cursor()
                        cursor.execute('exec sP_GetWX_access_token @Access_Token=%s', access_token)
                        conn.commit()
                        conn.close()
                        return access_token
                    else:
                        raise ValueError('Get wechat Access Token failed.')
            else:
                raise ValueError('Get wechat Access Token failed.')

# 获取微信打卡的json格式
def get_punchcard_info(access_token, opencheckindatatype, starttime, endtime, useridlist):
    API_PUNCH_CARD_URL = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata?access_token=' + access_token
    json_str = json.dumps(
        {'opencheckindatatype': opencheckindatatype, 'starttime': starttime, 'endtime': endtime, 'useridlist': useridlist})
    response = requests.post(API_PUNCH_CARD_URL, data=json_str, verify=False)
    if response.status_code == 200:
        rep_dic = json.loads(response.text)
        errcode = rep_dic.get('errcode')
        if errcode == 42001:
            access_token = get_access_token(True)
            API_PUNCH_CARD_URL = 'https://qyapi.weixin.qq.com/cgi-bin/checkin/getcheckindata?access_token=' + access_token
            json_str = json.dumps(
                {'opencheckindatatype': opencheckindatatype, 'starttime': starttime, 'endtime': endtime,
                'useridlist': useridlist})
            response = requests.post(API_PUNCH_CARD_URL, data=json_str, verify=False)
            rep_dic = json.loads(response.text)
            errcode = rep_dic.get('errcode')
            if errcode:
                raise ValueError('Get punch data failed1, errcode=%s' % errcode)
            else:
                value_str = rep_dic.get('checkindata')
                if value_str:
                    return value_str
                else:
                    raise ValueError('Get punch data failed2.')
        elif errcode:
            raise ValueError ('Get punch data failed3, errcode=%s' % errcode)
        else:
            value_str = rep_dic.get('checkindata')
            if value_str:
                return value_str
            else:
                raise ValueError('I do not find employee punch data.')
    else:
        raise ValueError ('Get punch data failed5.')

# 调用接口，获得数据
if __name__ == '__main__':
    today = datetime.date.today()
    oneday = datetime.timedelta(days=3)	# days，即获取几天内的
    yesterday = today - oneday
    starttime = datetime_timestamp(yesterday.strftime('%Y-%m-%d') + ' 00:00:00')
    endtime = datetime_timestamp(today.strftime('%Y-%m-%d') + ' 23:59:59')
    opencheckindatatype = 3
    access_token = get_access_token()
    if access_token:
        useridlist = get_userid_list()
        if useridlist:
            step = 100
            total = len(useridlist)
            n = math.ceil(total/step)
            for i in range(n):
                # print (useridlist[i*step:(i+1)*step])
                punch_card = get_punchcard_info(access_token, opencheckindatatype, starttime, endtime,useridlist[i*step:(i+1)*step])
                # print (punch_card)
                if punch_card:
                    conn = get_link_server()
                    cursor = conn.cursor()
                    for dic_obj in punch_card:
                        cursor.execute('exec sp_AnalysisPunchCard @Json=%s',
                                       (json.dumps(dic_obj, ensure_ascii=False)))
                        # print((json.dumps(dic_obj, ensure_ascii=False)))，sp_AnalysisPunchCard把获取到的数据解析后存入数据库中
                        conn.commit()
                    conn.close()
                    print ('Get punch card successed.')
                else:
                    raise ValueError('No userlist exists')

