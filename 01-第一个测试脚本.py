from selenium import webdriver
from time import sleep


# drvier=webdriver.Chrome()
#Executable_path添加环境变量
drvier=webdriver.Firefox(executable_path="E:\\driver\\geckodriver.exe")
drvier.get("http://www.baidu.com")

drvier.find_element_by_id("kw").send_keys("selenium")
drvier.find_element_by_id("su").click()
sleep(3)
drvier.quit()