#coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com/")

#打开搜索设置
link=driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

#对搜索结果的条数进行设置
sel=driver.find_element_by_xpath("//select[@id='nr']")
Select(sel).select_by_value('20')
sleep(2)

Select(sel).select_by_visible_text("每页显示50条")
sleep(2)

Select(sel).select_by_index("0")
sleep(2)

driver.quit()
