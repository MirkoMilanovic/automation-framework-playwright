from pages.account_created_page import AccountCreatedPage
from pages.base_page import BasePage


class SignupPage(BasePage):
    def create_account_button(self):
        return self.page.get_by_role("button", name="Create Account")

    def wait_until_loaded(self):
        self.page.wait_for_url("**/signup")
        self.create_account_button().wait_for(state="visible")
        return self

    def fill_account_information(self, user):
        self.data_qa("password").fill(user["password"])
        return self

    def fill_address_information(self, user):
        self.data_qa("first_name").fill(user["first_name"])
        self.data_qa("last_name").fill(user["last_name"])
        self.data_qa("address").fill(user["address"])
        self.data_qa("country").select_option(user["country"])
        self.data_qa("state").fill(user["state"])
        self.data_qa("city").fill(user["city"])
        self.data_qa("zipcode").fill(user["zipcode"])
        self.data_qa("mobile_number").fill(user["mobile_number"])
        return self

    def go_to_create_account(self):
        self.create_account_button().click()
        return AccountCreatedPage(self.page)
