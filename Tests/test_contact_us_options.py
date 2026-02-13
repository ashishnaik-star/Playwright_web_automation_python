from Pages.Homepage import HomePage
from playwright.sync_api import Page, expect
import pytest
from config import Config
from Utils.random_data_util import RandomDataUtil
from Pages.Homepage_dress import Homepagedress
from Pages.Contact_us_page import ContactUsPage
from config import Config


def test_contact_up(page):
    Hp = Homepagedress(page)
    Hp.contact_us.click()
    Cu = ContactUsPage(page)
    Cu.name_input.fill('test')
    Cu.email_input.fill('test@test.com')
    Cu.subject_input.fill('Test-Subject@@@@@')
    Cu.message_textarea.fill('Test Message here')
    Cu.upload_file()
    page.wait_for_timeout(2000)
    Cu.handle_pop_up()
    Cu.submit_button.click()
    expect(Cu.success_message).to_have_text('Success! Your details have been submitted successfully.')


