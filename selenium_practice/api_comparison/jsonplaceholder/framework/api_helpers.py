import os
import json
import requests
from deepdiff import DeepDiff

# ── Storage folder (relative to this file) ────────────────────────────────
RESPONSES_DIR = os.path.join(os.path.dirname(__file__), "../responses")

# ── Endpoints to test (JSONPlaceholder) ───────────────────────────────────
# Each entry: (api_name, url, method, payload)
ENDPOINTS = [
    ("get_all_posts",   "https://jsonplaceholder.typicode.com/posts",        "GET",  None),
    ("get_single_post", "https://jsonplaceholder.typicode.com/posts/1",      "GET",  None),
    ("get_comments",    "https://jsonplaceholder.typicode.com/posts/1/comments", "GET", None),
    ("get_all_users",   "https://jsonplaceholder.typicode.com/users",        "GET",  None),
    ("create_post",     "https://jsonplaceholder.typicode.com/posts",        "POST", {"title": "foo", "body": "bar", "userId": 1}),
    ("get_todos",       "https://jsonplaceholder.typicode.com/todos?userId=1", "GET", None),
    ("get_albums",      "https://jsonplaceholder.typicode.com/albums/1",     "GET",  None),
]

# ── Keys to ignore during comparison (dynamic / always-changing fields) ───
# JSONPlaceholder IDs are fixed/static — no fields need to be ignored
IGNORED_KEYS = set()


def get_paths(api_name):
    """Return (baseline, current, diff) JSON paths for a given api_name."""
    api_dir = os.path.join(RESPONSES_DIR, api_name)
    os.makedirs(api_dir, exist_ok=True)
    return (
        os.path.join(api_dir, f"{api_name}_baseline.json"),
        os.path.join(api_dir, f"{api_name}_current.json"),
        os.path.join(api_dir, f"{api_name}_diff.json"),
    )


def call_api(url, method="GET", payload=None):
    """Call the API and return (status_code, body_dict)."""
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers, timeout=15) \
        if method.upper() == "POST" \
        else requests.get(url, headers=headers, timeout=15)
    try:
        body = resp.json()
    except Exception:
        body = {"raw": resp.text}
    return resp.status_code, body


def save_response(api_name, status_code, body, path):
    """Persist status code + body as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"status_code": status_code, "body": body}, f, indent=2)
    print(f"  Saved → {path}")


def load_response(path):
    """Load a saved JSON response file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def compare_responses(baseline_path, current_path, diff_path):
    """
    Deep-compare baseline vs current.
    Returns True  → match (stale diff file removed).
    Returns False → differences written to diff_path.
    """
    baseline = load_response(baseline_path)
    current  = load_response(current_path)

    exclude_regex = (
        [rf"root\[.+\]\['{k}'\]" for k in IGNORED_KEYS] +
        [rf"root\['{k}'\]"       for k in IGNORED_KEYS]
    )
    diff = DeepDiff(baseline, current, ignore_order=True,
                    exclude_regex_paths=exclude_regex)

    if diff:
        diff_data = {
            "baseline_status": baseline.get("status_code"),
            "current_status":  current.get("status_code"),
            "differences":     diff.to_dict(),
        }
        with open(diff_path, "w", encoding="utf-8") as f:
            json.dump(diff_data, f, indent=2)
        print(f"  ❌ Differences → {diff_path}")
        return False

    if os.path.exists(diff_path):
        os.remove(diff_path)
    print("  ✅ Responses match.")
    return True

