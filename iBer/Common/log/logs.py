# coding=UTF-8
'''
date:2017/6/12
@author: SYW
用途：控制台log的打印形式修改，并且在module中调用
'''
import logging
import os

Log_FileName = os.getcwd()[:-4] +'Run_logs'      #获取到当前文件的目录，并检查是否有logs文件夹，如果不存在则自动新建logs文件
if not os.path.exists(Log_FileName):
    os.makedirs(Log_FileName)


# logging.basicConfig(level=logging.NOTSET,     #旧的log打印形式
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%Y-%m-%d %X',
#                 filename=Log_FileName,
#                 filemode='w')

'''以下修改log的打印方式-----SYW'''
logging.basicConfig(level=logging.NOTSET,
                format='[%(asctime)s] [line:%(lineno)d] [%(levelname)s] %(message)s',
                datefmt='%Y-%m-%d %X',
                #filename=Log_FileName+ r"\log.txt",
                filename=Log_FileName+ r"/log.txt",
                filemode='w')

console = logging.StreamHandler()
#console.setLevel(logging.INFO)   #显示等级为INFO，则自动过滤掉了系统debug提示
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [line:%(lineno)d] [%(levelname)s]: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

#logging.info("jaskdfjkajfkdl")   #运行写法示例