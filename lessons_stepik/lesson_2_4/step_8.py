# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

button_book = browser.find_element_by_id('book')
button_book.click()

x = int(browser.find_element_by_id('input_value').text)
result = str(math.log(abs(12 * math.sin(x))))

input = browser.find_element_by_id('answer')
input.send_keys(result)

submit = browser.find_element_by_id('solve')
submit.click()

time.sleep(5)
browser.quit()
