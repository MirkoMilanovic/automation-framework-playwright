import logging
from typing import Self

from playwright.sync_api import Locator

from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from utils.config import BASE_URL
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """Page object for the application home page."""

    # Navigation
    def open(self) -> Self:
        """Open the home page."""
        try:
            self.navigate(BASE_URL)
            return self
        except Exception as e:
            logger.error(msg := "Failed to open home page")
            raise RuntimeError(msg) from e

    def wait_until_loaded(self) -> Self:
        """Wait until the home page is fully loaded."""
        try:
            self.page.wait_for_url(f"{BASE_URL.rstrip('/')}/")
            self.features_items_title().wait_for(state="visible")
            return self
        except Exception as e:
            logger.error(msg := "Failed to load home page")
            raise RuntimeError(msg) from e

    def is_loaded(self) -> bool:
        """Check whether the current URL matches the expected home page URL."""
        current = self.page.url.rstrip("/")
        expected = BASE_URL.rstrip("/")
        return current == expected

    # Locators - header / navbar
    def signup_login_button(self) -> Locator:
        """Return the Signup / Login link."""
        return self.page.get_by_role("link", name="Signup / Login")

    def logout_button(self) -> Locator:
        """Return the Logout link."""
        return self.page.get_by_role("link", name="Logout")

    def cart_link(self) -> Locator:
        """Return the Cart link."""
        return self.page.get_by_role("link", name="Cart")

    def products_link(self) -> Locator:
        """Return the Products link."""
        return self.page.get_by_role("link", name="Products")

    def logged_user(self) -> Locator:
        """Return the logged-in user label."""
        return self.page.get_by_text("Logged in as")

    # Locators - content
    def features_items_title(self) -> Locator:
        """Return the FEATURES ITEMS title."""
        return self.page.get_by_role("heading", name="FEATURES ITEMS")

    # Page transitions
    def go_to_auth(self) -> AuthPage:
        """Navigate to the authentication page."""
        try:
            self.signup_login_button().click()
            return AuthPage(self.page)
        except Exception as e:
            logger.error(msg := "Failed to navigate from home page to auth page")
            raise RuntimeError(msg) from e

    def go_to_products(self) -> ProductsPage:
        """Navigate to the products page."""
        try:
            self.products_link().first.click()
            return ProductsPage(self.page)
        except Exception as e:
            logger.error(msg := "Failed to navigate from home page to products page")
            raise RuntimeError(msg) from e

    def go_to_cart(self) -> CartPage:
        """Navigate to the cart page."""
        try:
            self.cart_link().click()
            return CartPage(self.page)
        except Exception as e:
            logger.error(msg := "Failed to navigate from home page to cart page")
            raise RuntimeError(msg) from e
