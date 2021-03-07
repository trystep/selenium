from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_xpath('//*[@id="num1"]').text
num2 = browser.find_element_by_xpath('//*[@id="num2"]').text
result = int(num1) + int(num2)

select = Select(browser.find_element_by_xpath('//*[@id="dropdown"]'))
select.select_by_value(str(result))

submit = browser.find_element_by_xpath('//*[text()="Submit"]')
submit.click()
sleep(5)

browser.quit()
