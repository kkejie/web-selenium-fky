# coding=utf-8
import random


def randomStr(length=6, timeIn=False, lowerCaseLetter=False, capitalLetter=False, number=True, specialSign=False,
              otherSignsList=None):
    '''
    返回一个随机字符串
    :param length: 字符串长度
    :param time: 是否包含时间
    :param lowerCaseLetter: 是否包含小写字母
    :param capitalLetter: 是否包含大写字母
    :param number: 是否包含数字
    :param specialSign: 是否包含特殊符号
    :param otherSignsList: 其他字符
    :return:
    '''
    # res = []


    res = []
    if number == True:
        res.extend(map(lambda i: chr(i), [x for x in range(48, 58)]))
    if lowerCaseLetter == True:
        res.extend(map(lambda i: chr(i), [x for x in range(97, 123)]))
    if capitalLetter == True:
        res.extend(map(lambda i: chr(i), [x for x in range(65, 90)]))
    if specialSign == True:
        # res.extend(['_', '-'])
        if otherSignsList != None and isinstance(otherSignsList, list):
            res.extend(otherSignsList)
    str = ""
    if len(res) != 0:
        for x in range(length):
            index = random.randint(0, len(res) - 1)
            str = str + res[index]
    if timeIn == True:
        from SRC.common.utils import getCurrentTime

        str = str + getCurrentTime()
    return str

# ress = []
# s3 = randomStr(111)
# print(s3)
#
res = ["可乐","雪碧","芬达","啤酒"]
s1 = randomStr(1,False,False,False,False,True,["可乐","雪碧","芬达","啤酒"] )
print(s1)
#
# ress = ["南昌","上海","北京","深圳"]
# s2 = randomStr(111,False,True,False,False,False,True)
# print(s2*3)


# def compareJson(a, b):
# 	if not isinstance(a, dict):
# 		return False, '第一个参数的类型不是dict'
# 	if not isinstance(b, dict):
# 		return False, '第二个参数的类型不是dict'
# 	walk_sort(a)
# 	walk_sort(b)
#
#
# def walk_sort(v):
# 	if isinstance(v, dict):
# 		for i, j in v.items():
# 			walk_sort(j)
# 	if isinstance(v, (tuple, list)):
# 		v.sort()
# 		for i in v:
# 			walk_sort(i)
#
#
#
#
#
# target_key = 'name'
#
# def walk_find(k,v):
#     if k == target_key:
#         return v
#     if isinstance(v, dict):
#         for i,j in v.iteritems():
#             res = walk_find(i,j)
#             if res is not None:
#                 return res
#     if isinstance(v, (tuple, list)):
#         for i in v:
#             res = walk_find('', i)
#             if res is not None:
#                 return res
#     return None
#
# arr1 = walk_find('', d1)
