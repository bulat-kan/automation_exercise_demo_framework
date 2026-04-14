# Python Playwright UI Automation Demo

This project is a demo Python UI automation framework built with:

- `pytest`
- `Playwright`
- Page Object Model

The project is focused on end-to-end and smoke-style UI testing against a public practice web application.

## What This Project Covers

- homepage smoke tests
- login and signup flows
- products page behavior
- product details behavior
- cart behavior
- cross-feature user journeys
- reusable page objects and flow helpers

## Tech Stack

- Python 3.11
- pytest
- Playwright
- Faker

## Project Structure

```text
automation_exercise_sdet/
  pages/
    login_page.py
    signup_page.py
    products_page.py
    product_details_page.py
  tests/
    ui/
      conftest.py
      test_homepage.py
      test_auth_smoke.py
      test_signup_flow.py
      test_products_smoke.py
      test_product_details.py
      test_cart_smoke.py
      test_user_journeys.py
  utils/
    cart_helpers.py
    helpers.py
  requirements.txt
  pytest.ini
  README.md
```

## Setup

### 1. Create virtual environment

```bash
python3 -m venv .venv
```

### 2. Activate virtual environment

macOS / Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

## How To Run Tests

Run all tests:

```bash
python -m pytest -v
```

Run one file:

```bash
python -m pytest -v tests/ui/test_signup_flow.py
```

Run one test:

```bash
python -m pytest -v tests/ui/test_product_details.py::test_user_can_add_product_from_product_details
```

Run tests by keyword:

```bash
python -m pytest -k signup -v
```

## Notes

- The project uses a shared Playwright `page` fixture in `tests/ui/conftest.py`
- The framework uses small page objects only when repetition becomes meaningful
- Shared flow/state logic is kept in helper modules when it does not belong to a single page
- Some public demo sites may load ads or interstitials, so the project includes request blocking in shared Playwright setup to improve stability

## Current Focus

This project is being built as a learning and portfolio-oriented SDET framework with emphasis on:

- clean test organization
- practical Playwright usage
- page object design judgment
- reusable helpers
- stable assertions and flows
