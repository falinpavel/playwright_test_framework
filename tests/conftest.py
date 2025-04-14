import pytest
from playwright.sync_api import Browser, Page
from utils.logger import logger


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and "page" in item.funcargs:
        page = item.funcargs["page"]
        screenshot = page.screenshot()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
