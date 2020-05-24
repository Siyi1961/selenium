from selenium import webdriver
import unittest,time,logging
import traceback #异常类
import ddt
from selenium.common.exceptions import NoSuchElementException

from ExcelUtil import ParseExcel

#初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="G:\\report.log"
    #filemode='w'
)

excelPath = r'G:\Users\13962\Selenium\007-数据驱动\Excel\测试数据.xlsx'
sheetName = "搜索数据表"
excel=ParseExcel(excelPath, sheetName)

# 数据驱动装饰器
@ddt.ddt
class TestDemmo(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome("E:\\driver\\chromedriver.exe")

    @ddt.data(*excel.getDatasFromSheet())
    def test_dataDrivenByFile(self,data):
        # 强制将data改变为元组
        print("tuple(data)",tuple(data))
        testData, expectData=tuple(data)
        print("testData",testData)
        print("expectData", expectData)
        time.sleep(5)

        url="https://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        # 设置隐式等待
        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element_by_id("kw").send_keys(testData)
            self.driver.find_element_by_id("su").click()
            time.sleep(2)
            self.assertTrue(expectData in self.driver.page_source)
        except NoSuchElementException as e:
            # traceback.format_exc() 是将异常信息以字符串的形式返回
            logging.error("查找的页面元素不存在，异常信息："+str(traceback.format_exc()))
        except AssertionError as e:
            logging.info("搜索-'%s'，期望-'%s'，-失败"%(testData, expectData))
            # 搜索郎平，期望排球
        except Exception as e:
            logging.info("未知错误，错误信息："+str(traceback.format_exc()))
        else:
            logging.info("搜索-'%s'，期望-'%s'，-通过"%(testData, expectData))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__=='__main__':
    unittest.main()