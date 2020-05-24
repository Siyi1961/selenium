#coding=utf-8
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com")

print("Before search==========")
#打印当前页面title
title = driver.title
print("title:"+title)

#打印当前页面url
now_url=driver.current_url
print("now_url:"+now_url)


driver.find_element_by_id("kw").send_keys("王学丹")
driver.find_element_by_id("su").click()
sleep(3)

print("After search===========")
title = driver.title
print("title:"+title)

#打印当前页面url
now_url=driver.current_url
print("now_url:"+now_url)

#获取搜索结果 条数
num=driver.find_element_by_class_name("nums_text").text
print("result:"+num)

driver.quit()
