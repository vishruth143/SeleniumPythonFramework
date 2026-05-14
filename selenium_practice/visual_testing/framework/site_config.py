"""
Base class for site-specific visual-test configurations.

To add a new website, subclass SiteConfig in your site folder and implement:
  - BASE_URL        : root URL of the site
  - PAGES           : list of PageEntry(name, path, requires_login)
  - pre_navigate()  : optional hook called before navigating (e.g. handle login)
"""

import time
from dataclasses import dataclass, field


@dataclass
class PageEntry:
    """Describes a single page to visual-test."""
    name: str           # human-readable slug used for file names
    path: str           # URL path relative to BASE_URL  (e.g. "/cart.html")
    requires_login: bool = False
    extra_wait: float = 2.0   # seconds to wait after navigation


class SiteConfig:
    """
    Override this class per website under test.

    Minimal subclass example
    ------------------------
    class MySiteConfig(SiteConfig):
        BASE_URL = "https://example.com"
        PAGES = [
            PageEntry("home", "/"),
            PageEntry("about", "/about"),
        ]
    """

    BASE_URL: str = ""
    PAGES: list[PageEntry] = field(default_factory=list)

    # ── hooks ──────────────────────────────────────────────────────────────────

    def pre_navigate(self, driver, page: PageEntry) -> None:
        """
        Called just before the driver navigates to `page`.
        Override to implement login, cookie acceptance, etc.
        Default: no-op.
        """
        pass

    # ── navigation ─────────────────────────────────────────────────────────────

    def navigate_to(self, driver, page: PageEntry) -> None:
        """Navigate to the page, invoking pre_navigate hook when needed."""
        if page.requires_login:
            self.pre_navigate(driver, page)
        driver.get(f"{self.BASE_URL}{page.path}")
        time.sleep(page.extra_wait)

    # ── parametrize helper ─────────────────────────────────────────────────────

    def pytest_params(self):
        """Return list of (name, path, requires_login) tuples for parametrize."""
        return [(p.name, p.path, p.requires_login) for p in self.PAGES]
