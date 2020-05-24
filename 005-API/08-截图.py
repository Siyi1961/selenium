#coding=utf-8
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com/")
sleep(3)
#截取当前窗口，指定截图图片的保存位置
driver.save_screenshot("./baidu.png")
#关闭浏览器
driver.quit()
