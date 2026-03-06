from typing import Generator

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from utils.config import BROWSER, HEADLESS


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Create and yield a Playwright instance for the test session."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Launch and yield a browser instance for the test session."""
    browser_type = getattr(playwright_instance, BROWSER)

    browser_instance = browser_type.launch(headless=HEADLESS)
    yield browser_instance
    browser_instance.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Create and yield a new isolated browser context for each test."""
    browser_context = browser.new_context()
    yield browser_context
    browser_context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Create and yield a new page for each test."""
    browser_page = context.new_page()
    yield browser_page
    browser_page.close()
