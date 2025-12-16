# Waakia Web Automation Framework

A **scalable, maintainable, end-to-end web automation testing framework** built using **Playwright + Pytest (Python)**. This framework is designed to test **complex fintech and digital service platforms** such as **Waakia / KiiBank**, where reliability, security, and consistency are critical.

The framework supports **multi-application testing**, clean architecture, environment-based configuration, reusable components, and **CI/CD‑friendly execution**, making it suitable for both **enterprise QA teams** and **production-grade automation projects**.

---

## Key Features

* ✅ **Playwright (Python)** for fast, stable, and modern browser automation
* ✅ **Pytest** for structured test execution, grouping, and reporting
* ✅ **Page Object Model (POM)** for clean, maintainable tests
* ✅ **Multi‑application support** (Admin/Dashboard & Customer apps)
* ✅ **Environment‑based configuration** using `.env`
* ✅ **PowerShell runner scripts** for quick local execution
* ✅ **CI/CD‑ready project layout**
* ✅ **Reusable shared utilities and fixtures**
* ✅ **Extensible for API and database validation**

---

## Project Structure

```
WaakiaWeb_automation_framework/
│
├── artifacts/                  # Screenshots, logs, raw artifacts
├── ci/                         # CI/CD configs (GitHub Actions, pipelines)
│
├── customer_app/               # Customer-facing application automation
│   ├── pages/                  # Page Objects
│   └── tests/                  # Test cases
│
├── dashboard_app/              # Admin / Dashboard automation
│   ├── pages/                  # Page Objects
│   └── tests/                  # Test cases
│
├── shared/                     # Shared framework components
│   ├── base_page.py            # Base Playwright page
│   ├── browser_manager.py      # Browser lifecycle management
│   ├── config.py               # Environment & config loader
│   └── helpers.py              # Common helper utilities
│
├── testdata/                   # Static test data (JSON / CSV)
├── reports/                    # Execution reports
│
├── .env                        # Local environment config (NOT committed)
├── .env.example                # Sample environment config
├── .gitignore                  # Git ignore rules
│
├── init_env.py                 # Environment bootstrap
├── init_framework.py           # Framework initialization logic
├── main.py                     # Optional entry point
│
├── check_postgres_connection.py # Database connectivity check
│
├── run_all_tests.ps1           # Run all tests
├── run_customer_tests.ps1      # Run customer app tests
├── run_dashboard_tests.ps1     # Run dashboard app tests
│
├── pytest.ini                  # Pytest configuration
├── pyproject.toml              # Python project configuration
└── README.md                   # Project documentation
```

---

## Framework Design Principles

### 1⃣ Page Object Model (POM)

* Each page is represented by a dedicated class
* UI locators and actions are encapsulated
* Test cases remain clean, readable, and business‑focused

### 2⃣ Separation of Concerns

* **Tests** → What to test (business scenarios)
* **Pages** → How the UI behaves
* **Shared** → Browser setup, config, helpers

### 3⃣ Environment Safety

* ❌ No hard‑coded credentials
* ✅ Secrets loaded from `.env`
* ✅ `.env.example` provided for onboarding

---

## Tech Stack

| Tool           | Purpose                        |
| -------------- | ------------------------------ |
| Python 3.10+   | Programming language           |
| Playwright     | Browser automation             |
| Pytest         | Test execution framework       |
| PowerShell     | Execution scripts (Windows)    |
| PostgreSQL     | Database validation (optional) |
| GitHub Actions | CI/CD automation (optional)    |

---

## Getting Started

### 1⃣ Prerequisites

* Python **3.10+**
* Node.js **18+** (required by Playwright)
* Git
* PowerShell (Windows)

---

### 2⃣ Clone the Repository

```bash
git clone https://github.com/Adhikar100/waakiaweb_automation_framework.git
cd WaakiaWeb_automation_framework
```

---

### 3⃣ Create & Activate Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

### 4⃣ Install Dependencies

```powershell
pip install -r requirements.txt
playwright install
```

---

### 5⃣ Configure Environment Variables

> ⚠ **Never commit `.env` files to GitHub**

---

## Running Tests

### Run all tests

```powershell
.\run_all_tests.ps1
```

### Run dashboard tests

```powershell
.\run_dashboard_tests.ps1
```

### Run customer app tests

```powershell
.\run_customer_tests.ps1
```

---

## Running Tests via Pytest

```powershell
pytest
```

Using markers:

```powershell
pytest -m dashboard
pytest -m customer
```

---

## Reports & Artifacts

* 📸 Screenshots on failure → `artifacts/`
* 📄 Test execution reports → `reports/`
* 🧵 Playwright traces (optional)

---

## Database Validation (Optional)

Validate PostgreSQL connectivity:

```powershell
python check_postgres_connection.py
```

Used for:

* Campaign data verification
* Transaction consistency checks
* Backend vs UI validation

---

## CI/CD Ready

The framework is structured to support:

* GitHub Actions
* Azure DevOps Pipelines
* Jenkins

Easily extendable for:

* Pull request validation
* Nightly regression runs
* Automated report publishing

---

## Security Best Practices

* ✅ No secrets committed to the repository
* ✅ `.env` excluded via `.gitignore`
* ✅ Secrets configurable via CI/CD variables

---

## Author

**Adhikar Chaudhary**
Senior Software QA Engineer 
GitHub: [https://github.com/Adhikar100](https://github.com/Adhikar100)

---

## Future Enhancements

* API automation integration
* Allure / HTML reporting
* Dockerized execution
* Cross‑browser parallel runs
* Advanced test‑data factory

---

## Why This Framework?

* Built from **real fintech production experience**
* Designed for **scalability and long‑term maintenance**
* Suitable for **enterprise‑grade QA teams**
* Clean, professional, and **interview‑ready automation project**

