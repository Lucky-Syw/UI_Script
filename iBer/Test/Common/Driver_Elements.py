# coding=UTF-8
'''
Created on 2018.1.3
@author: Lucky
'''
from Test.logs.logs import logging
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,\
    expected_conditions
import time,os
from appium.webdriver.common.touch_action import TouchAction


class Driver_Elements:
    
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(20)

    def implicitly_Wait(self,time=20):
        logging.info(u"最大等待时长 %s" %time)
        self.driver.implicitly_wait(time)
       
    def touch_Id(self,id):  #通过 id点击元素
        '''
        method explain:通过id点击元素
        parameter explain: 【id】 uiautomator解析出的resource_id值
        Usage:
            device.touch_Id('id/product_id')
        '''
        logging.info("点击id-------'%s'【开始】"%(id))
        try:
            self.driver.find_element_by_id(id).click()
            logging.info("点击id-------'%s'【成功】"%(id))
        except:
            logging.warn("except------------touch_Id--%s【异常】"%(id))
            self.take_screenShot("not_%s"%id)
            assert 'assert touch_Id'
      
    def find_Element(self,type,value):   #查找元素
        '''
        method explain:查找某个元素
        parameter explain: 【type】 取值的类型包括：id\name\class_name...   【value】根据type的类型给值
        Usage:
            device.find_Element('name',"我的認證")
        '''
        logging.info("执行--------find_Element-------方法")
        logging.info("查找--------%s,%s-------【开始】"%(type,value))
        try:
            if type == 'id':
                try:
                    return self.driver.find_element(By.ID,value)
                except Exception,e:
                    logging.info("未找到------%s,%s---【失败】"%(type,value))
                    return False
            elif type == 'name':
                try:
                    return self.driver.find_element(By.NAME,value)
                except Exception,e:
                    logging.info("未找到-------%s,%s---【失败】"%(type,value))
                    return False
        except:
            logging.warn("此处已抛异常---------------find_Element【异常】")
            self.take_screenShot("find_Element")
            assert 'find_Element'


    def click(self):   #查找到元素进行点击
        '''
        method explain:查找某个元素
        parameter explain: 【type】 取值的类型   【value】根据type的类型给值
        Undertake method:device.find_Element(type,value)
        Usage:
            name_value == device.find_Element(type = 'name',value="我的認證")
            name_value.click()
        '''
        self.find_Element(type,self.value).click()
        
    def touch_Name(self,name):   #通过 name 点击元素
        '''
        method explain:通过name点击元素
        parameter explain: 【name】 uiautomator解析出的text值
        Usage:
            device.touch_Name('测试')
        '''
        logging.info("点击name---------%s【开始】"%(name))
        try:
            self.driver.find_element_by_name(name).click()
            logging.info("点击name---------%s【成功】"%(name))
        except:
            logging.warn("except------------touch_Name--%s【异常】"%(name))
            self.take_screenShot("not_%s"%name)
            assert 'assert touch_Name'

    def back(self,times):   #返回，times给定返回的次数
        '''
        method explain:点击back键返回
        parameter explain: 【times】 返回的次数
        Usage:
            device.back(2)
        '''
        logging.info("按返回键  %s次" %(times))
        for time in range(times):
            self.driver.back()
    
    def touch_ToNameContains(self,ContainsName):  #点击含有指定子串的字符串
        '''
        method explain:点击含有指定子串的字符串，比如：需点击‘产品列表’，运用此方法给值‘产品列’即可点击到 产品列表
        parameter explain: 【ContainsName】 字符串的子串
        Usage:
            device.touch_ToNameContains('产品列')
        '''
        logging.info("点击包含子串 --------'%s'的字符串【开始】" %(ContainsName))
        try:
            self.driver.find_element_by_android_uiautomator('textContains(\"'+ContainsName+'\")').click()
            logging.info("点击包含子串 --------'%s'的字符串【成功】" %(ContainsName))
        except:
            logging.warn("except-------未找到包含子串-'%s'的字符串【异常】"%(ContainsName))
            self.take_screenShot("not_%s"%ContainsName)
            assert 'assert touch_ToNameContains'
         
    def touch_ToContentDesc(self,content_desc): #通过content-desc点击
        '''
        method explain:通过ContentDesc点击元素
        parameter explain:【content_desc】content_desc的值
        Usage:
            device.touch_ToContentDesc('设置')
        '''
        logging.info('点击ContentDesc-----------%s【开始】'%content_desc)
        try:
            self.driver.find_element_by_android_uiautomator('description(\"'+content_desc+'\")').click()
            logging.info('点击ContentDesc-----------%s【成功】'%content_desc)
        except:
            logging.warn("except---------ContentDesc异常-%s【异常】"%(content_desc))
            self.take_screenShot("not_%s"%content_desc)
            assert 'assert touch_ToContentDesc' 
                
    def touch_ClassName(self,Class):  #通过Class点击元素
        '''
        method explain:通过Class点击元素
        parameter explain: 【Class】 uiautomator解析的Class
        Usage:
            device.touch_ClassName('android.widget.TextView')
        '''
        logging.info("点击Class----------'%s'【开始】"%(Class)) 
        try:
            self.driver.find_element_by_class_name(Class).click()
            logging.info("点击Class----------'%s'【成功】"%(Class)) 
        except:
            logging.warn("except------------点击touch_ClassName--%s【异常】"%(Class))
            self.take_screenShot("not_%s"%Class)
            assert 'assert touch_ClassName'
    
    def touch_ClassNames(self,Class,index):  #通过查找所有相同的Class，根据返回的下标进行点击
        '''
        method explain:通过查找所有相同的Class，根据返回的对应元素下标进行点击
        parameter explain: 【Class】 uiautomator解析的Class，【index】需要点击的元素下标
        Usage:
            device.touch_ClassNames('android.widget.TextView',2)
        '''
        logging.info("通过下标点击Class--------'%s'【开始】"%(Class))
        try:
            find_list_Class = self.driver.find_elements_by_class_name(Class)
            #print find_list_Class   打印所有的Class
            for i in range(len(find_list_Class)):
                if i == index:
                    logging.info( '给定的下标为*******'+str(index)+'*******')
                    find_list_Class[index].click()
                    break
                continue
            logging.info("通过下标点击Class--------'%s'【成功】"%(Class))
        except:
            logging.warn("except------------点击touch_ClassNames--%s【异常】"%(Class))
            self.take_screenShot("not_%s"%Class)
            assert 'assert touch_ClassNames' 

    def find_Toast(self,message,timeout=5,poll_frequency = 0.5):  #查找toast值
        '''
        method explain:查找toast的值
        parameter explain：【text】给定的toast值
        Usage:
            device.find_Toast('再按一次退出iBer')
        '''
        logging.info("获取toast值--------'%s'【开始】" %message)
        try:
            toast_loc = ("xpath",".//*[contains(@text,'%s')]" %message)
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.presence_of_element_located(toast_loc))
            logging.info("查找到toast---------'%s'【成功】"%message)
            return True
        except:
            logging.error("except----未查找到toast--'%s'【异常】"%message)
            return False
            
    def find_Toast2(self,message):  #查找toast值
        '''
        method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
        parameter explain：【text】查找的toast值
        Usage:
            device.find_Toast2('再按一次退出iBer')
        '''
        logging.info("查找toast值-----------%s【开始】" %(message))
        try:
            message = '//*[@text=\'{}\']'.format(message)
            WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
            logging.info("查找到toast---------%s【成功】"%message)
            return True
        except:
            logging.error("except------未查找到toast--%s【异常】"%message)
            return False
        
    def get_Toast(self,message):  #查找toast值
        '''
        method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
        parameter explain：【text】查找的toast值
        Usage:
            device.get_Toast('再按一次退出iBer')
        '''
        logging.info("查找toast值-----------%s【开始】" %(message))
        try:
            message = '//*[@text=\'{}\']'.format(message)
            ele = WebDriverWait(self.driver,5,0.5).until(expected_conditions.presence_of_element_located((By.XPATH,message)))
            return ele.get_attribute("text")
            logging.info("查找到toast----------%s【成功】"%message)
        except:
            logging.error("except-------未查找到toast--%s【异常】"%message)
            return False

    def touch_tap(self,x,y,duration=100):   #点击相对坐标  ,x1,x2,y1,y2
        '''
        method explain:点击坐标
        parameter explain：【x,y】坐标值,【duration】:给的值决定了点击的速度
        Usage:
            device.touch_coordinate(277,431)
        '''
        logging.info("点击坐标------------%s,%s【开始】"%(x,y))
        screen_width = self.driver.get_window_size()['width']  #获取当前屏幕的宽
        screen_height = self.driver.get_window_size()['height']   #获取当前屏幕的高
        a =(float(x)/screen_width)*screen_width
        x1 = int(a)
        b = (float(y)/screen_height)*screen_height
        y1 = int(b)
        self.driver.tap([(x1,y1),(x1,y1)],duration)
        logging.info("点击坐标------------%s,%s【结束】"%(x,y))
        
    def scroll(self,origin_elN,destination_elN):  #未完成
        '''
        method explain:从元素origin_el滚动至元素destination_el
        parameter explain：【origin_el】起始元素,【destination_el】:结束元素
        Usage:
            device.scroll('开始','结束')
        '''
        logging.info("从元素 --%s--滚动至元素--%s"%(origin_elN,destination_elN))
        origin_elN1 = self.driver.find_element_by_name(origin_elN)
        destination_elN1 = self.driver.find_element_by_name(destination_elN)
        self.driver.scroll(origin_elN1,destination_elN1)
        
    def drag_and_drop(self,origin_elN,destination_elN):  #找到要拖拽的元素origin_elN，然后拖拽到另一个元素destination_elN的位置
        '''
        method explain:找到要拖拽的元素origin_elN，然后拖拽到另一个元素destination_elN的位置
        parameter explain：【origin_el】起始元素,【destination_el】:结束元素
        Usage:
            device.scroll('开始','结束')
        '''
        origin_elN1 = self.driver.find_element_by_name(origin_elN)
        destination_elN1 = self.driver.find_element_by_name(destination_elN)
        self.driver.drag_and_drop(origin_elN1,destination_elN1)
        # ActionChains(self.driver).drag_and_drop(origin_elN1, destination_elN1)
       
    def open_notifications(self):  #快速打开状态栏
        '''
        method explain:快速打开状态栏
        '''
        logging.info("打开状态栏-------------【开始】")
        self.driver.open_notifications()
        
    def scroll_from_element(self,el,x,y):  #未完成
        action = TouchAction()
        action.scroll_from_element(self.driver.find_element_by_id(el),x,y)
        
    def press_keycode(self,keycode):   #点击android的keycode键值
        '''
        method explain:点击android的keycode键值
        parameter explain：keycode 给定的键值
        Usage:
            device.press_keycode('3')  #点击了home键
        android keycode键值介绍连接:http://blog.csdn.net/crisschan/article/details/50419963
        '''
        logging.info("短按code键----------%s【开始】" %keycode)
        self.driver.press_keycode(keycode)
        logging.info("短按code键----------%s【结束】" %keycode)
        
    def long_press_keycode(self,keycode):   #长按点击android的keycode键值
        '''
        method explain:点击android的keycode键值
        parameter explain：keycode 给定的键值
        Usage:
            device.long_press_keycode('3')  #长按点击了home键
        android keycode键值介绍连接:http://blog.csdn.net/crisschan/article/details/50419963
        '''
        logging.info("长按code键---------%s【开始】" %keycode)
        self.driver.long_press_keycode(keycode)
        logging.info("长按code键---------%s【成功】" %keycode)
        
    def long_press_Byname(self,name):  #通过元素的name实现长按操作
        '''
        method explain:通过元素的name实现长按操作
        parameter explain：【name】 需要长按的name名称
        Usage:
            device.long_press_Byname('iBer精英')
        '''
        logging.info("长按name-----------%s【开始】"%name)
        try:
            el = self.driver.find_element_by_name(name)
            elx = el.location.get("x")
            ely = el.location.get("y")
            self.driver.tap([(elx,ely)],1000)
            logging.info("长按name-----------%s【成功】"%name)
        except:
            logging.error("except---------长按%s【异常】"%name)
            self.take_screenShot("%s"%name)
            assert 'assert long_press_Byname'
        
    def long_press_Byid(self,id):  #通过元素的id实现长按操作
        '''
        method explain:通过元素的id实现长按操作
        parameter explain：【id】 需要长按的name名称
        Usage:
            device.long_press_Byid('iBer精英')
        '''
        logging.info("长按id-----------%s【开始】"%id)
        try:
            el = self.driver.find_element_by_id(id)
            elx = el.location.get("x")
            ely = el.location.get("y")
            self.driver.tap([(elx,ely)],1000)
            logging.info("长按id-----------%s【成功】"%id)
        except:
            logging.error("except---------长按%s【异常】"%id)
            self.take_screenShot('%s'%id)
            assert 'assert long_press_Byid'
            
    def set_value(self,El_name,value):  #未上线，ios专用
        '''
        method explain:点击android的keycode键值
        parameter explain：keycode 给定的键值
        Usage:
            device.long_press_keycode('3')  #长按点击了home键
        '''
        El_name1 = self.driver.find_element_by_name(El_name)
        logging.info('默认值为------'+El_name1) 
        self.driver.set_text()
        
    def set_text(self,Elname,text):  #查找默认的text值并输入内容
        '''
        method explain:找到text值并且输入内容
        parameter explain：【Elname】 要被替换的text值，【text】输入的内容
        Usage:
            device.set_text("输入收件人",'10086')  #短信--收件人处输入10086
        '''
        logging.info("向文本框：'%s'---输入内容：%s"%(Elname,text))
        try:
            element = self.driver.find_element_by_name(Elname)
            element.set_text(text)
            logging.info("向text默认文本值：'%s'--输入内容：'%s'成功"%(Elname,text))
            #return True
        except:
            self.take_screenShot("%s_%s"%(Elname,text))
            assert("向text默认文本值--'%s'--输入内容--'%s'失败"%(Elname,text))
        
    def take_screenShot(self,name = "takeShot"):   #获取当前屏幕的截图
        '''
        method explain:获取当前屏幕的截图
        parameter explain：【name】 截图的名称
        Usage:
            device.take_screenShot(u"个人主页")   #2018-01-13_17_10_58_个人主页.png
        '''
        day = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        #fq = "..\\screenShots\\"+day  android机器上则需如此写
        fq =os.getcwd()[:-4]+"screenShots"+"/"+day
        logging.info(fq + "00000----------fq")
        #fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
        tm = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime(time.time()))
        type = '.png'
        filename = ""
        if os.path.exists(fq):
            filename = fq+"/"+tm+"_"+name+type
        else:
            os.makedirs(fq)
            filename = fq+"/"+tm+"_"+name+type
#         c = os.getcwd()
#         r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
        self.driver.get_screenshot_as_file(filename)
                   
    def swipe_UP(self,duration = 500,n = 1): #屏幕向上滑屏
        '''
        method explain:屏幕向上滑动
        parameter explain：【duration】 滑动屏幕持续的时间，时间越短，滑动速度越快，默认为None，建议设置500~100较合适，【n】滑动的次数
        Usage:
            device.swipe_UP()
        explain:（由于手机屏幕的分辨率不一样，所以一个元素在手机上的坐标不一样，因此坐标不可写死，可采用获取屏幕的宽和高，再通过比例计算）
        '''
        sleep(4)
        screen_size = self.driver.get_window_size()   ##获取屏幕的大小
        x1 = screen_size['width'] * 0.5    #x坐标
        y1 = screen_size['height'] * 0.75   #起始y坐标
        y2 = screen_size['height'] * 0.25   #终点y坐标
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,duration)
            
    def swipe_Down(self,duration = 500,n = 1):  #屏幕向下滑动
        '''
        method explain:屏幕向下滑动
        parameter explain：【duration】 滑屏持续的时间  【n】滑动的次数
        Usage:
            device.swipe_Down()
        '''
        sleep(4)
        screen_size = self.driver.get_window_size()
        x1 = screen_size['width'] * 0.5 
        y1 = screen_size['height'] * 0.25   #起始y坐标
        y2 = screen_size['height'] * 0.75   #终点y坐标
        for i in range(n):
            self.driver.swipe(x1,y1,x1,y2,duration)
    
    def swipe_Left(self,duration = 1000,n = 1):  #屏幕向左滑动
        '''
        method explain:屏幕向左滑动
        parameter explain：【duration】 滑屏持续的时间  【n】滑动的次数
        Usage:
            device.swipe_Left()
        '''
        sleep(4)
        screen_size = self.driver.get_window_size()  #获取屏幕的大小
        print  screen_size
        x1 = screen_size['width'] * 0.75 
        print x1
        y1 = screen_size['height'] * 0.5   #起始y坐标
        print y1
        x2 = screen_size['width'] * 0.05   #终点y坐标
        print x2
        for i in range(n):
            self.driver.swipe(x1,y1,x2,y1,duration)
            
    def swipe_Right(self,duration = 1000,n = 1):  #屏幕向右滑动
        '''
        method explain:屏幕向右滑动
        parameter explain：【duration】 滑屏持续的时间  【n】滑动的次数
        Usage:
            device.swipe_Right()
        '''
        sleep(4)
        screen_size = self.driver.get_window_size()
        x1 = screen_size['width'] * 0.05 
        y1 = screen_size['height'] * 0.5   #起始y坐标
        x2 = screen_size['width'] * 0.75   #终点x坐标
        for i in range(n):
            self.driver.swipe(x1,y1,x2,y1,duration)
      
    def reset_APP(self):  #重置apk的方法,,待封装
        self.driver.resetApp
        
    def test_h5(self):     #待封装
        self.touch_Name("我")
        self.touch_Name("钱包")
        self.touch_Name("理财通")
        print self.driver.contexts


        
