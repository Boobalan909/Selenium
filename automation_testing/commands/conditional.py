from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

search_box = driver.find_element(By.ID, "small-searchterms")
print("displayed:", search_box.is_displayed())
print("enabled:", search_box.is_enabled())

radio_button_male = driver.find_element(By.ID, "gender-male")
radio_button_male.click()
radio_button_female = driver.find_element(By.ID, "gender-female")

print("male selection:", radio_button_male.is_selected())
print("female selection:", radio_button_female.is_selected())

time.sleep(5)
driver.quit()