import logging
from pathlib import Path
from typing import Any, Generator

import pytest
from playwright.sync_api import Page

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def block_ads(page: Page) -> None:
    """Block common ad provider requests to improve test stability."""
    ad_patterns = [
        "**doubleclick.net/**",
        "**googlesyndication.com/**",
        "**googleads.g.doubleclick.net/**",
    ]

    logger.info("Blocking common ad provider requests")

    for pattern in ad_patterns:
        page.route(pattern, lambda route: route.abort())


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Any, call: Any) -> Generator[Any, None, None]:
    """Capture a screenshot automatically when a UI test fails.

    If a test fails during execution and a Playwright `page` fixture
    is available, a full-page screenshot is saved to the
    artifacts/screenshots directory.
    """
    outcome = yield
    report = outcome.get_result()  # pyright: ignore

    if report.when != "call" or report.passed:
        return

    page: Page | None = item.funcargs.get("page")
    if page is None:
        return

    screenshots_dir = Path("artifacts/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    test_name = item.nodeid.replace("/", "_").replace("::", "__")
    screenshot_file = screenshots_dir / f"{test_name}.png"

    logger.error(f"Test failed: {item.nodeid}")
    logger.info(f"Saving failure screenshot to: {screenshot_file}")

    page.screenshot(path=str(screenshot_file), full_page=True)
