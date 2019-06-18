# -*- coding: utf-8 -*-
'''并发的测试
主要功能：
1、检查给定的端口是否被占用，如果占用则自动释放
2、并发启动appium服务
3、并发启动device服务
'''


from Common.device.multi_appium import appium_start
#from multi_device import appium_desire
from Common.device.multi_device import appium_desire
from Common.device.Check_port import *
from time import sleep
import multiprocessing
import sys
import yaml

#为了读取yaml中的中文，否则会报错
reload(sys)
sys.setdefaultencoding('utf8')

# 获取desired_caps.yam的路径
path = os.getcwd()
with open(path+"/desired_caps.yaml","r") as file:
    data = yaml.load(file)

devices_list = data["devices_list"]

def start_appium_action(host,port):
    print "start_appium_action------------------"
    if check_port(host,port)==False:
        release_port(port)
    elif check_port(host,port)==True:
        appium_start(host, port)
        return True
    else:
        print("appium %s start faild!"%port)
        return False

def start_devices_action(udid,port):
    host = "127.0.0.1"
    appium_desire(udid, port)

def appium_start_sync():
    appium_process = []
    for i in range(len(devices_list)):
        host = "127.0.0.1"
        port = 4723+2+i
        appium = multiprocessing.Process(target=start_appium_action,args=(host,port))
        appium_process.append(appium)


    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    sleep(5)

def devices_start_sync():
    desired_process = []
    for i in range(len(devices_list)):
        port = 4723+2+i
        desired = multiprocessing.Process(target=start_devices_action, args=(devices_list[i], port))
        desired_process.append(desired)

    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()

if __name__ == "__main__":
    appium_start_sync()
    devices_start_sync()

