from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 5000

    def click(self, selector: str):
        self.page.click(selector, timeout=self.timeout)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text, timeout=self.timeout)

    def wait_for_selector(self, selector: str):
        self.page.wait_for_selector(selector, timeout=self.timeout)
