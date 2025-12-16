import pytest
from customer_app.flows.auth_flows import CustomerAuthFlows

@pytest.mark.customer
@pytest.mark.smoke
def test_customer_login_smoke(page):
    flows = CustomerAuthFlows(page)
    flows.login_default_user()

    # Example assertion - adjust to your app
    # assert "/home" in page.url
