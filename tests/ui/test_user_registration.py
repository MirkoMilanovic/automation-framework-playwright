import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from utils.config import BASE_URL
from utils.test_data import create_dummy_user


@pytest.mark.e2e
@pytest.mark.ui
def test_user_registration_flow(page):
    user = create_dummy_user()

    auth = (
        HomePage(page)
        .open()
        .wait_until_loaded()
        .go_to_auth()
    )

    signup = (
        auth
        .fill_signup_information(user)
        .go_to_signup()
        .wait_until_loaded()
    )

    expect(signup.data_qa("name")).to_have_value(user["name"])
    expect(signup.data_qa("email")).to_have_value(user["email"])
    expect(signup.data_qa("email")).to_be_disabled()

    account_created = (
        signup
        .fill_account_information(user)
        .fill_address_information(user)
        .go_to_create_account()
        .wait_until_loaded()
    )

    expect(account_created.title()).to_be_visible()
    expect(account_created.page).to_have_url(f"{BASE_URL.rstrip('/')}/account_created")
