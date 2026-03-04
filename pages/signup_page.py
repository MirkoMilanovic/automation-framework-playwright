from pages.account_created_page import AccountCreatedPage
from pages.base_page import BasePage


class SignupPage(BasePage):
    def create_account_button(self):
        return self.page.get_by_role("button", name="Create Account")

    def wait_until_loaded(self):
        self.page.wait_for_url("**/signup")
        self.create_account_button().wait_for(state="visible")
        return self

    def field(self, data_qa):
        return self.page.locator(f'[data-qa="{data_qa}"]')

    def fill_account_information(self, user):
        self.field("password").fill(user["password"])
        return self

    def fill_address_information(self, user):
        self.field("first_name").fill(user["first_name"])
        self.field("last_name").fill(user["last_name"])
        self.field("address").fill(user["address"])
        self.field("country").select_option(user["country"])
        self.field("state").fill(user["state"])
        self.field("city").fill(user["city"])
        self.field("zipcode").fill(user["zipcode"])
        self.field("mobile_number").fill(user["mobile_number"])
        return self

    def go_to_create_account(self):
        self.create_account_button().click()
        return AccountCreatedPage(self.page)
