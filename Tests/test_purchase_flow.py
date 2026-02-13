from Pages.Homepage_dress import Homepagedress
from Pages.Cart import Cartpage
from playwright.sync_api import Page, expect


def test_category(page):
    Hp = Homepagedress(page)
    Hp.expand_women_category()
    expect(Hp.women_dress).to_be_visible()
    Hp.expand_men_category()
    expect(Hp.men_dress).to_be_visible()
    Hp.expand_kids_category()
    expect(Hp.kids_dress).to_be_visible()


def test_add_dress_cart(page):
    Hp = Homepagedress(page)
    Hp.add_dress_to_cart(0)
    Hp.add_dress_to_cart(1)
    Hp.add_dress_to_cart(3)
    Hp.cart.click()
    Cp = Cartpage(page)
    assert Cp.get_product_count() == 3


def test_brands(page):
    Hp = Homepagedress(page)
    Hp.brands_babyhug.click()
    babyhug = Hp.fetch_first_search('Sleeves Printed Top - White')
    expect(babyhug).to_have_text('Sleeves Printed Top - White')

def test_delete_items(page):
    Hp = Homepagedress(page)
    Hp.add_dress_to_cart(0)
    Hp.cart.click()
    Cp = Cartpage(page)
    expect(Cp.cart_empty).to_have_text('Cart is empty!')



# --Add cases for
# 2.file reader from csv , json, txt
# 3. search products

