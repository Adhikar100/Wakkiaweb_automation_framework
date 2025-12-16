from shared.core.config import settings
from customer_app.pages.login_page import CustomerLoginPage

class CustomerAuthFlows:
    def __init__(self, page):
        self.page = page
        self.login_page = CustomerLoginPage(page)

    def login_default_user(self):
        self.login_page.open()
        self.login_page.login(settings.customer_user, settings.customer_pass)
