from __future__ import annotations

from dashboard_app.pages.admin_login_page import AdminLoginPage
from shared.core.config import settings


class AdminAuthFlows:
    def __init__(self, page):
        self.login_page = AdminLoginPage(page)

    def login_super_admin(self) -> None:
        # Use .env credentials (don’t hardcode)
        self.login_page.login(
            email_or_phone=settings.admin_user,
            password=settings.admin_pass,
        )
