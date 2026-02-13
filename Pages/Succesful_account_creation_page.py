from playwright.sync_api import Page, expect

class SuccAccCreated:
    def __init__(self, page: Page):
        self.page = page
        self.succ_acc_creation_label = page.locator("b:has-text('ACCOUNT CREATED!')")
        self.Continue = page.get_by_role("link", name="Continue")

