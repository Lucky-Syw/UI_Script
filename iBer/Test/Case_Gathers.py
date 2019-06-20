# coding=UTF-8

'''
Created on 2019年04月22日
@author: Lucky
用途：集成所有要运行的case，一次执行多条不同case下的不同case条数
'''

import unittest
from Test.Case.iBer.iBer_Test_Login import Test_iBer_Test_Login
# from Test.Case.iBer.iBer_Test_shouYe import Test_iBer_Test_shouYe
from Test.Case.iBer.iBer_Test_Quan import Test_iBer_Test_Quan

fun = {
    "login":Test_iBer_Test_Login,
    "quan":Test_iBer_Test_Quan
}

class Case_ganthers:

    def __init__(self,driver):
       self.b = driver

    def suites(self):
        suite = unittest.TestSuite()
        for value in fun.values():
            value.driver = self.b

        ''' 登录的操作只执行一次'''
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_Login))

        for tmp in range(1):
            '''修改循环数代表着case运行的次数'''
            #loadTestsFromTestCase只可添加类，因此需要进行如上的赋值操作
            #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_shouYe))
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_Quan))
        return suite