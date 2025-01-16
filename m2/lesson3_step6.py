from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    # первое окно
    f_button = browser.find_element(By.CSS_SELECTOR, '.btn')
    f_button.click()

    # переключаем
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # форма с задачей
    x_el = browser.find_element(By.ID, 'input_value')
    x = x_el.text
    x = calc(x)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(x)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
