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


    @allure.step("Нажимаем кнопкеу 'Профиль")
    def click_profile_button(self):
        profile_button = self.page.locator("//a[@data-testid='profile']")
        profile_button.wait_for(state="visible", timeout=5000)
        profile_button.click()


    @allure.step("Проверяем наличие хедера 'Профиль: qa.volodin.test1'")
    def check_profile_header_text(self, header):
        profile_header =  self.page.locator("//h2")
        profile_header_text = profile_header.text_content()
        if not profile_header_text == header:
            raise ValueError("Текст хедера не соответствует ожидаемому")

    @allure.step("Проверяем наличие сообщения об ошибке ввода данных")
    def check_credentials_error_message_visibility(self):
        message = self.page.locator("//ul[@class='errorlist nonfield']/li")
        if not message.is_visible():
            raise ValueError("Сообщение об ошибке логина отсутствует на странице")

    @allure.step("Проверяем наличие сообщения'Обязательное поле' в поле логина")
    def check_login_is_mandatory_message(self):
        if not self.page.locator("(//ul[@class='errorlist']/li)[1]").is_visible():
            raise Exception("Сообщение 'Обязательное поле' отсутсвует на странице")

    @allure.step("Проверяем наличие сообщения'Обязательное поле' в поле пароля")
    def check_password_is_mandatory_message(self):
        if not self.page.locator("(//ul[@class='errorlist']/li)[2]").is_visible():
            raise Exception("Сообщение 'Обязательное поле' отсутсвует на странице")