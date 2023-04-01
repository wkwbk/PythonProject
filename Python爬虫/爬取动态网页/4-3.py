from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.ptpress.com.cn/search/books")
wait = WebDriverWait(driver, 10)
confirm_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div:nth-child(1) > div > div > div > button > i")))
print(confirm_btn)
driver.close()
