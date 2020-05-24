from selenium import webdriver
import os
import time

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe")
file_path="file:///" + os.path.abspath('upfile.html')
driver.get(file_path)
time.sleep(2)

driver.find_element_by_name("file").send_keys("E:\\zp\\00.jpg")
time.sleep(2)
driver.quit()