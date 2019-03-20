# coding=UTF-8
'''
Created on 2018.1.3
@author: Lucky
'''

# from Test.Common.appium_config import DriverClient
# from Test.Common.Driver_Elements import Driver_Elements
from Test.logs.logs import logging
from time import sleep
from appium import webdriver
import unittest

class test_Common(unittest.TestCase):
    def setUp(self):
        config = {
                'platformName':'Android',
                'platformVersion':'4.4',
                'deviceName':'11111',
                'newCommandTimeout':30,
                'automationName':'Appium',
                'appPackage':'com.ibroker.iBerHK', 
                'appActivity' :'.SplashActivity',
                'fullReset':'false',
                'unicodeKeyboard':'True',
                'resetKeyboard':'True',
                'fastReset':'false',
                'chromeOptions':"{'androidProcess':'com.ibroker.iBerHK:tools'}"
                } 
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',config)
        self.driver.implicitly_wait(20)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_Setting_MyCertification2(self):
    
        logging.info("start test iBer my certification")
        sleep(3)
        print '0000000000000000000000000'
        self.driver.find_element_by_name('產品列表').click()
        print '1111111111111111111111'
        self.driver.find_element_by_name('危疾查詢').click()
        print '22222222222222222222222222222'
        sleep(6)
        self.driver.find_element_by_name('植物人').click()
        sleep(3)
        print '333333333333333333333333333333'
        print self.driver.current_context
        print self.driver.page_source
        self.driver.switch_to.context('WEBVIEW_com.ibroker.iBerHK:tools')
        self.driver.find_element_by_name("關聯的保險產品").click()
        
        logging.info("product list test finishing*****************")
        
if __name__ == "__main__":
    unittest.main()
