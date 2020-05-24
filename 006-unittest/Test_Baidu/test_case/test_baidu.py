from selenium import webdriver
import unittest
from time import sleep

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("E:\\driver\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")
        sleep(5)

    def test_baidu(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("王学丹老师")
        driver.find_element_by_id("su").click()
        sleep(2)
        title=driver.title
        self.assertEqual(title,"王学丹老师_百度搜索")


    def tearDown(self):
        self.driver.quit()
