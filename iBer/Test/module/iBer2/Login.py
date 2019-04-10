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

class iBer_Login:

    def __init__(self,driver):
        print  "--------------iBer_Login-----------------"
        self.device = Driver_Elements(driver)
        self.device.implicitly_Wait(10)  # 测试验证

    def enter_login_page(self):
        logging.info("enter_login_page-----------------99999-")

       #-------------------------测试代码----开始-----------------------------------

        #self.device.press_keycode(3)
        # self.device.start_screen_record2(devices_list[0],12,"lucky4","/Users/lucky/Desktop/Auto/UI_Script/iBer/screenShots")
        # self.device.clean_mp4_file(devices_list[0])
        self.device.tap_screen_center()
        logging.info("&&&&&&&&&&***************************&&&&&&&&&&&&&&&&&&&")
        # -----------------------测试代码------结束---------------------------------

        # 欢迎页的滑屏
        sleep(12)
        # self.device.take_screenShot("%s" %self.device)
        # for i in range(5):
        #     self.device.swipe_Left()
        #     sleep(2)

        self.device.swipe_Left()
        sleep(2)
        # 点击"立即体验"按钮
        self.device.touch_tap(556, 1653, 500)
        self.device.hide_Keyboard()
        el_name=self.device.find_xpath_name("请输入手机号码")
        if el_name:
            el_name.click()
            el_name.send_keys("12606666333")
        self.device.back(1)

        xpath_name = self.device.find_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        xpath_name.click()
        xpath_name.send_keys("11111111")
        sleep(2)
        self.device.back(1)
        sleep(2)
        el_name2 = self.device.find_xpath_name(u"立即登录")
        if el_name2:
            logging.error("000000000000000000000000000000000")
            self.device.long_press(el_name2)

    def check_enter_login_pag(self):
        sleep(15)
        find_text = self.device.find_Element(type="name", value= "请输入手机号码")
        if find_text:
            logging.info("find login page")
        else:
            logging.error("000000000000000000000000000000000")
            assert False


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

