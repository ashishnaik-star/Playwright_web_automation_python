from playwright.sync_api import Page, expect
from Utils.random_data_util import RandomDataUtil


class Signupregpage:
    def __init__(self, page: Page):
        self.page = page
        self.new_user_signup_text = page.get_by_role("heading", name="New User Signup!")
        self.new_user_name = page.get_by_role("textbox", name="Name")
        self.new_user_email_id = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.get_by_role('button',name='Signup')
        self.login_email = page.locator("input[data-qa='login-email']")
        self.login_password = page.locator("input[placeholder='Password']")

    def enter_rand_user_name_email(self):
        randomutil = RandomDataUtil()
        name = randomutil.get_first_name()
        email = randomutil.get_email()
        self.new_user_name.fill("")
        self.new_user_name.fill(name)
        self.new_user_email_id.fill("")
        self.new_user_email_id.fill(email)
        return name, email

