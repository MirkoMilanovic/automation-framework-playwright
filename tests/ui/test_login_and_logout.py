import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from utils.config import BASE_URL
from utils.test_data import pre_existing_dummy_user


@pytest.mark.e2e
@pytest.mark.ui
def test_login_and_logout(page) -> None:
    """Verify that a user can log in and then log out successfully."""
    user = pre_existing_dummy_user()

    auth = (
        HomePage(page)
        .open()
        .wait_until_loaded()
        .go_to_auth()
    )

    login = (
        auth
        .fill_login_information(user)
        .go_to_login()
        .wait_until_loaded()
    )

    logout_button = login.logout_button()

    expect(login.logged_user()).to_contain_text(user["name"])
    expect(logout_button).to_be_visible()

    logout_button.click()

    expect(login.signup_login_button()).to_be_visible()
    expect(page).to_have_url(f"{BASE_URL.rstrip('/')}/login")

