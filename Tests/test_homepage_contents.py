from Pages.Homepage import HomePage
from playwright.sync_api import Page, expect
import pytest
from config import Config
from Utils.random_data_util import RandomDataUtil


def test_homepage_title_url(page):
    homepage = HomePage(page)
    title = homepage.homepage_title()
    url = homepage.homepage_url()
    assert title == 'Automation Exercise'
    assert url == Config.base_url


def test_available_button_headings(page):
    homepage = HomePage(page)
    expect(homepage.Home).to_be_visible()
    expect(homepage.Products).to_be_visible()
    expect(homepage.Cart).to_be_visible()
    expect(homepage.Signup_Login).to_be_visible()
    expect(homepage.Test_cases).to_be_visible()
    expect(homepage.API_Testing).to_be_visible()
    expect(homepage.Video_Tutorials).to_be_visible()
    expect(homepage.Contact_us).to_be_visible()


def test_homepage_content_visible(page):
    homepage = HomePage(page)
    expect(homepage.homepage_logo).to_be_visible()
    expect(homepage.test_cases_button).to_be_visible()
    expect(homepage.api_list_button).to_be_visible()
    expect(homepage.category_button).to_be_visible()
    expect(homepage.brands_button).to_be_visible()
    expect(homepage.Subscription).to_be_visible()
    expect(homepage.email_box).to_be_visible()


def test_subscription(page):
    homepage = HomePage(page)
    ru = RandomDataUtil()
    homepage.check_subscription(ru.get_email())
    expect(homepage.text_subscribe).to_have_text('You have been successfully subscribed!')
