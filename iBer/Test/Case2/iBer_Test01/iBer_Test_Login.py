# coding=UTF-8
'''
Created on 2017年12月5日

@author: Administrator
'''

from Test.module.iBer2.Login import iBer_Login
import unittest

class Test_iBer_Test_Login(unittest.TestCase):
#     @classmethod  
#     def setUpClass(cls):
#         super(Test_SYW01, cls).setUpClass()
#         print "1111111"
#         
#     @classmethod
#     def tearDownClass(cls):
#         super(Test_SYW01, cls).tearDownClass()
#         print "222222"
 
    def setUp(self):
        print "set up-----------lucky"
        self.iBer2 = iBer_Login()
         
    def tearDown(self):
        print "teardown222222---Test_iBer_Test_Settings2"
    
    def test_iBer_Login(self):
        '''
        #u(iBer test)
        self.iBer.Setting_MyCertification()
        self.iBer.Setting_MyCertification_MessageFill('實名認證','未填写','lucky','622630199407131707')
        self.iBer.Setting_MyCertification_ConfirmUpload('實名認證')
        #self.iBer.Music_M2()
        '''
        print "enter case page"
        self.iBer2.enter_login_page()
        self.iBer2.check_enter_login_pag()
        self.iBer2.login_information("126011111111")




        