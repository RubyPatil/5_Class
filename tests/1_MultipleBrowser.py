import time

from selenium import webdriver
browser='ie'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/5_Class/drivers/chromedriver.exe")
elif browser=='firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/Dell/PycharmProjects/5_Class/drivers/geckodriver.exe")
elif browser=='ie'
    driver = webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/5_Class/drivers/IEDriver.exe")
else:
    print("Provide appropriate browser name")

driver.get("http://makemytrip.com")
time.sleep(5)