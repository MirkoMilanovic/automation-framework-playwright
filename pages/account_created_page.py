import logging
from typing import Self

from playwright.sync_api import Locator

from pages.base_page import BasePage
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class AccountCreatedPage(BasePage):
    """Page object for the account created confirmation screen."""

    # Locators
    def continue_button(self) -> Locator:
        """Return the Continue button displayed after account creation."""
        return self.data_qa("continue-button")

    def title(self) -> Locator:
        """Return the account created title element."""
        return self.data_qa("account-created")

    # Actions / waits
    def wait_until_loaded(self) -> Self:
        """Wait until the account created page is fully loaded."""
        try:
            self.page.wait_for_url("**/account_created")
            self.continue_button().wait_for(state="visible")
            return self
        except Exception as e:
            logger.error(msg := "Failed to load account created page")
            raise RuntimeError(msg) from e
