# -*- coding:utf-8 -*-
# @Time   :2019/6/4 14:40
# @File   :myConf.py
# @Author :Vsonli
'''把其他py文件的路径解决好'''


import configparser
from common.constant import *

class confingObj(configparser.ConfigParser):
    path1 = os.path.abspath(os.path.dirname(os.getcwd()))+'\\'
    def __init__(self):
        super().__init__()
        # self.read(self.path1+'project_structure_18\conf\my.conf',encoding='utf8')
        self.read(os.path.join(CONF_DIR,'my.conf'), encoding='utf8')
conf = confingObj()