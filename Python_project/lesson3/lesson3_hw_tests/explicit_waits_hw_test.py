from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait



def test_explicit_wat_register(driver, wait):
    driver.get("https://victoretc.github.io/selenium_waits/")
    # Проверка заголовка
    assert driver.find_element(By.XPATH, "//h1").text == "Практика с ожиданиями в Selenium"
    # Дождаться появления кнопки "Начать тестирование"
    wait.until(EC.visibility_of_element_located((By.ID, "startTest")))
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
    success_message = wait.until(EC.visibility_of_element_located((By.ID, "successMessage")))
    assert success_message.text == "Вы успешно зарегистрированы!"
