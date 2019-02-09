import time

from selenium import webdriver
browser='chrome'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/5_Class/drivers/chromedriver.exe")
elif browser=='firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/Dell/PycharmProjects/5_Class/drivers/geckodriver.exe")
elif browser=='ie':
    driver = webdriver.Ie(executable_path="C:/Users/Dell/PycharmProjects/5_Class/drivers/IEDriver.exe")
else:
    print("Provide appropriate browser name")

driver.get("http://makemytrip.com")
time.sleep(5)
driver.find_element_by_id("header_tab_hotels").click()
time.sleep(5)
driver.find_element_by_id("header_tab_holidays").click()
driver.back()
time.sleep(5)
driver.forward()
