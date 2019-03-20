# coding=UTF-8
'''
Created on 2017/6/9
@author: SYW
用途：将测试结果集成到html报告中，并修改参数，生成相应的报告份数
'''
import HTMLTestRunner
import time,os
import logging
from Test.Case_Gathers import suite

 
if __name__ == "__main__":
    
    for tmp in range(1):   #可修改1代表的报告生成的份数  
        now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        File_Path = os.getcwd()[:-4] +'Report'+"/"      #获取到当前文件的目录，并检查是否有report文件夹，如果不存在则自动新建report文件
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
        
        logging.info(File_Path)
        Report_FileName = file(File_Path +now+ r"_ReportResult.html",'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=Report_FileName,title="test result",description="result:")
        runner.run(suite)    #suite为Case_Gathers.py中的suite，用法：将case中的suite添加到报告中生成
        Report_FileName.close()
        time.sleep(2)   #一轮测试完成之后，停留2s在开始下一轮测试

    