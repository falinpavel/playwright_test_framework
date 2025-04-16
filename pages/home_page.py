from pages.base_page import BasePage


class HomePage(BasePage):

    def go_to_page(self):
        self.page.goto("https://playwright.dev/")
