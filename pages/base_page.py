class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def get_text(self, locator):
        return self.page.text_content(locator)

    def is_visible(self, locator):
        return self.page.is_visible(locator)
