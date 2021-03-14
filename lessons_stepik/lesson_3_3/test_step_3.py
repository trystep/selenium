# Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# Создайте новый файл
# Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
# Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
# Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
# Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
# Запустите получившиеся тесты из файла
# Просмотрите отчёт о запуске и найдите последнюю строчку
# Отправьте эту строчку в качестве ответа на это задание

import string
from selenium import webdriver
import time
import random
import unittest


class TestStep13(unittest.TestCase):

    def random_string(self):
        words = string.ascii_lowercase
        return (''.join(random.choice(words) for i in range(10)))

    def test_registration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        # link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element_by_css_selector(
            'form > div.first_block > div.form-group.first_class > input')
        input_first_name.send_keys(self.random_string())

        # Ожидается NoSuchElementException
        input_last_name = browser.find_element_by_css_selector(
            'form > div.first_block > div.form-group.second_class > input')
        input_last_name.send_keys(self.random_string())

        input_email = browser.find_element_by_css_selector(
            'form > div.first_block > div.form-group.third_class > input')
        input_email.send_keys(self.random_string())

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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_first_name = browser.find_element_by_css_selector(
            'form > div.first_block > div.form-group.first_class > input')
        input_first_name.send_keys(self.random_string())

        # Ожидается NoSuchElementException
        input_last_name = browser.find_element_by_css_selector(
            'form > div.first_block > div.form-group.second_class > input')
        input_last_name.send_keys(self.random_string())

        input_email = browser.find_element_by_css_selector(
            'form > div.first_block > div.form-group.third_class > input')
        input_email.send_keys(self.random_string())

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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == '__main__':
    unittest.main()
