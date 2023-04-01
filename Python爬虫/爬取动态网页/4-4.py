import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ptpress.com.cn/search/books")
driver.execute_script("window.open()")
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get("http://www.tipdm.com")
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.get("http://www.tipdm.org")
