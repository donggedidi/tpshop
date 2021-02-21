import unittest
from time import sleep

from parameterized import parameterized

from page.page_login import PageLogin
from page.page_order import PageOrder
from tool.get_data import GetData
from tool.get_driver import GetDriver
from tool.get_logging import GetLogging

logger=GetLogging().get_logging()
def get_data():
    return GetData().read_data("order.txt")

class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("正在测试order模块")
        cls.driver=GetDriver().get_driver()
        cls.login=PageLogin(cls.driver)
        cls.order=PageOrder(cls.driver)
        cls.login.page_click_login_link()



    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()
        logger.info("完成测试order模块")


    @parameterized.expand(get_data())
    def test_order(self,username,password,verify_code,order_success_info):

        try:
            self.login.page_login(username,password,verify_code)
            sleep(2)
            self.order.page_back_to_index()
            sleep(2)
            self.order.page_order()
            msg=self.order.page_get_success_info()
            logger.info("文本是:{}".format(msg))
            self.assertIn(order_success_info,msg)
        except Exception as e:
            logger.error("error信息是{}".format(e))


