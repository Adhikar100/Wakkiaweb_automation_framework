from __future__ import annotations

from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return  # don't overwrite if already present
    path.write_text(content, encoding="utf-8")


def main() -> None:
    # -------------------------
    # Root: .gitignore
    # -------------------------
    write_file(ROOT / ".gitignore", dedent("""\
        # Python
        __pycache__/
        *.py[cod]
        *.pyd
        .Python
        .venv/
        venv/
        .env
        .pytest_cache/
        .ruff_cache/

        # IDEs
        .idea/
        .vscode/

        # Reports / Artifacts
        reports/
        artifacts/
        allure-results/
        allure-report/

        # OS
        Thumbs.db
        Desktop.ini
    """))

    # -------------------------
    # Shared core: logger/assertions/utils (missing)
    # -------------------------
    write_file(ROOT / "shared/core/logger.py", dedent("""\
        from __future__ import annotations
        import logging
        from pathlib import Path
        from datetime import datetime

        LOG_DIR = Path("reports") / "logs"
        LOG_DIR.mkdir(parents=True, exist_ok=True)

        def get_logger(name: str = "automation") -> logging.Logger:
            logger = logging.getLogger(name)
            if logger.handlers:
                return logger

            logger.setLevel(logging.INFO)

            fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

            # Console handler
            ch = logging.StreamHandler()
            ch.setFormatter(fmt)
            logger.addHandler(ch)

            # File handler
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            fh = logging.FileHandler(LOG_DIR / f"{name}_{ts}.log", encoding="utf-8")
            fh.setFormatter(fmt)
            logger.addHandler(fh)

            return logger
    """))

    write_file(ROOT / "shared/core/assertions.py", dedent("""\
        from __future__ import annotations
        from playwright.sync_api import Page, expect

        def assert_url_contains(page: Page, fragment: str) -> None:
            expect(page).to_have_url(lambda url: fragment in url)

        def assert_text_visible(page: Page, text: str) -> None:
            expect(page.get_by_text(text)).to_be_visible()

        def assert_locator_visible(page: Page, selector: str) -> None:
            expect(page.locator(selector)).to_be_visible()
    """))

    write_file(ROOT / "shared/core/utils.py", dedent("""\
        from __future__ import annotations
        import os
        from pathlib import Path

        def ensure_dir(path: str | Path) -> Path:
            p = Path(path)
            p.mkdir(parents=True, exist_ok=True)
            return p

        def env_bool(key: str, default: bool = False) -> bool:
            val = os.getenv(key)
            if val is None:
                return default
            return val.strip().lower() in {"1", "true", "yes", "y", "on"}
    """))

    # -------------------------
    # Shared reporting placeholders
    # -------------------------
    write_file(ROOT / "shared/reporting/allure_helpers.py", dedent("""\
        from __future__ import annotations

        # Optional: enable later if you install allure-pytest.
        # This file is a placeholder for reporting helpers.
        #
        # Example (after installing allure-pytest):
        # import allure
        #
        # def attach_text(name: str, text: str):
        #     allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)
    """))

    write_file(ROOT / "shared/reporting/attachments.py", dedent("""\
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
    """))

    # -------------------------
    # Shared data placeholders
    # -------------------------
    write_file(ROOT / "shared/data/faker_utils.py", dedent("""\
        from __future__ import annotations
        import random
        import string

        def random_email(domain: str = "example.com") -> str:
            user = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
            return f"{user}@{domain}"

        def random_phone(prefix: str = "98") -> str:
            rest = "".join(random.choices(string.digits, k=8))
            return f"{prefix}{rest}"
    """))

    write_file(ROOT / "shared/data/generators.py", dedent("""\
        from __future__ import annotations
        from dataclasses import dataclass
        from .faker_utils import random_email

        @dataclass
        class UserData:
            email: str
            password: str

        def generate_user(password: str = "Password123!") -> UserData:
            return UserData(email=random_email(), password=password)
    """))

    # -------------------------
    # Customer + Dashboard configs/env.yaml + testdata json
    # -------------------------
    write_file(ROOT / "customer_app/configs/env.yaml", dedent("""\
        env: local
        base_url: ${CUSTOMER_BASE_URL}
        headless: ${HEADLESS}
        browser: ${BROWSER}
    """))

    write_file(ROOT / "dashboard_app/configs/env.yaml", dedent("""\
        env: local
        base_url: ${DASHBOARD_BASE_URL}
        headless: ${HEADLESS}
        browser: ${BROWSER}
    """))

    write_file(ROOT / "customer_app/configs/testdata/customer_users.json", dedent("""\
        {
          "default_customer": {
            "username": "testuser@example.com",
            "password": "password123"
          }
        }
    """))

    write_file(ROOT / "dashboard_app/configs/testdata/admin_users.json", dedent("""\
        {
          "default_admin": {
            "email": "admin@example.com",
            "password": "password123"
          }
        }
    """))

    # -------------------------
    # Optional API folders placeholders
    # -------------------------
    for app in ("customer_app", "dashboard_app"):
        write_file(ROOT / app / "api" / "__init__.py", "")
        write_file(ROOT / app / "api" / "client.py", dedent("""\
            # Placeholder for API client helpers (requests/httpx).
            # Keep API logic app-specific (customer vs dashboard).
        """))
        write_file(ROOT / app / "api" / "endpoints.py", dedent("""\
            # Placeholder for API endpoint paths/constants.
        """))

    # -------------------------
    # CI Dockerfile placeholder
    # -------------------------
    write_file(ROOT / "ci" / "Dockerfile", dedent("""\
        # Optional Docker image for running tests in CI
        FROM python:3.11-slim

        WORKDIR /app
        COPY . /app

        RUN pip install --no-cache-dir pytest pytest-xdist python-dotenv playwright \\
            && python -m playwright install --with-deps

        CMD ["pytest"]
    """))

    # -------------------------
    # PowerShell run scripts (terminal-friendly)
    # -------------------------
    write_file(ROOT / "run_customer_tests.ps1", dedent(r"""\
        param(
          [string]$Marker = "customer",
          [switch]$Headed,
          [switch]$Trace
        )

        if (-not (Test-Path ".venv")) {
          Write-Host "❌ .venv not found. Create venv first." -ForegroundColor Red
          exit 1
        }

        $env:PYTHONPATH="."
        if ($Headed) { $env:HEADLESS="false" }

        # Optional trace toggle (you can wire this later into browser_factory)
        if ($Trace) { $env:TRACE="true" }

        pytest customer_app/tests -m $Marker
    """))

    write_file(ROOT / "run_dashboard_tests.ps1", dedent(r"""\
        param(
          [string]$Marker = "dashboard",
          [switch]$Headed,
          [switch]$Trace
        )

        if (-not (Test-Path ".venv")) {
          Write-Host "❌ .venv not found. Create venv first." -ForegroundColor Red
          exit 1
        }

        $env:PYTHONPATH="."
        if ($Headed) { $env:HEADLESS="false" }
        if ($Trace) { $env:TRACE="true" }

        pytest dashboard_app/tests -m $Marker
    """))

    write_file(ROOT / "run_all_tests.ps1", dedent(r"""\
        param(
          [string]$Marker = "",
          [switch]$Headed,
          [int]$Workers = 0
        )

        $env:PYTHONPATH="."
        if ($Headed) { $env:HEADLESS="false" }

        $xdist = ""
        if ($Workers -gt 0) { $xdist = "-n $Workers" }

        if ($Marker -ne "") {
          pytest $xdist -m $Marker
        } else {
          pytest $xdist
        }
    """))

    print("\n✅ Missing parts created successfully.")
    print("Next: run scripts like:  .\\run_customer_tests.ps1  or  .\\run_dashboard_tests.ps1")


if __name__ == "__main__":
    main()
