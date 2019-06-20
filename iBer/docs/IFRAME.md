# 框架结构
├── README.md  
└── iBer  
    ├── Common  
    │   ├── device  
    │   ├── html  
    │   └── log  
    ├── Report  
    ├── Run_logs  
    ├── appium_log  
    ├── docs  
    └── screenShots  
    ├── Test  
    │   ├── Case  
    │   │   ├── iBer  
    │   │   │   ├── iBer_Test_Login.py  
    │   │   │   ├── iBer_Test_Quan.py  
    │   │   └── Test  
    │   │       └── iBer_Test_Login2.py  
    │   ├── Driver_Elements  
    │   │   ├── Driver_Elements.py  
    │   ├── module  
    │   │   └── iBer  
    │   │       ├── Login.py  
    │   │       ├── iBerQuan.py  
    │   │   └── Test  
    │   │       └── iBer_Test_Login2.py  
    │   ├── Case_Gathers.py  
    │   ├── desired_caps.yaml  
    │   ├── Run_Tests.py  

# 框架编写注意点

## Driver_Elements
    #---接口层
    
    新增common方法必填信息，备注要求
    :method explain:
            - 此方法的解释
    :ndertake method:
            - 此方法的执行需要承接的前提条件的方法
    :Args:
            - element - 要查找的元素
    :Usage:
            - 方法示例
            
# module
    #---业务逻辑层
    
    1、介于对APP的不用模块将建立不同的方法行，login模块方法将执行一次即可，因此在login之外的module之间必不可少的方法：start_activity，back
    2、针对测试用例的要求将共用的方法单抽出来写成一个module，方便调用
    
#case
    #---用例逻辑层
    
    setUp：执行此用例的前提条件
    tearDown：执行完此用例的后置操作，每个case必加self.iBer.back_desktop()，避免掉测试用例之间的相互干扰
    按照实际的测试用例要求，根据module中封装的方法进行调用，顺序写测试用例


#Case_Gathers
    #---用例集合
    
    注意点：
        1、新增的testcase之间无关联
        2、testcase的循环修改for循环即可
        3、不需要执行的testcase直接注释
        
#desired_caps.yaml
    #---公共配置文件
    
    基础的配置如下：
    
        platformVersion: 5.1.1
        platformName: Android
        deviceName: oppo
        appPackage: com.iBer.iBerAppV2
        appActivity: com.iBer.iBerAppV2.MainActivity
        #appPackage: com.android.mms
        #appActivity: /com.qiku.android.mms.ui.MmsConversationListActivity
        noReset: False
        unicodeKeyborad: True   #使用Unicode编码方式发送字符串
        resetKeyborad: True     #隐藏键盘
        ip: 127.0.0.1
        devices_list: ["7f4bd69a","57614229"]  #给出需要启动的设备udid,此处启动2个真机
        phone: ["12606666333","12607777889"]
    
    说明：若不是公共的配置信息，请在对应的模块下新建配置文件。

#Run_Tests
    #---执行测试，启动文件
    
    运行case，执行点击此文件则开始运行。








