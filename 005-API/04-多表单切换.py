#coding=utf-8
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://mail.163.com/")

sleep(5)
driver.find_element_by_id("lbNormal").click()

driver.switch_to.frame(driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]"))
driver.find_element_by_name("email").send_keys("wang")
driver.find_element_by_name("password").send_keys("wang")

sleep(3)

#切换之后要切换回来
driver.switch_to.default_content()

driver.quit()