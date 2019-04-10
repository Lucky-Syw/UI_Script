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
    cmd_find = "lsof -i tcp:%s" %port
    print cmd_find

    result = os.popen(cmd_find).read()
    x = re.findall("node (.*) lucky",result)
    x2 = ''.join(x)   #获取到pid的数值
    print "%s,%s" %(port,x2)   #获取查看cmd_find的所有查询结果
    # if str(port) and "PID" in result:
    #     start = result.index("3")
    #     end = result.index("l")
    #     pid = result[start:end]   #获取到pid的数值
    #     print str(pid)+"这是已经被port占用的pid号"

    cmd_kill = "sudo kill -9 %s"%x2
    os.popen(cmd_kill)

    # else:
    #     print "port %s is available" %port

# if __name__ =="__main__":
#     host = "127.0.0.1"
#     port = 4726
#     check_port(host,port)
#     release_port(port)

