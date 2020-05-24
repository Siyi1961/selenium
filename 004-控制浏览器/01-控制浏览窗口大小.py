#coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com")

time.sleep(5)
print("设置浏览器宽480，高800显示")
driver.set_window_size(480,800)
time.sleep(3)

#设置全屏
driver.maximize_window()
time.sleep(3)

driver.quit()