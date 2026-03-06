from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from utils.config import BASE_URL


class HomePage(BasePage):
    def open(self):
        self.navigate(BASE_URL)
        return self

    def wait_until_loaded(self):
        self.page.wait_for_url(f"{BASE_URL.rstrip('/')}/")
        self.page.get_by_role("heading", name="FEATURES ITEMS").wait_for(state="visible")
        return self

    def is_loaded(self) -> bool:
        current = self.page.url.rstrip("/")
        expected = BASE_URL.rstrip("/")
        return current == expected

    def logout_button(self):
        return self.page.get_by_role("link", name="Logout")

    def signup_login_button(self):
        return self.page.get_by_role("link", name="Signup / Login")

    def cart_link(self):
        return self.page.get_by_role("link", name="Cart")

    def products_link(self):
        return self.page.get_by_role("link", name="Products")

    def logged_user(self):
        return self.page.get_by_text("Logged in as")

    def go_to_auth(self):
        self.signup_login_button().click()
        return AuthPage(self.page)

    def go_to_products(self):
        self.products_link().first.click()
        return ProductsPage(self.page)

    def go_to_cart(self):
        self.cart_link().click()
        return CartPage(self.page)
