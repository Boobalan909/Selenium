from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://google.com")


driver.find_element(By.ID, "APjFqb").send_keys("selenium") #locating the search bar
driver.find_element(By.ID, "APjFqb").send_keys(Keys.RETURN) #pressing enter

print(driver.title)
print(driver.current_url)
# print(driver.page_source)

time.sleep(5)
driver.quit()