#coding=utf-8
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#exception_conditions判断页面元素
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com")
sleep(5) #强制等待

element=WebDriverWait(driver,5,0.5).until(EC.visibility_of_element_located((By.ID,"kw")))
element.send_keys("selenium")

sleep(3)
driver.quit()
