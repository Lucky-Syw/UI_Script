# -*- coding: utf-8 -*-
'''
Created on 2019年04月22日

@author: Lucky
'''

from Test.module.iBer.Login import iBer_Login
import unittest
from Common.log.logs import logging


class Test_iBer_Test_Login(unittest.TestCase):
    driver = None

    def setUp(self):
        #传入driver
        self.iBer = iBer_Login(self.driver)

    def tearDown(self):
        self.iBer.back_to_firstPage()

    def test_iBer_Login(self):
        logging.info("***********************Test Case：test_iBer_Login*************************************")
        self.iBer.enter_login_page()
        #self.iBer.back_desktop()
        #self.iBer.enter_WeiJi_share()
        #self.iBer.check_enter_login_pag()
        # self.iBer.login_information()
        # self.iBer.login()
