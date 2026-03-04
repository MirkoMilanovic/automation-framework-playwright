from pages.base_page import BasePage
from pages.signup_page import SignupPage
from utils.config import BASE_URL


class AuthPage(BasePage):
    def open(self):
        self.navigate(f"{BASE_URL.rstrip("/")}/login")
        return self

    def signup_section(self):
        return self.page.locator("div.signup-form")

    def signup_button(self):
        return self.signup_section().get_by_role("button", name="Signup")

    def wait_until_loaded(self):
        self.page.wait_for_url("**/login")
        self.signup_button().wait_for(state="visible")
        return self

    def fill_signup_information(self, user):
        self.signup_section().get_by_placeholder("Name").fill(user["name"])
        self.signup_section().get_by_placeholder("Email Address").fill(user["email"])
        return self

    def go_to_signup(self):
        self.signup_button().click()
        return SignupPage(self.page)
