#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
Created on 2019年06月20日
@author: Lucky
'''

from appium import webdriver
import unittest
from time import sleep

'''直接在这个页面进行运行，查看自己电脑的环境配置是否ok'''
class Test_appium(unittest.TestCase):

    def setUp(self):
        desired_cups = {}
        desired_cups['platformName'] = 'Android'
        desired_cups['platformVersion'] = '4.4.2'
        desired_cups['deviceName'] = '57614229'  # 手机的串号，手机usb连接电脑，使用adb devices即可查看此串号，复制粘贴此处即可
        desired_cups['appPackage'] = 'com.iBer.iBerAppV2'  # 打开应用的包名
        desired_cups['udid'] = "57614229"
        desired_cups['appActivity'] = 'com.iBer.iBerAppV2.MainActivity'  # 应用的活动名称
        self.device = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                                       desired_cups)  # appium的服务，查看地方：打开已经安装的appium，点击“设置”查看端口
        sleep(2)

    def tearDown(self):
        pass


    def test_appium_01(self):
        '''打开短信app'''
        self.device.quit()  # 退出App
        print '00000000000'  # 随便打印的提示信息


if __name__ == '__main__':
    unittest.main()