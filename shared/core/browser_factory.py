from __future__ import annotations
from playwright.sync_api import sync_playwright, Browser, BrowserContext
from .config import settings

def _launch_browser(p) -> Browser:
    b = settings.browser.lower()
    if b == "firefox":
        return p.firefox.launch(headless=settings.headless)
    if b == "webkit":
        return p.webkit.launch(headless=settings.headless)
    return p.chromium.launch(headless=settings.headless)

def new_context(base_url: str) -> tuple[sync_playwright, Browser, BrowserContext]:
    p = sync_playwright().start()
    browser = _launch_browser(p)
    context = browser.new_context(base_url=base_url)
    return p, browser, context
