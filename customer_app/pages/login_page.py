from shared.core.base_page import BasePage

class CustomerLoginPage(BasePage):
    # Replace locators with your real app locators (prefer data-test-id)
    USERNAME = "[data-test-id='username']"
    PASSWORD = "[data-test-id='password']"
    LOGIN_BTN = "[data-test-id='login']"

    def open(self):
        self.goto("/login")

    def login(self, username: str, password: str):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
