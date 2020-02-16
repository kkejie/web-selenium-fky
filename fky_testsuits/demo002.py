#!/usr/bin/python2.7
# coding=utf-8

import json
import sys
from importlib import reload

# reload(sys)
# sys.setdefaultencoding('utf-8')

apis = ["/ecp/apis/ccsyckj/uc/loginPlatform.do", "/ecp/ccsyckj/co/coPublicNotice/save.do "]

outputFilePath = "C:/Users/Kejie/Desktop/postman.json"
itemDicts = []

for api in apis:
# 这里的base是postman里全局或者环境变量的baseUrl
    rawString = "{{test}}" + api
    paths = api.split('/')
    itemDict = { "name": api,
                "event": [
                            {"listen": "test",
                            "script": {
                                "id": "14d7825c-fef1-4d4a-a7b1-bdce259f7b41",
                                "type": "text/javascript",
                                "exec": [
                                    "pm.test(\"接口返回 200\", function () {",
                                    "    pm.response.to.have.status(200);",
                                    "});"
                                    ]
                                    }
                                    }
                                    ],
                                    "request": {
                                        "method": "POST",
                                        "header": [],
                                        "body": {},
                                        "url": {
                                            "raw": rawString,
                                            "host": [
                                                "{{test}}"
                                                ],
                                            "path": paths
                                        }
                        },
                        "response": []
                        }
    itemDicts.append(itemDict)

postmanDict = {
    "info": {
        "_postman_id": "bb6f7282-9c68-4b73-a463-d2087e3301c5",
        "name": "无参数",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item":itemDicts
        }
jsonStr = json.dumps( postmanDict, ensure_ascii=False)
with open(outputFilePath, 'wt') as f:
    f.write(jsonStr)

# print(postmanDict)