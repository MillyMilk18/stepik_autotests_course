from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def summa(x, y):
    return str(x + y)

browser = webdriver.Chrome()

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser.get(link)
    x_el = browser.find_element(By.ID, 'num1')
    x = int(x_el.text)
    y_el = browser.find_element(By.ID, 'num2')
    y = int(y_el.text)
    sum_find = summa(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum_find)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
