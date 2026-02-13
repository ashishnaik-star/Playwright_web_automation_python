from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.Home = page.get_by_role("link", name=" Home")
        self.Products = page.get_by_role("link", name=" Products")
        self.Cart = page.get_by_role("link", name=" Cart")
        self.Signup_Login = page.get_by_role("link", name=" Signup / Login")
        self.Test_cases = page.get_by_role("link", name=" Test Cases")
        self.API_Testing = page.get_by_role("link", name=" API Testing")
        self.Video_Tutorials = page.get_by_role("link", name=" Video Tutorials")
        self.Contact_us = page.get_by_role("link", name=" Contact us")
        self.test_cases_button = page.get_by_role("button", name="Test Cases")
        self.api_list_button = page.get_by_role("button", name="APIs list for practice")
        self.category_button = page.get_by_role("heading", name="Category")
        self.brands_button = page.get_by_role("heading", name="Brands")
        self.recommended_items = page.get_by_role("heading", name="recommended items")
        self.Subscription = page.get_by_role("heading", name="Subscription")
        self.email_box = page.get_by_role("textbox", name="Your email address")
        self.homepage_logo = page.get_by_alt_text("Website for automation practice")
        self.subscription = page.locator('#susbscribe_email')
        self.click_subscribe = page.locator('#subscribe')
        self.text_subscribe= page.locator('#success-subscribe > div')
        self.logout =page.locator("a[href='/logout']")


    def homepage_title(self) -> str:
        return self.page.title()

    def homepage_url(self) -> str:
        return self.page.url

    def check_subscription(self,email):
        self.subscription.fill(email)
        self.click_subscribe.click()

