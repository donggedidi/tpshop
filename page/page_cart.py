from time import sleep

import page
from base.base import Base
from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageCart(Base):
    def page_back_to_index(self):
        self.base_back_to_index(page.URL)

    def page_click_item(self):
        self.base_click(page.goods_item)

    def page_click_add_cart(self):
        self.base_click(page.join_cart)

    def page_switch_to_iframe(self):
        self.base_switch_to_iframe(page.success_frame)

    def page_get_cart_text(self):
        return self.base_get_text(page.join_success)

    def page_switch_to_default(self):
        self.base_switch_to_default()

    def page_click_close_frame(self):
        self.base_click(page.close_frame)

    def page_cart(self):
        # self.page_back_to_index()
        sleep(3)
        self.page_click_item()
        sleep(3)
        self.page_click_add_cart()

        # self.page_switch_to_iframe()
        # sleep(3)
        #
        # self.page_switch_to_default()
        # self.page_click_close_frame()


if __name__ == '__main__':
    driver=GetDriver().get_driver()
    PageLogin(driver).page_click_login_link()
    PageLogin(driver).page_login("18900000000","111111","8888")
    driver.get(page.URL)
    PageCart(driver).page_cart()
