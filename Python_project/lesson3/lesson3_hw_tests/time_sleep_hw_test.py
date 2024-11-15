from time import sleep
from selenium.webdriver.common.by import By

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver



@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

def test_explicit_wat_register(driver):
    driver.get("https://victoretc.github.io/selenium_waits/")
    # Проверка заголовка
    assert driver.find_element(By.XPATH, "//h1").text == "Практика с ожиданиями в Selenium"
    # Дождаться появления кнопки "Начать тестирование"
    sleep(6)
    # Кликнуть по кнопке "Начать тестирование".
    start_button = driver.find_element(By.ID, "startTest")
    start_button.click()
    # Ввести "login" в поле для логина.
    driver.find_element(By.ID, "login").send_keys("login")
    # Ввести "password" в поле для пароля.
    driver.find_element(By.ID, "password").send_keys("password")
    # Установить флажок в чекбокс "Согласен со всеми правилами".
    driver.find_element(By.ID, "agree").click()
    # Нажать кнопку "Зарегистрироваться".
    driver.find_element(By.ID, "register").click()
    # Удостовериться, что появился индикатор загрузки.
    sleep(6)
    success_message = driver.find_element(By.ID, "successMessage")
    assert success_message.text == "Вы успешно зарегистрированы!"