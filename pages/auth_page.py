from typing import TYPE_CHECKING, Dict, Self

if TYPE_CHECKING:
    from pages.home_page import HomePage

from playwright.sync_api import Locator

from pages.base_page import BasePage
from pages.signup_page import SignupPage
from utils.config import BASE_URL


class AuthPage(BasePage):
    """Page object for authentication actions: signup and login."""

    # Navigation
    def open(self) -> Self:
        """Open the authentication page."""
        self.navigate(f"{BASE_URL.rstrip('/')}/login")
        return self

    def wait_until_loaded(self) -> Self:
        """Wait until the authentication page is fully loaded."""
        self.page.wait_for_url("**/login")
        self.login_button().wait_for(state="visible")
        self.signup_button().wait_for(state="visible")
        return self

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
        self.data_qa("login-email").fill(user["email"])
        self.data_qa("login-password").fill(user["password"])
        return self

    def fill_signup_information(self, user: Dict[str, str]) -> Self:
        """Fill the signup form with initial user data."""
        self.data_qa("signup-name").fill(user["name"])
        self.data_qa("signup-email").fill(user["email"])
        return self

    # Page transitions
    def go_to_signup(self) -> SignupPage:
        """Submit signup form and return the signup details page."""
        self.signup_button().click()
        return SignupPage(self.page)

    def go_to_login(self) -> "HomePage":
        """Submit login form and return the home page."""
        from pages.home_page import HomePage

        self.login_button().click()
        return HomePage(self.page)
