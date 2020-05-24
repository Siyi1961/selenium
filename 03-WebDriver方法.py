from selenium import webdriver
import time

driver=webdriver.Chrome("E:\\driver\\chromedriver.exe")
driver.get("https://www.baidu.com")

time.sleep(5)
#1.返回百度页面底部的备案信息
a2=driver.find_element_by_id("s-bottom-layer-right").text
print(a2)

#2.定位页面元素
a1=driver.find_element_by_id("kw")
a1.clear()
a1.send_keys("身份")
a1.submit()
print("搜索输入框尺寸：",a1.size)

#3.返回元素属性值
attr=driver.find_element_by_id("su").get_attribute("type")
print(attr)

#4.返回元素的结果是否可见
res=driver.find_element_by_id("kw").is_displayed()
print(res)

driver.quit()