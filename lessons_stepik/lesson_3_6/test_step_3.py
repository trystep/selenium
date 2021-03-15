# открыть страницу
# ввести правильный ответ
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def fixture_browser():
    browser = webdriver.Chrome()
    yield browser
    # browser.quit()


@pytest.mark.parametrize('id_page', [
    "236895",
    "236896",
    "236897",
    "236898",
    "236899",
    "236903",
    "236904",
    "236905"
])
def test_correct_answer(fixture_browser, id_page):
    fixture_browser.get(f"https://stepik.org/lesson/{id_page}/step/1")

    answer = str(math.log(int(time.time())))

    input = WebDriverWait(fixture_browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.show-plugin textarea')))
    input.send_keys(answer)

    button = WebDriverWait(fixture_browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.submit-submission')))
    button.click()

    feedback = WebDriverWait(fixture_browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

    feedback = feedback.text

    assert feedback == 'Correct!'
