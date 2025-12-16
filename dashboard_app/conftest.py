import pytest
from shared.core.browser_factory import new_context
from shared.core.config import settings


@pytest.fixture(scope="function")
def page():
    p, browser, context = new_context(settings.customer_base_url)
    page = context.new_page()

    #  REQUIRED for BasePage.goto() resolver
    page.base_url = settings.customer_base_url

    yield page

    context.close()
    browser.close()
    p.stop()
