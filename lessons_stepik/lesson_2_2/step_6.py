# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
from time import sleep
import math

browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'
browser.get(link)
var_x = browser.find_element_by_xpath('//span[@id="input_value"]').text
result = math.log(abs(12 * math.sin(int(var_x))))
input = browser.find_element_by_xpath('//input[@id="answer"]')
input.send_keys(str(result))
checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
checkbox.click()
radiobutton = browser.find_element_by_xpath('//label[text()="Robots rule"]')
browser.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
radiobutton.click()

submit = browser.find_element_by_xpath('//button[text()="Submit"]')
submit.click()
sleep(10)
browser.quit()
