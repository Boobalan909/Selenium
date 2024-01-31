from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# TestCase-1

# Set up the Chrome driver with the ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

""" Maximize the browser window """
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")

""" finding the element by id 
    Clearing the previous text in the password field """
email = driver.find_element(By.ID, "Email")
email.clear()
email.send_keys("admin@yourstore.com")

password = driver.find_element(By.NAME, "Password")
password.clear()
password.send_keys("admin")

""" Finding the element by xpath if id and name both are not available 
    (right click on html element and copy xpath)"""
login_button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
login_button.click()

""" finding the element by class name """
class_name = driver.find_elements(By.CLASS_NAME, "ico-logout")
print(len(class_name))

""" finding the element by tag name """
tag_name = driver.find_elements(By.TAG_NAME, "a")
print(len(tag_name))

""" finding the element by CSS selector """
css_selector = driver.find_element(By.CSS_SELECTOR, "li.nav-item") #Tag and Class
css_selector.click()

time.sleep(5)

""" finding the element by link text and partial link text """
logout_link = driver.find_element(By.LINK_TEXT, "Logout")
# logout_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
logout_link.click()

# dashboard_expected_title = "Dashboard / nopCommerce administration"
# actual_title = driver.title

# if dashboard_expected_title == actual_title:
#     print("Test Passed")
# else:
#     print("Test Failed")

time.sleep(5)

driver.quit()