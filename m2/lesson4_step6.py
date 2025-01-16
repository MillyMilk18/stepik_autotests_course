from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    text_100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    f_button = browser.find_element(By.ID, 'book')
    f_button.click()

    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text
    x = calc(x)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(x)
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
