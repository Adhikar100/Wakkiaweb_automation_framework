from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)


@dataclass(frozen=True)
class Settings:
    env: str = os.getenv("ENV", "local")

    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    browser: str = os.getenv("BROWSER", "chromium")

    customer_base_url: str = os.getenv("CUSTOMER_BASE_URL", "")
    customer_user: str = os.getenv("CUSTOMER_USER", "")
    customer_pass: str = os.getenv("CUSTOMER_PASS", "")

    dashboard_base_url: str = os.getenv("DASHBOARD_BASE_URL", "")
    admin_user: str = os.getenv("ADMIN_USER", "")
    admin_pass: str = os.getenv("ADMIN_PASS", "")

    db_host: str = os.getenv("DB_HOST", "")
    db_port: int = int(os.getenv("DB_PORT", "5432"))
    db_name: str = os.getenv("DB_NAME", "")
    db_user: str = os.getenv("DB_USER", "")
    db_password: str = os.getenv("DB_PASSWORD", "")
    db_ssl: bool = os.getenv("DB_SSL", "false").lower() == "true"


settings = Settings()
