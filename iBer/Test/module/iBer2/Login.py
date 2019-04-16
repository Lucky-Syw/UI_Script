#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2017.12.5

@author: SYW
'''

from Test.logs.logs import logging
#from appium import webdriver
from time import sleep
#from Test.Common.appium_config import DriverClient
from Test.Common.Driver_Elements import Driver_Elements
import os,yaml

'''
在module中使用start_screen_record2方法，则需要使用如下此段获取到设备udid
'''
path = os.getcwd()
with open(path+"/desired_caps.yaml","r") as file:
    data = yaml.load(file)

devices_list = data["devices_list"]
phone_list = data["phone"]

class iBer_Login:

    def __init__(self,driver):
        print  "--------------iBer_Login-----------------"
        self.driver = driver
        self.device = Driver_Elements(self.driver)
        self.device.implicitly_Wait(20)  # 测试验证



    def enter_login_page(self):
        logging.info("enter_login_page-----------------99999-")
        #self.device.isExist_Popwindow(self.driver)
        sleep(8)  # 等待启动页加载完毕
        self.device.swipe_Left()
        sleep(2)
        # 点击"立即体验"按钮
        self.device.touch_tap(556, 1653, 500)
        el_name=self.device.find_xpath_name("请输入手机号码")
        el_name.click()
        el_name.send_keys("12606666333")


        sleep(3)
        for i in range(2):  #模拟器的坑，需要点2次才可以点中
            logging.info("&&&*************************************************&&")
            self.device.touch_tap(257,903,700)

        sleep(4)
        xpath_name = self.device.find_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        xpath_name.click()
        xpath_name.send_keys("11111111")


        el_name2 = self.device.find_xpath_name(u"立即登录")
        if el_name2:
            el_name2.click()   #因click无效果，因此需多使用一次click操作
            el_name2.click()

        #跳过
        sleep(3)
        el_name2 = self.device.find_xpath_name(u"跳过")
        if el_name2:
            el_name2.click()
            el_name2.click()


    def login_information(self):
        logging.info("输入登录信息")
        #self.device.set_text1(u"请输入手机号码",mobile)
        #self.device.set_text1("classname","android.widget.EditText",mobile)
        #self.device.set_text("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText",mobile)
        #self.device.class_1("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText",mobile)
        #self.device.set_text("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText",password)
        self.device.touch_tap(766,1750)
        # self.device.set_text2(password)
        #self.device.touch_Name(u"WeChat")

    def login(self):
        self.device.touch_tap(191,1663)

