# coding=UTF-8
'''
Created on 2017.12.5

@author: SYW
'''

from Test.logs.logs import logging
#from appium import webdriver
from time import sleep
from Test.Common.appium_config import DriverClient
from Test.Common.Driver_Elements import Driver_Elements

class iBer_MyCertification2:
    
    
    def __init__(self): 
        driver = DriverClient().getDriver()
        self.device = Driver_Elements(driver)
        self.device.implicitly_Wait(10)      #测试验证

    def enter_login_page(self):
        logging.info("enter_login_page---------")
        # 欢迎页的滑屏
        sleep(10)
        for i in range(5):
            self.device.swipe_Left()
            sleep(2)
        # 点击"立即体验"按钮
        self.device.touch_tap(556, 1653,500)
        sleep(2)

    def check_enter_login_pag(self):
        if self.device.find_Element(type="name", value="请输入手机号码"):
            logging.info("find login page")
        else:
            logging.error("000000000000000000000000000000000")


