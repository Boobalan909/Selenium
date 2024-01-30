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

# Navigate to the Google homepage
driver.get("https://google.com")

# Find the search box element using its ID
search_box = driver.find_element(By.ID, "APjFqb")

# Enter "selenium" in the search box
search_box.send_keys("selenium")

# Simulate pressing the Enter key to perform the search
search_box.send_keys(Keys.RETURN)

# Define the expected title
expected_title = "selenium - Google Search"

# Get the actual title of the current page
actual_title = driver.title

# Verify that the expected title matches the actual title
if expected_title == actual_title:
    print("Test Passed")
else:
    print("Test Failed")

time.sleep(10)

# Close the browser
driver.close()