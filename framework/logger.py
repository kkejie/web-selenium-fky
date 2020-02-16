# coding=utf-8
import logging
import time
import os.path

class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将文件存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler ，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        # log_path = os.path.dirname(os.getcwd())+'/logs/'      # 项目根目录下/logs , 保存日志
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        # 如果case组织结构式/testsuit/featuremodel/xxx.py,那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.logs'
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger