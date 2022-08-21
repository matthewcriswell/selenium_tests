from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import sys

username = os.getenv('REDDIT_USER')
password = os.environ.get('REDDIT_PASS')


def logIn():
    print("trying to login")
    try:
        sleep(2)
        # identify the iframe with the login class
        frame = driver.find_element(By.XPATH, "//iframe[@class='_25r3t_lrPF3M6zD2YkWvZU']")
        # switch to the iframe with the login (I think?)
        driver.switch_to.frame(0)

        username_object = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//fieldset//input[@id='loginUsername']")))
        username_object.send_keys(username)
        password_object = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//fieldset//input[@id='loginPassword']")))
        password_object.send_keys(password)
        password_object.send_keys(Keys.ENTER)

    except NoSuchElementException:
        print("did not find the elements")
        sys.exit(1)


service=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options, service=service)

driver.get("https://www.reddit.com/")

login=driver.find_element(By.LINK_TEXT, "Log In")
login.click()
logIn()
print("You are now logged into Reddit")
