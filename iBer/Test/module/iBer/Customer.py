# coding=UTF-8
'''
Created on 2017.12.12

@author: Administrator
'''
from Test.logs.logs import logging
from appium import webdriver
from time import sleep
from Test.appium_config import Singleton

class Customer:

#     def __init__(self):
#         logging.info("Test_appium.....setUp")  
#         desired_cups = {}
#         desired_cups['platformName'] = 'Android'
#         desired_cups['platformVersion'] = '7.0'
#         desired_cups['deviceName'] = 'aa'  
#         desired_cups['appPackage']= 'com.ibroker.iBerHK'  
#         desired_cups['appActivity'] = '.SplashActivity'  
#         self.device = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cups) 
#         self.device.implicitly_wait(20)    #全局默认等待最大时间
    def __init__(self): 
        #self.device = appium_config.appium_start()
        self.device = Singleton().getDriver()
        self.device.implicitly_wait(20)
        
    def Enter_Customer_List(self,name,mobile):
        '''select:通訊錄導入 and 手動添加'''
        logging.info("--------Enter_Customer_List-----")
        sleep(5)
        logging.info("点击-------------------‘客户’")
        #self.device.find_element_by_android_uiautomator('text(\"客戶\")').click()
        #self.driver.find_element_by_android_uiautomator('text(\"' + name +'\")')
        self.device.find_element_by_android_uiautomator('textContains(\"列表\")').click()
        logging.info("点击-----------------66666666666")
        sleep(10000)
        
        self.device.find_element_by_name("客戶").click()
        logging.info("通讯录导入")
        self.device.find_element_by_name("通訊錄導入").click()
        XIAZAI = self.device.find_element_by_name("A")
        if not XIAZAI:
            logging.info("查看是否有相机的权限框")
            self.device.find_element_by_name("禁止后不再询问").click()
            self.device.find_element_by_name("始终允许").click()
        logging.info("通讯录导入页面--手动添加成员")
        self.device.find_element_by_name("手動添加").click()
        input_name = self.device.find_element_by_name("請輸入姓名")
        input_name.click()
        input_name.send_keys(name) #lucky_love
        self.device.find_element_by_name("香港 +852").click()
        self.device.find_element_by_name(mobile).click()   #"香港 +852"
        self.device.find_element_by_name("儲存").click()
        logging.info("手动添加成员储存成功，已进入到‘通讯录导入’页面")
        self.device.find_element_by_android_uiautomator("new UiSelector().text('確定(1)')")

            
            
# if __name__ == "__main__":
#     iBer = Customer() 
#     iBer.Enter_Customer_List(name = '124',mobile='123')
#     iBer.Critical_illness()
#     iBer.Enter_Company()
#     iBer.Company_Product('�������Ǳ�����')
#     iBer.AttentionAndShare()
#     iBer.download_annexAndProductFeatures('���d�aƷ��ɫ�D')
#     iBer.download_annexAndProductFeatures('���d����')
#     iBer.Product_Compared()
#     iBer.exit_iBer()  
        
        
        

                
                
        
        
           
    
                
        
        