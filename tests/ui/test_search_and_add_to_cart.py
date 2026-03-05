import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage
from utils.config import BASE_URL


@pytest.mark.e2e
@pytest.mark.ui
def test_search_and_add_to_cart(page):
    search_item = "T-Shirt"

    products_page = (
        HomePage(page)
        .open()
        .wait_until_loaded()
        .go_to_products()
        .search_product(search_item)
    )

    first_product = products_page.get_first_product()

    add_button = products_page.add_to_cart_button(first_product)
    expect(add_button).to_be_visible()
    expect(add_button).to_be_enabled()
    add_button.click()

    product_details = products_page.get_product_details(first_product)

    cart_page = HomePage(page).open().wait_until_loaded().go_to_cart()
    first_product_in_cart = cart_page.get_first_cart()
    product_in_cart_details = cart_page.get_product_details(first_product_in_cart)

    assert product_details == product_in_cart_details, \
        f"Cart product details {product_in_cart_details} do not match selected product {product_details}"
    assert cart_page.get_product_quantity(first_product_in_cart) == "1", "Product quantity in cart should be 1"
