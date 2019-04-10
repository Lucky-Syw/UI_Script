# coding=UTF-8
'''
Created on 2017.12.12

@author: Administrator
'''
from Test.logs.logs import logging
#from appium import webdriver
from time import sleep
from Test.Common.appium_config2 import DriverClient
from Test.Common.Driver_Elements import Driver_Elements

class Product_List:

    def __init__(self):
#         logging.info("Test_appium.....setUp")  
#         desired_cups = {}
#         desired_cups['platformName'] = 'Android'
#         desired_cups['platformVersion'] = '7.0'
#         desired_cups['deviceName'] = 'aa'  
#         desired_cups['appPackage']= 'com.ibroker.iBerHK'  
#         desired_cups['appActivity'] = '.SplashActivity'  
#         self.device = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cups) 
        driver = DriverClient().getDriver()
        self.device = Driver_Elements(driver)
        self.device.implicitly_Wait(20)    #设置全局最大等待时间 
        
    def Enter_ProductList(self):
        logging.info("--------Enter_ProductList-----")
        sleep(2)
        self.device.back(2)
        self.device.touch_Name("產品列表")
        
        
    def Critical_illness(self):
        logging.info("--------Critical_illness--------")
        self.device.find_element_by_name("危疾查詢").click()
        self.device.find_element_by_name("植物人").click()
        sleep(2)
        for i in range(2):
            self.device.back()
    
    def Enter_Company(self):
        '''进入到公司'''
        logging.info("--------Enter_Company--------")
        sleep(2)
        self.device.tap([(35,628),(326,895)],100)
        
    def Company_Product(self,name="「多重智倍保」"):
        '''进入到产品详情页
        name：「多重智倍保」'''
        logging.info("--------Company_Product--------")
        sleep(2)
        self.device.find_element_by_name(name).click()
        logging.info('已经点击 多重智倍保')
        self.device.find_element_by_name("下載")
        for i in range(3):
            logging.info("滑动产品详情页查看是否闪退")
            self.device.swipe(524,1581,591,365)
            sleep(1)
        
    def AttentionAndShare(self):
        '''关注和分享'''
        logging.info("--------AttentionAndShare--------")
        sleep(3)
        logging.info("已点击关注")
        self.device.tap([(828,78),(954,204)],100)   
        logging.info("已点击分享")
        self.device.tap([(954,78),(1080,204)],100)   
        logging.info("ͨ选择微信分享")
        self.device.find_element_by_name("Wechat").click()   
        self.device.find_element_by_id("com.tencent.mm:id/jz").click()
        logging.info("进入到 传送确认页面")
        self.device.find_element_by_id("com.tencent.mm:id/akt").click()
        self.device.find_element_by_name("返回iBer").click()
        logging.info("产品详情页已经分享至微信完成")
        
    
    def download_annexAndProductFeatures(self,name):
        '''name :下載附件  和 下載產品特色圖'''
        logging.info("--------------download_annexAndProductFeatures----------")
        logging.info("%s"%name)
        self.device.find_element_by_name("下載").click()
        select_name = self.device.find_element_by_name(name)
        if select_name and name == '下載產品特色圖':
            select_name.click()
            #sleep(2)
            XIAZAI = self.device.find_element_by_name("下載")
            if not XIAZAI:
                logging.info("查看是否有相机的权限框")
                self.device.find_element_by_name("禁止后不再询问").click()
                self.device.find_element_by_name("始终允许").click()
        elif select_name and name =="下載附件":
            select_name.click()
            self.device.find_element_by_name("「多重智倍保」.pdf") 
            if self.device.find_element_by_name("下載"):
                self.device.find_element_by_name("下載").click()
                sleep(4)
                if self.device.find_element_by_name("打開"):
                    logging.info("附件下载并打开成功")
                    self.device.back()
            elif self.device.find_element_by_name("打開"):
                logging.info("附件下载并打开成功")
                self.device.back()
            else:
                logging.error("付建新下载失败")
                
        
    def Product_Compared(self):
        logging.info("--------------Product_Compared----------")
        logging.info("产品对比")
        self.device.find_element_by_name("對比").click()
        if self.device.find_element_by_name("選擇產品對比"):
            logging.info("进入到选择产品对比页面")
#         for i in range(5):
#             sleep(2)
#             if self.device.find_element_by_name("「多重智倍保」"):
#                 logging.info("选择产品对比加载完成")
#                 break
        #self.device.find_element_by_name("「多重智倍保」")
        self.device.find_element_by_name("「守護168」 危疾保障計劃").click()
        self.device.find_element_by_name("對比").click()
        if self.device.find_element_by_name("產品對比"):
            logging.info("产品对比完成")
    
    def exit_iBer(self):
        self.device.close_app()
            
            
# if __name__ == "__main__":
#     iBer = Product_List() 
#     iBer.Enter_ProductList()
#     iBer.Critical_illness()
#     iBer.Enter_Company()
#     iBer.Company_Product('「多重智倍保」')
#     iBer.AttentionAndShare()
#     iBer.download_annexAndProductFeatures('下載產品特色圖')
#     iBer.download_annexAndProductFeatures('下載附件')
#     iBer.Product_Compared()
#     iBer.exit_iBer()  
        
        
        

                
                
        
        
           
    
                
        
        