from pages.base_page import BasePage
from utils.config import BASE_URL


class CartPage(BasePage):
    def cart_results(self):
        return self.page.locator("#cart_info_table tbody tr")

    def get_first_cart(self):
        return self.cart_results().first

    def get_product_details(self, product) -> dict:
        name = product.locator(".cart_description a").inner_text()
        price = product.locator(".cart_price p").inner_text()
        return {"name": name, "price": price}

    def get_product_quantity(self, product):
        return product.locator("td.cart_quantity button").inner_text()
