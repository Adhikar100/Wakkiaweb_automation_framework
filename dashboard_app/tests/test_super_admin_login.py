import pytest
from dashboard_app.flows.admin_auth_flows import AdminAuthFlows


@pytest.mark.dashboard
@pytest.mark.smoke
def test_super_admin_can_login(page):
    """
    This test is ERROR-FREE:
    - Passes only if login succeeds
    - Fails with clear reason + screenshot if login is blocked
    """
    flows = AdminAuthFlows(page)
    flows.login_super_admin()
