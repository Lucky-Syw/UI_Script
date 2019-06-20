#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2017.12.5

@author: SYW
'''
from Common.log.logs import logging
from time import sleep
from Test.Driver_Elements.Driver_Elements import Driver_Elements
from Common.func_instructions import instructions

class iBer_Quan:

    def __init__(self,driver):
        self.driver = driver
        self.device = Driver_Elements(self.driver)
        self.log = logging
        self.device.implicitly_Wait(20)  # 测试验证

    @instructions.info("启动APP")
    def start_Activitys(self,app_package, app_activity):
        sleep(2)
        self.device.start_Activity(app_package, app_activity)

    @instructions.info("进入到圈子页面")
    def enter_quan(self):
        sleep(15)
        self.device.find_xpath_name("iBer圈").click()
        sleep(5)
        el_name2 = self.device.find_xpath_name(u"跳过")
        if el_name2:
            el_name2.click()
        sleep(3)
        self.log.info("点击更多，进入最新资讯列表，点击第一条资讯进入")
        self.device.find_xpath_name("更多").click()
        xpath_information = self.device.find_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]")
        xpath_information.click()
        sleep(5)
        self.log.info("编辑资讯感想")
        self.device.touch_ToContentDesc("写感想")
        sleep(2)
        self.device.element_set_text("name","写下您的分享心得或者浏览感想，感想支持分享","lucky Feel_content")
        sleep(2)
        self.device.touch_Name("储存")
        self.log.info("编辑资讯感想")
        sleep(5)
        self.device.touch_ToContentDesc("立即分享")
        sleep(5)

    def back_to_firstPage(self):
        self.device.back(5)