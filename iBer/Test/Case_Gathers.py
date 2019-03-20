# coding=UTF-8

'''
Created on 2017年6月13日
@author: SYW
用途：集成所有要运行的case，一次执行多条不同case下的不同case条数
'''

#from Test.case.iBer_Test01.iBer_Test_Settings import Test_iBer_Test_Settings
#from Test.case.iBer_Test01.Product_List import Test_iBer_Product_List
from Test.Case2.iBer_Test01.iBer_Test_Login import Test_iBer_Test_Login



import unittest

suite = unittest.TestSuite()
for tmp in range(1):    #可修改1代表的case运行的次数，
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_Settings))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Test_Login))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_iBer_Product_List))
