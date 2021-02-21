import unittest
from time import sleep

from parameterized import parameterized

from page.page_cart import PageCart
from page.page_login import PageLogin
from tool.get_data import GetData

from tool.get_driver import GetDriver
from tool.get_logging import GetLogging

logger=GetLogging().get_logging()
def get_data():
    return GetData().read_data("cart.txt")

class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("正在测试cart模块")
        cls.driver=GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)
        cls.cart = PageCart(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()
        logger.info("完成测试cart模块")

    @parameterized.expand(get_data())
    def test_cart(self,username,password,verify_code,join_cart_text):

        self.login.page_click_login_link()
        self.login.page_login(username,password,verify_code)
        sleep(3)
        self.cart.page_back_to_index()
        sleep(3)
        try:
            self.cart.page_cart()
            sleep(3)
            self.cart.page_switch_to_iframe()
            sleep(3)
            msg=self.cart.page_get_cart_text()
            logger.info("添加购物车后的文本是:{}".format(msg))
            self.assertEqual(msg,join_cart_text)
            sleep(3)
            self.cart.page_switch_to_default()
            self.cart.page_click_close_frame()
            # print("iframe关闭了")
            logger.info("iframe关闭了")

        except Exception as e:
            logger.error("error信息是{}".format(e))

