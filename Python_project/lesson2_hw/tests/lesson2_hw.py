from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

"""Тесты используют фикстуры login, driver from conftest"""

def test_misleplav_button_redirection(driver):
    driver.get("http://195.133.27.184/create/")
    driver.find_element(By.XPATH, "//a[text()='Мыслеплав']").click()
    assert driver.current_url == "http://195.133.27.184/", "Url не соответствует url главной страницы"


def test_create_listing_button_redirection(driver):
    driver.find_element(By.XPATH, "//a[contains(text(), 'Создать')]").click()
    assert driver.current_url == "http://195.133.27.184/create/", "Url не соответствует url страницы 'создать объявление'"


def test_filtering_by_category(driver):
    driver.get("http://195.133.27.184/list/")
    category_dropdown= Select(driver.find_element(By.ID, "categorySelect"))
    category_dropdown.select_by_index(1)
    driver.find_element(By.XPATH, "//button[text()='Фильтровать']").click()

    cards_category = driver.find_elements(By.XPATH, "//div[@class='card-body']/h6")
    expected_text = "Английский язык"
    assert all(expected_text in card.text for card in cards_category)

