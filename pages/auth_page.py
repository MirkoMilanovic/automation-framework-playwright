import logging
from typing import TYPE_CHECKING, Dict, Self

if TYPE_CHECKING:
    from pages.home_page import HomePage

from playwright.sync_api import Locator

from pages.base_page import BasePage
from pages.signup_page import SignupPage
from utils.config import BASE_URL
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class AuthPage(BasePage):
    """Page object for authentication actions: signup and login."""

    # Navigation
    def open(self) -> Self:
        """Open the authentication page."""
        try:
            self.navigate(f"{BASE_URL.rstrip('/')}/login")
            return self
        except Exception as e:
            logger.error(msg := "Failed to open authentication page")
            raise RuntimeError(msg) from e

    def wait_until_loaded(self) -> Self:
        """Wait until the authentication page is fully loaded."""
        try:
            self.page.wait_for_url("**/login")
            self.login_button().wait_for(state="visible")
            self.signup_button().wait_for(state="visible")
            return self
        except Exception as e:
            logger.error(msg := "Failed to load authentication page")
            raise RuntimeError(msg) from e

    # Locators - signup section
    def signup_button(self) -> Locator:
        """Return the Signup button."""
        return self.page.get_by_role("button", name="Signup")

    # Locators - login section
    def login_button(self) -> Locator:
        """Return the Login button."""
        return self.page.get_by_role("button", name="Login")

    def logged_user(self) -> Locator:
        """Return the logged-in user label."""
        return self.page.get_by_text("Logged in as")

    # Form actions
    def fill_login_information(self, user: Dict[str, str]) -> Self:
        """Fill the login form with user credentials."""
        try:
            self.data_qa("login-email").fill(user["email"])
            self.data_qa("login-password").fill(user["password"])
            return self
        except Exception as e:
            logger.error(msg := f"Failed to fill login information for user: {user['email']}")
            raise RuntimeError(msg) from e

    def fill_signup_information(self, user: Dict[str, str]) -> Self:
        """Fill the signup form with initial user data."""
        try:
            self.data_qa("signup-name").fill(user["name"])
            self.data_qa("signup-email").fill(user["email"])
            return self
        except Exception as e:
            logger.error(msg := f"Failed to fill signup information for user: {user['email']}")
            raise RuntimeError(msg) from e

    # Page transitions
    def go_to_signup(self) -> SignupPage:
        """Submit signup form and return the signup details page."""
        try:
            self.signup_button().click()
            return SignupPage(self.page)
        except Exception as e:
            logger.error(msg := "Failed to navigate from auth page to signup details page")
            raise RuntimeError(msg) from e

    def go_to_login(self) -> "HomePage":
        """Submit login form and return the home page."""
        from pages.home_page import HomePage

        try:
            self.login_button().click()
            return HomePage(self.page)
        except Exception as e:
            logger.error(msg := "Failed to submit login form")
            raise RuntimeError(msg) from e
