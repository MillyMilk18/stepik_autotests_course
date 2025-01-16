from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)

link = "http://suninjuly.github.io/find_xpath_form"

f_name = 'first_name'
l_name = 'last_name'
city_class = '.form-control.city'
country = 'country'
but = '//button[@type="submit"]'
try:
    browser.get(link)

    input1 = browser.find_element(By.NAME, f_name)
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, l_name)
    input2.send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, city_class).send_keys("Smolensk")
    input4 = browser.find_element(By.ID, country)
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, but)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла