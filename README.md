# SeleniumPythonFramework

A Python-based test automation framework covering **UI testing**, **Visual Testing**, and **API Comparison** using Selenium, Pytest, Pillow, and DeepDiff.

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| `selenium` | Browser automation |
| `pytest` | Test runner |
| `requests` | HTTP API calls |
| `Pillow` | Image comparison for visual testing |
| `deepdiff` | Deep JSON comparison for API testing |

---

## ⚙️ Setup

```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
SeleniumPythonFramework/
├── requirements.txt
└── selenium_practice/
    ├── broken_links/           # Broken link checker
    ├── handle_alert/           # Browser alert handling
    ├── handle_dropdown/        # Dropdown interaction
    ├── handle_popup/           # Popup handling
    ├── iframe/                 # iframe handling
    ├── launch_browsers/        # Chrome / Firefox / Edge launch tests
    ├── takescreenshot/         # Screenshot capture
    ├── waits/                  # Implicit, Explicit, Fluent waits
    │
    ├── sauce_demo/             # SauceDemo UI functional tests
    │   └── test_login.py       # Login, locked user, add-to-cart tests
    │
    ├── visual_testing/         # Visual regression testing
    │   └── sauce_demo/
    │       ├── conftest.py             # Shared Chrome driver fixture
    │       ├── visual_helpers.py       # Screenshot & comparison helpers
    │       ├── test_baseline_capture.py # STEP 1: capture baseline screenshots
    │       ├── test_visual_compare.py   # STEP 2: compare screenshots vs baseline
    │       ├── screenshots/             # Saved screenshots per page
    │       │   └── saucedemo/
    │       │       ├── login_page/
    │       │       ├── inventory_page/
    │       │       └── cart_page/
    │       └── report/
    │           └── visual_report.html   # Visual HTML report
    │
    └── api_comparison/         # API response comparison testing
        └── reqres/
            ├── conftest.py             # Pytest markers
            ├── api_helpers.py          # API call, save & compare helpers
            ├── test_api_baseline.py    # STEP 1: capture baseline responses
            ├── test_api_compare.py     # STEP 2: compare responses vs baseline
            ├── responses/              # Saved JSON responses per endpoint
            │   ├── users_list/
            │   ├── single_user/
            │   ├── users_not_found/
            │   ├── create_user/
            │   └── list_resources/
            └── report/
                └── api_report.html     # API comparison HTML report
```

---

## 🧪 Modules

### 1. UI Tests — SauceDemo (`sauce_demo/`)

Functional tests against [https://www.saucedemo.com](https://www.saucedemo.com).

| Test | Description |
|------|-------------|
| `test_login_success` | Verifies all valid users can log in |
| `test_login_locked_user` | Verifies locked users see an error |
| `test_add_all_items_to_cart` | Adds all inventory items and checks cart count |

```bash
pytest selenium_practice/sauce_demo/test_login.py -v
```

---

### 2. Visual Testing — SauceDemo (`visual_testing/sauce_demo/`)

Pixel-by-pixel screenshot comparison of SauceDemo pages.

**Pages tested:** `login_page`, `inventory_page`, `cart_page`

#### How it works
1. **Capture baseline** — takes reference screenshots and saves them
2. **Compare** — takes new screenshots and diffs them pixel-by-pixel
3. **Report** — open `report/visual_report.html` to view results visually

```bash
# Step 1 — Capture baselines (run once)
pytest selenium_practice/visual_testing/sauce_demo/test_baseline_capture.py -v

# Step 2 — Run visual regression
pytest selenium_practice/visual_testing/sauce_demo/test_visual_compare.py -v
```

> To re-capture a baseline, delete the relevant `*_baseline.png` file and re-run Step 1.

---

### 3. API Comparison — ReqRes (`api_comparison/reqres/`)

Deep JSON response comparison against [https://reqres.in](https://reqres.in).

**Endpoints tested:**

| API Name | Method | URL |
|----------|--------|-----|
| `users_list` | GET | `/api/users?page=1` |
| `single_user` | GET | `/api/users/2` |
| `users_not_found` | GET | `/api/users/23` |
| `create_user` | POST | `/api/users` |
| `list_resources` | GET | `/api/unknown` |

#### How it works
1. **Capture baseline** — calls each API and saves the response as JSON
2. **Compare** — calls each API again and deep-diffs against the baseline
3. **Report** — open `report/api_report.html` to view side-by-side JSONs

```bash
# Step 1 — Capture baselines (run once)
pytest selenium_practice/api_comparison/jsonplaceholder/test_api_baseline.py -v

# Step 2 — Run API comparison
pytest selenium_practice/api_comparison/jsonplaceholder/test_api_compare.py -v
```

> Dynamic fields (`id`, `createdAt`, `updatedAt`) are automatically ignored during comparison.

---

## 📊 HTML Reports

| Report | Location | Shows |
|--------|----------|-------|
| Visual Testing | `visual_testing/sauce_demo/report/visual_report.html` | Baseline / Actual / Diff screenshots |
| API Comparison | `api_comparison/reqres/report/api_report.html` | Baseline / Current JSON + differences |

> Open reports via a local web server (e.g. VS Code Live Server) to allow JSON/image loading.

---

## ▶️ Run All Tests

```bash
# All tests
pytest selenium_practice/ -v

# Only visual tests
pytest selenium_practice/visual_testing/ -v

# Only API tests
pytest selenium_practice/api_comparison/ -v

# Only UI functional tests
pytest selenium_practice/sauce_demo/ -v
```
