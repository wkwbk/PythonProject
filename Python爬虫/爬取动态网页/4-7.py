from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.ptpress.com.cn/search/books')
input_first = driver.find_element(By.ID, "searchVal")
input_second = driver.find_element(By.CSS_SELECTOR, "#searchVal")
input_third = driver.find_element(By.XPATH, '//*[@id="searchVal"]')
print(input_first)
print(input_second)
print(input_third)
driver.close()
