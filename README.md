# Automation Framework (Playwright + Pytest)

Lightweight and scalable QA automation framework built with **Playwright (sync API)** and **Pytest**.

The framework follows **Page Object Model (POM)** principles and includes logging, failure screenshots, and a clean separation between UI and API tests.

Designed to be **maintainable, readable, and easily extensible**.

---

# Test Application

Demo test application used for automation:

https://www.automationexercise.com/

---

# Tech Stack

- Python 3.12
- Playwright (sync API)
- Pytest
- Python logging module

---

# Project Structure

```
Automation Framework
    │
    ├── fixtures        # Playwright browser and API fixtures
    ├── pages           # Page Object Model implementation
    ├── tests
    │ ├── api           # API tests
    │ └── ui            # UI end-to-end tests
    │
    ├── utils           # Configuration, logging and test data
    ├── artifacts       # Logs and screenshots generated during test execution
    │
    ├── pytest.ini
    ├── requirements.txt
    └── README.md
```

---

## Folder Description

- **fixtures/** – Playwright browser and API fixtures shared across tests
- **pages/** – Page Object Model classes encapsulating UI interactions
- **tests/** – Test suites organized by type (UI / API)
- **utils/** – Shared utilities such as logging configuration, test data and global configuration
- **artifacts/** – Execution artifacts including logs and failure screenshots

---

# Design Notes

The framework is intentionally kept small and focused for the scope of the task.

UI and API tests are separated to keep browser-specific setup independent from API-only execution.

Shared setup is managed through fixtures, while UI interactions are encapsulated using the Page Object Model.
The structure is designed to stay simple for the current scope, but also easy to extend if the test suite grows.

---

# Features

## Page Object Model (POM)

UI interactions are encapsulated inside page classes to improve maintainability, readability and reuse.

Each page object exposes high-level actions instead of raw locator operations.

---

## Logging

The framework includes centralized logging using Python's `logging` module.

Logs provide clear insight into test execution flow.

Example log output:
```
2026-03-07 14:22:17 | INFO | test_login_and_logout | Starting login and logout test
```

Logs are stored in:
```
artifacts/logs/
```

## Screenshots on Failure

UI tests automatically capture screenshots when a failure occurs.

Screenshots are saved to:
```
artifacts/screenshots/
```

This helps identify UI issues and speeds up debugging.

---

## Test Markers

Tests are organized using Pytest markers.

Available markers:
```
smoke
e2e
ui
api
```
Example:

```python
@pytest.mark.ui
@pytest.mark.e2e
```

Markers allow flexible test execution and filtering.

# Requirements

- Python 3.12+

# Setup

Create a virtual environment:

```bash
py -3.12 -m venv venv
```

Activate environment:

Windows:
```bash
venv\Scripts\activate
```
macOS / Linux:
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

---

# Run Tests

Run all tests:

```bash
pytest
```

Run only UI tests:

```bash
pytest -m ui
```

Run only API tests:

```bash
pytest -m api
```

Run tests with console logs:

```bash
pytest -s
```

---

# Example Test Coverage

The framework currently includes both UI and API tests.

## UI tests

- Homepage load verification
- Login and logout flow
- Product search and add-to-cart
- User registration flow

## API tests

Retrieve brands list (`GET /api/brandsList`)

---

# Observations

During implementation of the logout scenario, the task description mentions that the user should be redirected to the homepage after logout.

However, the current application behavior redirects the user to the login page instead.

The test implementation follows the actual behavior of the application. In a real project this would typically be clarified with the product owner or development team.

---

# Future Improvements

Potential improvements for further framework evolution:

- Parallel test execution with pytest-xdist
- Shared UI components (e.g. navigation bar)
- CI integration (e.g. Jenkins or similar)
- HTML test reports
- Environment configuration support

---

# Author

Mirko Milanovic
Automation QA Engineer
