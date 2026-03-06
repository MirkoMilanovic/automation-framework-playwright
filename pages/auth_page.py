from pages.base_page import BasePage
from pages.signup_page import SignupPage
from utils.config import BASE_URL


class AuthPage(BasePage):
    def open(self):
        self.navigate(f"{BASE_URL.rstrip("/")}/login")
        return self

    def signup_button(self):
        return self.page.get_by_role("button", name="Signup")

    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    def logged_user(self):
        return self.page.get_by_text("Logged in as")

    def wait_until_loaded(self):
        self.page.wait_for_url("**/login")
        self.login_button().wait_for(state="visible")
        self.signup_button().wait_for(state="visible")
        return self

    def fill_login_information(self, user):
        self.data_qa("login-email").fill(user["email"])
        self.data_qa("login-password").fill(user["password"])
        return self

    def fill_signup_information(self, user):
        self.data_qa("signup-name").fill(user["name"])
        self.data_qa("signup-email").fill(user["email"])
        return self

    def go_to_signup(self):
        self.signup_button().click()
        return SignupPage(self.page)

    def go_to_login(self):
        from pages.home_page import HomePage

        self.login_button().click()
        return HomePage(self.page)
