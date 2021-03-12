# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
import math

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

button = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_xpath('//span[@id="input_value"]').text
result = str(math.log(abs(12 * math.sin(int(x)))))

input = browser.find_element_by_xpath('//input[@id="answer"]')
input.send_keys(result)

submit = browser.find_element_by_xpath('//button[text()="Submit"]')
submit.click()

sleep(5)
browser.quit()
