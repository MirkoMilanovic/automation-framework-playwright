import pytest

from fixtures.browser import browser, context, page, playwright_instance


@pytest.fixture(autouse=True)
def block_ads(page):

    ad_patterns = [
        "**doubleclick.net/**",
        "**googlesyndication.com/**",
        "**googleads.g.doubleclick.net/**",
    ]

    for pattern in ad_patterns:
        page.route(pattern, lambda route: route.abort())
