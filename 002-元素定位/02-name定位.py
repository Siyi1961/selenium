#encoding=utf-8

#导入模块
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")

time.sleep(3)
driver.find_element_by_name("wd").send_keys("selenium3")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()