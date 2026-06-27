# Vidhyan Playwright Automation

This repository contains a `Playwright + Python + Pytest` automation framework for the Vidhyan web application.

The project is currently in a starter-to-growing phase. It already has working login, authentication, navigation, student, teacher, and basic dashboard coverage, and it is structured to expand into a broader end-to-end automation suite.

## Application Overview

Vidhyan is a school management platform that includes functional areas such as:

- Authentication and access control
- Dashboard and operational overview
- Students and guardians
- Teachers
- Staff
- Academics
- Attendance
- Fees and finance modules
- Setup, users, and settings

This repository is intended to automate these browser workflows end to end.

## Current Automation Coverage

Based on the current repository contents, the implemented automation currently covers:

- Login page validation
- Valid and invalid authentication flows
- Forgot password navigation checks
- Left navigation verification for major modules
- Dashboard widget visibility checks
- Student module landing and action entry points
- Teacher module landing and action entry points

## Repository Structure

```text
vidhyan_automation_repo2/
├── config/
│   └── config.json
├── pages/
│   └── login_page.py
├── tests/
│   ├── test_auth.py
│   ├── test_dash_.py
│   ├── test_nav.py
│   ├── test_student.py
│   └── test_teacher.py
├── conftest.py
├── requirements.txt
├── test_demo.py
└── README.md
```

## Framework Components

### `config/config.json`

Stores environment-specific values such as:

- application URL
- dashboard URL
- school code
- username/email
- password
- negative test input values

### `pages/login_page.py`

Contains the current page object used for:

- login actions
- forgot password actions
- left-navigation actions
- dashboard element references
- student module element references
- teacher module element references

At the moment, this is a single large page object used across multiple modules.

### `conftest.py`

Provides shared fixtures for:

- loading configuration
- creating the login page object
- creating a logged-in session for authenticated tests

### `tests/`

Contains the executable test cases:

- `test_auth.py` for authentication flows
- `test_dash_.py` for dashboard checks
- `test_nav.py` for module navigation checks
- `test_student.py` for student-area checks
- `test_teacher.py` for teacher-area checks

## Tech Stack

- `Python`
- `Pytest`
- `Playwright`
- `pytest-playwright`
- `pytest-html`
- `pytest-xdist`
- `pytest-rerunfailures`
- `allure-pytest`

Supporting libraries already included:

- `requests`
- `faker`
- `pyyaml`
- `pandas`
- `openpyxl`
- `python-dotenv`

## Setup Instructions

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

```bash
playwright install
```

## How To Run

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_auth.py
```

Run a single test:

```bash
pytest tests/test_nav.py -k test_nav_002
```

Generate HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## Current Design Notes

This framework currently follows a simple approach:

- one shared page object for multiple modules
- direct config loading from JSON
- fixture-based login reuse
- straightforward UI assertions using Playwright `expect`

This makes it beginner-friendly and easy to understand, especially while coverage is still growing.

## Recommended Next Evolution

As the suite grows, the next good improvements would be:

1. Split `login_page.py` into module-wise page objects such as `dashboard_page.py`, `students_page.py`, and `teachers_page.py`
2. Add a `base_page.py` for shared actions like click, navigation wait, and common assertions
3. Move secrets to `.env` or environment variables
4. Add `pytest.ini` for markers and standardized run options
5. Add smoke and regression grouping
6. Replace any fixed sleeps with Playwright-native waits where needed

## Goal of This Repository

The goal of this framework is to become a maintainable end-to-end automation suite for Vidhyan, starting from simple readable tests and gradually evolving into a scalable module-based framework.
