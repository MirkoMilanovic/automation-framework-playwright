from pages.base_page import BasePage
from utils.config import BASE_URL


class ProductsPage(BasePage):
    def search_bar(self):
        return self.page.locator("#search_product")

    def search_button(self):
        return self.page.locator("#submit_search")

    def wait_until_loaded(self):
        self.page.wait_for_url("**/products*")
        self.search_bar().wait_for(state="visible")
        self.search_button().wait_for(state="visible")
        return self

    def search_product(self, product: str):
        self.search_bar().fill(product)
        self.search_button().click()
        self.page.wait_for_url("**/products?search=*")
        self.product_results().first.wait_for(state="visible")
        return self

    def product_results(self):
        return self.page.locator("div.single-products")

    def get_first_product(self):
        return self.product_results().first

    def get_product_details(self, product) -> dict:
        name = product.locator("div.productinfo p").inner_text()
        price = product.locator("div.productinfo h2").inner_text()
        return {"name": name, "price": price}

    def get_product_names(self):
        return self.page.locator("div.productinfo p").all_inner_texts()

    def add_to_cart_button(self, product):
        return product.locator("div.productinfo a.add-to-cart[data-product-id]").first

    def cart_modal(self):
        return self.page.locator("#cartModal.show")

    def cart_modal_title(self):
        return self.cart_modal().locator("h4.modal-title", has_text="Added!")
