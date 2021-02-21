import unittest
from time import sleep

from parameterized import parameterized

from page.page_login import PageLogin
# from tool.get_data import get_data_file
from tool.get_data import GetData
from tool.get_driver import GetDriver
from tool.get_logging import GetLogging

logger=GetLogging().get_logging()
# def get_data():
#     arrs = []
#     for data in get_data_file("login.txt"):
#         arrs.append(data.strip().split(","))
#     return arrs[1::]

def get_data():
    return GetData().read_data("login.txt")

class TestLogin(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=GetDriver().get_driver()
        cls.login=PageLogin(cls.driver)
        cls.login.page_click_login_link()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().driver_quit()
        logger.info("完成测试login模块")

    @parameterized.expand(get_data())
    def test_login(self,username,password,verify_code,expect,status):
        logger.info("正在测试login模块")
        self.login.page_login(username,password,verify_code)
        sleep(3)
        if status == "True":
            try:
                self.assertTrue(self.login.page_if_login_success())
                # print("登录成功")
                logger.info("登录成功")
                self.login.page_click_logout()
                logger.info("退出成功")
                self.login.page_click_login_link()
            except Exception as e:
                logger.error("error是{}".format(e))
                self.login.page_get_screenshot()


        else:
            msg=self.login.page_get_error_text()
            try:

                self.assertEqual(expect,msg)
                self.login.page_click_error_btn()
            except Exception as e:
                logger.error("error信息是{}".format(e))
                # print("error信息是{}".format(msg))
                self.login.page_get_screenshot()
                self.login.page_click_error_btn()


