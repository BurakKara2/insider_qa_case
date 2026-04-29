from base.base_page import BasePage

class HomePage(BasePage):
    # Locators
    URL = "https://insiderone.com/"
    ACCEPT_COOKIES_BTN = "#accept-cookies" 
    CAREERS_MENU = "a[href='/careers/']" 

    def __init__(self, page):
        # Navigate to the page first, then initialize the base class to trigger check()
        page.goto(self.URL)
        super().__init__(page)

    def check(self):
        # Verify page readiness according to the architectural pattern
        self.page.wait_for_load_state("networkidle")
        # Ensure the core navigation element is visible before proceeding
        self.page.wait_for_selector(self.CAREERS_MENU, state="visible")

    # Action Methods
    def navigate_to_careers(self):
        # Navigate to the Careers section
        self.wait_and_click(self.CAREERS_MENU)
        return self # Return self to support fluent pattern