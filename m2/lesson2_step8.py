from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
first_name = "firstname"
last_name = "lastname"
email = "email"
try:
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.NAME, first_name)
    input1.send_keys("Milena")
    input2 = browser.find_element(By.NAME, last_name)
    input2.send_keys("Zhilinskaya")
    input3 = browser.find_element(By.NAME, email)
    input3.send_keys("millymilk18@gmail.com")

    file_open_element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_22_8.txt')
    file_open_element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()