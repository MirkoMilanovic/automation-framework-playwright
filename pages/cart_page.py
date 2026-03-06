from playwright.sync_api import Locator

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the shopping cart page."""

    # Locators
    def cart_results(self) -> Locator:
        """Return all product rows displayed in the cart table."""
        return self.page.locator("#cart_info_table tbody tr")

    def get_first_cart(self) -> Locator:
        """Return the first product row from the cart."""
        return self.cart_results().first

    # Data extraction
    def get_product_details(self, product: Locator) -> dict[str, str]:
        """Extract product name and price from a cart row."""
        name = product.locator(".cart_description a").inner_text()
        price = product.locator(".cart_price p").inner_text()
        return {"name": name, "price": price}

    def get_product_quantity(self, product: Locator) -> str:
        """Extract product quantity from a cart row."""
        return product.locator("td.cart_quantity button").inner_text()
