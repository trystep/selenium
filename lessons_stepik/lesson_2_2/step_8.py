# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from time import sleep
import os
import random
import string


def random_string():
    word = string.ascii_letters
    return ''.join(random.choice(word) for i in range(1))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

firstname = browser.find_element_by_name('firstname')
firstname.send_keys(random_string())

lastname = browser.find_element_by_name('lastname')
lastname.send_keys(random_string())

email = browser.find_element_by_name('email')
email.send_keys(random_string())

file = browser.find_element_by_name('file')
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test_file_upload.txt')  # добавляем к этому пути имя файла
file.send_keys(file_path)

submit = browser.find_element_by_xpath('//button[text()="Submit"]')
submit.click()
sleep(5)

browser.quit()
