from selenium import webdriver
from selenium.webdriver.common.by import By


firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
driver = webdriver.Remote(
    command_executor='http://192.168.88.10:4444',
    options=firefox_options
)
driver.get("https://www.google.com")
driver.get("https://reddit.com")
    # Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

for e in elements:
    print(e.text)
driver.quit()
