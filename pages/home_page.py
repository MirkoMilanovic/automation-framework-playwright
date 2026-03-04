from pages.base_page import BasePage
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
