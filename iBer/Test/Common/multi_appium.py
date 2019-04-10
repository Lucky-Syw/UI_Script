# -*- coding: utf-8 -*-

'''
python启动多个appium服务----并发
'''
import subprocess
from time import ctime
import sys,os
import yaml

reload(sys)
sys.setdefaultencoding('utf8')

path = os.getcwd()
print path
with open(path+"/desired_caps.yaml","r") as file:
    data = yaml.load(file)
devices_list = data["devices_list"]

def appium_start(host,port):
    print "-----------------------------appium_start-----------------------------"
    '''启动appium服务'''
    #此处的port+3是为了appium服务的启动端口不跟multi_device中的端口重复
    bootstrap_port = str(port+3)
    print "bootstrap_port" + str(bootstrap_port)
    '''# win
            start /b appium -a 127.0.0.1 -p 4723  --log xxx.log --local-timezone
            # mac
            appium -a 127.0.0.1 -p 4723  --log xxx.log --local-timezone  &'''
    # cmd = "start /b appium -a"+host+" -p "+str(port)+" -bp "+str(bootstrap_port)  windows上的写法
    cmd = "appium -a " + host + " -p " + str(port) + " -bp " + str(bootstrap_port)


    print "%s at %s"%(cmd,ctime())
    print path+'/appium_log/'+str(port)+'.log'

    logpath = os.getcwd()[:-5]
    print logpath
    subprocess.Popen(cmd,shell=True,stdout=open(logpath+'/appium_log/'+str(port)+'.log','wa'),stderr=subprocess.STDOUT)

# if __name__ == "__main__":
#     host = "127.0.0.1"
    # port = 4723
    # appium_start(host,port)

# appium_process = []  lucky注销，释放开则是并发的启动appium服务
#
for i in range(len(devices_list)):   #根据连接Android设备的数量，可更改此处的值
    host = "127.0.0.1"
    port = 4723+2+i
    print port
    appium_start(host, port)

    # appium = multiprocessing.Process(target=appium_start,args=(host,port))
    # appium_process.append(appium)

# if __name__ == "__main__":  lucky注销
#
#     for appium in appium_process:
#         appium.start()
#     for appium in appium_process:
#         appium.join()