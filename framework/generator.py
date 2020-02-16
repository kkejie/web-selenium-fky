"""一些生成器方法，生成随机数，手机号，以及连续数字等"""
import random
from faker import Factory

fake = Factory().create('zh_CN')

def random_phone_number():
    """随机手机号"""
    return fake.phone_number()

def random_name():
    """随机姓名"""
    return fake.name()

def random_address():
    """随机地址"""
    return fake.address()

def random_email():
    """随机email"""
    return fake.email()

def random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()

def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        # rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator

def randomStr(length=6, number=True, timeIn=False, lowerCaseLetter=False, capitalLetter=False, specialSign=False,
              otherSignsList=None):
    '''
    返回一个随机字符串
    :param length: 字符串长度
    :param number: 是否包含数字
    :param time: 是否包含时间
    :param lowerCaseLetter: 是否包含小写字母
    :param capitalLetter: 是否包含大写字母
    :param specialSign: 是否包含特殊符号
    :param otherSignsList: 其他字符
    :return:
    '''

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



# if __name__ == '__main__':
#     print(random_phone_number())
#     print(random_name())
#     print(random_address())
#     print(random_email())
#     print(random_ipv4())
# print(random_str(min_chars=1, max_chars=8))
#     print(randomStr(11,True))
#     print(random_phone_number())
#
#     choices = ['John', 'Sam', 'Lily', 'Rose']
#     choice_gen = factory_choice_generator(choices)()
#     for i in range(5):
#         print(next(choice_gen))

# print(randomStr(1, False, False, False, False, True, ["客商", "客户", "供应商", "拓展", "合作伙伴"]))