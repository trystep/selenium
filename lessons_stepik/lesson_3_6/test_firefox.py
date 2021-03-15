from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
