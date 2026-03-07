import logging
from typing import Dict, Self

from playwright.sync_api import Locator

from pages.account_created_page import AccountCreatedPage
from pages.base_page import BasePage
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class SignupPage(BasePage):
    """Page object for the account details form shown during registration."""

    # Locators
    def create_account_button(self) -> Locator:
        """Return the Create Account button."""
        return self.page.get_by_role("button", name="Create Account")

    # Waits
    def wait_until_loaded(self) -> Self:
        """Wait until the signup details page is fully loaded."""
        try:
            self.page.wait_for_url("**/signup")
            self.create_account_button().wait_for(state="visible")
            return self
        except Exception as e:
            logger.error(msg := "Failed to load signup details page")
            raise RuntimeError(msg) from e

    # Form actions
    def fill_account_information(self, user: Dict[str, str]) -> Self:
        """Fill the account information section."""
        try:
            self.data_qa("password").fill(user["password"])
            return self
        except Exception as e:
            logger.error(msg := "Failed to fill account information section")
            raise RuntimeError(msg) from e

    def fill_address_information(self, user: Dict[str, str]) -> Self:
        """Fill the address details section."""
        try:
            self.data_qa("first_name").fill(user["first_name"])
            self.data_qa("last_name").fill(user["last_name"])
            self.data_qa("address").fill(user["address"])
            self.data_qa("country").select_option(user["country"])
            self.data_qa("state").fill(user["state"])
            self.data_qa("city").fill(user["city"])
            self.data_qa("zipcode").fill(user["zipcode"])
            self.data_qa("mobile_number").fill(user["mobile_number"])
            return self
        except Exception as e:
            logger.error(msg := "Failed to fill address information section")
            raise RuntimeError(msg) from e

    # Page transitions
    def go_to_create_account(self) -> AccountCreatedPage:
        """Submit the registration form and go to the account created page."""
        try:
            self.create_account_button().click()
            return AccountCreatedPage(self.page)
        except Exception as e:
            logger.error(msg := "Failed to submit registration form")
            raise RuntimeError(msg) from e
