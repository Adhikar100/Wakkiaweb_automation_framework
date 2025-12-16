# Web Automation Framework (Customer + Dashboard) - Playwright + Pytest (POM)

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

pip install -e .
playwright install
```

## Configure environment
- Copy `.env.example` to `.env`
- Set:
  - CUSTOMER_BASE_URL
  - DASHBOARD_BASE_URL
  - credentials (optional)

## Run tests
### Customer
```bash
pytest customer_app/tests -m customer
```

### Dashboard
```bash
pytest dashboard_app/tests -m dashboard
```

### Both
```bash
pytest
```

## Notes
- Customer and Dashboard are independent apps.
- Only shared/ contains reusable engine utilities.
