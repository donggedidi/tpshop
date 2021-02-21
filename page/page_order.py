from time import sleep

import page
from base.base import Base
from tool.get_logging import GetLogging

logger=GetLogging().get_logging()

class PageOrder(Base):
    def page_back_to_index(self):
        self.base_back_to_index(page.URL)

    def page_click_goto_cart(self):
        self.base_click(page.my_cart)

    def page_check_select_all(self):
        try:
            if self.base_find_element(page.select_all).is_selected():
                self.base_click(page.take_order)
            else:
                self.base_click(page.select_all)
                self.base_click(page.take_order)
        except Exception as e:
            logger.error("error信息是{}".format(e))

    def page_find_person(self):
        self.base_find_element(page.order_person)

    def page_submit_order(self):
        self.base_click(page.submit_order)

    def page_get_success_info(self):
        return self.base_get_text(page.order_success_info)

    def page_order(self):
        self.page_click_goto_cart()
        sleep(2)
        self.page_check_select_all()
        # self.page_take_order()
        # sleep(2)
        self.page_find_person()
        self.page_submit_order()







