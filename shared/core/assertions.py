from __future__ import annotations
from playwright.sync_api import Page, expect

def assert_url_contains(page: Page, fragment: str) -> None:
    expect(page).to_have_url(lambda url: fragment in url)

def assert_text_visible(page: Page, text: str) -> None:
    expect(page.get_by_text(text)).to_be_visible()

def assert_locator_visible(page: Page, selector: str) -> None:
    expect(page.locator(selector)).to_be_visible()
