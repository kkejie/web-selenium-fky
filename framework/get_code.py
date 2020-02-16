#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5

class RClient(object):
    def __init__(self, username, password, soft_id, soft_key):
        self.username = username
        self.password = md5(password.encode("utf-8")).hexdigest()
        self.soft_id = soft_id
        self.soft_key = soft_key
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }
    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.png', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()
    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()

def get_code(im_file):
    rc = RClient('kejie1994', 'kejie0208', '94522', '62c235939b7240879453f31603733fd6')
    im_source = open(im_file, "rb").read()
    dict = rc.rk_create(im_source, 3040)
    return dict["Result"]
# if __name__ == '__main__':
    # wbe = webdriver.Chrome()
    # wbe.get("https://www.dajiang365.com/login/index.html")
    # time.sleep(2)
    # wbe.save_screenshot("das.png")
    # element = wbe.find_element_by_xpath('//*[@id="entry_name"]/p[3]/img')
    # left = element.location['x']
    # top = element.location['y']
    # right = element.location['x'] + element.size['width']
    # bottom = element.location['y'] + element.size['height']
    # im = Image.open(r'das.png')
    # im = im.crop((left, top, right, bottom))
    # im.save('a.png')
    # time.sleep(2)
    # get_code("a.png")