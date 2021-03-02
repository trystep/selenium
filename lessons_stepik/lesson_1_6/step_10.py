import string
from selenium import webdriver
import time
import random


def random_string():
    words = string.ascii_lowercase
    return (''.join(random.choice(words) for i in range(10)))


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element_by_css_selector('.form-control.first')
    input_first_name.send_keys(random_string())

    input_last_name = browser.find_element_by_css_selector('.form-control.second')
    input_last_name.send_keys(random_string())

    input_email = browser.find_element_by_css_selector('.form-control.third')
    input_email.send_keys(random_string())

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
