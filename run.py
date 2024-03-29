# -*- coding:utf-8 -*-
# @Time   :2019/6/4 14:44
# @File   :run.py
# @Author :Vsonli
import unittest
from librarys.HTMLTestRunnerNew import HTMLTestRunner
from testcases.testcase import RegisterTestCase
from common.constant import *
from common.myConf import conf

path = os.path.join(REPORT_DIR,'report.html')
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RegisterTestCase))


with open(path,'wb') as f:
    '''写入的文件名，写入的等级（2是最高的，0，1，2），报告名称，报告相关描述，测试者名称'''
    runner = HTMLTestRunner(
                            stream=f,
                            verbosity=int(conf.get('runs','verbosity')),
                            title=conf.get('runs','title'),
                            description=conf.get('runs','description'),
                            tester=conf.get('runs','tester')
                            )
    runner.run(suite)