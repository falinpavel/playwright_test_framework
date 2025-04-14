from pages.base_page import BasePage


class HomePage(BasePage):

    def goto(self):
        self.page.goto("https://playwright.dev/")
