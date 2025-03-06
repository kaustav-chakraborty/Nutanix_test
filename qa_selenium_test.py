from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)  

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

# Enter "New York" in the search box
search_box = driver.find_element(By.XPATH, "//div[@id='example_filter']//input[1]")
search_box.send_keys("New York")

# Wait for search results to update
time.sleep(2)  

# Validate the number of displayed entries
pagination_text = driver.find_element(By.ID, "example_info").text  
assert "Showing 1 to 5 of 5 entries" in pagination_text, f"Validation failed! Found: {pagination_text}"

print("✅ Validation Passed: Correct number of entries displayed.")

time.sleep(10)
driver.quit()
