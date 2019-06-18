# -*- coding: utf-8 -*-
'''
Created on 2019年04月22日

@author: Lucky
'''

from Test.module.iBer.iBerQuan import iBer_Quan
import unittest
from Common.log.logs import logging

class Test_iBer_Test_Quan(unittest.TestCase):
    driver = None

    def setUp(self):
        #传入driver
        self.iBer = iBer_Quan(self.driver)

    def tearDown(self):
        self.iBer.back_to_firstPage()

    def test_iBer_Quan(self):
        logging.info("***********************Test Case：test_iBer_Quan*************************************")
        self.iBer.start_Activitys("com.iBer.iBerAppV2", "com.iBer.iBerAppV2.MainActivity")
        self.iBer.enter_quan()
        #self.iBer.back_desktop()

