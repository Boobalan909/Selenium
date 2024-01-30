from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# TestCase-1

# Set up the Chrome driver with the ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Maximize the browser window
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")

email = driver.find_element(By.ID, "Email")
# Clearing the previous text in the email field
email.clear()
email.send_keys("admin@yourstore.com")

password = driver.find_element(By.NAME, "Password")
# Clearing the previous text in the password field
password.clear()
password.send_keys("admin")

# Finding the element by xpath if id and name both are not available (right click on html element and copy xpath)
login_button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
login_button.click()

dashboard_expected_title = "Dashboard / nopCommerce administration"
actual_title = driver.title

if dashboard_expected_title == actual_title:
    print("Test Passed")
else:
    print("Test Failed")

time.sleep(5)

driver.quit()