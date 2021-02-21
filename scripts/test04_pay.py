import unittest

from parameterized import parameterized

from page.page_login import PageLogin
from page.page_pay import PagePay
from tool.get_data import GetData
from tool.get_driver import GetDriver
from tool.get_logging import GetLogging

logger = GetLogging().get_logging()


def get_data():
    return GetData().read_data("pay.txt")


class TestPay(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("正在测试pay模块")
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)
        cls.pay = PagePay(cls.driver)
        cls.login.page_click_login_link()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()
        logger.info("完成测试pay模块")

    @parameterized.expand(get_data())
    def test_pay(self, username, password, verify_code, order_success_info):
        try:
            self.login.page_login(username, password, verify_code)
            self.pay.page_back_to_index()

            self.pay.page_pay()
            msg = self.pay.page_get_text()
            logger.info("文本是:{}".format(msg))
            self.assertEqual(msg, order_success_info)
        except Exception as e:
            logger.error("error信息是{}".format(e))
