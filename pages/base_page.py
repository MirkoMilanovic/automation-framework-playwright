class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def data_qa(self, name):
        return self.page.locator(f'[data-qa="{name}"]')
