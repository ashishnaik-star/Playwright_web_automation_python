from playwright.sync_api import Page, expect


class Cartpage:
    def __init__(self, page: Page):
        self.page = page
        self.no_of_added_items = page.locator('#cart_info_table>tbody>tr>td:nth-child(2)')
        self.delete_added_item = page.locator((".cart_quantity_delete[data-product-id='2']"))
        self.cart_empty = page.locator('#empty_cart>p>b')

    def get_product_count(self):
        return self.no_of_added_items.count()

    def del_added_item(self):
        return self.delete_added_item.click()

    def check_cart_empty(self):
        return self.cart_empty


