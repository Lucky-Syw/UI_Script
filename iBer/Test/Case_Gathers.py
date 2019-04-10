# coding=UTF-8

'''
Created on 2017年6月13日
@author: SYW
用途：集成所有要运行的case，一次执行多条不同case下的不同case条数
'''

import unittest
from Test.Case.iBer2.iBer_Test_Login import Test_iBer_Test_Login

class Case_ganthers:

    def __init__(self,driver):
       self.b = driver


    def suites(self):
        suite = unittest.TestSuite()
        '''可修改1代表的case运行的次数'''

        for tmp in range(1):

            Test_iBer_Test_Login.driver = self.b
            #loadTestsFromTestCase只可添加类，因此需要进行如上的赋值操作
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_Login))
            #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_Login))
        return suite