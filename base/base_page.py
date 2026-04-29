from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.check() # Bootcamp rule: check() must be executed as soon as the page is instantiated

    def check(self):
        """
        Each page should override this method to wait for its core elements to load.
        """
        pass

    def wait_and_click(self, locator: str):
        # Playwright's smart wait instead of a hardcoded sleep
        self.page.wait_for_selector(locator, state="visible")
        self.page.locator(locator).click()