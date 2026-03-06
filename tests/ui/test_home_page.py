import pytest

from pages.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.ui
def test_homepage_loads_successfully(page) -> None:
    """Verify that the homepage loads successfully."""
    home = (
        HomePage(page)
        .open()
        .wait_until_loaded()
    )

    assert home.is_loaded(), "Homepage should load and show 'FEATURES ITEMS' section"
