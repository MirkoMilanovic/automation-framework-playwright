from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def continue_button(self):
        return self.page.locator('[data-qa="continue-button"]')

    def title(self):
        return self.page.locator('[data-qa="account-created"]')

    def wait_until_loaded(self):
        self.page.wait_for_url("**/account_created")
        self.continue_button().wait_for(state="visible")
        return self
