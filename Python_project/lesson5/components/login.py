import allure
from playwright.sync_api import Page


class Login:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Нажимаем кнопку 'Войти' в хедере")
    def click_login_button(self):
        self.page.get_by_text("Войти").click()

    @allure.step("Заполняем поле никнейм")
    def fill_nick(self, nick):
        self.page.get_by_placeholder("Введите имя пользователя").fill(nick)

    @allure.step("Заполняем пароль")
    def fill_password(self,password):
        self.page.get_by_placeholder("Введите пароль").fill(password)


    @allure.step("Нажимаем кнопку 'Войти")
    def click_enter_button(self):
        self.page.locator('//button[@type="submit"]').click()


