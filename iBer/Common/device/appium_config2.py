# -*- coding: utf-8 -*-

from appium import webdriver
from time import ctime
import yaml
import sys
import multiprocessing
from Test.logs.logs import logging

#为了读取yaml中的中文，否则会报错
reload(sys)
sys.setdefaultencoding('utf8')

with open("/Users/lucky/Desktop/Auto/UI_Script/iBer/Test/Common/desired_caps.yaml","r") as file:
    data = yaml.load(file)

devices_list = ["7f4bd69a","57614229"]  #给出需要连接的设备udid号
#
# def test(uuid, port):
#     return Singleton(uuid, port)

def tests(udid,port):
    desired_caps = {}
    desired_caps["platformName"] = data["platformName"]
    desired_caps["platformVersion"] = data["platformVersion"]
    desired_caps["deviceName"] = data["deviceName"]
    desired_caps["udid"] = udid
    # desired_caps["app"]=data["app"]
    desired_caps["appPackage"] = data["appPackage"]
    desired_caps["appActivity"] = data["appActivity"]
    desired_caps["noReset"] = data["noReset"]

    print ("appium port:%s start run %s at %s" % (port, udid, ctime()))
    print str(data['ip']) + str(port)

    device = webdriver.Remote('http://' + str(data['ip']) + ':' + str(port) + '/wd/hub', desired_caps)
    print device
    print "888888885555555555555555555555888"
    return udid,port,device

class Singleton(object):

    driver = None
    print "8888888888888888"

    # 构建desired的进程组
    desired_process = []
    def __new__(cls,*args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            print "____new____"
            tests()
            cls._instance = orig.__new__(cls,*args, **kwargs)
        return cls._instance

    #加载desired进程
    for i in range(len(devices_list)):
        port = 4723+2+i
        print port
        desired = multiprocessing.Process(target = tests(),args = (devices_list[i],port))
        desired_process.append(desired)


class DriverClient(Singleton):
    print "66666666666666666"
    for desired in Singleton.desired_process:
        print "55555555555555"
        desired.start()
    for desired in Singleton.desired_process:
        desired.join()    #等所有的子进程执行结束再关闭

    def getDriver(self):
        logging.info('get driver')
        print self.driver
        return self.driver