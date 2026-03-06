from typing import Self

from playwright.sync_api import Locator

from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    """Page object for the account created confirmation screen."""

    # Locators
    def continue_button(self) -> Locator:
        """Return the Continue button displayed after account creation."""
        return self.page.locator('[data-qa="continue-button"]')

    def title(self) -> Locator:
        """Return the account created title element."""
        return self.page.locator('[data-qa="account-created"]')

    # Actions / waits
    def wait_until_loaded(self) -> Self:
        """Wait until the account created page is fully loaded."""
        self.page.wait_for_url("**/account_created")
        self.continue_button().wait_for(state="visible")
        return self
