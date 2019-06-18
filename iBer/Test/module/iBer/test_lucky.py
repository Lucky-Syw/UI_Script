# -*- coding: utf-8 -*-
import os

def kill_server(port):
    cmd = "lsof -i:%s|awk 'NR==2{print $2}'" % port
    print cmd
    pid = os.popen(cmd).read()
    print pid
    cmd = "kill -9 %s" % pid
    print cmd
    os.popen(cmd).read()
    print os.popen(cmd).read()

def stopAppium():
    r = os.popen("ps -ef | grep appium")
    info = r.readlines()
    for line in info:  # 按行遍历
        eachline = line.split()
        appium_pid = eachline[1]
        action = os.popen("kill " + appium_pid)
        print("kill" + appium_pid)
stopAppium()
#kill_server(4723)
