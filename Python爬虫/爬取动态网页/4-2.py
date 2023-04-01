from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ptpress.com.cn/search/books")
data = driver.page_source
print(data)

driver.quit()
