import unittest
from time import sleep
from selenium import webdriver
from baidu_page import BaiduPage

class TestBaidu(unittest.TestCase):
    # @classmethod修饰符，对应的函数不需要实例化，不需要self参数，第一个参数需要是表示自身类的class参数
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome("E:\\driver\\chromedriver.exe")

    def test_baidu_search_case(self):
        page=BaiduPage(self.driver)
        page.open()
        page.search_input("selenium")
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(),"selenium_百度搜索")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__=="__main__":
    '''
    verbosity表示测试结果的信息复杂度：
    0-静默模式
    1-默认模式
    2-详细模式
    '''
    unittest.main(verbosity=2)