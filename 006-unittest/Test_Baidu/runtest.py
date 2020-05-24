import unittest
from HTMLTestRunnerCN import HTMLTestRunner
import time

test_dir='./test_case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__=='__main__':
    report_dir='./test_report'
    now=time.strftime("%Y-%m-%d %H_%M%S")
    report_name=report_dir+"/"+now+'_result.html'

    with open(report_name, 'wb') as f:
        runner=HTMLTestRunner(stream=f, title="百度搜索报告",description="针对百度搜索功能进行自动化测试报告总结")
        runner.run(discover)