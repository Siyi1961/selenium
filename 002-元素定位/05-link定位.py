#encoding=utf-8

#导入模块
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")

time.sleep(3)
driver.find_element_by_link_text("新闻").click()
time.sleep(3)

driver.quit()