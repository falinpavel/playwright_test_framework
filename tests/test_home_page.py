import allure
from pages.home_page import HomePage


@allure.feature("Авторизация")
class TestHomePage:
    @allure.story("Успешный вход")
    def test_navigation(self, page):
        self.page = HomePage(page)
        self.page.goto()