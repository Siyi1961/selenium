#encoding=utf-8

#导入模块
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")

time.sleep(3)
driver.find_element_by_class_name("s_ipt").send_keys("王历史")
time.sleep(2)
driver.find_element_by_class_name("bg s_btn").click()
time.sleep(2)
driver.quit()