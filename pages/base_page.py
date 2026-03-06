from playwright.sync_api import Locator, Page


class BasePage:
    """Base page object containing shared Playwright helpers."""
    def __init__(self, page: Page) -> None:
        """Initialize the page object with a Playwright page instance."""
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigate to the provided URL."""
        self.page.goto(url)

    def data_qa(self, name: str) -> Locator:
        """Return an element located by the data-qa attribute."""
        return self.page.locator(f'[data-qa="{name}"]')
