from selenium import webdriver
import os
import time

options=webdriver.ChromeOptions()

prefs={'profile.default_content_setting.popups':0,
       'download.default_directory':os.getcwd()}

options.add_experimental_option('prefs',prefs)

driver=webdriver.Chrome(executable_path="E:\\driver\\chromedriver.exe",chrome_options=options)
driver.get("https://pypi.org/project/selenium/#files")
time.sleep(5)
driver.find_element_by_link_text("selenium-3.141.0.tar.gz").click()

input("是否下载成功")
driver.quit()