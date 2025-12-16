import pytest
from dashboard_app.flows.admin_auth_flows import AdminAuthFlows
from dashboard_app.flows.category_management_flows import CategoryManagementFlows

@pytest.mark.dashboard
def test_add_category_with_image_and_names(page):
    AdminAuthFlows(page).login_super_admin()
    CategoryManagementFlows(page).add_categories_with_image_and_service_type()
