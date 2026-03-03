from pages.base_page import BasePage
from utils.config import BASE_URL


class HomePage(BasePage):
    def open(self):
        self.navigate(BASE_URL)

    def features_items_heading(self):
        return self.page.get_by_role("heading", name="FEATURES ITEMS")

    def is_loaded(self) -> bool:
        current = self.page.url.rstrip("/")
        expected = BASE_URL.rstrip("/")
        self.features_items_heading().wait_for(state="visible")
        return current == expected
