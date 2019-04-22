#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2017.12.5

@author: SYW
'''
from Test.logs.logs import logging
from time import sleep
from Test.Common.Driver_Elements import Driver_Elements


class iBer_Quan:

    def __init__(self,driver):
        print  "--------------enter_quan-----------------"
        self.driver = driver
        self.device = Driver_Elements(self.driver)
        self.log = logging
        self.device.implicitly_Wait(20)  # 测试验证

    def start_Activitys(self,app_package, app_activity):
        sleep(2)
        self.device.start_Activity(app_package, app_activity)

    def enter_quan(self):
        self.log.info("----------------enter_quan--------------")
        sleep(15)
        self.device.find_xpath_name("iBer圈").click()
        sleep(5)
        el_name2 = self.device.find_xpath_name(u"跳过")
        if el_name2:
            el_name2.click()
        sleep(3)
        self.device.find_xpath_name("海报").click()

    def back_desktop(self):
        self.device.back(5)