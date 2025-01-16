from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = 'https://suninjuly.github.io/math.html'
    browser.get(link)
    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text
    x = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    radio = browser.find_element(By.CSS_SELECTOR, '[for = "robotsRule"]')
    radio.click()
    chek = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    chek.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
