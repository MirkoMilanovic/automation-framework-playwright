import pytest
from playwright.sync_api import expect

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from utils.test_data import create_dummy_user


@pytest.mark.e2e
@pytest.mark.ui
def test_user_registration_flow(page):
    user = create_dummy_user()

    home = HomePage(page)
    home.open().wait_until_loaded()

    signup = (
        AuthPage(page)
        .open()
        .fill_signup_information(user)
        .go_to_signup()
    )

    signup.wait_until_loaded()
    expect(signup.field("name")).to_have_value(user["name"])
    expect(signup.field("email")).to_have_value(user["email"])
    expect(signup.field("email")).to_be_disabled()

    signup.fill_account_information(user)
    signup.fill_address_information(user)

    account_created = signup.go_to_create_account()
    account_created.wait_until_loaded()

    expect(account_created.title()).to_be_visible()
