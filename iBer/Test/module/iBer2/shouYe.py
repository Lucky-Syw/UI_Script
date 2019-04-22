#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2019年04月22日

@author: Lucky
'''
from Test.logs.logs import logging
from time import sleep
from Test.Common.Driver_Elements import Driver_Elements


class iBer_shouYe:

    def __init__(self,driver):
        print  "--------------iBer_shouYe-----------------"
        self.driver = driver
        self.device = Driver_Elements(self.driver)
        self.log = logging
        self.device.implicitly_Wait(20)  # 测试验证

    def start_Activitys(self,app_package, app_activity):
        sleep(2)
        self.device.start_Activity(app_package, app_activity)

    def enter_Dangerous_disease(self):
        self.log.info("----------------enter_Dangerous_disease--------------")
        sleep(15)
        self.device.swipe_UP(duration=1000, n=1)
        logging.info("-------------------重疾查询------------------")
        sleep(10)
        self.device.find_xpath_name("重疾查询").click()
        sleep(3)

    def back_desktop(self):
        self.device.back(5)