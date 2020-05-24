#encoding=utf-8

#导入模块
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")

time.sleep(3)
driver.find_element_by_partial_link_text("新")
#driver.find_element_by_partical_link_text("新").click()
time.sleep(3)

driver.quit()