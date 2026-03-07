import logging
from typing import Self

from playwright.sync_api import Locator

from pages.base_page import BasePage
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


class ProductsPage(BasePage):
    """Page object for the products listing and search page."""

    # Locators - search section
    def search_bar(self) -> Locator:
        """Return the product search input field."""
        return self.page.locator("#search_product")

    def search_button(self) -> Locator:
        """Return the search submit button."""
        return self.page.locator("#submit_search")

    # Locators - product list
    def product_results(self) -> Locator:
        """Return all product cards displayed in search results."""
        return self.page.locator("div.single-products")

    def get_first_product(self) -> Locator:
        """Return the first product card from the results list."""
        return self.product_results().first

    def add_to_cart_button(self, product: Locator) -> Locator:
        """Return the add-to-cart button for a given product card."""
        return product.locator("div.productinfo a.add-to-cart[data-product-id]").first

    # Locators - modal
    def cart_modal(self) -> Locator:
        """Return the cart confirmation modal."""
        return self.page.locator("#cartModal.show")

    def cart_modal_title(self) -> Locator:
        """Return the title shown in the cart confirmation modal."""
        return self.cart_modal().locator("h4.modal-title", has_text="Added!")

    # Waits / actions
    def wait_until_loaded(self) -> Self:
        """Wait until the products page is fully loaded."""
        try:
            self.page.wait_for_url("**/products*")
            self.search_bar().wait_for(state="visible")
            self.search_button().wait_for(state="visible")
            return self
        except Exception as e:
            logger.error(msg := "Failed to load products page")
            raise RuntimeError(msg) from e

    def search_product(self, product: str) -> Self:
        """Search for a product by name."""
        try:
            self.search_bar().fill(product)
            self.search_button().click()
            self.page.wait_for_url("**/products?search=*")
            self.product_results().first.wait_for(state="visible")
            return self
        except Exception as e:
            logger.error(msg := f"Failed to search for product: {product}")
            raise RuntimeError(msg) from e

    # Data extraction
    def get_product_details(self, product: Locator) -> dict[str, str]:
        """Extract product name and price from a product card."""
        try:
            name = product.locator("div.productinfo p").inner_text()
            price = product.locator("div.productinfo h2").inner_text()
            return {"name": name, "price": price}
        except Exception as e:
            logger.error(msg := "Failed to extract product details from product card")
            raise RuntimeError(msg) from e

    def get_product_names(self) -> list[str]:
        """Return the names of all products visible in the result list."""
        try:
            return self.page.locator("div.productinfo p").all_inner_texts()
        except Exception as e:
            logger.error(msg := "Failed to extract product names from search results")
            raise RuntimeError(msg) from e
