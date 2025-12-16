from playwright.sync_api import Page
from pathlib import Path
from datetime import datetime


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str, timeout: int = 60000) -> None:
        self.page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        self.page.wait_for_timeout(500)

    def screenshot(self, name: str) -> str:
        Path("artifacts/screenshots").mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"artifacts/screenshots/{name}_{ts}.png"
        self.page.screenshot(path=path, full_page=True)
        return path
