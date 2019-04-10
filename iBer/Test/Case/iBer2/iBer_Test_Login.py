# -*- coding: utf-8 -*-
'''
Created on 2017年12月5日

@author: Administrator
'''

from Test.module.iBer2.Login import iBer_Login
import unittest


class Test_iBer_Test_Login(unittest.TestCase):
    driver = None

    def setUp(self):
        #传入driver
        self.iBer = iBer_Login(self.driver)

    def tearDown(self):
        pass

    def test_iBer_Login(self):
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ enter case page"
        self.iBer.enter_login_page()
        #self.iBer.check_enter_login_pag()
        # self.iBer.login_information()
        # self.iBer.login()
