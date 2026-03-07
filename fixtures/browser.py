import logging
from typing import Generator

import pytest
from playwright.sync_api import (
    APIRequestContext,
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from utils.config import BASE_URL, BROWSER, HEADLESS
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Create and yield a Playwright instance for the test session."""
    logger.info("Starting Playwright instance")
    with sync_playwright() as playwright:
        yield playwright
    logger.info("Playwright instance closed")


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Launch and yield a browser instance for the test session."""
    browser_type = getattr(playwright_instance, BROWSER)

    logger.info(f"Launching browser: {BROWSER} (headless={HEADLESS})")

    browser_instance = browser_type.launch(headless=HEADLESS)

    yield browser_instance

    logger.info("Closing browser")
    browser_instance.close()


@pytest.fixture(scope="function")
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    """Create and yield a new isolated browser context for each test."""
    logger.info("Creating new browser context")

    browser_context = browser.new_context()

    yield browser_context

    logger.info("Closing browser context")
    browser_context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    """Create and yield a new page for each test."""
    logger.info("Opening new page")

    browser_page = context.new_page()

    yield browser_page

    logger.info("Closing page")
    browser_page.close()


@pytest.fixture(scope="session")
def api_context(playwright_instance) -> Generator[APIRequestContext, None, None]:
    """Create and yield a Playwright API request context for API tests."""
    logger.info(f"Creating API request context with base URL: {BASE_URL}")

    context = playwright_instance.request.new_context(base_url=BASE_URL)

    yield context

    logger.info("Disposing API request context")
    context.dispose()
