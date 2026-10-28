from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        return self.page.goto(url)

    def reload(self):
        return self.page.reload(wait_until='domcontentloaded')