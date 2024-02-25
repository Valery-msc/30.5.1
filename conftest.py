from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def driver():
    _driver = webdriver.Chrome()
    _driver.get('http://petfriends.skillfactory.ru/login')
    yield _driver
    _driver.quit()