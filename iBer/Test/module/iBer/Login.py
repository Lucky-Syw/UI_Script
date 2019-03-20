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

class iBer_Login:

    def __init__(self): 
        driver = DriverClient().getDriver()
        self.device = Driver_Elements(driver)
        self.device.implicitly_Wait(10)      #测试验证

    sleep(20)
    def enter_login_page(self):
        print "module---------"
        # 欢迎页的滑屏
        for i in range(5):
            self.device.swipe(1020, 1036, 51, 1036)
            sleep(2)
        # 点击"立即体验"按钮
        self.device.tap([(556, 1653), (556, 1653), (556, 556)], 500)
        sleep(2)

    def check_enter_login_pag(self):
        if self.device.find_Element(type ="name",value="请输入手机号码"):
            logging.info("find login page")
        else:
            logging.error("000000000000000000000000000000000")


        
    def Setting_MyCertification2(self):
        
        logging.info("start test iBer my certification")
        '''我的认证'''
        self.device.test_h5()
        logging.info("product list test finishing*****************")
        
    def Setting_MyCertification(self):
        logging.info("start test iBer my certification")
        
        
        
        self.device.test_h5()
        
        sleep(2000)
        
        
        
        
        
        '''我的认证'''
        sleep(5)
        self.device.touch_ClassName("android.widget.ImageView")
        #self.device.touch_Name("我的認證")
        
        a = self.device.find_Element(type = 'name',value="我的認證")
        a.click()
        a = self.device.find_Element(type = 'name',value="我")
        if a == False:
            logging.info( '888888888888888888999999999999999')
            
            
        self.Setting_MyCertification_MessageFill(Cname='實名認證',default_Sname='未填寫',default_Snumber='請輸入證件號碼',Sname='lucky',Snumber='622630199407131707')
        #上传正面照片 
        self.device.touch_Name("上傳證件正面照片")
        #sleep(2) 
        self.device.touch_Name("拍照上傳")
        #判断相机权限获取弹框提示
        #sleep(3)
        camera_button = self.device.find_element_by_id("com.huawei.camera:id/shutter_button")
        if not camera_button:
            always_allow = self.device.find_Name("始终允许")
            self.device.touch_Name("禁止后不再询问")
            always_allow.click()
            if always_allow:
                self.device.touch_Name("禁止后不再询问")
                always_allow.click()
        camera_button.click()
        #sleep(1)
        self.device.touch_Id("com.huawei.camera:id/btn_review_confirm")
        #上传背面照片
        self.device.touch_Name("上傳證件背面照片")
        #sleep(2) 
        self.device.touch_Name("拍照上傳")
        #判断相机权限获取弹框提示
        #sleep(3)
        camera_button = self.device.find_Id("com.huawei.camera:id/shutter_button")
        if not camera_button:
            always_allow = self.device.find_Name("始终允许")
            self.device.touch_Name("禁止后不再询问")
            always_allow.click()
            if always_allow:
                self.device.touch_Name("禁止后不再询问")
                always_allow.click()
        camera_button.click()
        #sleep(1)
        self.device.touch_Id("com.huawei.camera:id/btn_review_confirm")
        #sleep(3)
        self.Setting_MyCertification_ConfirmUpload('實名認證')
    
    def Setting_MyCertification_MessageFill(self,Cname,default_Sname,default_Snumber,Sname,Snumber):
        
        '''方法说明：点击认证名称进入，直到操作到上传图片的上一步
        Cname:认证的名称
        default_Sname:认证的默认提示名称
        default_Snumber:输入的默认提示认证账号名称
        Sname:输入的认证名称
        Snumber:输入的认证账号
        '''
        logging.info("----------开始***%s---------"%Cname)
        self.device.touch_Name("%s"%Cname)   #實名認證
#         logging.info("此处有问题，还需在调整22222222222222222222222222222222")
#         if self.device.find_element_by_name("開始實名認證，讓客戶放心信任，讓溝通更加順暢。"):
#             self.device.find_element_by_name("確定").click() 
        sleep(3)
        logging.info('***************************************')
        if self.device.find_Name("重新認證"):
            self.device.touch_Name("重新認證")
        sleep(1)
        unfilled = self.device.find_Name("%s"%default_Sname) #未填写
        if not unfilled:
            self.device.back(2)
        unfilled.click()
        unfilled.send_keys("%s"%Sname)  #lucky
        sleep(1)
        a = self.device.find_Name("未填寫")
        a.click()
        a.send_keys("777777")
        ID_number = self.device.find_Name("%s"%default_Snumber) #請輸入證件號碼
        ID_number.click()
        ID_number.send_keys("%s"%Snumber)   #622630199407131707
        self.device.swipe(588,773,588,773)   #随便点击一个地方取消输入框
        
    def Setting_MyCertification_ConfirmUpload(self,Cname):
        '''
                    方法说明：确认上传方法的封装
        Cname:认证的名称
        '''
        logging.info("上传认证信息！！！！！！")
        self.device.touch_Name("確認上傳")   #确认上传
        sleep(4)
        upload_successfully = self.device.find_Name("上傳成功")
        logging.info("判断是否上传成功！！！！")
        sleep(3)
        if upload_successfully:
            self.device.swipe(951,765,951,765)    #上传成功后的弹框点击x
        logging.info("----------结束***%s---------"%Cname)
        

if __name__ == "__main__":
    a = iBer_MyCertification()
    a.Setting_MyCertification2()
            