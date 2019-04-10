# coding=UTF-8
'''
Created on 2018.1.3
@author: Lucky
'''

from Test.Common.appium_config2 import DriverClient
from Test.Common.Driver_Elements import Driver_Elements
from Test.logs.logs import logging
from time import sleep
from selenium import webdriver

class test_Common:
    
    def __init__(self): 
        driver = DriverClient().getDriver()
        self.device = Driver_Elements(driver)
       
        
        
    def Setting_MyCertification2(self):
        logging.info("start test iBer my certification")
            #self.device.start_activity('com.ibroker.iBerHK', '.SplashActivity')
        #sleep(5)
        #self.device.touchToNameContains("iiii")
        #self.device.touch_ClassNames('android.widget.TextView',1)
        
        #      self.device.back(1)
        #self.device.find_Toast('再按一次退出iBer')
        
#         self.device.touch_tap(265,451)
#         sleep(3)
#         self.device.touch_tap(178,768)
        #self.device.scroll("「都市三保」醫療危疾保障計劃", "「充裕未來」計劃 2")
#         self.device.back(5)
#         self.device.drag_and_drop('优酷','鑫聚财')
        #self.device.press('產品列表')
        #self.device.long_press_keycode('82')  
        
        #self.device.set_text("输入收件人",'10086')
        
        
#         a = self.device.get_Toast('再按一次退出iBer')
#         print a
#         self.device.take_Shot(u'测试')
#         logging.info("product list test finishing*****************")


# H5        self.driver.find_element_by_name('產品列表').click()
#         print '1111111111111111111111'
#         self.driver.find_element_by_name('危疾查詢').click()
#         print '22222222222222222222222222222'
#         sleep(16)
#         self.driver.find_element_by_name('植物人').click()
#         sleep(3)
#         print '333333333333333333333333333333'
#         webview = self.driver.contexts   
#         print webview
#         for context in webview:
#             print '4444444444444444444444'
#             if 'WEBVIEW' in context:
#                 print '5555555555555555555555'
#                 self.driver.switch_to.context(context)
#                 break
#         print 'jhjhjhjhjhjh'
#         self.driver.find_element_by_link_text("關聯的保險產品").click()
#         
        
        
#         self.driver.find_element_by_name('產品列表').click()
       
        self.device.touch_Name("產品列表")
#         self.driver.find_element_by_name('危疾查詢').click()
        print '1111111111111111111111'
        self.device.touch_Name("危疾查詢")
        print '22222222222222222222222222222'
#         sleep(10)
#         self.device._find_element_by_swipe('up','name','昏迷')

        logging.info("product list test finishing*****************")
        
if __name__ == "__main__":
    a = test_Common()
    a.Setting_MyCertification2()
