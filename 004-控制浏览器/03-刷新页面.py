#coding=utf-8
from selenium import webdriver
from time import sleep
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com")
sleep(2)
driver.refresh()

time.sleep(2)
driver.quit()