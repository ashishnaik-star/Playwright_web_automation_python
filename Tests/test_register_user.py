from Pages.Homepage import HomePage
from Pages.Signup_login_reg_page import Signupregpage
from Pages.Signup_page import Signuppage
from playwright.sync_api import Page, expect
import pytest
from config import Config
from Utils.random_data_util import RandomDataUtil
from Pages.Succesful_account_creation_page import SuccAccCreated


def test_new_user_signup(page):
    homepage = HomePage(page)
    homepage.Signup_Login.click()
    signupregpage = Signupregpage(page)
    name, email = signupregpage.enter_rand_user_name_email()
    print(f'username=>>{name}\n email ==>{email}')
    signupregpage.signup_button.click()
    signup = Signuppage(page)
    expect(signup.enter_acc_info_heading).to_be_visible()


def test_validate_autofetched_name_email(page):
    homepage = HomePage(page)
    signupregpage = Signupregpage(page)
    signup = Signuppage(page)
    homepage.Signup_Login.click()
    name, email = signupregpage.enter_rand_user_name_email()
    signupregpage.signup_button.click()
    name_auto, email_auto = signup.fetch_email_name_autofilled()
    assert name == name_auto
    assert email == email_auto


@pytest.fixture
def test_register_user(page):
    homepage = HomePage(page)
    signupregpage = Signupregpage(page)
    signup = Signuppage(page)
    cf = Config()
    homepage.Signup_Login.click()
    name, email_id = signupregpage.enter_rand_user_name_email()
    cf.Email_id.append(email_id)
    signupregpage.signup_button.click()
    signup.title_mr_radio.check()
    signup.password.fill(cf.password)
    signup.date_select(cf.day, cf.month, cf.year)
    signup.news_letter_checkbox.check()
    signup.offer_chekbox.check()
    rd = RandomDataUtil()
    signup.first_name.fill(rd.get_first_name())
    signup.last_name.fill(rd.get_last_name())
    signup.Company.fill(cf.company)
    signup.Address.fill(rd.get_random_address())
    signup.Address_two.fill(rd.get_random_address())
    signup.country_select(cf.country)
    expect(signup.Country).to_have_value(cf.country)
    signup.Address_state.fill(rd.get_random_state())
    signup.Address_zipcode.fill(rd.get_random_numeric(6))
    signup.mobile_number.fill(rd.get_random_numeric(10))
    signup.city.fill(rd.get_random_city())
    signup.create_account.click()
    succ_acct = SuccAccCreated(page)
    expect(succ_acct.succ_acc_creation_label).to_be_visible()
    succ_acct.Continue.click()
    homepage.logout.click()
    return {
        "Email": email_id,
        "Name": name
    }


def test_login_valid_creds(page, test_register_user):
    homepage = HomePage(page)
    homepage.Signup_Login.click()
    signup = Signupregpage(page)
    cf = Config()
    signup.login_email.fill(test_register_user["Email"])
    signup.login_password.fill(cf.password)

