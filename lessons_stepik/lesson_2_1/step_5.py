import math
from selenium import webdriver
import time


# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
x = x_element.text
result = calc(x)
input = browser.find_element_by_xpath('//*[@id="answer"]')
input.send_keys(result)
time.sleep(1)
checkbox = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
checkbox.click()
radiobutton = browser.find_element_by_xpath('//*[@id="robotsRule"]')
radiobutton.click()
time.sleep(1)
submit = browser.find_element_by_xpath('//*[text()="Submit"]')
submit.click()
time.sleep(5)
browser.quit()
