#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2019年04月22日

@author: Lucky
'''

from Common.log.logs import logging
from time import sleep
from Test.Driver_Elements.Driver_Elements import Driver_Elements
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
        sleep(13)  # 等待启动页加载完毕
        self.device.swipe_Left()
        sleep(2)
        # 点击"立即体验"按钮
        self.device.touch_tap(556, 1653, 500)
        el_name=self.device.find_xpath_name("请输入手机号码")
        el_name.click()
        el_name.send_keys("12606666333")
        self.device.back(1)

        #sleep(3)
        for i in range(2):  #模拟器的坑，需要点2次才可以点中
            logging.info("&&&*************************************************&&")
            self.device.touch_tap(257,903,700)
        self.device.adb_input_English(devices_list[0], "11111111")

        # sleep(4)
        # xpath_name = self.device.find_xpath2("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        # xpath_name.click()
        # xpath_name.set_Text("11111111")
        # for i in range(2):  # 模拟器的坑，需要点2次才可以点中
        #self.device.touch_tap(257, 903)
        #os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '11111111'")

        self.device.back(1)  #将输入键盘取消
        el_name2 = self.device.find_xpath_name(u"立即登录")
        if el_name2:
            el_name2.click()   #因click无效果，因此需多使用一次click操作
            el_name2.click()

        #跳过
        sleep(4)
        el_name2 = self.device.find_xpath_name(u"跳过")
        if el_name2:
            el_name2.click()


    def back_to_firstPage(self):
        self.device.back(5)



    def enter_WeiJi_share(self):
        sleep(3)
        self.device.swipe_UP(duration = 1000,n = 1)
        logging.info("-------------------重疾查询------------------")
        sleep(10)
        self.device.find_xpath_name("重疾查询").click()
        sleep(3)
        logging.info("-------------------癌症------------------")
        self.device.find_xpath_name("癌症").click()
        sleep(7)
        logging.info("-------------------ndroid.view.ViewGroup------------------")
        #self.device.touch_ClassNames("android.view.ViewGroup",0)
        a= self.device.find_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup")
        a.click()
        sleep(2)
        self.device.find_xpath_name("WeChat").click()
        self.device.find_xpath_name("微信").click()
        # sleep(2)
        # self.device.touch_Id("com.qiku:id/text1")   微信的ID
        sleep(4)
        self.device.find_xpath_name("％Lucky").click()
        sleep(4)
        #self.device.touch_Id("com.tencent.mm:id / au_")  #分享的ID
        self.device.find_xpath_name("分享").click()
        sleep(2)
        self.device.find_xpath_name("留在微信").click()
        #如下是在微信中的操作
        sleep(2)
        self.device.find_xpath_name("％Lucky").click()
        sleep(3)
        self.device.find_xpath_name("癌症").click()
        sleep(7)

        #执行的是fautotest的代码
        self.device.find_xpath_name("相關資訊").click()
        sleep(3)
        self.device.find_xpath_name("立即諮詢").click()




        self.device.back(7)
        #self.device.startActivity(devices_list[0],"com.iBer.iBerAppV2.MainActivity")



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

