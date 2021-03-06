# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
import math

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

button = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
button.click()

allert = browser.switch_to.alert
allert.accept()

x = browser.find_element_by_xpath('//span[@id="input_value"]').text
result = math.log(abs(12 * math.sin(int(x))))

input = browser.find_element_by_xpath('//input[@id="answer"]')
input.send_keys(str(result))

submit = browser.find_element_by_xpath('//button[text()="Submit"]')
submit.click()

sleep(5)
browser.quit()
