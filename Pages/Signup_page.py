from playwright.sync_api import Page, expect


class Signuppage:
    def __init__(self, page: Page):
        self.page = page
        self.enter_acc_info_heading = page.locator("b:has-text('ENTER ACCOUNT INFORMATION')")
        self.title_mr_radio = page.get_by_role("radio", name="Mr.")
        self.title_mrs_radio = page.get_by_role("radio", name="Mrs.")
        self.Name = page.get_by_role("textbox", name="Name *", exact=True)
        self.password = page.locator('#password')
        self.email_autofilled = page.locator('#email')
        self.name_autofilled = page.locator('#name')
        self.days_dropdown = page.locator("#days")
        self.year_dropdown = page.locator("#years")
        self.month_dropdown = page.locator("#months")
        self.news_letter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.offer_chekbox = page.get_by_role("checkbox", name="Receive special offers from")
        self.Country = page.locator("#country")
        self.first_name = page.get_by_role("textbox", name="First name *")
        self.last_name = page.get_by_role("textbox", name="Last name *")
        self.Company = page.get_by_role("textbox", name="Company", exact=True)
        self.Address = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.Address_two = page.get_by_role("textbox", name="Address 2")
        self.Address_state = page.locator('#state')
        self.Address_zipcode = page.locator("#zipcode")
        self.mobile_number = page.get_by_role("textbox", name="Mobile Number *")
        self.create_account = page.get_by_role("button", name="Create Account")
        self.city = page.locator('#city')

    def fetch_email_name_autofilled(self):
        name = self.name_autofilled.get_attribute('value')
        email = self.email_autofilled.get_attribute('value')
        return name, email

    def date_select(self, day, month, year):
        self.days_dropdown.select_option(value=str(day))
        self.month_dropdown.select_option(value=str(month))
        self.year_dropdown.select_option(value=str(year))

    def country_select(self,country):
        self.Country.select_option(country)

