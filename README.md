# Playwright POM Framework

[![Playwright Tests](https://github.com/criptic87/Playwright-POM-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/criptic87/Playwright-POM-framework/actions/workflows/tests.yml)

A QA automation framework built with Python, Playwright, and pytest. Demonstrates UI automation, API testing, network mocking, and the Page Object Model pattern.

## Tech stack

- **Python 3.12** — primary language
- **Playwright** — browser automation and API testing
- **pytest** — test runner, fixtures, parametrization
- **GitHub Actions** — continuous integration

## Architecture

The framework follows the Page Object Model. Each page of the application is represented by a class containing its selectors and actions. Tests interact with these classes rather than raw Playwright calls, which keeps tests readable and maintenance centralized.

Fixtures in `conftest.py` provide shared setup: page objects pre-navigated and ready, test data loaded from JSON, and sensible default timeouts applied to every test.

## What's covered

- UI tests across multiple page flows (login, secure area, checkboxes, dropdown)
- API testing using Playwright's request context
- Network mocking via `page.route()` to simulate server responses
- Parametrized tests for data-driven scenarios
- Automatic failure artifacts (screenshots, videos, Playwright traces)
- CI pipeline running the full suite on every push and pull request

## Running the tests

```bash
pip install -r requirements.txt
playwright install chromium
pytest
```

Headed mode (watch the browser work):
```bash
pytest --headed
```

## Project structure

- `pages/` — Page Object classes
- `tests/` — test files, one per feature area
- `test_data/` — JSON test data, separated from test logic
- `conftest.py` — shared fixtures
- `pytest.ini` — pytest configuration including artifact capture

## Key design decisions

**Separation of concerns** — selectors and actions live in page objects, verifications in `should_*` methods, test data in JSON. Tests themselves only describe scenarios.

**Auto-waiting over hard waits** — timeout defaults are set globally in `conftest.py`; tests rely on Playwright's built-in waiting rather than `time.sleep`.

**Mocked over real for third-party calls** — network mocking makes the UI suite fast and deterministic. A separate contract-test layer would verify real API compatibility.