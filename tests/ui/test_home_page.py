import logging

import pytest

from pages.home_page import HomePage
from utils.logger import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.ui
def test_homepage_loads_successfully(page) -> None:
    """Verify that the homepage loads successfully."""
    logger.info("Starting smoke test: homepage loads successfully")

    home = (
        HomePage(page)
        .open()
        .wait_until_loaded()
    )

    logger.info("Verifying homepage loaded successfully")

    assert home.is_loaded(), "Homepage should load and show 'FEATURES ITEMS' section"
