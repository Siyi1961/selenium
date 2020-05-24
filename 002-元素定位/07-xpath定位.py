#encoding=utf-8

from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")

driver.get("https://www.baidu.com")
#1.绝对路径
#driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/span/input").send_keys("王老师")

#2.相对路径(利用元素属性定位)
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium3")
#3.层级与属性相结合
# driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys("selenium3")

#4.使用逻辑运算符
# driver.find_element_by_xpath("//input[@id='kw' and @class='s_ipt']").send_keys("selenium")
#5.使用contains方法
driver.find_element_by_xpath("//span[contains(@class,'s_ipt')]/input").send_keys("selenium3")

driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()


