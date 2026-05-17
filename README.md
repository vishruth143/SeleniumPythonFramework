# 🌐 Selenium Python Framework

> **Enterprise-grade browser automation, visual testing, and API comparison framework** built with [Selenium WebDriver](https://www.selenium.dev/) and [pytest](https://docs.pytest.org/), written in Python 3.

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.44.0-green?logo=selenium)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-9.x-orange?logo=pytest)](https://docs.pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running Tests](#running-tests)
- [Module Documentation](#module-documentation)
  - [sauce\_demo (UI Tests)](#sauce_demo-ui-tests)
  - [launch\_browsers](#launch_browsers)
  - [waits](#waits)
  - [handle\_alert](#handle_alert)
  - [handle\_dropdown](#handle_dropdown)
  - [handle\_popup](#handle_popup)
  - [iframe](#iframe)
  - [takescreenshot](#takescreenshot)
  - [visual\_testing](#visual_testing)
  - [api\_comparison](#api_comparison)
- [Best Practices](#best-practices)
- [CI/CD Integration](#cicd-integration)
- [Contributing](#contributing)

---

## Overview

This framework demonstrates **professional browser automation** techniques using Selenium WebDriver's Python API. It covers all major web automation challenges encountered in enterprise QA environments:

| Capability | Description |
|---|---|
| 🌐 **Cross-Browser Testing** | Chrome, Firefox, Microsoft Edge |
| ⏱️ **Wait Strategies** | Implicit, Explicit, and Fluent waits |
| 🚨 **Alert Handling** | Simple alerts, JS confirms, and JS prompts |
| 📋 **Dropdown Handling** | Single-select and multi-select `<select>` elements |
| 🪟 **Popup / New Window Handling** | Window handle switching |
| 🖼️ **iFrame Handling** | Frame context switching |
| 📸 **Screenshots** | Viewport screenshot capture |
| 🎨 **Visual Testing** | Pixel-by-pixel baseline screenshot comparison |
| 🔌 **API Comparison** | Deep JSON response diffing with baseline capture |
| ✅ **UI Functional Tests** | Parameterized login tests against SauceDemo |

---

## Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.13 | Programming language |
| Selenium | 4.44.0 | Browser automation engine |
| pytest | 9.0.3 | Test runner & reporting |
| requests | 2.34.0 | HTTP API calls |
| Pillow | 12.2.0 | Image comparison for visual testing |
| deepdiff | latest | Deep JSON comparison for API testing |

---

## Project Structure

```
SeleniumPythonFramework/
│
├── selenium_practice/                          # All automation scripts & tests
│   │
│   ├── sauce_demo/                             # SauceDemo UI functional tests
│   │   └── test_login.py                       # Parameterized login tests for all users
│   │
│   ├── launch_browsers/                        # Browser launch demonstrations
│   │   ├── chrome_bowser_test.py               # Launch & interact with Google Chrome
│   │   ├── edge_browser_test.py                # Launch & interact with Microsoft Edge
│   │   └── firefox_browser_test.py             # Launch & interact with Mozilla Firefox
│   │
│   ├── waits/                                  # Selenium wait strategy demonstrations
│   │   ├── implicit_wait_in_selenium.py        # driver.implicitly_wait()
│   │   ├── explicit_wait_in_selenium.py        # WebDriverWait + expected_conditions
│   │   └── fluent_wait_in_selenium.py          # WebDriverWait with poll_frequency
│   │
│   ├── handle_alert/
│   │   └── alert_handle.py                     # Simple alert, JS Confirm & JS Prompt handling
│   │
│   ├── handle_dropdown/
│   │   └── handle_drop_down.py                 # Single-select and multi-select dropdowns
│   │
│   ├── handle_popup/
│   │   └── popup_handle.py                     # New window / tab popup handling
│   │
│   ├── iframe/
│   │   └── Iframe_handling.py                  # iFrame interaction via switch_to.frame()
│   │
│   ├── takescreenshot/
│   │   ├── screen_shot_handle.py               # Viewport screenshot capture
│   │   └── screenshots/                        # Auto-generated screenshot output folder
│   │
│   ├── broken_links/
│   │   └── broken_links.py                     # Broken link checker using requests
│   │
│   ├── visual_testing/                         # Visual regression testing
│   │   └── sauce_demo/
│   │       ├── conftest.py                     # Shared Chrome driver fixture
│   │       ├── site_config.py                  # Page URLs and config
│   │       ├── test_sauce_demo_visual_testing.py # Baseline capture & pixel comparison
│   │       ├── screenshots/                    # Saved screenshots per page
│   │       │   ├── login_page/
│   │       │   ├── inventory_page/
│   │       │   └── cart_page/
│   │       └── report/
│   │           └── visual_report.html          # Visual HTML report
│   │
│   └── api_comparison/                         # API response comparison testing
│       └── jsonplaceholder/
│           ├── conftest.py                     # Pytest fixtures & markers
│           ├── framework/
│           │   └── api_helpers.py              # API call, save & compare helpers
│           ├── tests/
│           │   ├── test_api_baseline.py        # STEP 1: capture baseline responses
│           │   └── test_api_compare.py         # STEP 2: compare responses vs baseline
│           ├── responses/                      # Saved JSON responses per endpoint
│           └── report/
│               └── api_report.html             # API comparison HTML report
│
├── requirements.txt                            # Python package dependencies
├── .gitignore                                  # Git ignore rules
└── README.md                                   # This file
```

---

## Prerequisites

Ensure the following are installed on your machine before proceeding:

- ✅ [Python 3.10+](https://www.python.org/downloads/) (3.13 recommended)
- ✅ [pip](https://pip.pypa.io/en/stable/)
- ✅ [Git](https://git-scm.com/)
- ✅ [Google Chrome](https://www.google.com/chrome/), [Firefox](https://www.mozilla.org/firefox/), or [Microsoft Edge](https://www.microsoft.com/edge) (matching browser driver required)
- ✅ [PyCharm](https://www.jetbrains.com/pycharm/) or any Python IDE (optional, recommended)

> **Note:** Selenium 4.6+ includes Selenium Manager which automatically downloads the correct browser driver. No manual ChromeDriver / GeckoDriver installation is needed for modern setups.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/SeleniumPythonFramework.git
cd SeleniumPythonFramework
```

### 2. Create & Activate Virtual Environment

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PyCharm (Optional)

To set **pytest** as the default test runner in PyCharm:

1. Open `File` → `Settings` → `Tools` → `Python Integrated Tools`
2. Under **Testing**, set **Default test runner** to `pytest`
3. Click **Apply** → **OK**

---

## Running Tests

### Run All Tests

```bash
pytest selenium_practice/ -v
```

### Run a Specific Test File

```bash
pytest selenium_practice/sauce_demo/test_login.py -v
```

### Run a Specific Test Function

```bash
pytest selenium_practice/sauce_demo/test_login.py::test_login -v
```

### Run Tests with HTML Report

```bash
pytest selenium_practice/ -v --html=reports/report.html --self-contained-html
```

> Install `pytest-html` first: `pip install pytest-html`

### Run Standalone Scripts (Non-pytest)

```bash
python selenium_practice/handle_alert/alert_handle.py
python selenium_practice/handle_dropdown/handle_drop_down.py
python selenium_practice/handle_popup/popup_handle.py
python selenium_practice/iframe/Iframe_handling.py
python selenium_practice/takescreenshot/screen_shot_handle.py
```

---

## Module Documentation

### `sauce_demo` (UI Tests)

Functional tests against [https://www.saucedemo.com](https://www.saucedemo.com).

| File | Description |
|---|---|
| `test_login.py` | Parameterized login tests for all 6 SauceDemo users, including locked-out user validation |

**Test users covered:**

| Username | Expected Outcome |
|---|---|
| `standard_user` | Successful login → inventory page |
| `locked_out_user` | Error message — "Sorry, this user has been locked out" |
| `problem_user` | Successful login (broken images) |
| `performance_glitch_user` | Successful login (slow response) |
| `error_user` | Successful login |
| `visual_user` | Successful login |

```bash
pytest selenium_practice/sauce_demo/test_login.py -v
```

---

### `launch_browsers`

Demonstrates how to launch and interact with different browsers using Selenium's WebDriver API.

| File | Browser | Key API |
|---|---|---|
| `chrome_bowser_test.py` | Google Chrome | `webdriver.Chrome()` |
| `edge_browser_test.py` | Microsoft Edge | `webdriver.Edge()` |
| `firefox_browser_test.py` | Mozilla Firefox | `webdriver.Firefox()` |

---

### `waits`

Demonstrates the three Selenium wait strategies.

| File | Strategy | Key API |
|---|---|---|
| `implicit_wait_in_selenium.py` | Implicit Wait | `driver.implicitly_wait(seconds)` |
| `explicit_wait_in_selenium.py` | Explicit Wait | `WebDriverWait(driver, timeout).until(EC.condition)` |
| `fluent_wait_in_selenium.py` | Fluent Wait | `WebDriverWait(driver, timeout, poll_frequency, ignored_exceptions)` |

| Wait Type | Scope | Polling | Ignore Exceptions |
|---|---|---|---|
| Implicit | Global (all elements) | Fixed | No |
| Explicit | Per condition | Fixed | No |
| Fluent | Per condition | Configurable | Yes |

---

### `handle_alert`

**File:** `handle_alert/alert_handle.py`

Handles all JavaScript dialog types in Selenium.

| Dialog Type | Selenium API | Action |
|---|---|---|
| Simple Alert | `driver.switch_to.alert` | `alert.accept()` |
| JS Confirm | `driver.switch_to.alert` | `alert.dismiss()` |
| JS Prompt | `driver.switch_to.alert` | `alert.send_keys("text")` → `alert.accept()` |

> ⚠️ **Note:** In Selenium, `driver.switch_to.alert` must be called **after** the dialog has been triggered.

---

### `handle_dropdown`

**File:** `handle_dropdown/handle_drop_down.py`

Handles HTML `<select>` dropdowns using Selenium's `Select` class.

| Selection Method | Selenium API |
|---|---|
| By visible text | `Select(el).select_by_visible_text("Option")` |
| By value attribute | `Select(el).select_by_value("value")` |
| By index | `Select(el).select_by_index(2)` |
| Get all options | `Select(el).options` |

---

### `handle_popup`

**File:** `handle_popup/popup_handle.py`

Handles new browser windows/tabs opened by user interactions.

```python
# Selenium approach — store main handle, iterate all handles to find the new one
main_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "Click Here").click()

for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        driver.close()

driver.switch_to.window(main_window)
```

---

### `iframe`

**File:** `iframe/Iframe_handling.py`

Interacts with elements inside HTML iFrames using `switch_to.frame()`.

```python
# Selenium approach — must switch context into the iframe, then switch back out
iframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
driver.switch_to.default_content()  # Switch back to main page
```

---

### `takescreenshot`

**File:** `takescreenshot/screen_shot_handle.py`

Captures screenshots for visual validation, debugging, and reporting.

| Screenshot Type | Selenium API |
|---|---|
| Viewport screenshot | `driver.save_screenshot(path)` |
| Element screenshot | `element.screenshot(path)` |

Screenshots are saved to: `selenium_practice/takescreenshot/screenshots/`

---

### `visual_testing`

**Directory:** `visual_testing/sauce_demo/`

Pixel-by-pixel screenshot comparison of SauceDemo pages using Pillow.

**Pages tested:** `login_page`, `inventory_page`, `cart_page`

#### How it works

1. **Capture baseline** — takes reference screenshots and saves them as `*_baseline.png`
2. **Compare** — takes new screenshots and diffs them pixel-by-pixel using Pillow
3. **Report** — open `report/visual_report.html` to view baseline / actual / diff images

```bash
pytest selenium_practice/visual_testing/sauce_demo/ -v
```

> To re-capture a baseline, delete the relevant `*_baseline.png` file and re-run the test.

---

### `api_comparison`

**Directory:** `api_comparison/jsonplaceholder/`

Deep JSON response comparison against [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com) using DeepDiff.

#### How it works

1. **Capture baseline** — calls each API endpoint and saves the response as a JSON file
2. **Compare** — calls each API again and deep-diffs the response against the saved baseline
3. **Report** — open `report/api_report.html` to view side-by-side JSON and differences

```bash
# Step 1 — Capture baselines (run once)
pytest selenium_practice/api_comparison/jsonplaceholder/tests/test_api_baseline.py -v

# Step 2 — Run API comparison
pytest selenium_practice/api_comparison/jsonplaceholder/tests/test_api_compare.py -v
```

> Dynamic fields (`id`, `createdAt`, `updatedAt`) are automatically ignored during comparison.

---

## Best Practices

### ✅ Do

- Use `WebDriverWait` with `expected_conditions` instead of `time.sleep()`
- Use `driver.implicitly_wait()` as a global fallback timeout, not a replacement for explicit waits
- Use `Select` class for all `<select>` dropdown interactions
- Always store `driver.current_window_handle` before triggering a popup
- Use `driver.switch_to.default_content()` after interacting with an iFrame
- Use `os.path.join()` for cross-platform compatible screenshot paths
- Use `os.makedirs(path, exist_ok=True)` to safely create output directories
- Wrap tests in `try/finally` to ensure `driver.quit()` always runs

### ❌ Avoid

- `time.sleep()` — use `WebDriverWait` or Fluent Wait instead
- Mixing implicit and explicit waits — this can cause unpredictable timeouts
- Hard-coded absolute file paths — use `os.path` utilities
- Forgetting to switch back from iFrames or popup windows with `switch_to.default_content()` / `switch_to.window()`

---

## CI/CD Integration

### GitHub Actions Example

```yaml
# .github/workflows/selenium.yml
name: Selenium Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Install Chrome
        uses: browser-actions/setup-chrome@v1

      - name: Run Selenium tests
        run: pytest selenium_practice/ -v --html=reports/report.html --self-contained-html

      - name: Upload test report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: selenium-report
          path: reports/
          retention-days: 30
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

### Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Usage |
|---|---|
| `feat:` | New feature or script |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code refactor without behaviour change |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks (deps, config) |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> **Maintained by:** QA Automation Team  
> **Last Updated:** May 2026
