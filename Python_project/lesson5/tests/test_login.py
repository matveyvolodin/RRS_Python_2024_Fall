from time import sleep

import pytest


# Для запуска тестов логина необходимо закоментить фикстуры авторизации page и storage в conftest


def test_login_successful (header,login):
    """Удачная попытка входа при помощи существующего в базе логина и пароля"""
    header.visit()
    login.click_login_button()
    login.fill_nick("qa.volodin.test1")
    login.fill_password("Qazwsx1!")
    login.click_enter_button()
    login.click_profile_button()
    login.check_profile_header_text("Профиль: qa.volodin.test1")

@pytest.mark.negative
def test_login_wrong_password(header, login):
    """Попытка входа с использованием корректного логина и некорректного пароля"""
    header.visit()
    login.click_login_button()
    login.fill_nick("qa.volodin.test1")
    login.fill_password("Qwerty1@")
    login.click_enter_button()
    login.check_credentials_error_message_visibility()

@pytest.mark.negative
def test_login_wrong_nick(header, login):
    """Попытка входа с использованием некорректного логина и корректного пароля"""
    header.visit()
    login.click_login_button()
    login.fill_nick("Qwerty1@")
    login.fill_password("Qazwsx1!")
    login.click_enter_button()
    login.check_credentials_error_message_visibility()

@pytest.mark.negative
def test_login_wrong_nick(header, login):
    """Попытка входа с использованием корректного логина и пароля от разных учетных записей"""
    header.visit()
    login.click_login_button()
    login.fill_nick("qa.volodin.test1")
    login.fill_password("Qazwsx2!")
    login.click_enter_button()
    login.check_credentials_error_message_visibility()

@pytest.mark.negative
def test_login_empty_fields(header, login):
    """Попытка авторизации с пустыми полями логина/пароля"""
    header.visit()
    login.click_login_button()
    login.fill_nick("")
    login.fill_password("")
    login.click_enter_button()
    login.check_login_is_mandatory_message()
    login.check_password_is_mandatory_message()

