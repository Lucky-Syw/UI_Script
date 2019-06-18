# -*- coding: utf-8 -*-
'''
意义：端口的自动检测

'''
import socket
import  os
import re

def check_port(host,port):
    '''检测端口是否可用'''

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #socket.SOCK_STREAM 或 SOCK_DGRAM
    try:
        s.connect((host,port))
        s.shutdown(2)     #禁止在一个socket上进行数据的接收与发送，利用shutdown函数使socket双向数据传输变为单向数据传输，
        # shutdown需要一个单独的参数，该参数表示了如何关闭socket，0：表示禁止将来读，1：表示禁止将来写，2：表示禁止将来读写

    #except OSError as msg:
    except:
        print("port %s is avaliable")%port  #端口可用
        return True
    else:
        print ("port %s alreadly be in use ！！！")%port  #端口已被占用
        return  False


def release_port(port):
    print"release_port-------------杀掉已占用的端口"
    '''杀掉正在执行的端口'''
    cmd = "lsof -i:%s|awk 'NR==2{print $2}'" % port
    pid = os.popen(cmd).read()
    print "find port:%s, pid is value：%s" %(port,pid)
    cmd = "kill -9 %s" % pid
    print "kill port：%s，pid value：%s"%(port,pid)
    os.popen(cmd).read()



# if __name__ =="__main__":
#     host = "127.0.0.1"
#     port = 4726
#     check_port(host,port)
#     release_port(port)

