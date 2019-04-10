# -*- coding: utf-8 -*-
'''
Created on 2017.12.5

@author: SYW
'''

from Test.logs.logs import logging
from time import sleep
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

       #-------------------------测试代码---------------------------------------
        # 测试keycode的方法使用
        #self.device.press_keycode(3)

        #测试录制视频操作的方法使用
        # self.device.start_screen_record(devices_list[0],12,"lucky4","/Users/lucky/Desktop/Auto/UI_Script/iBer/screenShots")
        # self.device.clean_mp4_file(devices_list[0])


        #xpath的方法用法
        # xpath_name = self.device.find_xpath2(
        #     "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText")
        # xpath_name.click()
        # xpath_name.set_text("11111111")
