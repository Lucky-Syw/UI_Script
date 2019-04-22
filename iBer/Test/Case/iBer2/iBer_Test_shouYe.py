# -*- coding: utf-8 -*-
'''
Created on 2019年04月22日

@author: Lucky
'''

from Test.module.iBer2.shouYe import iBer_shouYe
import unittest
from Test.logs.logs import logging

class Test_iBer_Test_shouYe(unittest.TestCase):
    driver = None

    def setUp(self):
        #传入driver
        self.iBer = iBer_shouYe(self.driver)

    def tearDown(self):
        pass

    def test_iBer_shouYe(self):
        logging.info("***********************Test Case：test_iBer_shouYe*************************************")
        self.iBer.start_Activitys("com.iBer.iBerAppV2", "com.iBer.iBerAppV2.MainActivity")
        self.iBer.enter_Dangerous_disease()
        self.iBer.back_desktop()

