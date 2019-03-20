# coding=UTF-8
'''
Created on 2017.12.19

@author: Lucky
'''
from appium import webdriver
from Test.logs.logs import logging
import os

class Singleton(object):   
    driver = None 
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            logging.info('-------------------------------')
            #os.system("start /b node D:\\AutoTest\\appium\\Appium\\node.exe lib\\server\\main.js --address 127.0.0.1 --port 4723 --platform-name Android --platform-version 23 --automation-name Appium --log-no-color")
            logging.info('-----------------------init driver----------------------')
            
            config = {
                'platformName':'Android',
                'platformVersion':'4.4',
                'deviceName':'11111',
                'newCommandTimeout':30,
                'automationName':'Appium',
#                 'appPackage':'com.ibroker.iBerHK', 
#                 'appActivity' :'.SplashActivity',
                'udid':'7f4bd69a',
                'appPackage':'com.iBer.iBerAppV2',
                'appActivity' :'com.iBer.iBerAppV2.MainActivity',

                #'autoLaunch':'false'   #appium是否要自动启动或安装APP，默认为ture
                #'newCommandTimeout':'60'  设置未接受到新命令的超时时间，默认60s，说明：如果60s内没有接收到新命令，appium会自动断开，如果我需要很长时间做driver之外的操作，可设置延长接收新命令的超时时间
#                 'unicodeKeyboard':True,
#                 'resetKeyboard':True  
                #'noReset':'True'  #在会话前是否重置APP状态，默认是false
                #'chromeOptions':"{'androidProcess':'com.tencent.mm:tools'}"   #H5页面必不可少的一步
                } 
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',config)
        return cls._instance
                  
class DriverClient(Singleton):
    
    def getDriver(self):
        logging.info('get driver')
        return self.driver
     
       
    
    