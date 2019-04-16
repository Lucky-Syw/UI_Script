# -*- coding: utf-8 -*-

from appium import webdriver
from time import ctime
import yaml
import sys

from Add_Case_Gather import Run_test
import os,time
from time import sleep
#为了读取yaml中的中文，否则会报错
reload(sys)
sys.setdefaultencoding('utf8')

#获取desired_caps.yaml的存放路径
path = os.getcwd()
with open(path+"/desired_caps.yaml","r") as file:
    data = yaml.load(file)
devices_list = data["devices_list"]

#开始执行设备
for i in range(len(devices_list)):
    port = 4723 + 2 + i
    def appium_desire(udid,port):
        print "--------------------appium_desire-------------------------"
        desired_caps = {}
        desired_caps["platformName"] = data["platformName"]
        desired_caps["platformVersion"] = data["platformVersion"]
        desired_caps["deviceName"] = data["deviceName"]
        desired_caps["udid"]=udid
        desired_caps["appPackage"] = data["appPackage"]
        desired_caps["appActivity"] = data["appActivity"]
        desired_caps["noReset"] = data["noReset"]

        print ("appium port:%s start run %s at %s" %(port,udid,ctime()))
        print str(data['ip'])+str(port)
        driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
        print driver

        #调用需要执行的步骤操作方法
        Run_test(driver).run_test1()


        return devices_list[i],port


