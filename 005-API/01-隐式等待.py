#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com")
time.sleep(5) #强制等待
driver.implicitly_wait(10) #隐式等待

driver.get("https://www.baidu.com")

try:
    print(time.ctime())
    driver.find_element_by_id("wang").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(time.ctime())
    time.sleep(2)
    driver.quit()