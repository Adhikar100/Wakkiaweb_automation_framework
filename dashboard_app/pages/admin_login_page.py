from __future__ import annotations

from pathlib import Path
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import Error as PlaywrightError

from shared.core.base_page import BasePage
from shared.core.config import settings


class AdminLoginPage(BasePage):
    INPUT_EMAIL_OR_PHONE = '//input[@placeholder="Enter your email or phone"]'
    INPUT_PASSWORD = '//input[@placeholder="Enter your password"]'
    BTN_LOGIN = '//button[normalize-space()="Login"]'

    def open(self) -> None:
        base = settings.dashboard_base_url.rstrip("/")
        dashboard_url = f"{base}/en/dashboard/admin"
        fallback_login_url = f"{base}/en/login"

        # Debug listeners (optional)
        self.page.on("console", lambda msg: print(f"[BROWSER:{msg.type}] {msg.text}"))
        self.page.on("pageerror", lambda err: print(f"[PAGEERROR] {err}"))
        self.page.on("requestfailed", lambda req: print(f"[REQFAILED] {req.url} -> {req.failure}"))

        try:
            print(f"🌐 Opening dashboard: {dashboard_url}")
            self.page.goto(dashboard_url, wait_until="domcontentloaded", timeout=60000)
        except PlaywrightError as e:
            print(f"⚠️ Dashboard open failed: {e}")
            print(f"🌐 Trying fallback login URL: {fallback_login_url}")
            try:
                self.page.goto(fallback_login_url, wait_until="domcontentloaded", timeout=60000)
            except PlaywrightError as e2:
                shot = self.screenshot("dashboard_open_net_failed")
                raise AssertionError(
                    "❌ Network/Reachability issue.\n\n"
                    f"Dashboard URL failed: {dashboard_url}\n"
                    f"Fallback URL failed: {fallback_login_url}\n\n"
                    f"Error1: {e}\n"
                    f"Error2: {e2}\n\n"
                    f"Screenshot: {Path(shot).resolve()}"
                )

        try:
            self.page.locator(self.INPUT_EMAIL_OR_PHONE).wait_for(state="visible", timeout=20000)
        except PlaywrightTimeoutError:
            shot = self.screenshot("login_form_not_found")
            raise AssertionError(
                "❌ Open succeeded but login form not visible.\n"
                f"Current URL: {self.page.url}\n"
                f"Screenshot: {Path(shot).resolve()}"
            )

    def login(self, email_or_phone: str, password: str) -> None:
        self.open()
        self.page.locator(self.INPUT_EMAIL_OR_PHONE).fill(email_or_phone)
        self.page.locator(self.INPUT_PASSWORD).fill(password)
        self.page.locator(self.BTN_LOGIN).click()
        self._verify_login_result()

    def _verify_login_result(self) -> None:
        try:
            self.page.wait_for_url(lambda url: "/login" not in url, timeout=20000)
            return
        except PlaywrightTimeoutError:
            shot = self.screenshot("dashboard_login_failed")
            raise AssertionError(
                "❌ Dashboard login failed.\n\n"
                f"Still on: {self.page.url}\n\n"
                "Possible reasons:\n"
                "- Invalid credentials\n"
                "- OTP/MFA required\n"
                "- CAPTCHA enabled\n"
                "- Role restriction\n\n"
                f"Screenshot: {Path(shot).resolve()}"
            )
