from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
driver.get("http://www.baidu.com")

#1.通过class定位
# driver.find_element_by_css_selector(".s_ipt").send_keys("css定位")

#2.通过ID定位
# driver.find_element_by_css_selector("#kw").send_keys("css定位")

#3.通过标签层级单位定位
# driver.find_element_by_css_selector("span>input").send_keys("selenium3")

#4.通过属性定位
driver.find_element_by_css_selector("[name='wd']").send_keys("selenium")

time.sleep(3)
driver.quit()