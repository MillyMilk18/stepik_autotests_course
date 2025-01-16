from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
first_name = "//input[contains(@class, 'first') and contains(@placeholder, 'first')]"
last_name = "//input[contains(@class, 'second') and contains(@placeholder, 'last')]"
email = ".third"
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, first_name)
    input1.send_keys("Milena")
    input2 = browser.find_element(By.XPATH, last_name)
    input2.send_keys("Zhilinskaya")
    input3 = browser.find_element(By.CSS_SELECTOR, email)
    input3.send_keys("millymilk18@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()