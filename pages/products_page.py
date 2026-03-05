from pages.base_page import BasePage
from utils.config import BASE_URL


class ProductsPage(BasePage):
    def search_bar(self):
        return self.page.locator("#search_product")

    def search_button(self):
        return self.page.locator("#submit_search")

    def search_product(self, product):
        self.search_bar().fill(product)
        self.search_button().click()
        return self

    def product_results(self):
        return self.page.locator("div.single-products")

    def get_first_product(self):
        return self.product_results().first

    def get_product_details(self, product) -> dict:
        name = product.locator("div.productinfo p").inner_text()
        price = product.locator("div.productinfo h2").inner_text()
        return {"name": name, "price": price}

    def add_to_cart_button(self, product):
        return product.locator("a.add-to-cart[data-product-id]").first
