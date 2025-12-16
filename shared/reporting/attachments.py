from __future__ import annotations
from pathlib import Path
from playwright.sync_api import Page
from datetime import datetime

ARTIFACTS = Path("artifacts")
SCREENSHOTS = ARTIFACTS / "screenshots"
TRACES = ARTIFACTS / "traces"
VIDEOS = ARTIFACTS / "videos"

for d in (SCREENSHOTS, TRACES, VIDEOS):
    d.mkdir(parents=True, exist_ok=True)

def save_screenshot(page: Page, name_prefix: str = "shot") -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = SCREENSHOTS / f"{name_prefix}_{ts}.png"
    page.screenshot(path=str(path), full_page=True)
    return path
