import pytest
from dashboard_app.flows.admin_auth_flows import AdminAuthFlows

@pytest.mark.dashboard
@pytest.mark.smoke
def test_dashboard_login_smoke(page):
    flows = AdminAuthFlows(page)
    flows.login_default_admin()

    # Example assertion - adjust to your app
    # assert "/dashboard" in page.url
