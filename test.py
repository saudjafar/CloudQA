import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

os.environ['PATH'] += r"C:/SeleniumDrvers"
driver = webdriver.Chrome()

driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")
driver.implicitly_wait(3)

test_element_1 = driver.find_element(By.ID, "fname")

test_element_2 = driver.find_element(By.ID, "male")

test_element_3 = driver.find_element(By.ID, "state")
 

test_element_1.send_keys("First name")

test_element_2.click()

select = Select(test_element_3)
select.select_by_value("India")

input("Press any key to exit...")