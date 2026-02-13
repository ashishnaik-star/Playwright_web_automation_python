from playwright.sync_api import Page, expect


class Homepagedress:
    def __init__(self, page: Page):
        self.page = page
        self.women_category = page.locator('//a[normalize-space()="Women"]')
        self.men_category = page.locator('//a[normalize-space()="Men"]')
        self.kids_category = page.locator('//a[normalize-space()="Kids"]')
        self.women_dress = page.locator('a[href="/category_products/1"]')
        self.men_dress = page.locator('a[href="/category_products/3"]')
        self.kids_dress = page.locator('//div[@id="Kids"]//a[contains(text(),"Dress")]')
        # self.hover_dress_one = page.locator('.productinfo.text-center').nth(0)
        self.add_to_cart_dress_number = page.locator('//div[@class="single-products"][1]/div/a/i')
        self.continue_shopping = page.get_by_text('Continue Shopping')
        self.cart =page.locator('a[href="/view_cart"]').nth(0)
        self.brands_babyhug = page.locator('[href="/brand_products/Babyhug"]')
        self.contact_us = page.locator("a[href='/contact_us']")


    def expand_women_category(self):
        self.women_category.click()

    def expand_men_category(self):
        self.men_category.click()

    def expand_kids_category(self):
        self.kids_category.click()

    def add_dress_to_cart(self, dress_number):
        self.add_to_cart_dress_number.nth(dress_number).click()
        self.continue_shopping.click()

    def fetch_first_search(self,text):
        return self.page.locator(f"//p[contains(text(),'{text}')]").nth(0)



