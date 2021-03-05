from selenium import webdriver
import time
import math


# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

element_image = browser.find_element_by_xpath("//img[@id='treasure']")
value_element_image = element_image.get_attribute("valuex")
result = calc(value_element_image)
input = browser.find_element_by_xpath('//*[@id="answer"]')
input.send_keys(result)
checkbox = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
checkbox.click()
radiobutton = browser.find_element_by_xpath('//*[@id="robotsRule"]')
radiobutton.click()
submit = browser.find_element_by_xpath('//*[text()="Submit"]')
submit.click()
time.sleep(5)
browser.quit()
