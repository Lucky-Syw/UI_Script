# # -*- coding: utf-8 -*-
# '''
# Created on 2017.12.5
#
# @author: SYW
# '''
#
# from Test.logs.logs import logging
# from time import sleep
# from Test.Common.Driver_Elements import Driver_Elements
# import os,yaml
#
# '''
# 在module中使用start_screen_record2方法，则需要使用如下此段获取到设备udid
# '''
# path = os.getcwd()
# with open(path+"/desired_caps.yaml","r") as file:
#     data = yaml.load(file)
#
# devices_list = data["devices_list"]
#
# class iBer_Login:
#
#     def __init__(self,driver):
#         print  "--------------iBer_Login-----------------"
#         self.device = Driver_Elements(driver)
#         self.device.implicitly_Wait(10)  # 测试验证
#
#     def enter_login_page(self):
#         logging.info("enter_login_page-----------------99999-")
a = ['1','2']

for i in range(len(a)):
    print i
    print a[i]

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

        # 用adb命令输入密码
        # for i in range(2):  # 模拟器的坑，需要点2次才可以点中
        #     self.device.touch_tap(257, 903)
        # os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '11111111'")
        # sleep(2)

        #用adb命令输入表情
        #self.device.adb_input_UnicodeChars(devices_list[0],"128568,32,67,97,116")

        #判断权限弹框
        # class iBer_Login:
        #
        #     def __init__(self, driver):
        #         print  "--------------iBer_Login-----------------"
        #         self.driver = driver
        #         self.device = Driver_Elements(self.driver)
        #         self.device.implicitly_Wait(20)  # 测试验证
        #
        #     def enter_login_page(self):
        #         logging.info("enter_login_page-----------------99999-")
        #         self.device.isExist_Popwindow(self.driver)  要传driver

