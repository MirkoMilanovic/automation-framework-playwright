import logging

from playwright.sync_api import Locator, Page

from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class BasePage:
    """Base page object containing shared Playwright helpers."""
    def __init__(self, page: Page) -> None:
        """Initialize the page object with a Playwright page instance."""
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigate to the provided URL."""
        try:
            self.page.goto(url)
        except Exception as e:
            logger.error(msg := f"Failed to navigate to URL: {url}")
            raise RuntimeError(msg) from e

    def data_qa(self, name: str) -> Locator:
        """Return an element located by the data-qa attribute."""
        return self.page.locator(f'[data-qa="{name}"]')
