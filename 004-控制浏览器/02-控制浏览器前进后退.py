#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
# driver.get("https://www.baidu.com")

#访问百度首页
first_url="https://www.baidu.com"
print("now access: %s"%(first_url))
driver.get(first_url)
time.sleep(2)
#访问新闻页
second_url="https://news.baidu.com"
print("now access: %s"%(second_url))
driver.get(second_url)
time.sleep(2)
#后退
print("back to %s"%(first_url))
driver.back()
time.sleep(2)
#前进
print("forward to %s"%(second_url))
driver.forward()
time.sleep(2)
driver.quit()




driver.quit()