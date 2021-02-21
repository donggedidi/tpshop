from time import sleep

import page
from base.base import Base


class PagePay(Base):
    def page_back_to_index(self):
        sleep(2)
        self.base_back_to_index(page.URL)

    def page_switch_to_handle(self,title):
        self.base_switch_to_handle(title)

    def page_click_myorder_link(self):
        self.base_click(page.my_order)

    def page_click_pay_now(self):
        self.base_click(page.pay_now_btn)

    def page_delivery_radio(self):
        self.base_click(page.delivery_radio)

    def page_confirm_payment(self):
        self.base_click(page.confirm_payment)

    def page_get_text(self):
        return self.base_get_text(page.pay_success_info)

    def page_pay(self):
        # self.page_switch_to_handle()
        self.page_click_myorder_link()
        self.page_switch_to_handle("我的订单")
        self.page_click_pay_now()
        self.page_switch_to_handle("订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城")
        self.page_delivery_radio()
        self.page_confirm_payment()

