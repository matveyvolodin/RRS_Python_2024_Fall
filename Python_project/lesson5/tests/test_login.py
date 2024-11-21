

def test_login (header,login):
    # Для запуска этого теста необходимо отключать фикстуру авторизации
    header.visit()
    login.click_login_button()
    login.fill_nick("qa.volodin.test1")
    login.fill_password("Qazwsx1!")
    login.click_enter_button()

def test_create_listing_is_presented(header,page):
    header.visit()
    page.get_by_test_id("from playwright.sync_api import Pa").is_visible()
